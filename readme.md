# Setup 
## run the following commands 

1) Using script 
chmod +x setup_env.sh
./setup_env.sh

2) non using script (this assumes windows please see your own language for more details)
python -m venv ./venv
./venv/Scripts/activate 
pip install requests

# Setting Up the Load balancer 
## run the following: 
chmod +x start_load_balancer.sh
./start_load_balancer.sh

## next
open a browser and input localhost:9000 to see the different servers return a response simulating a multiserver web application running on the three local ports 

## lastly 
Kill the terminals running both the load balancer (port 9000) and the three server instances ports (8081, 8082, 8083) and just run the loadbalancer and see what happens using the command 
python (or python3) loadbalancer.py and then trying to opening a browser 
http://localhost:9000 to see my program handling the case when no servers are healthy

