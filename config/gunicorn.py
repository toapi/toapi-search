#!/usr/bin/env python
import os

WORKERS = os.getenv('WORKERS', 4)

bind = '0.0.0.0:5000'
max_requests = 1000
worker_class = 'gevent'
workers = WORKERS
preload_app = True
graceful_timeout = 30
preload = True
