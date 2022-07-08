from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateItem

def mainpage(request):
   if request.method == 'POST':
         sname=request.POST['Sname']
         fname=request.POST['Fname']
         mname=request.POST['Mname']
         age=request.POST['Age']
         add=request.POST['Address']
         contact=request.POST['Contact']
         disease=request.POST['Dropdown']
         specifydisease=request.POST['Specify']
         plan=request.POST['Dropdown2']
         total=request.POST['Total']
         data = Item.objects.create(sname=sname, fname=fname, mname=mname, age=age, add=add, contact=contact, disease=disease,
         specifydisease=specifydisease, plan=plan, total=total)
         data.save()
   return render(request, 'mainpage.html')

def page2 (request):
   if request.method == 'POST':
      ExercisePlan.objects.create(intensity=request.POST['intensity'],
         focus=request.POST['focus'])
   page2storage=ExercisePlan.objects.all()
   return render(request, 'page2.html',{'planstorage':page2storage})

def page3 (request):
   if request.method == 'POST':
      Program.objects.create(DietPlan=request.POST['diet'],
         Trainer=request.POST['trainer'],
         Duration=request.POST['date2'])
   page3storage=Program.objects.all()
   return render(request, 'page3.html',{'programstorage':page3storage})
   
def page4 (request):
   if request.method == 'POST':
      Products.objects.create(protein=request.POST['whey'],
         gymbags=request.POST['bag'],
         mat=request.POST['mat'],
         others=request.POST['RB'],
         Loss=request.POST['loss'],
         locker=request.POST['choice'])
   page4storage=Products.objects.all()
   return render(request, 'page4.html',{'productstorage':page4storage})

def page5(request):
   item=Item.objects.all()
   storage=Products.objects.all()
   page3storage=Program.objects.all()
   page2storage=ExercisePlan.objects.all()
   return render(request, 'page5.html',{'Products':storage, 'Item':item, 'Program':page3storage, "ExercisePlan":page2storage})

def removepage(request, id):
    p = Products.objects.get(id=id)
    for x in Products.objects.only('id'):
        if p == x:
            x = Products.objects.get(id=id).delete()
            break
    return redirect('/page5')

def edit(request, id):
	item = Item.objects.get(id=id)
	form = CreateItem(instance=item)
	if request.method == 'POST':
		form = CreateItem(request.POST, instance = item)
		if form.is_valid():
			form.save()
			return redirect('/page5')

	return render(request, 'edit.html', {'form':form})