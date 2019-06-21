import datetime
now = datetime.datetime.now()


def suffix(d):
	return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
	
weekdict = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

weday = now.weekday()

day = now.day

month = now.strftime("%B")

year = now.year

hour = now.hour

minte = now.minute

hm = str(hour)+':'+str(minte)

output = weekdict[weday]+' '+str(day)+suffix(day)+" of "+str(month)+' '+str(year)+' at '+hm

print(output)



#Wednesday 1st of May 2019 at 07:05
