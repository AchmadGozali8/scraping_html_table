# encoding=utf8

from bs4 import BeautifulSoup as bs

import urllib2
import csv
import sys

reload(sys)

# set default encoding
sys.setdefaultencoding('utf8')

def content(url):

	page = urllib2.urlopen(url).read()

	tree = bs(page,"lxml")
	table_tag = tree.select("table")[0]
	tab_data = [[item.text for item in row_data.select("th,td")] for row_data in table_tag.select("tr")]

	return tab_data


def write_to_csv(header, data):
	with open('edustack.csv', mode='w') as data_file:
		wr = csv.writer(data_file, delimiter=",")

		wr.writerow(header)
		for d in data[1:]:
			wr.writerow(list(d))


data = content("https://www.edustack.org/manual/edx/xblocks-list/")
header = ["name", "developer","tak tahu", "description", "license"]
write_to_csv(header, data)