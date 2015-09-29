import urllib2

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



def get_page(web_link):							# this function returns the page source of the given web link
	response = urllib2.urlopen(web_link)
	return response.read()


def next_url(page_string, search_from):
	start_link = page_string.find('<a href=', search_from)   #start_link stores the index of first occurance of "<a href=" in the input string
	if start_link == -1:
		return None, 0
	start_pos = page_string.find('"', start_link)	# start_pos is the starting index of the url
	end_pos = page_string.find('"', start_pos + 1)	# end_pos is the ending index of the url
	url = page_string[start_pos+1:end_pos]
	return url, end_pos								# returns the url and end index of the url

def extract_all_url(page_string):
	list_url = []								# stores the list of url in the given page	
	remaining_string = 0
	while True:
		url_output, remaining_string = next_url(page_string, remaining_string)
		if url_output:
			list_url.append(url_output)
			tmp_page_string = page_string[remaining_string + 1:]
		else:
			break
	return list_url


def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([keyword,[url]])


def add_page_to_index(index, url, content):
	words = content.split()
	for ele in words:
		add_to_index(index, ele, url)



def crawl_web(seed_link):
	tocrawl = []
	tocrawl.append(seed_link)
	crawled = []
	tmp_list = []
	index = []
	while True:
		if tocrawl:
			page_url = tocrawl[-1]
			page_source = get_page(page_url)
			contents = strip_tags(page_source)
			
			add_page_to_index(index, page_url, contents)
			tmp_list = extract_all_url(page_source)
			
			popped = tocrawl.pop()
			crawled.append(popped)
			for e in tmp_list:
				if (e not in crawled) and (e not in tocrawl):
					tocrawl.append(e)
		else:
			break
	return index



list_url_collected = []
seed_link = 'https://www.udacity.com/cs101x/index.html'
#seed_link = 'https://www.nba.com'

#print seed_link
#seed_page_source = get_page(seed_link)
#next_url , end_string = next_url(seed_page_source)
#list_url_collected = extract_all_url(seed_page_source,seed_link)
indexed_list_url_collected = crawl_web(seed_link)



print ''
print ''
for e in indexed_list_url_collected:
	print e


#print list_url_collected


def lookup(index, keyword):
	emptylist = []
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return emptylist
