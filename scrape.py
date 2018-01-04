from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

count = 0

def get_count():
    global count
    with open("count") as f:
        content = f.read()
        if content == '':
            count = 0
        else:
            count = int(content)

def img_download(url, folder, filename):
    global count
    img = urlopen(url).read()
    name = folder + "/" + filename + ".jpg"
    with open(name, "wb") as f:
        f.write(img)
    count += 1

def save_count():
    with open("count", "w") as f:
        f.write(str(count))

def get_all_urls_on_page(main_url, number):
    urls = []
    errors = 0
    url = main_url + "?p=" + str(number)
    page = urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    ul = soup.find("ul", {"id": "thumbs2"})
    if ul == None:
        print("Page #" + str(number) + " is member only or doesn't exist.")
        return []
    li_list = ul.findChildren("li")
    for li in li_list:
        a = li.p.a
        try:
            urls.append(str(a['href']))
        except Exception:
            errors += 1
    print("Got " + str(len(urls)) + " from page #" + str(number) + ". Couldn't get " + str(errors) + " member pics.")
    return urls

def download_all(urls, folder):
    for url in urls:
        img_download(url, folder, str(count))

def get_all_urls(main_url, first_page, last_page):
    if first_page < 1:
        print("first page must be > 1")
        exit()
    urls = []
    n = first_page
    while n <= last_page:
        urls.extend(get_all_urls_on_page(main_url, n))
        n += 1
    return urls

def main(main_url, first_page, last_page, folder_name):
    get_count()

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("Created " + folder_name + " directory")
    else:
        print(folder_name + " already exists")

    print("Extracting all urls...")
    urls = get_all_urls(main_url, first_page, last_page)
    print("URLs have been extracted (" + str(len(urls)) + ")")
    print("Starting to download images...")
    download_all(urls, folder_name)
    print("Downloaded all")

    save_count()