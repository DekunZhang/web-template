import json

import web

urls = (
    '/', 'index',
    '/json', 'json_handler',
)


class index:
    def GET(self):
        data = web.input()
        message = data.get('message')
        name = data.get('name')
        age = data.get('age')
        return f"Hello {name}, you are {age} years old and you sent a message: " \
               f"{message}"

    def POST(self):
        data = web.input()
        message = data.get('message')
        name = data.get('name')
        age = data.get('age')
        return f"Hello {name}, you are {age} years old and you sent a message: " \
               f"{message}"


class json_handler:
    def GET(self):
        data = {'message': 'Hello, world!'}
        web.header('Content-Type', 'application/json')
        return json.dumps(data)

    def POST(self):
        data = web.data()
        json_data = json.loads(data)
        message = json_data['message']
        return f'Received message: {message}'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
