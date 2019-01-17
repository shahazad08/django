from django.shortcuts import render, HttpResponse, redirect
import json
from django.utils.safestring import mark_safe
# If you know what you're doing, you can now use mark_safe to indicate that the text is trusted
# (i.e. not coming from user input).mark_safe tells django templates that a
# string should be used AS IS, from your python code


def home(request):
    # return HttpResponse('home')

    return render(request, 'registration/home.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
})