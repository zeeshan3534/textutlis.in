from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'temp.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    lowercase = request.POST.get('lowercase', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        result = ""
        for char in djtext:
            if char not in punctuations:
                result += char

        working = {'purpose':'Removed Punctuations', 'analyzed_text': result}
        djtext = result

    elif(fullcaps=="on"):
        result = ""
        for char in djtext:
            result += char.upper()

        working = {'purpose': 'Changed to Uppercase', 'analyzed_text': result}
        djtext = result


    elif(extraspaceremover=="on"):
        result = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                result =result+ char

        working = {'purpose': 'Removed NewLines', 'analyzed_text': result}
        djtext = result

    elif (newlineremover == "on"):
        result = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                result = result + char

        working = {'purpose': 'Removed NewLines', 'analyzed_text': result}
    elif (lowercase == "on"):
        result = ""
        for char in djtext:
            result += char.lower()

        working = {'purpose': 'Changed to Uppercase', 'analyzed_text': result}
        djtext = result

    if(removepunc == "off" and newlineremover=="off" and extraspaceremover=="off" and fullcaps=="off" and lowercase=='off'):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', working)