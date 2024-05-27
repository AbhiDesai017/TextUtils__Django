from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalizer = request.POST.get('capitalizer', 'off')
    newliner = request.POST.get('newliner', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    #analyze text
    if removepunc == 'on':
        punctuations = '''!()-[]{};:''\,<>./?@#$%^&*_-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if capitalizer == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Capitalizer', 'analyzed_text': analyzed}
        djtext = analyzed

    if newliner == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'new liner', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'spaceremove', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'charcount', 'analyzed_text': analyzed}

    if removepunc != 'on' and capitalizer != "on" and newliner != "on" and spaceremove != "on" and charcount != "on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

