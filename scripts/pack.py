import urllib.request
import shutil

print("Start building the package")

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url = "https://gitlab.com/roseguarden/roseguarden/-/jobs/artifacts/master/download?job=pack"
url = "https://gitlab.com/roseguarden/roseguarden/-/jobs/artifacts/master/download?job=pack"
req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)

# Download the file from `url` and save it locally under `file_name`:
with open("release.zip", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

print("finished") 