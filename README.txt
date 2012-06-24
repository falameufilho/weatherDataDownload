This is a simple program I wrote while learning Python.

The user inputs a year and it connects to WeatherUnderground.com to fetch the snowfall data for that year's winter in New York City. It uses beautifulsoup to find and parse the data and the code is based on an example by Nathan Yau on chapter 1 of his book "Visualizing Data".

To do:

- Modularize the urlopen() function so connection errors can be caught and retried.
- Catch some cases in which the letter "T" shows up in lieu of the expected data in the WU site.
- Make some parameters dynamic:
	- The data to be fetched
	- The location (right now hardcoded to JFK)
	- The dates
	- The output (screen, csv file, etc)