from django.core.management.base import BaseCommand
from seminars.tasksapp.models import Throws


class Command(BaseCommand):
    help = "Throws"

    # def add_arguments(self, parser):
    #     parser.add_argument('pk', type=int, help='User ID')

    def handle(self):
        datetime_throws = datetime.now()
        result = choice(['орёл', 'решка'])
        throws = Throws(res_throws=result, time_throws=datetime_throws)
        throws.save()
        logger.info('throws successful')
        return HttpResponse(f'{throws} сохранен в БД')
