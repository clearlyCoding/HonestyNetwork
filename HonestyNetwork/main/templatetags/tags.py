from django import template
import json
import math
register = template.Library()



@register.filter
def subtract (value, arg):
	return (value - arg)

@register.filter
def user_list (jsn):
	lst = []
	jsonLoad = json.loads(jsn)
	for keys, values in jsonLoad.items():
		lst.append(values)
	# for keys in json:
	return lst

@register.filter
def dict_values (dictz, user):
	lst=[]
	try:
		for keys,values in dictz.items():
			lst.append(values)
		if user in lst:
			return True
		else:
			return False
	except:
			return False

@register.filter
def checkUser (username, jsn):
	lst = user_list(jsn)
	if username in lst:
		return True
	else:
		return False

@register.filter
def checkremaining(set_):
	loads = json.loads(set_.setUsers)
	return (set_.setPeopleLimit - len(loads))

@register.filter
def tlate(word):
	if word == "MTHY":
		return "Months"
	elif word == "WKLY":
		return "Weeks"

@register.filter
def tlate2(word):
	if word == "MTHY":
		return "Monthly"
	elif word == "WKLY":
		return "Weekly"

@register.filter
def tlate3(word):
	if word == "MTHY":
		return "Month"
	elif word == "WKLY":
		return "Week"

@register.filter
def js_length(var):
	loads = json.loads(var)
	return len(loads)

@register.filter
def diff_paid (set_):
	count1 = len(set_.setPaid)
	count2 = js_length(set_.setUsers)
	num = count2 - count1
	return range(0,num)

@register.filter
def jsonloop(var):
	num = js_length(var)
	return range(0, num)

@register.filter
def dictloop(var):
	num = len(var)
	return range(0, num)


@register.filter
def div(var,time):
	value =math.trunc(math.ceil(var/time*100)/100)
	return value

@register.filter
def check_in(id_, IDSET):
	if id_ in IDSET:
		return False
	else:
		return True

@register.filter
def checkNone(Sets, SIDS):
	IDLIST=[]
	SIDSLIST=SIDS
	flag = True
	for Set in Sets:
		if not Set.setReady:
			IDLIST.append(Set.setID)
	print (IDLIST)
	print (SIDSLIST)
	for ID in IDLIST:
		if ID not in SIDSLIST:
			flag = False
			break

	return flag
