import requests

# send post request to login website
start_url = 'https://pythonscraping.com/pages/cookies/welcome.php'
payload = {'username': 'eric', 'password': 'password'}

r = requests.post(start_url, data=payload)
print(r.url)
print(r.text)
print(r.cookies.get_dict())

# retrieve profile page with cookie
profile_url = 'https://pythonscraping.com/pages/cookies/profile.php'
profile = requests.get(profile_url, cookies=r.cookies)
print(r.url)
print(r.text)

