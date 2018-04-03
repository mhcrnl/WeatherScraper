#import libraries
import csv
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup

# TODO: Give date and time range to program
# Should output csv file with date and wind speed data.
# Would be good to give location and find nearest weather station.

url = 'https://www.wunderground.com/history/airport/EGKA/2017/8/5/DailyHistory.html?req_city=Brighton&req_statename=United%20Kingdom'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")

# Find the table with the weather data.
table = soup.find("table", attrs={"class":"obs-table responsive"})
rows = table.find_all(["tr"])
result = []

# Select the relevant data from each row.
for row in rows:
    cells = row.findChildren("td")
    row_text = []

    for cell in cells:
        if cell.text.strip():
            if cell.text[:1] != "\n":
                value = cell.text
                row_text.append(value)

    # Wind data is stored in spans.
    row_spans = []
    for spans in row.find_all("span", attrs={"class":"wx-value"}):
        value = spans.text
        row_spans.append(value)

    row_text.extend(row_spans[3:4])
    row_text.extend(row_spans[0:2])
    result.append(row_text)
# [Time,Humidity,WindDirection,WindSpeed(kph),Temp,DewPoint]
print result
