import time
from multiprocessing import Process

from client import app
from client import db


def before_all(context):
    print('\nbefore_all start')
    context.config.setup_logging()
    db.create_all()
    context.server = Process(target=app.run, name='Flask Server', kwargs=dict(debug=True, port=5000))
    context.server.start()
    time.sleep(1)  # To make sure server is already up
    context.base_uri = 'http://localhost:5000'
    print('\nbefore_all end')


def after_all(context):
    print('\nafter_all start')
    context.server.terminate()
    context.server.join()
    print('\nafter_all end')


def before_feature(context, feature):
    print('\nbefore feature' + str(feature))


def after_feature(context, feature):
    print('\nafter feature' + str(feature))
