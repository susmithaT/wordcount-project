from django.http import HttpResponse
from django.shortcuts import render
import operator

def overview(Request):
    return render(Request, "homepage.html")


def home(Request):
    return render(Request, 'homepage.html')


def login(Request):
    return render(Request, "login.html")


def count(Request):
    totalwords = Request.GET['sentense']
    wordslist = totalwords.split()#list
    wordDict = {}
    for word in wordslist:
        if word in wordDict:
            wordDict[word] = wordDict[word]+1
        else:
            wordDict[word] = 1
    sortedwordDict = sorted(wordDict.items(),key=operator.itemgetter(1),reverse=True)
    return render(Request, 'count.html',{"fulltext":totalwords,"wordDict":sortedwordDict,"wordsCount":len(wordslist)})

def about(Request):
    return render(Request,'about.html')
def check(Request, a, b):
    return HttpResponse(a + b)
