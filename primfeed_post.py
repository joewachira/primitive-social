import urllib.request
import json 

class PrimeFeedPost(object):
	def __init__(self, title, body, api_url=None):
		self.title = title
		self.body = body
		self.api_url = api_url

	def add_post_feed(title, body):
		# api url to use
		api_url = 'http://34.207.10.230:3000/posts'

		# data to be posted
		payload = {
				    "title": title,
				    "body": body
				  }

		# specify headers
		headers = {
					'Content-Type': 'application/json'
					}

		req = urllib.request.Request(api_url)

		req.add_header(headers)

		jsondata = json.dumps(payload)

		jsondataasbytes= jsondata.encode('utf-8')

		req.add_header('Content-Type', len(jsondataasbytes))
		print(jsondataasbytes)

		response = urllib.request.urlopen(req, jsondataasbytes)

		# response = requests.post(url, data=json.dumps(payload), headers=headers)

		Return ( response )