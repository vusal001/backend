import requests
from pprint import pprint

def client():
    many = {
        'username': 'newuser6',
        'first_name': 'Namik',
        'email': 'nenem5@mail.ru',
        'password1': 'test123...',
        'password2': 'test123...',
        
    }

    response = requests.post(
        url= 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data= many,
    )

    print('Status', response.status_code)

    response_data = response.json()

    pprint(response_data)


if __name__ == '__main__':
    client()