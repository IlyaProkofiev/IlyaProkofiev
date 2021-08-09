import requests

requests.post('https://petstore.swagger.io/v2/user',
              data={"id": "1",
                    "username": "User1",
                    "firstName": "Ilya",
                    "lastName": "Prokofiev",
                    "email": "gsi@mail.ru",
                    "password": "richard",
                    "phone": "+375",
                    "userStatus": "1"})

link = 'https://petstore.swagger.io/v2/user/User1'

r = requests.get(link)
if r.status_code == 200:
    print ('User created')
else:
    print('User doesnt exist')

requests.put(link,
             data={"id": "1",
                   "username": "User1",
                   "firstName": "Ilias",
                   "lastName": "Prokofyeu",
                   "email": "gsi@yandex.ru",
                   "password": "richard",
                   "phone": "+37529",
                   "userStatus": "1"})

r = requests.get(link)
if r.status_code == 200:
    print ('User updated')
else:
    print('Fail: user was not updated')

requests.delete(link)
r = requests.get(link)
if r.status_code == 200:
    print ('User deleted')
else:
    print('User was not deleted')

r = requests.get(link)
if r.status_code == 404:
    print ('User is not existing')
else:
    print('Try again')
