import requests

# send post request to login website
start_url = 'https://pythonscraping.com/pages/cookies/welcome.php'
payload = {'username': 'Morvan', 'password': 'password'}

session = requests.Session()
r = session.post(start_url, data=payload)
print(r.url)
print(r.text)
print(r.cookies.get_dict())

# retrieve profile page with cookie
profile_url = 'https://pythonscraping.com/pages/cookies/profile.php'
profile = session.get(profile_url)
print(r.url)
print(r.text)

