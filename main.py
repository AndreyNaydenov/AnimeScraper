import scrape
import sys

if len(sys.argv) != 5:
    print("This is script that downloads pictures from zerochan.net\n" +
          "Usage: main.py <https://www.zerochan.net/Tohsaka+Rin> <start page> <number of pages> <folder>")
    exit()

main_url = sys.argv[1]

try:
    first_page = int(sys.argv[2])
    last_page = int(sys.argv[3])
except Exception:
    print("Wrong arguments")
    exit()

folder = sys.argv[4]

scrape.main(main_url, first_page, last_page, folder)
