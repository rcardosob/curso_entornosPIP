import requests

url_catego = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(url_catego)
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])

