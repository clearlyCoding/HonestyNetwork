from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, random
from .models import SetModels
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from datetime import datetime, timezone,timedelta
from dateutil.relativedelta import relativedelta
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.conf import settings
from django.urls import reverse
import stripe, math, string

# from .forms import EmptyForm

# Create your views here.
stripe.api_key = settings.STRIPE_PRIVATE_KEY
AMT=0
def jsonCheck(json):
	try:
		a_jsn = json.loads(json)
		return True
	except:
		return False
@csrf_exempt
def makePayment(request):
	global AMT
	if request.method == "POST":
		setID = request.POST.get("authSID")
	try:
		set_ = SetModels.objects.get(setID__exact = setID )
	except:
		#add error message for not being able to retrieve details internal error contact ADMINS
		return render (request, 'main:homepage', context={})
	pubkey = settings.STRIPE_PUBLIC_KEY
	AMT = math.ceil(set_.setAmt/set_.setTime*100)
	intent = stripe.PaymentIntent.create(
		amount = AMT,
		currency = 'cad')
	context = {'client_secret':intent.client_secret, 'pubkey':pubkey, "set_":set_}
	return render(request, 'main/makePayment.html', context)

	

@csrf_exempt
def handlePay(request, *args):
	global AMT
	if request.method =='POST':
		data = json.loads(request.body)
		set_ = SetModels.objects.get(setID__exact=data['setID'])
		username = request.user.username
		try:
			intent = stripe.PaymentIntent.create(
				amount = AMT,
				currency = 'cad',
				payment_method = data['payment_method_id'],
				confirm = True,
				error_on_requires_action = True,
			)
			return HttpResponse(generate_response(intent, username, set_), content_type = "application/json")
		except stripe.error.CardError as e:
			return HttpResponse(json.dumps({'error': e.user_message}), content_type = "application/json")
		return redirect ("main:makePayment")

def thanks(request):
	return render (request, 'main/thanks.html')

def generate_response(intent, username, set_):
	global AMT

	if intent.status == 'succeeded':
		lennum = len(set_.setPaid)
		set_.setPaid[str(lennum + 1)] = username
		set_.setPaid[str(lennum + 1) + "conf-amt"] = str(AMT) 
		set_.setPaid[str(lennum + 1) + "conf-code"] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20)) #confirmationcode
		set_.save()
		# Handle post-payment fulfillment
		return json.dumps({'success': True})
	else:
		# Any other status would be unexpected, so error
		return json.dumps({'error': 'Invalid PaymentIntent status'})

###########################################################################################

def homepage(request):
	sets = SetModels.objects.all()
	sID=[]
	if request.user.is_authenticated :
		template_name = "main/dashboard.html"
		for set_ in sets:
			loaded = json.loads(set_.setUsers)
			if request.user.username in loaded.values():
				sID.append(set_.setID)
		newset = SetModels.objects.filter(setID__in=sID)
		print (newset)

		context = {"Sets": sets, "SIDS":sID, "curr_":'dashboard'}
		return render(request,template_name, context)
	else:
		return render(request = request,
				  template_name = 'main/home.html',
				  context={"Sets": SetModels.objects.all(), "curr_":'home'})

def selectedSet (request):
	sets = SetModels.objects.all()
	loadl = []
	if request.method == "POST":
		setID = request.POST.get('setID')
		sets_= SetModels.objects.get(setID__exact = setID)
		loaded = json.loads(sets_.setUsers)
		for values in loaded.values():
			loadl.append(values)
		return render(request= request,
					template_name = 'main/selectedSet.html',
					context={"set_":sets_, "curr_":'selectedSet',"names":loadl})

def sets_ (request):
	sets = SetModels.objects.all()
	sID=[]
	if request.user.is_authenticated :
		for set_ in sets:
			loaded = json.loads(set_.setUsers)
			if request.user.username in loaded.values():
				sID.append(set_.setID)
		context = {"Sets": sets, "SIDS":sID, "curr_":'sets'}
	else:
		context = {"Sets": sets, "curr_":'sets'}
	return render(request= request,
				  template_name= 'main/sets.html',
				  context= context)

def startSet (set_):
	set_.setReady = True
	set_.setStart = datetime.now(timezone.utc)
	set_.setDateLock =True

	
	if set_.setRepitations == "MTHY":
		set_.setTimeLimit = 15
		set_.setEnd = set_.setStart + relativedelta(months=set_.setTime)
	else:
		set_.setTimeLimit = 3
		set_.setEnd = set_.setStart + timedelta(days=set_.setTime*7)






def saveperson(currentuser, set_, pop):
	lst={}
	if not pop:
		try:
			curUsers = json.loads(set_.setUsers)
		except json.decoder.JSONDecodeError:
			curUsers=""
		curUserAmt = len(curUsers)
		curPos = set_.setPeopleLimit - (set_.setPeopleLimit - curUserAmt)	
		lst = json.loads(set_.setUsers)
		keyname = "user" +str(curPos+1)
		if curPos+1  == set_.setPeopleLimit:
			startSet(set_)
		lst[keyname] = currentuser.username
		set_.setUsers=json.dumps(lst,indent = 0)
		set_.save()
	else:
		try: 
			curUsers = json.loads(set_.setUsers)
		except json.decoder.JSONDecodeError:
			curUsers=""
		if not set_.setReady:
			for keys in curUsers: 
				if curUsers[keys] == currentuser.username:
					curUsers.pop(keys)
					newdict ={}
					i=1
					for keys in curUsers:
						keyname = 'user' + str(i)
						newdict[keyname] = curUsers[keys]
						i+=1
					set_.setUsers=json.dumps(newdict, indent =0)
					set_.save()
					break
		else:
			x=1+1
			#add message to contact admins to be removed

def decisionSet (request):
	sets = SetModels.objects.all()
	if request.method == "POST":
		currentuser = request.user
		response = request.POST.get('addReq')
		lvresponse = request.POST.get('LeaveSet')
		setID = request.POST.get('authSID')
		set_ = SetModels.objects.get(setID__exact = setID)
		
		if lvresponse:
			saveperson(currentuser,set_,True)
			#Add message that they have been removed
		if response == "Yes":
			
			if set_.setReady != True:
				saveperson(currentuser,set_, False)
				#add message that they have been added
	return redirect("main:homepage")


def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect ("main:homepage")

	form = UserCreationForm
	return render(request = request,
				  template_name = "main/register.html",
				  context={"form": form, "curr_":'registration'})


def logout_request(request):
	logout(request)
	messages.info(request, "Log Out Success")
	return redirect("main:homepage")



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request = request, data= request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				return redirect("main:homepage")
			else:

				messages.error(request, "Invalid user or pass")
		else:

			messages.error(request, "Invalid user or pass")

	form = AuthenticationForm()
	return render(request = request,
				  template_name = "main/login.html",
				  context={"loginform": form, "curr_":'login'})