import requests
import time
from requests.exceptions import Timeout
a = list(range(210150001,210300000))
i=1
for tokens in a:
	try:
		headers={'User-Agent':'Mozilla/5.0','Authorization':'Token be2c85854c5b7c1950ed019624d48bb04a34760c'}
		response = requests.post('https://id-api.spooncast.net/users/'+str(tokens)+'/follow/',headers=headers,timeout=1)
		response2 = requests.post('http://id-api.spooncast.net/users/'+str(tokens)+'/fanmessages/',headers=headers,json={'contents':'aca ga bisa move on dari Yora , bantu aca move on dengan cara fanback ya '},timeout=1)
		print(response)
		print(response2)
		print(i)
		i+=1
		print(tokens)
	except Timeout:
		print('ke '+str(tokens)+' gagal')
	except:
		print('error internet')
