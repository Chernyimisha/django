from django.shortcuts import HttpResponse
from random import choice

from .models import Throws
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def throws(request):
    result = choice(['орёл', 'решка'])
    throws = Throws(res_throws=result)
    throws.save()
    logger.info('throws successful')
    return HttpResponse(f'{throws} сохранен в БД')


def main(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Первый Django-сайт</title>
        <h1>Это мой первый Django-сайт</h1>
    </head>
    <body>
    
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Первый Django-сайт</title>
        <h1>О НАС</h1>
    </head>
    <body>

    </body>
    </html>
    """
    return HttpResponse(html)


def throws_values(request):
    res = Throws.values()
    resp = ''
    for i in res:
        resp += str(i) + '\n'
    print(resp)
    return HttpResponse(resp)


