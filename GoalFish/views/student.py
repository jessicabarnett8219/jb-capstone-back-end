from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from ..models import Student

@login_required
def list_students(request):
    '''[Queries the database for all objects in the student table and uses them in rendering the all_students template]

    Arguments:
        request

    Returns:
        [render] -- [renders the all_students template]
    '''

    all_students = Student.objects.all()
    template_name = 'goalfish/all_students.html'
    return render(request, template_name, {'students': all_students})