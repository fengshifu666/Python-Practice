import time
import requests
from tqdm import tqdm

def catalogscan(URL):
	time.sleep(1)
	try:
		status=requests.get(URL,headers=headers,proxies=proxies)
		if status.status_code in range(0,400):
			print('\n',URL,status.status_code)
	except:
		print('connection wrong')


headers = {
    'Content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
                  ' x64) AppleWebKit/537.36 (KHTML, like'
                  ' Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Cookie': 'JSESSIONID=123456789;name=value'
}

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
}
domain=input('please input your scan domain:')
domain=domain if domain.startswith('http') else 'http://' + domain
with tqdm(total=len(open('catalog.txt','r').readlines())) as pbar:
	for x in open('catalog.txt','r'):
		host=domain+x
		catalogscan(host.strip('\n'))
		pbar.update(1)