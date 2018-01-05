"""Main file of image scarpe project."""
import sys
import zerochan
import safebooru
import utils

def main():
    """Entry point."""

    main_url, first_page, last_page, folder = parse_argvs(sys.argv)
    urls = []

    if "zerochan.net" in main_url:
        urls = zerochan.get_all_urls(main_url, first_page, last_page)
        utils.download_all_images(urls, folder)
    elif "safebooru.org" in main_url:
        #safebooru
        pass
    else:
        print("Wrong arguments")
        exit()

def parse_argvs(args):
    """
    Parse command line arguments and return dict with main_url, start_page, last_page, folder.
    """

    if len(args) != 5:
        print("This is script that downloads pictures from zerochan.net\n" +
              "Usage: main.py <https://www.zerochan.net/tag> <start page> <last page> <folder>")
        exit()
    main_url = sys.argv[1]
    try:
        first_page = int(sys.argv[2])
        last_page = int(sys.argv[3])
    except ValueError:
        print("Wrong arguments")
        exit()
    folder = sys.argv[4]
    return (main_url, first_page, last_page, folder)

main()
