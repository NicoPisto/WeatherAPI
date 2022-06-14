# WeatherAPI

The proposed homework was:
“Using the API https://openweathermap.org/api , build a simple server-side application that provides a search for Canadian cities based on the list of cities provided by the API (http://bulk.openweathermap.org/sample/).
Once a city is clicked, the corresponding weather data is rendered.”

Looking at this problem I created a simple HTML + Python solution using Django that could use the API not only for Canadian cities, but for the entire world.
It consists of a simple search that passes the value of the input to the API in python, then it is concatenated and creates the custom URL to be used to consult the API.
The program consists of the index URL and the /Weather.
If you try to access the /Weather without data, it shall return blank.
If you don’t input any information, it will also return blank.
If you input an invalid city, it will return blank.
The API searches directly using the input information, being the fastest available option. There is no filter for cities nor option to input the ID instead of the city name, as it would require further coding in python and the usage of more file or databases to put the JSON, thus not being as simple as the homework requested. 
To further prove my point, I would like to add that there are around 3000 thousand searchable cities in Canada using this API. The amount of information would be huge to display on a simple page.
