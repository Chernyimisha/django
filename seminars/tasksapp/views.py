from django.shortcuts import HttpResponse, render
from random import choice, randint
from .forms import Game
from .models import Throws, Bones, Numbers
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def throws(request, attempts):
    results = []
    for i in range(attempts):
        result = choice(['орёл', 'решка'])
        throws = Throws(res_throws=result)
        throws.save()
        results.append(throws)
    logger.info(f'{len(results)} throws successful')
    context = {
        "game": 'Броски монеты',
        "attempts": results
    }
    return render(request, 'tasksapp/game_rezults.html', context)


def bones(request, attempts):
    results = []
    for i in range(attempts):
        result = randint(1, 6)
        bones = Bones(res_bones=result)
        bones.save()
        results.append(bones)
    logger.info(f'{len(results)} bones successful')
    context = {
        "game": 'Игральные кости',
        "attempts": results
    }
    return render(request, 'tasksapp/game_rezults.html', context)


def numbers(request, attempts):
    results = []
    for i in range(attempts):
        result = randint(0, 1000)
        randnumber = Numbers(res_random=result)
        randnumber.save()
        results.append(randnumber)
    logger.info(f'{len(results)} randnumber successful')
    context = {
        "game": 'Случайные числа',
        "attempts": results
    }
    return render(request, 'tasksapp/game_rezults.html', context)


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


# def get_index(request):
#     context = {
#         'title': 'Первый Django-сайт',
#         'header': 'Это мой первый Django-сайт',
#     }
#     return render(request, 'tasksapp/base.html', context)
#
#
# def get_about(request):
#     context = {
#         'title': 'Первый Django-сайт',
#         'header': 'О НАС',
#     }
#     return render(request, 'tasksapp/base.html', context)

def get_index(request):
    return render(request, 'tasksapp/index.html')


def get_about(request):
    return render(request, 'tasksapp/about.html')


def game_forms(request):
    if request.method == 'POST':
        form = Game(request.POST)
        if form.is_valid():
            choice_game = form.cleaned_data['choice_game']
            attempts = form.cleaned_data['attempts']
            logger.info(f'Получили {choice_game=}, {attempts=}.')
            if choice_game == 'throws':
                return throws(request, attempts)
            elif choice_game == 'bones':
                return bones(request, attempts)
            else:
                return numbers(request, attempts)
    else:
        form = Game()
        return render(request, 'tasksapp/game.html', {'form': form})


