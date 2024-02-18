#!/bin/bash

# Run JupyterLab
jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser --NotebookApp.token='' --NotebookApp.password='' &

# Run your Python script