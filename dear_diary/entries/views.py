from django.shortcuts import render,redirect
from .models import entry
from .forms import EntryForm
# Create your views here.
def index(request):
    entries=entry.objects.order_by('-date')
    context={'entries':entries}
    return render(request,'index.html',context)

def add(request):
    if(request.method=='POST'):
        form =EntryForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    else:
        form=EntryForm()
    form =EntryForm()
    context={'form':form}
    return render(request,'add.html',context) 