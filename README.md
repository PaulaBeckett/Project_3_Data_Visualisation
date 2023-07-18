### Objective: 

The primary goal of this project is to develop a web-based Flask application that analyzes and presents the history and impact of Australian Bushfires. With bushfires being a pervasive and regular phenomenon in Australia, significantly shaping the continent's landscape over millions of years, the project aims to delve deeper into the origins of current and historical bushfires. Through interactive features and insightful data visualizations, the web app will offer information on Australian bushfire locations, global bushfire hotspots, historical and current fire counts, the profound impact of bushfires on human and wildlife populations, as well as the role of climate in the occurrence of these fires. The end result will be an informative and engaging platform, encompassing a home page and an about page, to provide a comprehensive understanding of the subject matter.

Data Source: https://www.kaggle.com/datasets/nagarajbhat/australian-bush-fire-satellite-data-nasa

**Useful parts of data:
-	Lat/long
-	Brightness
-	Date & time in UTC
-	Day or night
-	Satellite location & type

** Four tables to be put into SQL.
-	Note time columns to be brought in as fixed 4 digits.
-	Additional table to be added for types (e.g., volcanic or vegetation)
-	Four tables to be merged into one table, adding a column for type from our additional table.
-	Maybe add a column for the conversion of time from UTC to Australian Central
-	Conversion of Kelvin to Celsius
-	Export merged table as csv.

** Use Flask to create an app instance.
-	One option (app route) could be:
o	Using Leaflet to plot fire spots.
o	Colour gradient based off brightness/intensity.
o	Layers to toggle between:
	the fire type, or
	the date (data has 5 months, these could be the options)
o	More detail could be added using the marker hover.
-	Another app route option could be:
o	A page with charts:
	This could be a good place to use the new JS library.
•	An example is Chart.js which has a lot of chart options and tooltips.
	Options for user dropdown
•	Day/Night
•	Fire Type
•	Date
•	Satellite
	Lots of options for charts depending on the choice of user dropdown





Requirements
For Project 3, you will work with your group to tell a story using data visualisations. Here are the specific requirements:
1.	Your visualisation must include a Python Flask-powered API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).
2.	Your project should fall into one of the following three tracks:
o	A combination of web scraping and Leaflet or Plotly
o	A dashboard page with multiple charts that update from the same data
o	A server that performs multiple manipulations on data in a database prior to visualisation (must be approved)
3.	Your project should include at least one JS library that we did not cover.
4.	Your project must be powered by a dataset with at least 100 records.
5.	Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
6.	Your final visualisation should ideally include at least three views.
For this project, you can focus your efforts within a specific industry, as detailed in the following examples.

