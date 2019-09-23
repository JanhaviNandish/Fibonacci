from django.http import Http404
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import time

# Create your views here.

def fib_solve(num):
    if num<2:
        return 1
    else:
        n1=1
        n2=1

        for n in range(2, num):
            t = n1+n2
            n1=n2
            n2=t
        return n2

@api_view(["POST"])
def fib_num(value):
    number = json.loads(value.body)
    if number:
        stime=time.time()
        #number=json.loads(value.body)
        numm=number
        result=fib_solve(numm)
        etime=time.time()- stime
        time_taken=etime

        return Response({'Nth term is ':result, 'time taken is': time_taken })