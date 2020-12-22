from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from TestApp.forms import SignUpForm
from django.http import HttpResponseRedirect
from rest_framework import generics
from django.contrib.auth.models import User
from TestApp.serializers import UserSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(request):
    return render(request,"TestApp/home.html")

@login_required
def exam(request):
    return render(request,"TestApp/exam.html")


def signup_view(request):
    form=SignUpForm
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login")
    return render(request,"TestApp/signup.html",{"form":form})


def logout_view(request):
    return render(request,"TestApp/logout.html")



class CreateUserAPI(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class RetrieveUserAPI(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field="id"
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]


def api(request):
    current_user = request.user
    t=current_user.id
    if t is not None:
        return render(request,"TestApp/api.html",{"id":t})
    return render(request,"TestApp/api.html")
