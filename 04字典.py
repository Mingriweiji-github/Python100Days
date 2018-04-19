#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import requests
#response = requests.get('https://httpbin.org/ip')
#print('Your IP is {0}'.format(response.json()['origin']))

#dict = {'a':1,'b':2,'c':3,'d':4}
#print(dict)
#print(dict['a'])
#print(dict['f'])
#print(dict.get('f',6))

#d = {}
#if 'list' not in d:
#	d['list'] = []
#	d['list'].append(1)
#	
##	print(d['list'])
#d.setdefault('list', []).append(2)
#print(d['list'])
#d = {'a': 61, 'b': 62, 'c': 63, 'd': 64, 'e': 65}
#for(key,value) in d.items():
#	print(key,value)

#字典的魔术方法
class MyDic(dict):
	def __missing__(self,key):
		if key.islower():
			raise keyError(key)
		else:
			return self[key.lower()]			
d = MyDic({'a':61})
'A' in d
print(d['A'])

