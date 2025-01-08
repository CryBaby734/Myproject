from django.shortcuts import render,redirect
from .models import Block
from .forms import BlockForm


def index(request):
    list = Block.objects.all()
    return render(request,'index.html',{'list':list})
    
def list(request):
    list = Block.objects.all()
    return render(request,'list.html',{'list':list})
    
    
def create(request):
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BlockForm()
    return render(request,'form.html',{'form':form})

def update(request,pk):
    block = Block.objects.get(id=pk)
    if request.method == 'POST':
        form = BlockForm(request.POST,instance=block)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BlockForm(instance=block)
    return render(request,'form.html',{'form':form})

def delete(request,pk):
    block = Block.objects.get(id=pk)
    block.delete()
    return render(request,'index.html')