import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/6a99f146537c10ce0eba4626/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
