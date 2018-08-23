import json
from datetime import datetime

import bottle
from bottle import error, HTTPError
from bottle import response

application = bottle.Bottle()


@application.hook('after_request')
def after_request():
    response.content_type = 'application/json'


LIST = [
    {
        'text': 'Just an item',
        'createdAt': datetime.now()
    },
    {
        'text': 'Just an item 2',
        'createdAt': datetime.now()
    }
]


@application.get('/')
@application.get('/list')
def index():
    return json.dumps(LIST, default=str)

def build_error_msg(status, msg):
    response.content_type = 'application/json'
    err = {
        'code': status,
        'message': msg
    }
    return json.dumps(err, default=str)

@application.error(500)
def insernal_error(err):
    return build_error_msg(500, 'Unexpected error')


@application.error(404)
def not_found(err):
    return build_error_msg(404, 'Not found')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8002)
