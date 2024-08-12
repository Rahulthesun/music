from django.shortcuts import render
import joblib
from django.http import HttpResponse

# Create your views here.

def music_form(request):
    return render(request , 'base/music_form.html' , context = {})


def music_ml_model(request):
    model = joblib.load('music-rec.joblib')
    age = int(request.GET.get('age'))
    gender = int(request.GET.get('gender'))
    predictions = model.predict([[age , gender]])
    context = {
        "music": predictions[0]
    }
    return render(request , 'base/result.html' , context)