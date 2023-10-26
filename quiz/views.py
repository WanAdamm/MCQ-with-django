from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def subject_list(request):
    subjects = Subjects.objects.order_by().values_list('subject', flat=True).distinct()
    context = {
        "subjects": subjects
    }

    return render(request, 'subject.html', context)

def question_list(request, subject):
    if request.method == 'POST':
        print(request.POST)
        # filter by  foreign key
        questions=Questions.objects.filter(subject__subject = subject)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if str(q.answer) ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        try:
            percent = round(score/(total*10) *100,2)
        except ZeroDivisionError:
            percent = 0

        time = int(request.POST.get('timer'))
        try:
            time = time
        except time > 59:
            time = time/60
        context = {
            'score':score,
            'time': time,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'subject':subject,
        }
        return render(request,'result.html',context)
    else:
        questions=Questions.objects.filter(subject__subject = subject)
        context = {
            'questions':questions,
            'subject':subject,
        }
        return render(request,'question.html',context)