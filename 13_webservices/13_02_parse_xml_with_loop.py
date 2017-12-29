import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

tree = ET.fromstring(data)

users = tree.findall('users/user')
print('User count: ', len(users))

for item in users:
    print('Id: ', item.find('id').text)
    print('Name: ', item.find('name').text)
    print('Attribute: ', item.get('x'))
