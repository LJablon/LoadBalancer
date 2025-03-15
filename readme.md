# Setup 
## run the following commands 
### This is purely for configurting the python virtual env
1) Using script 
chmod +x setup_env.sh
./setup_env.sh

2) non using script (this assumes windows)
python -m venv ./venv
./venv/Scripts/activate 
pip install requests

# Setting Up the Load balancer 
## run the following: 
chmod +x start_load_balancer.sh
./start_load_balancer.sh

## next
open a browser and input localhost:9000 to see the different servers return a response simulating a multiserver web application running on the three local ports 

