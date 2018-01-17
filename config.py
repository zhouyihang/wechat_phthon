import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

youto_app_id = os.environ['OPENSHIFT_ENV_YOUTO_APP_ID']
youto_secret_id = os.environ['OPENSHIFT_ENV_YOUTO_SECRET_ID']
youto_secret_key = os.environ['OPENSHIFT_ENV_YOUTO_SECRET_KEY']
youto_qq = os.environ['OPENSHIFT_ENV_QQ']
