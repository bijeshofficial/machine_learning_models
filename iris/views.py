from django.shortcuts import render
import pandas as pd

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
        model = pd.read_pickle('./iris/pickles/iris_scv.pkl')

        print(model)

        #Make prediction
        result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

        #Saved the prediction in this new variable
        classification = result[0]

        print(classification)

        # context = {
        #     'classification': classification,
        # }

        # return render(request, 'iris/iris.html', context)

    else:
        return render(request, 'iris/iris.html')

    