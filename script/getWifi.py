import subprocess
import concurrent.futures

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode(errors='replace').split('\n')
profiles =[i.split(':')[1][1:-1] for i in data if "All User Profile" in i]
print(profiles)
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as e:
    for hostinfo in e.map(lambda i: print(i +'='+ [b.split(':')[1][1:-1] for b in subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode(errors='replace').split('\n') if 'Key Content' in b][0] + '\n',end=''), profiles):
        pass
input()
