from django.shortcuts import render

from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io




def cvpdf(request):
    
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous','')
        skills = request.POST.get('skills','')
        
        cv_data = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        cv_data.save()
    return render (request, 'pdf/accept.html',{})


def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    context = {
        "user_profile":user_profile
    }
    
    template = loader.get_template('pdf/resume.html')
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,options)
    response =  HttpResponse(pdf,content_type='application/pdf')
    response['content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response


def resumelist(request):
    profile = Profile.objects.all()
    context = {
        "profiles":profile
    }
    return render(request,'pdf/resumelist.html',context)