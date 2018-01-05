from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_all_posts_on_page(main_url, number):
    posts = []
    url = main_url + "&pid=" + str(number * 40)
    page = urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    div = soup.find("div", {"id": "post-list"})
    if div is None:
        print("Page #" + str(number) + " doesn't exist.")
        return []
    div1 = div.contents[-1]
    div2 = div1.contents[3]
    spans = div2.findChildren("span")
    for span in spans:
        a = span.a
        posts.append(a['href'])
    print("Got " + str(len(posts)) + " from page #" + str(number))
    return posts

def get_pic_url_from_post(post_relative_url):
    post_url = "http://safebooru.org/" + post_relative_url
    page = urlopen(post_url).read()
    soup = BeautifulSoup(page, "html.parser")
    div = soup.find("div", {"id": "right-col"})
    div1 = div.contents[-1]
    img = div1.contents[4]
    src = "http:" + img['src']
    return src

def get_all_posts(main_url, first_page, last_page):
    if first_page < 0:
        print("first page must be >= 0")
        exit()
    posts = []
    n = first_page
    print("Searching for posts...")
    while n <= last_page:
        posts.extend(get_all_posts_on_page(main_url, n))
        n += 1
    print("Total number of posts: " + str(len(posts)))
    return posts

def posts_to_pic_urls(posts):
    urls = []
    print("Converting posts to image urls...")
    for post in posts:
        pic_url = get_pic_url_from_post(post)
        highres = highres_url(pic_url)
        urls.append(highres)
    print("Converted")
    return urls

def highres_url(image_url):
    if "//samples/" in image_url:
        image_url = image_url.replace("//samples/", "//images/")
        image_url = image_url.replace("sample_", "")
    return image_url