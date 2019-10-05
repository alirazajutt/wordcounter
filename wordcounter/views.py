# this file is created by -- Ali Raza
# featured1 branch
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['mytext']
    word_list = data.split()
    list_len = len(word_list)

    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_list = sorted(word_dict.items(),key =operator.itemgetter(1))

    return render(request,'count.html',{'fulltext':data,'word':list_len,'word_dict':sorted_list})

def about(request):
    return render(request,'about.html')