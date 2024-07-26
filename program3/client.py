import requests
url='http://127.0.0.1:5000/data'
data={'name':'bellingoal',
      'age':21,
      'team':'RMA'}
response=requests.post(url,json=data)
print(response.json())