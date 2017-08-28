from client.client_api import app


def before_all(context):
    # app.run(debug=True, port=5000)
    context.client = app.test_client()
