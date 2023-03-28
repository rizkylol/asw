#Reverse MultiThread Unlimited 
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
##############################
#####################################
import requests, re, urllib2, os, sys, codecs, random	
import requests_random_user_agent				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from random import randint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

          $$\           $$\                  $$$$$$\  $$$$$$$$\ 
          \__|          $$ |                $$$ __$$\ \____$$  |
 $$$$$$\  $$\ $$$$$$$$\ $$ |  $$\ $$\   $$\ $$$$\ $$ |    $$  / 
$$  __$$\ $$ |\____$$  |$$ | $$  |$$ |  $$ |$$\$$\$$ |   $$  /  
$$ |  \__|$$ |  $$$$ _/ $$$$$$  / $$ |  $$ |$$ \$$$$ |  $$  /   
$$ |      $$ | $$  _/   $$  _$$<  $$ |  $$ |$$ |\$$$ | $$  /    
$$ |      $$ |$$$$$$$$\ $$ | \$$\ \$$$$$$$ |\$$$$$$  /$$  /     
\__|      \__|\________|\__|  \__| \____$$ | \______/ \__/      
                                  $$\   $$ |                    
                                  \$$$$$$  |                    
                                   \______/                     

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()
print ("""
1. osint.sh Revip
2. sonar.omnisint Revip
3. tntdomains Revip
4. Bing AllDomains
5. Bing Dork
6. Bing Revip
7. HTTP Weblist
8. Scanner Clear
9. IP From Weblist
10. dns-osint.net revip

""")

nels = raw_input("root@Jancok:~# ")

