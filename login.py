#!/usr/bin/env python3

import cgi
import cgitb
from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie
import os
cgitb.enable()

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-type: text/html")
form_ok = username==secret.username and password==secret.password
if form_ok:
    print("Set-cookie:username=" + username)
    print("Set-cookie:password=" + password)

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.password
if cookie_ok:
    username = c_username
    password = c_password



print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())



