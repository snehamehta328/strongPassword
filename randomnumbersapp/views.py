from django.shortcuts import render

import random
import string
# Create your views here.


def main(request):
    length=14
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits
    symbols=string.punctuation
    final=lower+upper+num+symbols
    genRandom=random.sample(final,length)
    password=genRandom
    print(password)
    # print("hi")
    # context={}
    # context['password']=password
    # print("hi")
    return render(request, 'randomnumbersapp/design.html',{'result':password})
