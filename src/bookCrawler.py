import urllib2
from bs4 import BeautifulSoup, Tag
import sys

def save(txt, file_name):
    with open(file_name, 'aw') as f:
        f.write(txt.encode('utf8'))

def parse(html_txt):
    soup = BeautifulSoup(html_txt)
    paragraph = soup.find('td', {'width': '820', 'align': 'left', 'bgcolor': '#FFFFFF'})
    tag_brs = paragraph.contents[1].contents
    result = unicode('')
    for item in tag_brs:
        if isinstance(item, Tag): continue
        result += unicode(item)
    import pdb; pdb.set_trace()
    save(result, '../book.txt')

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
