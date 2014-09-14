import bottle;

request = bottle.request;
response = bottle.response;
app = bottle.Bottle();
render = bottle.template;

@app.get('/')
def hello_world():
    return 'Hello from Bottle()!'

