# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nagarajupothamsetti.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0Et-iV1mGseJmMEU0v2DQ2oVpZhZvPRI0Sc9capbMJUVX_2he3ljBmKw32OlepdlaA4DWeUVJkh8YAK2wBuMnvDQ3CSn-e2d7c1brj_37NwH7PUB8F3hZ1qCEmH8rQPxp6aG3eJcIjRCmjjJQ4g-OrXzTjrXkBECRvWzEUk-RJRE=B83D1897"
auth = HTTPBasicAuth("nagaraju.pothamsetti@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "PP"
    },
    "issuetype": {
      "id": "10001"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
