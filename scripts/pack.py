import urllib.request
import shutil
import zipfile
import os


def copyfile(src, dst):
    shutil.copy2(src, dst)

def copytree(src, dst, exclude=[], symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if item not in exclude:
                copytree(s, d, exclude, symlinks, ignore)
        else:
            shutil.copy2(s, d)


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

if os.path.exists(package_name):
    shutil.rmtree(package_name)

if os.path.exists("roseguarden"):
    shutil.rmtree("roseguarden")


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

try:
    if not os.path.exists("roseguarden"):
        os.makedirs("roseguarden")
    if not os.path.exists("roseguarden/client"):
        os.makedirs("roseguarden/client")
except Exception as e:
    print("Failed to create package directory {}".format(str(e)))
    exit(1)

try:
    copytree("backend/api", "roseguarden/api", exclude=['__pycache__'])
    copytree("backend/core", "roseguarden/core", exclude=['__pycache__'])
    copytree("backend/migrations", "roseguarden/migrations", exclude=['__pycache__'])
    copytree("backend/tests", "roseguarden/tests", exclude=['__pycache__'])
    copytree("backend/workspaces", "roseguarden/workspaces", exclude=['__pycache__'])
    copyfile("backend/requirements.txt", "roseguarden/requirements.txt")
    copyfile("backend/setup.py", "roseguarden/setup.py")
    copyfile("backend/config.template", "roseguarden/config.template")
    copyfile("backend/app.py", "roseguarden/app.py")
    copyfile("backend/config.py", "roseguarden/config.py")
    copyfile("backend/devEnv.py", "roseguarden/devEnv.py")
    copyfile("backend/README.md", "roseguarden/README.md")
    copyfile("backend/LICENSE", "roseguarden/LICENSE")
except Exception as e:
    print("Failed to copy backend to package {}".format(str(e)))
    exit(1)

if not os.path.exists("frontend/dist"):
    if not os.path.exists("latest_package/roseguarden/client"):
        copytree("latest_package/roseguarden/client", "roseguarden/client", exclude=['__pycache__'])
    else:
        print("No frontend build found in 'frontend'")
        exit(1)
else:
    copytree("frontend/dist", "roseguarden/client", exclude=['__pycache__'])


print("finished")
