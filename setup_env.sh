#!/bin/bash

# this is to setup the environment 
python -m venv ./venv  # NOTE 2: This may be different depending on the shell you are using as I'm sure you know
./venv/scripts/activate # this assumes assuming windows or git/bash

pip install requests 