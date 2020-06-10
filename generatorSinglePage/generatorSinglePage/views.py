import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update(request):
    if request.method == 'POST':
        repo = git.Repo("nikit34.pythonanywhere.com/")
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Update code on server")
    else:
        return HttpResponse("Could`t update the code on server")
