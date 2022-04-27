import json

import os
from HonestyNetwork import wsgi
from main import views
import random
import string
from main.models import SetModels
from datetime import datetime, timezone



class Management():

	def checkDateLock (self, set_):
		if set_.setDateLock == True:
			return True
		else:
			return False
	def dateDifference (self, set_):
		lst=[]
		now = datetime.now(timezone.utc)
		difmth = now.month - set_.setStart.month
		difday = now.day - set_.setStart.day
		difhour = now.hour - set_.setStart.hour
		difmin  = now.minute - set_.setStart.minute
		lst = [difmth,difday,difhour,difmin]
		return difday

	def depositAware(set_):
		if set_.setRepitations == "MTHY":
			if self.dateDifference(set_)+set_.setTimeLimit == 30 + (30*self.countDict(set_.setProgressLimit)):
				return True
			else:
				return False
		else: 
			if self.dateDifference(set_)+set_.setTimeLimit == 7 + (7*self.countDict(set_.setProgressLimit)):
				return True
			else:
				return False
	def orderList(self, set_):

		if self.countDict(set_.setCurrentProgress)==0:
			newdict={}
			lst=[]
			n=0
			loads = json.loads(set_.setUsers)
			values = loads.values()
			for value in values:
				lst.append(value)
			values = random.sample(lst, len(lst))
			for keys in loads.keys():
				newdict[keys] = values[n]
				n+=1
			set_.setCurrentProgress = json.dumps(newdict)
			set_.save()
			print ("Ordered List for ", set_.setID)

	def sendNotification (self, set_):
		return True

	def countDict(self,jsn):
		loads = json.loads(jsn)
		return (len(loads))

	def progress(self, set_): #this progresses the set forward, increments the users in the set so that the payout is for the next person in the sorted list. 
		load_c = json.loads(set_.setCurrentProgress)
		load_p = json.loads(set_.setProgressLimit)
		popuser=''
		for keys,values in load_c.items():
			load_p[keys]= values
			popuser = values
			load_c.pop(keys)
			break
		set_.setProgressLimit = json.dumps(load_p)
		set_.setCurrentProgress = json.dumps(load_c)
		set_.save()
		return popuser

	def checkSets(self):
		breakflag =False
		m=12
		sets = SetModels.objects.all()
		iteration = 0
		while True:
			for set_ in sets:
				if set_.setReady and self.checkDateLock(set_):

					#order the list randomly - will need to add reputation handling
					self.orderList(set_) #setCurrentProgress Established

					#send notification to the Users of the Set
					self.sendNotification(set_)
					#check the date difference to see if the Set's length (monthly, weekly) half point is reached
					if self.dateDifference (set_) == set_.setTimeLimit:
						print ("Notify Users of Deposits Open")

						#if the date difference from start to timelimit+(timelimit*progress)
						if self.depositAware(set_):
							UserWithdraw = self.progress(set_)
							print("DO WITHDRAWL for ", UserWithdraw)
							#CREATE PROGRESSLIMIT FOR USERS
					#calculate deltas in Time
					#call in TimeLimit Function
					#assign reputations





if __name__ == "__main__":
	sMGR = Management()
	sets = SetModels.objects.all()
	for sets_ in sets:
		print(sets_.setTest.keys())
		print(sets_.setTest.values())
	# for set_ in sets:
	# 	# sMGR.progress(set_)
	# 	print(set_.setCurrentProgress)

	# sMGR.checkSets()


