from django.shortcuts import HttpResponse
import logging
from dz2app.models import Customer


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


