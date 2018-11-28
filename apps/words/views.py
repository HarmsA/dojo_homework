from django.shortcuts import render, redirect
from datetime import datetime

def words(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'word_list' not in request.session:
        request.session['word_list'] = []
    return render(request, 'words/word.html')

def process(request):
    # if 'count' not in request.session:
    #     request.session['count'] = 0
    # else:
    request.session['count'] = request.session['count']+1

    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    request.session['big_font'] = request.POST['big_font']
    myDate = datetime.now()
    formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
    request.session['datetime'] = formatedDate
    request.session.modified = True

    temp_list = request.session['word_list']
    temp_list.append({'word':request.POST['word'],'color':request.POST['color'],
                     'big_font':request.POST['big_font'], 'datetime':request.session['datetime']})
    request.session['word_list'] = temp_list

    return render(request, 'words/success.html')

def clear(request):
    request.session.clear()
    return redirect('/')


