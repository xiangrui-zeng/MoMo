#encoding: utf8
import aiohttp, asyncio  
from termcolor import colored
from requests import get
import re
import time

def getProxy(completion, TargetNum, proxynum, ProxyList):
    global proxies

    if completion >= TargetNum: return 0
    print('[+] %s' %colored('get proxy...', 'blue', attrs=['bold']), end='')
    
    while 1:
        try:
            url = 'http://www.66ip.cn/mo.php?tqsl=%s' %proxynum
            html = get(url).text
            proxies = set(re.findall('([0-9].+)<br />', html)) - set(ProxyList)

            if not len(proxies): 
                print('\n  [-]Waiting')
                time.sleep(3)
                continue
            
            print(colored('[%d]' %len(proxies), 'yellow', attrs=['bold'] ), '%s' %(colored('Done!', 'green', attrs=['bold'])))
            return 1
        except: 
            print('  [-]Waiting')
            time.sleep(5)
    

async def autoVisit(proxy, sem):  
    global ProxyList, completion
    async with sem:  
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url='', proxy='http://'+proxy, timeout=5) as resp:  # Your url
                    print('[%s]' %colored(proxy, 'cyan', attrs=['bold']), colored('Successfully!', 'green', attrs=['bold']))
                    ProxyList.append(proxy)
                    completion += 1
            except Exception as e:
                print('[%s] Failed!' %proxy)


proxies = []
ProxyList = []
completion = 0

# how many proxies you want to 
# get in one request of free proxy site
proxynum = 100 

# how many visition your want to get
TargetNum = 40

loop = asyncio.get_event_loop()   
sem = asyncio.Semaphore(proxynum) #
while getProxy(completion, TargetNum, proxynum, ProxyList): 
    tasks = [asyncio.ensure_future(autoVisit(i, sem)) for i in proxies]  
    loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
print(colored(completion, 'yellow', attrs=['bold']))
