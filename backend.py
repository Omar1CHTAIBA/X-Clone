import falcon
import json

class MessageResource:
    def __init__(self):
        self.messages = []

    def on_get(self, req, resp):
        resp.media = self.messages

    def on_post(self, req, resp):
        message = json.load(req.bounded_stream)
        self.messages.append(message)
        resp.media = {'status': 'Message received'}

app = falcon.App()
messages = MessageResource()
app.add_route('/messages', messages)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8000)
