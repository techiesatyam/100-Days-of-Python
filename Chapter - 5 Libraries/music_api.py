import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Whola!\nSee you next time")

rolli = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(rolli.json())