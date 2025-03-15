import socket
import threading

def start_backend_server(port: int) -> None: 
  # Create a TCP/IP socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: 
    # bind socket to port 
    server_socket.bind(("localhost", port))
    
    # listen for incoming requests 
    server_socket.listen()
    print(f"Server listing on port {port}")
    
    while True: 
      # accept a new connection from the client 
      client_socket, client_address = server_socket.accept()
      
      # Receive the request from the client 
      request_data = client_socket.recv(1024).decode()
      
      # Log the request data
      print("Received request from:", client_socket.getpeername())
      print(request_data)
      
      response = f"HTTP/1.1 200 OK\r\n\r\nHello from server that Lucas created at port {port}"
      client_socket.sendall(response.encode())
      
      # close the client socket 
      client_socket.close()

def main(): 
  ports = [8081, 8082, 8083]
  for port in ports: 
    thread = threading.Thread(target=start_backend_server, args=(port,))
    thread.start()
    
main()
   