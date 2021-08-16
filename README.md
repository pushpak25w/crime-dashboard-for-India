# crime-dashboard-for-India
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Features to be added](#features-to-be-added)
* [Setup](#setup)


## General info
This website is a dashboard for crimes in India displaying and predicting different crimes in different states and districts.

## Technologies:
1. python3.8
2. matplotlib-3.4.2
3. Flask-2.0.1
4. Flask_SQLAlchemy-2.5.1
5. geopandas-0.9.0
6. pandas-1.3.0
7. numpy-1.21.1
8. scikit_learn-0.24.2

## Features:
1. Heatmaps for country and states. (country map for 21 crimes and state maps for 28 states for 4 dfferent crime)
2. Plots for multiple selected crimes in districts. (718 districts and 21 crimes)
3. Interactive plot for crime against children vs literacy rate in country.
4. Prediction of 7 different crimes against women and 10 different crimes against children in 28 states and 9 union territories.

## Features to be added:
1. Accessing data from database instead of reading csv files.
2. Update and delete for records in database.

## Setup
To run this project, install libraries given above:

```
$ cd crime-dashboard-for-India/
$ flask run
```

## Two types of visualizations:
![image](https://user-images.githubusercontent.com/50488701/121695486-b7cfbb80-cae8-11eb-8d36-85cc1fd79d8e.png)

## For heatmap of India based on crime:
![image](https://user-images.githubusercontent.com/50488701/121695616-d930a780-cae8-11eb-8365-41800afcfe3e.png)
![image](https://user-images.githubusercontent.com/50488701/121695705-ef3e6800-cae8-11eb-952d-5b90593434a0.png)

## Statewise heatmap based on crime:
![image](https://user-images.githubusercontent.com/50488701/121695793-05e4bf00-cae9-11eb-9779-e25309c091cc.png)
![image](https://user-images.githubusercontent.com/50488701/121695845-15640800-cae9-11eb-93a6-b1eebe9f516a.png)

## Multiple crimes districtwise:
![image](https://user-images.githubusercontent.com/50488701/121695951-30367c80-cae9-11eb-9790-037fbd31c542.png)

This helps to focus on selected crimes 
e.g theft,robbery,burglary,auto theft.
![image](https://user-images.githubusercontent.com/50488701/121696001-40e6f280-cae9-11eb-8c38-6b4415a1e8c3.png)


