def get_weather(destination, travel_date):
    sample_weather = {
        "Shimla": "cold and snowy",
        "Mumbai": "hot and humid",
        "Delhi": "warm with light breeze",
        "Goa": "sunny and pleasant"
    }
    return sample_weather.get(destination, "moderate climate")
