from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def count(request):
    text=request.GET.get('text','')
    word_count=len(text.split())
    return render(request,'count.html',{'text':text,'count':word_count})
