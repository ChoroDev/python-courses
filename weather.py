def weather(temperature, weather_type):
    temperature = float(temperature)
    weather_type = str(weather_type).strip()

    print('What to wear?\n')

    if temperature > 20 and weather_type == 'rain':
        print('You may wear shorts and t-short\n')
    elif temperature > 20 and weather_type == 'clear':
        print('Weather is clear, you may get dressed easier\n')
    elif 20 >= temperature > 1 and weather_type == 'rain':
        print('Wear something better than t-short and pick an umbrella\n')
    elif 0 >= temperature >= -15 and weather_type == 'snow':
        print('You have to wear winter things')
    elif 0 >= temperature >= -15 and weather_type == 'wind':
        print('You have to wear winter things and don\'t forget about scarf\n')
    else:
        print('undefined')
