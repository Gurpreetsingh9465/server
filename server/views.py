from django.http import JsonResponse
import os
import numpy as np
import pickle
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


classes = ['A','B','C','D']

@csrf_exempt
def findAppliance(request):
    kmeans = pickle.load(open(os.path.join(settings.BASE_DIR,"server","save.pkl"), "rb"))
    try:
        W = np.array(request.POST.get('w').split(','), dtype=float)
        VAR = np.array(request.POST.get('var').split(','), dtype=float)
        dW = W[:-1] - W[1:]
        dVAR = VAR[:-1] - VAR[1:]
        val = kmeans.predict([[np.mean(dW), np.mean(dVAR)]])
        return JsonResponse({"class": classes[val[0]]},status=200)
    except Exception as e:
        print("=================",e)
        return JsonResponse({"404":e},status=404)