class males():
	def alldomains(self):
		iya = raw_input("List@Dork:~  ")
		iya = open(iya, 'r')
		for asw in iya:
			dom = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
				'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
				'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
				'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
				'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
				'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
				'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
				'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
				'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
				'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
				'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it',
				'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
				'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
				'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
				'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
				'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
				'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
				'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
				'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
				'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
				'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
				'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
				'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
				'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
				'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
				'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel',
				'name', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 'museum',
				'pro', 'travel']
			for udah in dom:
				tam = []
				pages = 1
				while pages < 159:
					bing = "https://www.bing.com/search?q="+asw+' site:.'+udah+"+&count=50&first="+str(pages)
					rek = requests.get(bing,verify=False)
					eee = rek.content
					nemu = re.findall('<h2><a href="(.*?)"', eee)
					for o in nemu:
						i = o.split('/')
						if (i[0]+'//'+i[2]) in tam:
							pass
						else:
							tam.append(i[0]+'//'+i[2])
							print '[>>]',(i[0]+'//'+i[2])
							with open('AllDomains.txt', 'a') as s:
								s.writelines((i[0]+'//'+i[2])+'\n')
					pages = pages+50

	def randomdomen(self):
		bo = raw_input("List@Dork:~# ")
		bo = open(bo, 'r')
		for oaja in bo:
			sa = []
			tu = 1
			while tu < 159:
				bing0 = "https://www.bing.com/search?q="+oaja+"+&count=50&first="+str(tu)
				iyoo = requests.get(bing0,verify=False)
				rrr = iyoo.content
				sip = re.findall('<h2><a href="(.*?)"', rrr)
				for i in sip:
					o = i.split('/')
					if (o[0]+'//'+o[2]) in sa:
						pass
					else:
						sa.append(o[0]+'//'+o[2])
						print '[>>]',(o[0]+'//'+o[2])
						with open('Random.txt', 'a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				tu = tu+50

	def grabip(self):
		oooke = raw_input("List@IP:~# ")
		oooke = open(oooke, 'r')
		for zzzzz in oooke:
			bo = []
			lonk = 1
			while lonk < 299:
				bingung = "https://www.bing.com/search?q=IP%3A"+zzzzz+"+&count=50&first="+str(lonk)
				iyagw = requests.get(bingung,verify=False)
				gans = iyagw.content
				ya = re.findall('<h2><a href="(.*?)"', gans)
				for z in ya:
					o = z.split('/')
					if (o[0]+'//'+o[2]) in bo:
						pass
					else:
						bo.append(o[0]+'//'+o[2])
						print '[>>]',(o[0]+'//'+o[2])
						with open('Grab.txt','a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				lonk = lonk+50

	def revsip(self):
		oke = raw_input("List@IP:~# ")
		oke = open(oke, 'r')
		for zz in oke:
			Exp = 'https://osint.sh/reverseip/'
			grab = requests.post(Exp, data={"domain": zz }, timeout=10).text
			if '/domain' in grab:
				res = re.findall('<td data-th="Domain">\n(.*?)<',grab)
				for rr in res:
					resk = rr.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','').replace('                    ','').replace('mta-sts.','').replace('    ','error')
					print(kuning+'[+]' + str(resk) + ijo +' '+  '>' +'OK')
					open('osint.txt', 'a').write('http://'+resk+'\n')
				else:
					print(kuning+"[+]" + str(zz) + abang + " " + ">" +" error can't reslove domain")

	def revsipp(self):
		ooke = raw_input("List@IP:~# ")
		ooke = open(ooke, 'r')
		for zzz in ooke:
			Expp = 'https://sonar.omnisint.io/reverse/'+zzz
			grabb = requests.get(Expp, timeout=10)
			if '{"error":' in grabb.text:
				print(kuning+'[+]' + zzz + abang + '>' +'Failed')
			else:
				result = json.loads(grabb.text)
				print(kuning+'[+]' + birtu+'IP :'+' ' +ijo + str(zzz) +' '+'Total Domain =>' ), len(result)
				for rrr in result:
					reskk = rrr.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','').replace('mta-sts.','').replace('smtp.','')
					print(kuning+'[+]' + str(reskk) + ijo +' '+  '>' +'OK')
					open('sonar.txt', 'a').write('http://'+reskk+'\n')
				else:
					print(kuning+"[+]" + str(zzz) + abang + " " + ">" +" error can't reslove domain")

	def revsiipp(self):
		ookke = raw_input("List@IP:~# ")
		ookke = open(ookke, 'r')
		for zzzz in ookke:
			Exxpp = 'https://domains.tntcode.com/ip/'+zzzz
			graabb = requests.get(Exxpp, timeout=10).text
			if '/domain/' in graabb:
				reess = re.findall('/domain/(.*?)"',graabb)
				for rrrr in reess:
					print(kuning+'[+]' + str(rrrr) + ijo +' '+  '>' +'OK')
					open('tntrevip.txt', 'a').write('http://'+rrrr+'\n')
				else:
					print(kuning+"[+]" + str(zzzz) + abang + " " + ">" +" error can't reslove domain")

	def reviposint(self):
		ookkee = raw_input("List@IP:~# ")
		ookkee = open(ookkee, 'r')
		for zzzzz in ookkee:
			apikey = "4T9UkbcItYI"
			Eexxpp = 'https://www.dns-osint.net/reverse/'+apikey+'/'+zzzzz
			revip = requests.get(Eexxpp, timeout=10)
			if '{"status":"success"' in revip.text:
				reff = json.loads(revip.text)["data"]
				for res in reff:
					asal = res.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','').replace('mta-sts.','').replace('smtp.','')
					print(kuning+'[+]' + str(asal) + ijo +' '+  '>' +'OK')
					open('dnsosint.txt', 'a').write('http://'+asal+'\n')
				else:
					print(kuning+"[+]" + str(asal) + abang + " " + ">" +" error can't reslove domain")

	def http(self):
		kep = raw_input("List@Sites:~# ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print("http://"+i)
			with open('HTTP.txt', 'a') as o:
				o.write("http://" + i + '\n')
		print("[>>] D0N3! Check HTTP.txt")

	def clean(self):
		print ("URL LIST WITHOUT HTTP://")
		oh = raw_input("List@Sites:~#")
		oh = open(oh, 'r')
		for i in oh:
			i = i.rstrip()
			with open("Cleaner.txt", 'a') as f:
				f.write(i.split('/')[0] + '\n')
		print('[>>] D0N3! Check Cleaner.txt')

	def getip(self):
		hooh = raw_input("List@IP:~# ")
		hooh = open(hooh, 'r')
		for i in hooh.readlines():
			done = i.rstrip()
			try:
				done = done.rstrip()
				bine = requests.get('http://api.hackertarget.com/reverseiplookup/?q='+done)
				if '.' in bine.content:
					print ("[>>]" + (bine.content))
					with open('site.txt', 'a') as o:
						o.writelines(bine.content + '\n')
				else:
					pass

			except:
				pass


dahah = males()
if nels == '1':
	dahah.revsip()
elif nels == '2':
	dahah.revsipp()
elif nels == '3':
	dahah.revsiipp()
elif nels == '4':
	dahah.alldomains()
elif nels == '5':
	dahah.randomdomen()
elif nels == '6':
	dahah.grabip()
elif nels == '7':
	dahah.http()
elif nels == '8':
	dahah.clean()
elif nels == '9':
	dahah.getip()
elif nels == '10':
	dahah.reviposint()
else:
	print("?")
	
