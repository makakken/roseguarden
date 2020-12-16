import urllib.request
import shutil
import zipfile


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url = "https://gitlab.com/roseguarden/roseguarden/-/jobs/artifacts/master/download?job=pack"
req = urllib.request.Request(url, headers=hdr)

try:
    response = urllib.request.urlopen(req)
except Exception as e:
    print("Failed to get latest package {}".format(str(e)))
    exit(1)

package_name = "latest_package"

try:
    with open(package_name + ".zip", 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
except Exception as e:
    print("Failed to save latest package {}".format(str(e)))
    exit(1)

try:
    with zipfile.ZipFile(package_name + ".zip", 'r') as zip_ref:
        zip_ref.extractall(package_name)
except Exception as e:
    print("Failed to unzip latest package {}".format(str(e)))
    exit(1)

print("finished")
