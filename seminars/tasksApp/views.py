from django.shortcuts import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


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