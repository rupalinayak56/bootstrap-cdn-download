from django.shortcuts import render

# Create your views here.
def cdn_bs(request):
    return render(request,"cdn_bs.html")
def cdn_bs1(request):
    return render(request,"cdn_bs1.html")
def cdn_bs2(request):
    return render(request,'cdn_bs2.html')
def cdn_bs3(request):
    return render(request,'cdn_bs3.html')
def download(request):
    return render(request,'download.html')



