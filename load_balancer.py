import socket
import threading
import random
import requests

current_server_idx = 0
healthy_servers = []
# backend_servers = [("localhost", 8081), ("localhost", 8082), ("localhost", 8083)]
backend_servers = ["wserver1", "wserver2", "wserver3"]
dns = {
  "www.example.com/api/hifromlucas" : ("localhost", 9000),
  "wserver1": "localhost:8081", 
  "wserver2" : "localhost:8082", 
  "wserver3" : "localhost:8083"
}

def round_robin(size: int) -> None:
  current_server_idx = (current_server_idx + 1) % size
  
def health_check(): 
  global healthy_servers
  for server in backend_servers: 
    try: 
      server_address = dns[server]
      print("Server address:", server_address)
      response = requests.get(f"http://{server_address}/health")
      if response.status_code == 200: 
        if server not in healthy_servers: 
          healthy_servers.append(server)
      else: 
        if server in healthy_servers: 
          healthy_servers.remove(server)
    except Exception as e: 
      print(f"Error during health check for server {server}: {e}")
      if server in healthy_servers: 
        healthy_servers.remove(server)

def handle_client(client_socket: socket) -> None:
  request_data = client_socket.recv(1024).decode()
  if not healthy_servers: 
    client_socket.sendall(b"HTTP/1.1 503 No Service is unavailable \r\n\r\nNo Healthy Upstream available")
    client_socket.close()
    return 
    
  print("Received Request from:", client_socket.getpeername())
  print(request_data)
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket: 
    
    # choose from pool of backend servers
    backend_servers = [("localhost", 8081), ("localhost", 8082), ("localhost", 8083)]
    backend_address = random.choice(backend_servers)
    
    # send the data
    backend_socket.connect(backend_address)
    backend_socket.sendall(request_data.encode())
    
    # receive the data 
    response_data = backend_socket.recv(1024)
    print(f"The response data is {response_data}")
    
    
  client_socket.sendall(response_data)
  client_socket.close()
  

def start_load_balancer(port: int) -> None: 
  health_check()
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: 
    # bind the socket to the port 
    server_socket.bind(("localhost", port))
    
    # listen to incoming connections
    server_socket.listen()
    
    print(f"Load Balancer is listening at port {port}")
    
    while True: 
      client_socket, client_address = server_socket.accept()
      
      # handle the connection in a separate thread
      threading.Thread(target=handle_client, args=(client_socket,)).start()

def main(): 
  start_load_balancer(9000)
  
main()