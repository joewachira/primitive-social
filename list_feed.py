from urllib import request, parse


def create_post():
  url = 'http://34.207.10.230:3000/posts'
  title = input("Enter Post title\n")
  body = input("Enter body content\n")
  request_data = {'title': title, 'body': body}
  data = parse.urlencode(request_data).encode()
  req = request.Request(url, data=data)
  resp = request.urlopen(req)
  print(resp.__dict__)
create_post()