# https://www.kaggle.com/leogenzano/clean-data-ufo

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

headers = ['datetime', 'country', 'state', 'city', 'shape', 'duration(minutes)', 'comments', 'datePosted', 'latitude', 'longitude']

# creates data using only the first 335 rows
data = pd.read_csv("UFOSightings.csv", usecols = headers, nrows = 500)

# establishes column variables
dateTime = data["datetime"]
country = data["country"]
state = data["state"]
city = data["city"]
shape = data["shape"]
durationOfSighting = data["duration(minutes)"]
comments = data["comments"]
datePosted = data["datePosted"]
latitude = data["latitude"]
longitude = data["longitude"]

# creates window with graph showing amount of sightings per country
plt.figure(1)

ams = plt.subplot()

ams.set_title("Amount of Sightings by Country")

countryNames = 'USA', 'Canada', 'United Kingdom', 'Australia', 'Other'
amountOSights = [data.query('country == "USA"').country.count(), data.query('country == "Canada"').country.count(), data.query('country == "United Kingdom"').country.count(), data.query('country == "Australia"').country.count(), 7]

ams.pie(amountOSights, labels = countryNames, explode = (0.1, 0.1, 0.1, 0.1, 0.1), autopct = '%1.1f%%')
ams.axis('equal')

# ams.bar("USA", data.query('country == "USA"').country.count(), color="b")
# ams.bar("Canada", data.query('country == "Canada"').country.count(), color="b")
# ams.bar("UK", data.query('country == "United Kingdom"').country.count(), color="b")
# ams.bar("Australia", data.query('country == "Australia"').country.count(), color="b")
# ams.bar("Bermuda", data.query('country == "Bermuda"').country.count(), color="b")
# ams.bar("Lithuania", data.query('country == "Lithuania"').country.count(), color="b")
# ams.bar("PR", data.query('country == "PR"').country.count(), color="b")
# ams.bar("Norway", data.query('country == "Norway"').country.count(), color="b")
# ams.bar("Russian Federation", data.query('country == "Russian Federation"').country.count(), color="b")
# ams.bar("New Zealand", data.query('country == "New Zealand"').country.count(), color="b")
# ams.bar("Iceland", data.query('country == "Iceland"').country.count(), color="b")

# ams.set_xlabel("Country Name")
# ams.set_ylabel("Amount of Sightings")

# ams.tick_params(axis='x', rotation=75)

# ams.yaxis.set_minor_locator(MultipleLocator(10))


# creates second window with graph showing duration of sightings
plt.figure(2)

dus = plt.subplot()

dus.scatter(country, durationOfSighting)

dus.set_xlabel("Country")
dus.set_ylabel("Duration of Sightings (minutes)")

dus.tick_params(axis='x', rotation=75)
dus.set_title("Duration of sightings by country (minutes)")

dus.yaxis.set_minor_locator(MultipleLocator(100))

# creates third window with graph depicting U.S. state and amount of sightings
plt.figure(3)

sts = plt.subplot()
dus.scatter(country, durationOfSighting)

dus.set_xlabel("Country")
dus.set_ylabel("Duration of Sightings (minutes)")

dus.tick_params(axis='x', rotation=75)
dus.set_title("Duration of sightings by country (minutes)")

dus.yaxis.set_minor_locator(MultipleLocator(100))

plt.show()