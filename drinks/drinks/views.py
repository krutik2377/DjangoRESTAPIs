from .models import Drinks
from django.http import HttpResponse, JsonResponse
from .serializers import DrinkSerializer

def drink_list(request):

    # get all the drinks , serialize them and return Json
    drinks = Drinks.objects.all()
    DrinkSerializer(drinks, many=true)
    return JsonResponse(serializer.data)