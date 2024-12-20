import sys
import multiprocessing
import os

# Path to your application directory
app_path = os.path.abspath(os.path.join(os.path.dirname('app.py'), 'API'))

# Add the application directory to the PYTHONPATH
sys.path.append(app_path)

# Address and port to bind
bind = os.getenv("GUNICORN_BIND", "0.0.0.0:9080")  # Default to 0.0.0.0:8000

# Number of worker processes
workers = int(os.getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1))  # Default: (CPU cores * 2) + 1

# Number of threads per worker
threads = int(os.getenv("GUNICORN_THREADS", 4))  # Default to 4 threads per worker

# Timeout for requests (in seconds)
timeout = int(os.getenv("GUNICORN_TIMEOUT", 120))  # Default to 120 seconds

# Logging level
loglevel = os.getenv("GUNICORN_LOGLEVEL", "info")  # Default to "info"

# Access log file (can be set to "-" for stdout)
accesslog = os.getenv("GUNICORN_ACCESSLOG", "-")  # Default to stdout

# Error log file (can be set to "-" for stderr)
errorlog = os.getenv("GUNICORN_ERRORLOG", "-")  # Default to stderr

# Preload app for performance (if safe for your application)
preload_app = os.getenv("GUNICORN_PRELOAD", "true").lower() == "true"

# Enable keep-alive connections
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", 4))  # Default to 4 seconds

forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }


