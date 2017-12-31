import time
from multiprocessing import Process

from client.client_api import app


def before_all(context):
    print('before_all')
    context.server = Process(target=app.run, name='Flask Server', kwargs=dict(debug=True, port=5000))
    context.server.start()
    time.sleep(1)  # To make sure server is already up
    context.base_uri = 'http://localhost:5000'


def after_all(context):
    context.server.terminate()
    context.server.join()
    print('after_all')
