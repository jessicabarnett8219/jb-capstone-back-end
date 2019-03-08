from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from ..models import Student, User, GradeLevel, Goal, Evaluation
from django.urls import reverse

@login_required(login_url='/login')
def display_eval_form(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    goals = Goal.objects.all()

    template_name = "goalfish/eval_form.html"

    return render(request, template_name, {'student': student, 'goals': goals})

@login_required(login_url='/login')
def add_evaluation(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    goal1 = get_object_or_404(Goal, pk=1)
    goal2 = get_object_or_404(Goal, pk=2)
    goal3 = get_object_or_404(Goal, pk=3)
    goal4 = get_object_or_404(Goal, pk=4)
    goal5 = get_object_or_404(Goal, pk=5)
    goal6 = get_object_or_404(Goal, pk=6)

    score1 = request.POST["score1"]
    score2 = request.POST["score2"]
    score3 = request.POST["score3"]
    score4 = request.POST["score4"]
    score5 = request.POST["score5"]
    score6 = request.POST["score6"]

    new_evaluation = Evaluation(
        date = "2019-02-11",
        schoolWeek = 2,
        score1 = int(score1),
        score2 = int(score2),
        score3 = int(score3),
        score4 = int(score4),
        score5 = int(score5),
        score6 = int(score6),
        goal1 = goal1,
        goal2 = goal2,
        goal3 = goal3,
        goal4 = goal4,
        goal5 = goal5,
        goal6 = goal6,
        student = student
    )
    new_evaluation.save()

    return HttpResponseRedirect(reverse('goalfish:all_students'))

