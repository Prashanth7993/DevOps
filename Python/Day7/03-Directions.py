import requests


# response = requests.get("https://www.google.com")
# print(response)
# print(response.status_code)


# response = requests.post("https://httpbin.org/post",data={'key':'value'})
response = requests.put("https://httpbin.org/post",data={'key':'value'})

print(response)
print(response.status_code)
print(response.content)