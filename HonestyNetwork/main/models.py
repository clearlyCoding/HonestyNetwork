from django.db import models
import random
import string
import json
import datetime
# Create your models here.
class SetModels(models.Model):
	# def __init__(self):
	# 	x = 1+1

	def build_def_json(sPL):
		userslist={}
		for i  in range(1, sPL):
			userlist['user'] = ''
			json_data = json.dumps(userlist)
		return json_data
	OCCURANCE_CHOICE =(
		("WKLY", 'Weekly'),
		("MTHY", 'Monthly')
	)
	setAmt = models.IntegerField(default = 000000)
	setPeopleLimit =models.IntegerField(default = 000)
	setCity = models.CharField(max_length = 50, default ="", blank =True)
	setCityUp = models.CharField(max_length = 50, default ="" , blank =True)
	setRepitations = models.CharField(max_length = 4, choices = OCCURANCE_CHOICE, default = "MTHY")
	setTime = models.IntegerField(default = 000)
	setUsers = models.JSONField(max_length = 500000, blank = True, default = '{}') 
	setReady = models.BooleanField(default = False)
	setID = models.CharField(max_length=20, default =  ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20)), blank = False)
	setStart= models.DateTimeField()
	setEnd=models.DateTimeField()
	setUT=models.DateTimeField()
	setTimeLimit =models.IntegerField(default=0) #days
	setProgressLimit = models.JSONField(max_length = 500000, blank = True, default = '{}') #People that have passed
	setCurrentProgress = models.JSONField(max_length = 500000, blank = True, default = '{}') #People that are left
	setRepPts = models.JSONField(max_length = 500000, blank = True, default = '{}') #f(x) of users, AMT, length
	setPaid =models.JSONField(max_length = 500000, blank = True, default = dict) 
	setDateLock =models.BooleanField(default =False)
	setTest = models.JSONField(max_length = 500000, blank = True, default = dict) #People that have passed
	def __str__(self):
		return  self.setID

	# setAmt = The Amount of Money that each Set will be established for
	# setPeopleLimit = The Amount of People that can register to participate in a set
	# setCity = The City in whcih the set is occuring
	# setCityUp = The Province or State
	# setRepitations = Repetitive Unit for this set, is it monthly or weekly?
	# setTime = How many units will this set run for. Ideally, this should equal your People Limit
	# setUsers = The Users that are registered for this set, initiallized as empty
	# setReady = Boolean, triggered when set is ready
	# setID = Randomized IDs for Sets
	# setStart= Start date, not initialized by Admin
	# setEnd= End Date, not initialized by Admin
	# setUT= Universal Time, not initialized by Admin
	# setTimeLimit = TimeLimit for delinquency checks
	# setProgressLimit = Users that have received their Payouts
	# setCurrentProgress = Users that have not received their payouts. A Sorted List of Users, in order of payouts. Earliest First. 
	# setRepPts = Reputation Points Scheme Tracker
	# setPaid = Users that have made payments within TimeLimit
	# setDateLock  = Boolean, triggered when set is ready
	# setTest = Test Dictionary