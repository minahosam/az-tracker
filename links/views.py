from django.shortcuts import render , redirect
from .forms import *
from .models import *
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    error = None
    no_discounted = 0
    if request.method=='POST':
        form = linkForm(request.POST)
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = 'ops--------------couldnot get the name of tracked order'
        except:
            error='ops-----something went error'
    else:
        form = linkForm()
        print('ss')
    qs=link.objects.all()
    all_tracked_items=qs.count()
    if all_tracked_items > 0 :
        discounted_list=[]
        for item in qs:
            if item.old_price > item.current_price:
                discounted_list.append(item)
            no_discounted=len(discounted_list)
    return render(request,'links/main.html',{'error':error,'no_discounted':no_discounted,'qs':qs,'all_tracked_items':all_tracked_items,'form':form})
class deleteLink(DeleteView):
    model = link
    template_name = 'links/confirm_delete.html'
    success_url = reverse_lazy('home:home')
def update(request):
    qs=link.objects.all()
    for item in qs:
        item.save()
    return redirect ('home:home')