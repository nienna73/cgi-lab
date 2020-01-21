#!/usr/bin/env python3

import cgi
import cgitb
from templates import login_page
import secret
cgitb.enable()

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html\n")
form_ok = username==secret.username and password==secret.password

if form_ok:
    print("Set-Cookie: username=", username)
    print("Set-Cookie: password=", password)
    
print()
print(login_page())
print(cgi.FieldStorage())



