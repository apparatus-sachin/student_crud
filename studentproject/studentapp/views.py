from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from .forms import *

def student_details(request):
    info = studentinfo.objects.all()
    return render(request,"student_details.html",{'info':info})

def student_add(request):
    if request.method == 'POST':
        form = studentinfoForm(request.POST,request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('student_details')
    else:
        form = studentinfoForm()
    return render(request,"student_add.html",{'form':form})


def student_edit(request,id):
    info = studentinfo.objects.get(id=id)
    form = studentinfoForm(request.POST,request.FILES,instance=info)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('student_details')
    return render(request,'student_edit.html',{'info':info})


def student_update(request,id):
    info = studentinfo.objects.get(id=id)
    return render(request,"student_add.html",{'form': form})

def student_trash(request,id):
    info = studentinfo.objects.get(id=id)
    info.delete()
    return redirect('/')