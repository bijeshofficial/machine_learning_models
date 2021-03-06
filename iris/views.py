from django.shortcuts import render
import pandas as pd
from .models import IrisResult
# from django.contrib import messages

# Create your views here.
def iris(request):
    if request.method == 'POST':
        #Receive data from the client
        sepal_length = request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepal_width')
        petal_length = request.POST.get('petal_length')
        petal_width = request.POST.get('petal_width')

        # print(type(sepal_length), sepal_width, petal_length, petal_width)
    
        #Unpickle the model
        model = pd.read_pickle('./pickles/iris_scv.pkl')

        #Make prediction
        result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

        #Saved the prediction in this new variable
        classification = result[0]
        
        IrisResult.objects.create(sepal_length = sepal_length, sepal_width = sepal_width, petal_length = petal_length, petal_width = petal_width, classification = classification)

        context = {
            'classification': classification,
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
        }

        return render(request, 'iris/iris.html', context)

    else:
        return render(request, 'iris/iris.html')


def results(request):

    context = {
        'dataset' : IrisResult.objects.all(),
    }
    return render(request, 'iris/results.html', context)