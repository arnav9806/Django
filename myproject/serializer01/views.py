from django.shortcuts import render
from serializer01.serializers import UserSerializer
from serializer01.models import User
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def user_detail(request):
    u1= User.objects.get(id=1)
    print(u1)
    serializer = UserSerializer(u1)
    print(serializer)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')