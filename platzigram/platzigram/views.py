# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Oh, hi!, Current server time is {now}'.format(
        now=str(now))
    )


def sort_integers(request):
    numbers = [int(e) for e in request.GET['numbers'].split(
        ',')] if 'numbers' in request.GET else []
    data = {
        'status': 'ok',
        'numbers': sorted(numbers),
        'message': 'Sorted without problems'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here '.format(name)
    else:
        message = 'Hello {}!, Welcome to Platzigram'.format(name)
    return HttpResponse(message)
