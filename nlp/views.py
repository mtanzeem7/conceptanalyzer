from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import nltk
from nltk.corpus import treebank


def index(request):
    return render(request,'nlp/home.html')

def compare(request):
	text1 = request.GET.get("input1")
	text2 = request.GET.get("input2")
	#token_set1 = nltk.word_tokenize(text1)
	#token_set2 = nltk.word_tokenize(text2)
	#t = treebank.parsed_sents('wsj_0001.mrg')[0]
	#t.draw()
	print "text.."
	print token_set1
	print token_set2
	return HttpResponse("yeayy")
