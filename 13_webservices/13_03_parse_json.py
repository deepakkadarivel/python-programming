import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]
'''

users = json.loads(data)
print('count: ', len(users))

for user in users:
    print('Name: ', user['name'])
    print('Id: ', user['id'])
    print('Attribute: ', user['x'])
