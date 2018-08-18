# Create your views here.
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.http import HttpResponse
from models import Person

class PersonForm(ModelForm):
	class meta:
		model = Person
@csrf_exempt
def create_account(request):
	account = bank.object.all()
	#start form code
	if request.method == 'POST':
		form =PersonForm(request.Post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
		form = PersonForm()
    		t=loader.get_template('bank/home.html')
    		c= Context({'homeform':homeform.as_p()})
    		return HttpResponse(t.render(c))


def viewMoney(request, id):
	p = Person.objects.get(id=id)
	print p
	t = loader.get_template('bank/view.html')
	# print p.amount
	c = Context({'person':p})
	return HttpResponse(t.render(c))
'''
def secretDeposit(request):
	if ispost....
		add moneey to person
		return HttpResponse - just deposititedd!
	make a form with only money a single money field
	show the form
'''
# Create your views here.

class TransferForm(forms.Form):
	fromp = forms.IntegerField()
	top = forms.IntegerField()
	amount = forms.FloatField()
	def __unicode__(self):
		return self.From
@csrf_exempt
def transfer(request):
	'''transfer = transferForm.objects.all()
	for Person.accnum == transfer.From:
		Person.amount= Person.amount -transfer.amount
	for Person.accnum == transfer.To:
		Person.amount = Person.amount + transer.amount'''
	if request.method == 'POST':
		fromp = Person.objects.get(accnum=int(request.POST['fromp']))
		top = Person.objects.get(accnum=int(request.POST['top']))		
		fromp.amount -= int(request.POST['amount'])
		fromp.save()
		top.amount += int(request.POST['amount'])
		top.save()
		return HttpResponse('Done transfer')
	form = TransferForm()
	t = loader.get_template('bank/transfer.html')
	c = Context({'form':form})
	return HttpResponse(t.render(c))



class homeForm(ModelForm):
	class meta:
		exclude =['dob','phone','email','address','created','amount']

def homepage(request):
	home = homeForm.object.all()
	if request.method == 'POST':
		form =homeForm(request.Post)
		if form.is_valid():
			return HttpResponseRedirect('home/report.html')
	


