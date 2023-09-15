from django.shortcuts import render
from .forms import StudentForm, Sform
from .models import student


# Create your views here.
def show(request):
    return render(request, "home.html")


def register(request):
    title = "New Student Registration"
    form = StudentForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['s_name']
        father_name = form.cleaned_data['s_father_name']
        student_contact_no = form.cleaned_data['s_contact_no']
        parent_contact_no = form.cleaned_data['s_parent_c_no']
        course_name = form.cleaned_data['s_course_id']
        program_name = form.cleaned_data['s_program_id']
        address = form.cleaned_data['s_addr']
        Batch = form.cleaned_data['s_batch']
        email_id = form.cleaned_data['s_email']
        Date_of_joining = form.cleaned_data['s_date']
        email = student.objects.filter(s_email=email_id)
        if len(email) > 0:
            return render(request, 'ack.html', {"title": "Student Already Exists...Try with another email"})
        else:
            p = student(s_name=name,
                        s_father_name=father_name,
                        s_contact_no=student_contact_no,
                        s_parent_c_no=parent_contact_no,
                        s_course_id=course_name,
                        s_program_id=program_name,
                        s_addr=address,
                        s_batch=Batch,
                        s_email=email_id,
                        s_date=Date_of_joining
                        )
            p.save()
            return render(request, 'ack.html', {"title": "Registration Completed Successfully"})

    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'register.html', context)


def existing(request, quertset=None):
    title = "All Registered Students"
    queryset = student.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'existing.html', context)


def search(request):
    title = "Search Student"
    form = Sform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = student.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request, 'ack.html', {'title': "Student Does not exist...Please enter correct data "})
        context = {
            'title': title,
            'queryset': queryset,
        }
        return render(request, 'existing.html', context)

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'search.html', context)


def dropout(request):
    title = "Drop Out"
    form = Sform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = student.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request, 'ack.html', {'title': "Student Does not exist...Please enter correct data "})
        else:
            queryset = student.objects.filter(s_name=name).delete()
            return render(request, 'ack.html', {'title': "Student removed from Database"})

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'drop.html', context)
