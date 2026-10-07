import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Whola!\nSee you next time")

rolli = requests.get("https://itunes.apple.com/search?entity=song&limit=45&term=" + sys.argv[1])
print(json.dumps(rolli.json(), indent = 2))

o = rolli.json()
for result in o['results']:
    print(result['trackName'] + " - " + result['artistName'])