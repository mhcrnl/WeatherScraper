#import libraries
import csv
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup

# TODO: Give date and time range to program.
# Should output csv file with date and wind speed data.

url = 'https://www.wunderground.com/history/airport/EGKA/2017/8/5/DailyHistory.html?req_city=Brighton&req_statename=United%20Kingdom'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")

table = soup.find("table", attrs={"class":"obs-table responsive"})
rows = table.find_all(["tr"])
result = []

for row in rows:
    cells = row.findChildren("td")
    row_text = []

    for cell in cells:
        if cell.text.strip():
            if cell.text[:1] != "\n":
                value = cell.text
                row_text.append(value)

    row_spans = []
    for spans in row.find_all("span", attrs={"class":"wx-value"}):
        value = spans.text
        row_spans.append(value)

    row_text.extend(row_spans[3:4])
    result.append(row_text)

print result
