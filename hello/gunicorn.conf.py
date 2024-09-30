import multiprocessing

bind = "0.0.0.0:8000"
# workers = multiprocessing.cpu_count()
workers = 2
# wsgi_app = 'startup:app'
wsgi_app = 'hello_app.webapp:app'
accesslog = '-'