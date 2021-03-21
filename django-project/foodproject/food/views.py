from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView

from .models import Item
from .forms import ItemForm


def index(request):
    #return HttpResponse("hello")
    item_list = Item.objects.all()
    return render (request, 'food/index.html',{'item_list':item_list})


class IndexClassBasedView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name  = 'item_list'
    
    
class DetailClassBasedView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

def item(request):
    return HttpResponse("item")


def detailView(request, item_id):
    item_data = Item.objects.get(pk=item_id)
    context = {
        "item":item_data
    }
    #return HttpResponse("this is item id:%s" %item_id)
    return render(request,'food/detail.html',context)


class CreateClassBasedView(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user  
        return super().form_valid(form)
        
        
   


def createItem(request):
    form = ItemForm(request.POST or None)
    context = {"form":form }
    if form.is_valid():
        form.save()
        return redirect('food:index')

    
    return render(request,'food/item-form.html', context)


def updateItem(request,id):
    item = Item.objects.get(id=id)
    print(item)
    form = ItemForm(request.POST or None, instance=item)
    context = {'form':form,'item':item}
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html',context)
    
    

def deleteItem(request,id):
        item = Item.objects.get(id=id)
        if request.method == 'POST':
            item.delete()
            return redirect('food:index')
        return render(request,'food/item-delete.html',{'item':item})