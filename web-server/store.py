import requests

def get_categories():
  request = requests.get('https://api.escuelajs.co/api/v1/categories')

  print(request.status_code)
  print(request.text)
  print(type(request.text))

  categories = request.json()

  for category in categories:
    print(category['name'])
