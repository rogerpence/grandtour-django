from django.views import View
from django.shortcuts import render
from django.forms.models import model_to_dict
import json
from django.core import serializers


# # Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.template import loader

# from .models import Tourstop
# from .repository import *

class Index(View):
    def get(self, request):
        # miles = 132
        # tourstops = get_all_tourstops()
        # distance = []

        # for tourstop in tourstops:
        #     distance.append(miles)
        #     miles += 21

        context = {
            # "tourstops": tourstops,
            # "distance" : distance
        }
        return render(request, 'tourstops/index.html', context)


# def show(request):
#     return HttpResponse("Tour stop show page.")

# def get_tourstops_as_json(request):
#     tourstops = get_all_tourstops()
#     # return JsonResponse(model_to_dict(tourstops), safe=False)

#     # tmpJson = serializers.serialize("json", tourstops)
#     # tmpObj = json.loads(tmpJson)

#     # return HttpResponse(json.dumps(tmpObj))
#     return HttpResponse(as_json(tourstops))
