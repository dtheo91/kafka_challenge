#!/bin/bash

# Run JupyterLab
jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser --NotebookApp.token='' --NotebookApp.password='' &

# Wait for JupyterLab to fully initialize (adjust the sleep duration as needed)
sleep 5

# Run the Python consumer script
python consumer1.py &
python consumer2.py &
python consumer3.py &

# Keep the container running
sleep infinity