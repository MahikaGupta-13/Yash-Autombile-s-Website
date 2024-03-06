from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('bikename')
        number = request.POST.get('number')
        problem = request.POST.get('problem')
        time = request.POST.get('time')

        obj = ServiceBooking.objects.create(
            user=user,
            bikeName=name,
            model_no = number,
            problem = problem,
            time = time
        )
        obj.save()
        return redirect('/services/bookings')
    
    return render(request, 'services.html')


def showMessage(request):
    user = request.user
    obj = SendMessage.objects.filter(user=user)
    return render(request, 'notification.html', {'msgs': obj})


def bookServices(request):
    return render(request, 'book1.html')

def displayTable(request):
    vec = ServiceBooking.objects.filter(user=request.user)
    return render(request, 'table.html', {'vecs': vec})


@login_required(login_url="/accounts/login")

def details(request,id):
    vec = ServiceBooking.objects.filter(id=id)
    return render(request, 'details.html', {'vecs': vec})


def studentDiscussion(request):
    return render(request, 'dicussion.html')

@login_required(login_url='/accounts/login')
def question_list(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, 'dicussion.html', {'questions': questions })

def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})

def post_question(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')

        obj = Question(title=title, content=content, user=user)
        obj.save()
        return redirect('/')

def post_answer(request, question_id):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content')
        question = Question.objects.get(pk=question_id)
        print(content)
        obj = Answer.objects.create(content=content, user=user, question=question)
        obj.save()
        return redirect('/services/discussion')



