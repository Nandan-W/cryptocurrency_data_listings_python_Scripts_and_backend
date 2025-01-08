#!/bin/bash

# Start the web server and log output
gunicorn app:app --bind 0.0.0.0:$PORT --daemon --access-logfile access.log --error-logfile error.log

# Start the worker process and log output
python python_script_for_dataFetch_analysis_and_update.py > worker.log 2>&1
