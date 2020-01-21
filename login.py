#!/usr/bin/env python3

import cgi
import cgitb
from templates import login_page, secret_page, after_login_incorrect
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

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page())
else:
    print(after_login_incorrect())



