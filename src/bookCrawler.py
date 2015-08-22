import urllib2
from bs4 import BeautifulSoup
import sys

def save(txt, file_name):
    pass

def parse(html_txt):
    print html_txt.encode('utf8')
    pass

def crawl(start, end):
    start_num = start.split('/')[-1].split('.')[0]
    end_num = end.split('/')[-1].split('.')[0]
    prefix = '/'.join(start.split('/')[:-1])
    tail = '.html'
    for i in range(int(start_num), int(end_num) + 1):
        addr = prefix + '/' + str(i) + tail
        resp = urllib2.urlopen(addr)
        parse(resp.read())
        print addr
    pass

def main():
    if len(sys.argv) != 3:
	print 'usage: bookCrawler.py <start page> <end page>'
        return
    crawl(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
