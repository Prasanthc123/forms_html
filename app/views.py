from django.shortcuts import render

# Create your views here.
def htmlpages(request):
    return render(request,'htmlpages.html')