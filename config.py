import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

youtu_app_id = os.environ['OPENSHIFT_ENV_YOUTU_APP_ID']
youtu_secret_id = os.environ['OPENSHIFT_ENV_YOUTU_SECRET_ID']
youtu_secret_key = os.environ['OPENSHIFT_ENV_YOUTU_SECRET_KEY']
youtu_qq = os.environ['OPENSHIFT_ENV_YOUTU_QQ']
