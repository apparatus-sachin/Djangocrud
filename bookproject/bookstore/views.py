from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404

from .models import store
from .forms import storeForm


def list(request):
	book = store.objects.all()
	return render(request,"list.html",{'book':book})

def add(request):
	if request.method == 'POST':
		form=storeForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('list')
	else:
		form = storeForm()
	return render(request,"add.html",{'form':form})



def edit(request,id):
	book=store.objects.get(id=id)
	form= storeForm(request.POST,request.FILES,instance=book)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'edit.html',{'book':book})
	
def update(request,id):
	book = store.objects.get(id=id)
	return render(request,'edit.html',{'form':form})


def delete(request,id):
	Book = store.objects.get(id=id)
	Book.delete()
	return redirect('/')
	
