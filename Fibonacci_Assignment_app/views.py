from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
#Welcome Program OUTPUT will be "Hi CallHub!!!..."
def welcome(request):
    return render(request,'user_input.html',{'name':'CallHub'})
#Fibonacci_program to find the element in Fibonacci_series
def Fibonacci_calc(request):
    start_time=time.time()
    input_number=request.POST['num']#Getting user input
    if input_number.isdigit():
        input_number=int(input_number)
        first_number,second_number=1,1        #First two no's in the Series
        if input_number==1:
            result= input_number
            end_time=time.time()
            Time=str(round((end_time-start_time),4))+'secs'
        elif input_number==0:
            result=0
            end_time=time.time()
            Time=str(round((end_time-start_time),4))+'secs'
        else:
            for i in range(2,input_number):
                result        = first_number+second_number
                first_number  = second_number              #Swapping two numbers
                second_number = result                     
            end_time=time.time()
            Time=str(round((end_time-start_time),4))+'secs' #Time taken for Program Excecution
    else:
        result="Invalid Input...."
        end_time=time.time()
        Time=str(round((end_time-start_time),4))+'secs' #Time taken for Program Excecution
 
    return render(request,'result.html',{'result':result,'time_cal':Time,'enter_num':input_number})
"""from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
#Welcome Program OUTPUT will be "Hi CallHub!!!..."
def welcome(request):
    return render(request,'user_input.html',{'name':'CallHub'})
#Fibonacci_program to find the element in Fibonacci_series
def add(request):
    start_time=time.time()
    input_number=request.POST['num']#Getting user input
    if input_number.isdigit():
        input_number=int(input_number)
        first_number,second_number=1,1        #First two no's in the Series
        if input_number==1:
            result= input_number
            end_time=time.time()
            Time=str(round((end_time-start_time),4))+'secs'
        elif input_number==0:
            result=0
            end_time=time.time()
            Time=str(round((end_time-start_time),4))+'secs'
        else:
            for i in range(2,input_number):
                result        = first_number+second_number
                first_number  = second_number              #Swapping two numbers
                second_number = result                     
            end_time=time.time()
            Time=str(round((end_time-start_time),4))+'secs' #Time taken for Program Excecution
    else:
        result="Invalid Input...."
        end_time=time.time()
        Time=str(round((end_time-start_time),4))+'secs' #Time taken for Program Excecution
 
    return render(request,'result.html',{'result':result,'time_cal':Time,'enter_num':input_number})"""