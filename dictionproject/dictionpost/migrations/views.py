from django.shortcuts import render,get_object_or_404,render
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.


class BlogList(ListView):
    template_name='list.html'
    model=Product
    

class BlogDetail(DetailView):
    template_name="detail.html"
    model=Product


def topic_posts(request,pk):
        object=get_object_or_404(Product,pk=pk)
        object.views +=1
        object.save()
        return render(request,'topics.html',{"object":object})