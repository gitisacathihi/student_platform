from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    success_message = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "✅ Your information has been successfully submitted."
            
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form, 'success_message': success_message})
