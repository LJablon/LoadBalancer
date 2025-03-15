#!/bin/bash

python multi_thread_server.py & # NOTE 1: you may need to change this to python3 if using mac
python load_balancer.py &

