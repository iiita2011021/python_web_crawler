index = []

def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([keyword,[url]])


def lookup(index, keyword):
	emptylist = []
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return emptylist


def add_page_to_index(index, url, content):
	words = content.split()
	for ele in words:
		add_to_index(index, words, url)

