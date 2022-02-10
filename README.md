# python2_assignment2
# Visualizing Blockchain analytics tool with Django + Charts.js
The application visualizes top 100 Ethereum addresses by their balance and showing 3 types of charts: Pie Chart, Bar Chart and Linear Chart

## Installation 
You can either install each module specified in requirments one by one separately or type in your shell ```pip install -r requirements.txt```.

## Usage
* Run ```python manage,py runserver``` to launch the application
* Afterwards go to ```localhost:8000``` or to ```127.0.0.1:8000```route on you're browser to the home page of Django application.
* The app using celenium library in order to retrieve data from top 100 Ethereum addresses by ETH Balance
* The data then is analyzed by the Charts.js js framework and visuallized into charts
* The home page will show 3 types of the chart:
   -  Bar chart
   -  Line char
   -  Pie chart

## Example
Ather running ```python manage,py runserver``` to launch the app, open the browser and go to ```localhost``` route.
The welcoming home page displays 3 different charts.
### Bar chart
![This is an image](https://cdn.discordapp.com/attachments/540499123053396013/941005151660023818/unknown.png)
### Line chart
![This is an image](https://cdn.discordapp.com/attachments/540499123053396013/941005152364679258/unknown.png)
### Pie chart
![This is an image](https://cdn.discordapp.com/attachments/540499123053396013/941005152066895902/unknown.png)
