class WeatherService:
    @staticmethod
    def weather_data_enum(data):
        return data  # no changes needed

    @staticmethod
    def process_weather_data(WeatherData, city, query):
        # check for city existence
        if city not in WeatherData:
            return f"Error: Invalid city name {city}"

        info = WeatherData[city]

        if query == "temperature":
            temp = info.get("temperature")
            if not temp:
                return ("Error: Invalid or missing temperature data")
            try:
                temp = int(temp)
            except ValueError:
                return "Error: Invalid temperature data format"
            if temp < -20 or temp > 50:
                return f"Error: Temperature {temp} is out of range"
            return f"The temperature for {city} is {temp}"

        elif query == "forecast":
            forecast = info.get("forecast")
            if not forecast:
                return "Error: Invalid or missing forecast data"
            return f"The forecast for {city} is {forecast}"

        else:
            return f"Error: Invalid query type {query}"

# Driver Code
if __name__ == "__main__":
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]

    n = int(lines[0])
    data = {}

    # load city weather data
    for i in range(1, n + 1):
        parts = lines[i].split(",")
        city = parts[0]
        temp = parts[1] if len(parts) > 1 else ""
        forecast = parts[2] if len(parts) > 2 else ""
        data[city] = {"temperature": temp, "forecast": forecast}

    WeatherData = WeatherService.weather_data_enum(data)

    q = int(lines[n + 1])
    for i in range(n + 2, n + 2 + q):
        city, query = lines[i].split(",")
        print(WeatherService.process_weather_data(WeatherData, city, query))
