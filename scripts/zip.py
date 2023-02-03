import urllib.request
import shutil
import zipfile
import os


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


with zipfile.ZipFile("roseguarden.zip", "w", zipfile.ZIP_DEFLATED) as zip_rel:
    zipdir("roseguarden", zip_rel)

print("finished")
