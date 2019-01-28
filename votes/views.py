from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate,Position,Vote
from .forms import QuestionModelForm
from .forms import QuestionModelForm1
from django.http import HttpResponseRedirect

def index(request):
    context = {}
    votes = Post.objects.all()
    context['votes'] = votes
    return render(request, "index.html", context)

def candidate_detail(request, vote_id):
    context = {}
    context['vote'] = Candidate.objects.get(id=vote_id)
    return render(request, 'candidate_detail.html', context)

def candidate_create(request):
    context = {}

    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'candidate_create.html', context)
    else:
        context['form'] = QuestionModelForm()
        return render(request, 'candidate_create.html', context)


def candidate_update(request, vote_id):

    post = Post.objects.get(id=vote_id)
    context = {}

    if request.method == 'POST':
        form = QuestionModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return detail(request, vote_id)
        else:
            context['form'] = form
            return render(request, 'candidate_update.html', context)
    else:
        context['form'] = QuestionModelForm(instance = post)
        return render(request, 'candidate_update.html', context)

def position_create(request):
    context = {}

    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'position_create.html', context)
    else:
        context['form'] = QuestionModelForm()
        return render(request, 'position_create.html', context)

#
# def comment(request):
#     context = {}
#
#     if request.method == 'POST':
#         form = QuestionModelForm1(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Comment Created")
#         else:
#             context['form'] = form
#             return render(request, 'comment.html', context)
#     else:
#         context['form'] = QuestionModelForm1()
#         return render(request, 'comment.html', context)
