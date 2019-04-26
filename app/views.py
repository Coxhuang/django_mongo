from django.shortcuts import HttpResponse
from app.models import Test




def test(request):

    Test.objects.create(
        name = "cox",
        age = 12,
    )

    return HttpResponse("hello mongodb")