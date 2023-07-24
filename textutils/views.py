from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')

    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #chexk with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext=analyzed

    if(charcount=="on"):
        analyzed="Total Number of Character-"+str(len(djtext))
        params = {'purpose': 'count character', 'analyzed_text': analyzed}
        djtext=analyzed
       
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext=analyzed
    
   
    return render(request,'analyze.html',params)


    

