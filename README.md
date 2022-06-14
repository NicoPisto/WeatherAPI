# WeatherAPI

The proposed homework was:
“Using the API https://openweathermap.org/api , build a simple server-side application that provides a search for Canadian cities based on the list of cities provided by the API (http://bulk.openweathermap.org/sample/).
Once a city is clicked, the corresponding weather data is rendered.”

To run the API you should type into the console the command "python manage.py runserver" while you have Django installed.

"You will be judged on the functionality of the application, the technology you choose, why you choose them, performance of your application and completeness of your code."

-Functionality of the application: I've tested with multiple cities from the entire world, the only known problem is if you have a smaller city with the same name, as it searches using the name, not the ID.
-Technology I chose: Only DJANGO, as it would give me tools for fast and simple HTML integration, without the need for using Javascript. I wanted to keep it as simple as possible.
-Performance of the application: There are no known issues with the performance as it contacts directly the API and displays it on the HTML. It concatenates the name of the city in the URL (and the API Key).
-Completeness of the code: I didn't do any CSS or Javascript code to keep it simple and fast, the biggest problem for me is that in order to achieve the option to click on the cities, It would require a more robust code, as the Json included over 3000 canadian cities.



Looking at this problem I created a simple HTML + Python solution using Django that could use the API not only for Canadian cities, but for the entire world.
It consists of a simple search that passes the value of the input to the API in python, then it is concatenated and creates the custom URL to be used to consult the API.
The program consists of the index URL and the /Weather.
If you try to access the /Weather without data, it shall return blank.
If you don’t input any information, it will also return blank.
If you input an invalid city, it will return blank.
The API searches directly using the input information, being the fastest available option. There is no filter for cities nor option to input the ID instead of the city name, as it would require further coding in python and the usage of more file or databases to put the JSON, thus not being as simple as the homework requested. 
To further prove my point, I would like to add that there are around 3000 thousand searchable cities in Canada using this API. The amount of information would be huge to display on a simple page.

I thank you all for the opportunity to display my skills and for your time!

Fingers crossed and I hope I can learn a lot more with the team!
