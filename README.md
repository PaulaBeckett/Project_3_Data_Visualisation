### Objective: 

To analyze and present the history and impact of Australian Bushfires through a web app.
Bushfires in Australia are a widespread and regular occurrence that has contributed significantly to moulding the nature of the continent over millions of years. Bushfires have killed approximately 800 people in Australia since 1851, and billions of animals. The purpose of this project is to dig deeper into the roots of current and historical bushfires in Australia and present the findings and analysis results in the form of a web-based Flask app with routes for -  Australian bushfire locations, global bushfire locations, current and historical fire counts, the impact caused by bushfires and climate’s role in causing the bushfires, home and about page.



### Technologies Used:

*   APP – Flask, Flask-SQLAlchemy, Python
*	Database – MySQL on GCP. Script created using SQL
*   Templates – HTML, CSS, Bootstrap
*   Interactive Features – JavaScript, Plotly
*   Visualizations – Plotly map, bar graph, pie chart, line graph, scatter plot
*	Web Scraping – Requests, Beautiful Soup


### Data Sources:

*   Australia and Global Fire Locations – NASA, Fire Information for Resource Management System (FIRMS)
*   https://www.kaggle.com/datasets/nagarajbhat/australian-bush-fire-satellite-data-nasa


### Project Data Routes:

There are 4 files in the data. Files are classified as Archive or NRT. The archive data is older and well-calibrated. Whereas NRT(near real time) data is generated within just 3 hours of satellite detection. It is to support the immediate needs. Archive data is between sept 1,2019 to Dec 31, 2019. Whereas NRT data is between Jan 1, 2020, to Jan 31, 2020. Both files can be merged.

The files are also classified based on satellite - MODIS (M6) and VIIRS( V1). In MODIS (Moderate Resolution Imaging Spectroradiometer) each hotspot detection represents the center of l km, meaning at least one fire is located in less than 1km region. VIIRS (Visible Infrared Imaging Radiometer Suite) has an improved spatial resolution of 375m.

The measurement FRP(Fire radioactive power) can be used to detect fire.
