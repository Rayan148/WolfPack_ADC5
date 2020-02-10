from django.shortcuts import render
from forum.models import Thread
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_api(request):
    if request.method == 'POST':
        decoded_data=request.body.decode('utf-8')
        thread_data=json.loads(decoded_data)
        title=thread_data['title']
        description=thread_data['description']
        threadobj = Thread.objects.create(title=title, description = description)
        threadobj.save()
        return JsonResponse({"message": "Successfully created ! "})


def read_api_data(request):
    thread = Thread.objects.all()
    dict_value = {'thread':list(thread.values('title', 'description', 'file'))}
    return JsonResponse(dict_value)



@csrf_exempt
def update_api_data(request, pk):
    thread = Thread.objects.get(pk=pk)
    if request.method=="GET":
        return JsonResponse({"title":thread.title, "descripton":thread.description})
    if request.method == 'POST':
        decoded_data=request.body.decode('utf-8')
        thread_data=json.loads(decoded_data)
        thread.title=thread_data['title']
        thread.description=thread_data['description']
        #thread.file=thread_data['file']
        thread.save()
        return JsonResponse({"message": "Successfully updated ! "})


@csrf_exempt
def delete_api_data(request, pk):
    if request.method == 'DELETE':
        thread = Thread.objects.get(pk = pk )
        thread.delete()
        return JsonResponse({"message": "Post Deleted!"})


def api_pagination(request,PAGENO, SIZE):
    skip = SIZE * (PAGENO - 1)
    threads = Thread.objects.all()[skip: (PAGENO * SIZE)]
    dict_value = {"threads": list(threads.values("title","description"))}
    return JsonResponse(dict_value)
