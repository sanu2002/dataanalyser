from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def fun(request):
    djtext = request.POST.get('text', 'default')
    djtext1 = request.POST.get('chk1', 'off')
    djtext2 = request.POST.get('fullcaps', 'off')

    # if djtext1 == "on" and djtext2 == "on":
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed = ""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char
    #     analyzed = analyzed.upper()
    #     params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    #     djtext=analyzed
        # return render(request, 'analyse.html', params)

    # or

    if djtext1 == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyse.html', params)

    if (djtext2 == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext= analyzed
        # Analyze the text
        # return render(request, 'analyse.html', params)
    if (djtext1 != "on") and (djtext2!="on"):
        # params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # djtext=analyzed

        return HttpResponse("error")
    return render(request, 'analyse.html', params)



# these are the concept how can we handle bugs because in the previous on our both button is not working but in this section we fixed it
# i have another soution for that in vieswrestote.py