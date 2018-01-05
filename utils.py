"""Module with utils to image scrape project."""
from urllib.request import urlopen
from urllib.error import HTTPError
import os

def img_download(url, folder, filename):
    """
    Download image from $url to ./<folder>/<filename>.<extension>.
    Identifies <extension> by <url>.
    If this folder doesn't exists, creates it.
    """
    if ".png" in url:
        extension = ".png"
    else:
        extension = ".jpg"

    try:
        img = urlopen(url).read()
    except HTTPError:
        print("Couldn't download " + str(url))
        return
    except ValueError:
        print("Value error. Url: " + str(url))
        return
    if not folder:
        folder_path = "./"
    else:
        folder_path = "./" + folder + "/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("Created " + folder_path + " directory")
    name = folder_path + filename + extension
    with open(name, "wb") as file:
        file.write(img)

def download_all_images(urls, folder):
    """
    Download all images from <urls> list to <folder>.
    Uses count file to store and name files.
    """
    count = get_count()

    print("Downloading images...")
    for url in urls:
        img_download(url, folder, str(count))
        count += 1
    print("Downloaded")
    save_count(count)

def get_count():
    """
    Get current count from count file.
    If count file doesn't exist, create new with value 0.
    If count file contains wrong, value overwrite it with value 0.
    """

    with open("count") as file:
        content = file.read()
    if content == '':
        return 0
    try:
        count = int(content)
        return count
    except ValueError:
        return 0

def save_count(count):
    """Write <count> to count file."""

    with open("count", "w") as file:
        file.write(str(count))
