# Ola-Bike-Ride-Request-Forecast
predict ride-request for a particular hour using machine learning. One can refer to the below explanation for the column names in the dataset and their values as well.

### season
1}spring __
2}summer __
3}fall __
4}winter __

### weather
Clear, Few clouds, Partly cloudy, Partly cloudy
Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

**casual** – number of non-registered user rentals initiated
**registered** – number of registered user rentals initiated
**count** – number of ride request raised on the app for that particular hour.

## Python libraries used 
**Pandas** – This library helps to load the data frame in a 2D array format and has multiple functions to perform analysis tasks in one go.
**Numpy** – Numpy arrays are very fast and can perform large computations in a very short time.
**Matplotlib/Seaborn** – This library is used to draw visualizations.
**Sklearn** – This module contains multiple libraries are having pre-implemented functions to perform tasks from data preprocessing to model development and evaluation.
**XGBoost** – This contains the eXtreme Gradient Boosting machine learning algorithm which is one of the algorithms which helps us to achieve high accuracy on predictions.

## Line plot for the average count of ride requests
![Capture10](https://github.com/crew-12-to-moon/Ola-Bike-Ride-Request-Forecast/assets/106720341/fedeee95-b052-4e22-bc3a-8f17f1f656f7)

From the above line plots we can confirm some real-life observations:
1.There is no such pattern in the day-wise average of the ride requests.
2.More ride requests in the working hours as compared to the non-working hours.
3.The average ride request count has dropped in the month of festivals that is after the 7th month that is July that is due to more holidays in these months.

## Bar plot for the average count of the ride request
![Capture11](https://github.com/crew-12-to-moon/Ola-Bike-Ride-Request-Forecast/assets/106720341/9284b147-9366-4bb3-b005-ca8014a9083d)

From the above bar plots we can confirm some real-life observations:
1.Ride request demand is high in the summer as well as season.
2.The third category was extreme weather conditions due to this people avoid taking bike rides and like to stay safe at home.
3.On holidays no college or offices are open due to this ride request demand is low.
4.More ride requests during working hours as compared to non-working hours.
5.Bike ride requests have increased significantly from the year 2011 to the year 2012.

## Distribution plot to visualize the data distribution for some columns
![Capture12](https://github.com/crew-12-to-moon/Ola-Bike-Ride-Request-Forecast/assets/106720341/788ffe70-470c-4c75-8f2a-7af17b65dbfd)

Temperature values are normally distributed but due to the high number of 0 entries in the windspeed column, the data distribution shows some irregularities.




