from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from slangtranslator.styleformer.demo import results, source_sentences
from slangtranslator.regional_identification import parse
from slangtranslator.percent_slang import slang_ratio
from slangtranslator.agerange import agePrediction
from slangtranslator.sentiment import sentiment_analysis
#from slangtranslator.styleformer import styleformer
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World')


def slangreturn(request):
    my_string = results(source_sentences)
    return JsonResponse({'string':my_string})



@csrf_exempt    
@require_POST
def submit_string(request):
    test = []
    received_json_data = json.loads(request.body)
    received_string1 = received_json_data['string']
    age_range = agePrediction(received_string1)
    percent_slang = slang_ratio(received_string1)
    received_string2 = test.append(received_string1)
    received_string = results(test)
    region = parse(received_string1)
    sentiment = sentiment_analysis(received_string)

    if received_string == None:
        received_string = 'ERROR'
        return JsonResponse({'Error':received_string})
    else:
        return JsonResponse({'received_string':received_string, 'region': region, 'age_range':age_range, 'percent_slang':percent_slang, 'sentiment': sentiment})
