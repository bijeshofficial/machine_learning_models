from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

# Create your views here.
def iris(request):
    return render(request, 'iris/iris.html')

def predict_changes(request):
    if request.POST.get('action') == 'post':
        #Receive data from the client
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))
    
        #Unpickle the model
        model = pd.read_pickle('pickles/iris_scv.pkl')

        #Make prediction
        result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

        #Saved the prediction in this new variable
        classification = result[0]

        return JsonResponse({
            'result':classification, 'sepal_length': sepal_length, 'sepal_width': sepal_width,'petal_length': petal_length, 'petal_width': petal_width,
        },safe = False)