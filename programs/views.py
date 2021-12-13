from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Program
from .forms import ProgramForm

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


def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program successfully added!')
            return redirect(reverse('add_program'))
        else:
            messages.error(request, 'Addition failed. Please make sure all inputs are correct.')
    else:
        form = ProgramForm()

    template = 'programs/add_program.html'
    context = {
        'form': form,
    }

    return render(request, template, context)