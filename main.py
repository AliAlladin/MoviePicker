import http.client
conn = http.client.HTTPSConnection("imdb-api.com", 443)
payload = ''
headers = {}
apiKey = 'k_duwxdunl'
conn.request("GET", "/en/API/Top250Movies/" + apiKey, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))