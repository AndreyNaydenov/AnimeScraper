from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_all_urls_on_page(main_url, number):
    urls = []
    errors = 0
    url = main_url + "?p=" + str(number)
    page = urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    ul = soup.find("ul", {"id": "thumbs2"})
    if ul is None:
        print("Page #" + str(number) + " is member only or doesn't exist.")
        return []
    li_list = ul.findChildren("li")
    for li in li_list:
        try:
            a = li.p.findChildren("a")[-1]
            urls.append(str(a['href']))
        except Exception:
            errors += 1
    print("Got " + str(len(urls)) + " from page #" + str(number) + ". Couldn't get " + str(errors) + " pic(s).")
    return urls

def get_all_urls(main_url, first_page, last_page):
    if first_page < 1:
        print("first page must be >= 1")
        exit()
    urls = []
    n = first_page
    while n <= last_page:
        urls.extend(get_all_urls_on_page(main_url, n))
        n += 1
    return urls
