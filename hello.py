#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()

print("Content-Type: text/html\n")
print()
print(os.environ)