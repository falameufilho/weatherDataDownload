import sys
import urllib2
from BeautifulSoup import BeautifulSoup

def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False

def add(x,y): #TODO catch the cases where the letter "T" comes as data and cant be parsed as float
	return float(x)+float(y)

def retrieveData(dataDayRange, dataMonth, dataYear):
	if dataMonth == 12:
		dataMonthW = "December"
	elif dataMonth == 1:
		dataMonthW = "January"
	elif dataMonth == 2:
		dataMonthW = "February"
	elif dataMonth == 3:
		dataMonthW = "March"

	for dataDay in dataDayRange:
		print "fetching snowfall data for  " + dataMonthW + " " + str(dataDay) + " " + str(dataYear)
		url = "http://www.wunderground.com/history/airport/JFK/" + str(dataYear) + "/" + str(dataMonth) + "/" + str(dataDay) + "/DailyHistory.html"
		page = urllib2.urlopen(url) #TODO modularize this to catch network timeouts and retry
		soup = BeautifulSoup(page)
		snow = soup.find(attrs={"class":"typeBG br3"}, text="Snow").findNext(attrs={"class":"nobr"}).span.string
		print "snowfall in " + dataMonthW + " " + str(dataDay) + " was " + str(snow)
		totalSnowfall.append(snow)

#----------------- Start here ----------------------------------------------------

year = input('Choose a year (1949-2012):')
if year < 1949:
	print 'Year must be 1949 or later'
	sys.exit()

if year > 2012:
	print 'Year must be 2012 or earlier'
	sys.exit()

nextYear = year + 1
totalSnowfall = list()

decemberRange = range(21,32)
retrieveData(decemberRange, 12, year)

print "\n\n snowfall for December complete, moving to January \n\n"

januaryRange = range(1,32)
retrieveData(januaryRange, 1, year+1)

print "\n\n snowfall for January complete, moving to February \n\n"	

print "checking if this year is a leap year"

if is_leap_year(nextYear):
	februaryRange = range(1,30)
	print str(nextYear) + " is a leap year"
else:
	februaryRange = range(1,29)
	print str(nextYear) + " is not a leap year"

retrieveData(februaryRange, 2, year+1)

print "\n\n snowfall for February complete, moving to March \n\n"	

marchRange = range(1,20)
retrieveData(marchRange, 3, year+1)

totalSnowfallValue = reduce(add, totalSnowfall)
print "Total snowfall in the winter of " + str(year) + "/" + str(year+1) + " was " + str(totalSnowfallValue)
