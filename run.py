#!/usr/bin/python

R='\033[31;1m'
W='\033[37;1m'

import os
import smtplib
import getpass
import sys

os.system("clear")
print R + "[=======================================================>"
print R + "[+] \033[37;1mAuthor \033[31m: \033[37;1mGunadiCBR"
print R + "[+] \033[37;1mDate \033[31m  : \033[37;1m01-10-2018" 
print R + "[+] \033[37;1mGithub \033[31m: \033[37;1mhttps://github.com/afelfgie"
print R + "[=======================================================>"
print " "
server = raw_input ('\033[39;1mMailServer \033[31;1mgmail \033[37;1mor \033[31;1myahoo : \033[32;1m')
print " "
user = raw_input('\033[31mEmail:\033[37;1m ')
passwd = getpass.getpass('\033[31mPassword:\033[37;1m ')


to = raw_input('\n\033[31mTo:\033[37;1m ')
#subject = raw_input('Subject: ') 
body = raw_input('\033[31mMessage:\033[37;1m ')
total = input('\033[31mNumber of send:\033[37;1m ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    os.system("python2 run.py")
