#-------  fetching and displaying data  ----------#

def display_data(weather_data, user_input):

    
#-------  fetching the data  ----------#
    temp = weather_data[user_input]["temperature"]
    conds = weather_data[user_input]["conditions"]
    wind_speed = weather_data[user_input]["wind_speed"]
    humidity = weather_data[user_input]["humidity"]

#-------  displaying the data  ----------#
    print(f"the current temperature for {user_input} is {temp}, condition is {conds}")
    print(temp)
    print(conds)
    print(wind_speed)
    print(humidity)

#-------  weather data  ----------#
weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
"New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
"Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
"Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity":  "60%"},
 "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} }

#-------  welcoming the user  ----------#

print("Hello, Welcome to Irah's Weather Forecast!")

#-----------  taking input ------------#

user_input = input("Please state which city you would like to get your weather forecast on:")

#------- checking if input is valid -------#

while not (user_input in weather_data):
    print("This is not a city")
    user_input = input("Write a valid city name (no spaces, no commas, just the city name, first letter is capital: ")

#-------  fetching weather data -------#
display_data(weather_data, user_input)


#-------  thanking the user  ------#
print("Thank you user")

