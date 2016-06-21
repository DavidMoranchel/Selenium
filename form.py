import requests
page = 'http://viavanilla.com/index.php?route=information/contact'
info = {
	'name':'David',
	'email':'david.arcshtag',
	'enquiry':'Increibles lentes'

}

r = requests.post(page,data=info)
print(r.text)