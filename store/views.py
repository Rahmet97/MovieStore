from moviestore.models import Movie
import datetime
from django.http import response
from store.forms import AddMovieForm
from django.shortcuts import redirect, render
from rest_framework.views import APIView
import requests
from MovieStoreProject import settings


class Home(APIView):
    template_name = 'home.html'

    def get(self, request, format = None):
        url = 'http://127.0.0.1:8000/api/movies/'
        response = requests.get(url)
        result = response.json()
        # print(result)
        return render(
            request,
			self.template_name,
            {'response': result}
        )


def handle_uploaded_file(f):   
    with open(settings.MEDIA_ROOT + '/movie/', 'wb+') as destination:
        for chunk in f.chunks(): 
            destination.write(chunk)

def handle_uploaded_image(f):   
    with open('/pics/', 'wb+') as destination:
        for chunk in f.chunks(): 
            destination.write(chunk)


class AddMovie(APIView):
    template_name = 'add.html'

    def get(self, request, format=None):
        addform = AddMovieForm()
        return render(
            self.request,
            self.template_name,
            {'addform': addform}
        )
    # ['nomi', 'janr', 'narxi', 'yili', 'davomiyligi', 'movie', 'batafsil', 'reyting', 'avtor', 'rasm']
    def post(self, request, format=None):
        addform = AddMovieForm(request.POST, request.FILES)
        # print(addform.data['movie'])
        if addform.is_valid():
            data = dict(
                nomi = addform.data['nomi'],
                janr = addform.data['janr'],
                narxi = addform.data['narxi'],
                yili = addform.data['yili'],
                davomiyligi = addform.data['davomiyligi'],
                movie = handle_uploaded_file(request.FILES["movie"]), #addform.data['movie'],
                batafsil = addform.data['batafsil'],
                # reyting = addform.cleaned_data['avtor'],
                rasm = handle_uploaded_image(request.FILES["rasm"]) #addform.data.get('rasm')
            )
            # data = dict(addform.data())
            # print(data)
            url = 'http://127.0.0.1:8000/api/movies/'
            response = requests.post(url, json=data)
            result = response.json()
            print(result)
        return redirect('home')