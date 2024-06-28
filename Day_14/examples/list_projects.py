# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nagarajupothamsetti.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0Ld9D4z072PLzGAxpU-mJzb12TdYtUgvLQMpHvkuRp0K3bHIzT36uLjcdlrRx2mHwB1386KcQF2T-tqAqbNAFFln2RvZJ4PYo92ud9IyotGr7hXmLyTYfJKH2vNlNWHsGCN_omhdBKU9_v4v3AMhRRyHLREIisYE4uA0A8Oz1orQ=655D59C3"

auth = HTTPBasicAuth("nagaraju.pothamsetti@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
