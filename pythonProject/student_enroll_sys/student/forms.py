from django import forms


class StudentForm(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student Name')
    s_father_name = forms.CharField(max_length=30,label='Student Fathers Name')
    s_contact_no = forms.CharField(max_length=30,label='Student contact number')
    s_parent_c_no = forms.CharField(max_length=30,label='Student parent contact')
    s_course_id = forms.CharField(max_length=30,label='Student Course Name')
    s_program_id = forms.CharField(max_length=30,label='Student Program')
    s_addr = forms.CharField(max_length=30,label='Student Address')
    s_batch = forms.CharField(max_length=30,label='Student Batch')
    s_email = forms.CharField(max_length=30,label='Student email id')
    s_date = forms.CharField(max_length=30,label='Student Date of join')


class Sform(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student Name')


