#!/usr/bin/python

import os, re
from collections import OrderedDict


root='/Personal/B-Sorted/Astronomy/DSO/20-Stacks/'
#root='D:\\B-Sorted\\Astronomy\\DSO\\20-Stacks\\'
path=os.path.join(root,raw_input('Please provide the folder under '+root+' to your DSS html files: '))

files=[]
htmls=[]
expTimes=[]
totalsubs=[]
Filters={}
L='               -  '
Ha='              -  '
R='               -  '
G='               -  '
B='               -  '
htmls=[fn for fn in os.listdir(path) if 'html' in fn]

print
print 'Scanning '+path+' and found these files:'
print htmls
print
for fn in htmls:
	datetimes=[]
	subs=[]
	temps=[]
	obj=open(os.path.join(path,fn)).readlines()
	#exptimes=[t for t in obj if 'total exposure' in t]
	for i,s in enumerate(obj):
		if 'title' in s:
			title=obj[i].split()[-1].rstrip('</title></head>')
			COLOR=title[-1:]
		if 'A-Inbox' in s:
			for t in s.split('<br>'):
				T=[t for t in s.split('<br>')]
			try:
				T.remove('<b>Flat</b>')
				T.remove('\r\n')
			except:
				pass
			for t in T:
				try:
					obj=t.split('\\')[4].split('-')[0]
					date=t.split('\\')[4].split('-')[-1]
					time=t.split('\\')[-1].split('_')[3]
					datetimes.append(date+'-'+time)
					
					filter=t.split('\\')[5]

					sub=t.split('\\')[-1].split('_')[0]
					subs.append(int(sub.strip('sec')))
		
					temp=t.split('\\')[-1].split('_')[4].strip('C')
					temps.append(float(temp))

				except:
					pass
	print '================================================='
	print filter+' '+(datetimes)[0]+' to '+sorted(datetimes)[-1]
	#print filter+' '+re.sub('[^0-9]','',times[0])+' to ' +re.sub('[^0-9]','',times[-1])
	m, s = divmod(sum(subs), 60)
	h,m=divmod(m,60)
	print 'Total time: '+str(len(subs))+' x '+str(sum(subs)/len(subs))+'s = '+str(h)+'h '+str(m)+'m '+str(s)+'s'
	print 'Average temp in Celsius is: '+str(round(sum(temps)/len(temps),1))
	print '================================================='
	if filter == 'R':
		R=str(len(subs))+'x'+str(sum(subs)/len(subs))+'s='+str(h)+'h:'+str(m)+'m  -  '
		totalsubs.extend(subs)
	if filter == 'G':
		G=str(len(subs))+'x'+str(sum(subs)/len(subs))+'s='+str(h)+'h:'+str(m)+'m\r\n'
		totalsubs.extend(subs)
	if filter == 'B':
		B=str(len(subs))+'x'+str(sum(subs)/len(subs))+'s='+str(h)+'h:'+str(m)+'m\r\n'
		totalsubs.extend(subs)
	if filter == 'L':
		L=str(len(subs))+'x'+str(sum(subs)/len(subs))+'s='+str(h)+'h:'+str(m)+'m\r\n'
		totalsubs.extend(subs)
	if filter == 'Ha':
		Ha=str(len(subs))+'x'+str(sum(subs)/len(subs))+'s='+str(h)+'h:'+str(m)+'m  -  '
		totalsubs.extend(subs)
	try:
                M,S=divmod(sum(totalsubs),60)
                H,M=divmod(M,60)
                TOTAL=str(H)+'h:'+str(M)+'m'
        except:
                pass
try:
        print '\r\n\r\n\r\n'
        print 'Ha='+Ha+'L='+L+'R='+R+'G='+G+'B='+B
        print '\r\n\r\n\r\n'
        print 'Total = '+TOTAL
except:
        pass
