import os

DEBUG = 1

JOBS_DIR = os.environ.get('JOBS_DIR', '/data/ci_jobs')
WORKER_DIR = os.environ.get('WORKER_DIR', '/data/workers')

LOCAL_ARTIFACTS_DIR = os.environ.get('LOCAL_ARTIFACTS_DIR', '/data/artifacts')
GCE_BUCKET = os.environ.get('GCE_BUCKET')
STORAGE_BACKEND = os.environ.get(
    'STORAGE_BACKEND', 'jobserv.storage.gce_storage')

INTERNAL_API_KEY = os.environ.get('INTERNAL_API_KEY', '').encode()

CARBON_HOST = os.environ.get('CARBON_HOST')
if CARBON_HOST:
    parts = CARBON_HOST.split(':')
    if len(parts) == 1:
        CARBON_HOST = (CARBON_HOST, 2003)  # provide default port
    elif len(parts) == 2:
        CARBON_HOST = (parts[0], int(parts[1]))
    else:
        raise ValueError('Invalid CARBON_HOST setting: ' + CARBON_HOST)

CARBON_PREFIX = os.environ.get('CARBON_PREFIX', 'jobserv')
if CARBON_PREFIX and CARBON_PREFIX[-1] != '.':
    CARBON_PREFIX += '.'
