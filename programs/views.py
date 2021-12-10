from django.shortcuts import render, get_object_or_404
from .models import Program

# Create your views here.

def all_programs(request):
    """ A view to show all programs"""

    programs = Program.objects.all()
    
    context = {
        'programs': programs
    }

    return render(request, 'programs/programs.html', context)


def program_detail(request, program_id):
    """ A view to show individual program details"""

    program = get_object_or_404(Program, pk=program_id)
    
    context = {
        'program': program
    }

    return render(request, 'programs/program_detail.html', context)