temperature=float(input('What is the temperature? '))
grade=input('Fahrenheit or Celsius (F/C)? ').capitalize()
wind_speed=int(5)

def temperature_convert(temperature):
    temperature=(temperature*(9/5))+32
    return temperature

def wind_chill(wind_speed):
    wind_chill_temperature=35.74+(.6215*temperature)-35.75*(wind_speed**.16)+.4275*temperature*(wind_speed**.16)
    return wind_chill_temperature

if grade=='C':
    temperature=temperature_convert(temperature)

while wind_speed<61:
    wind_chill_temperature=wind_chill(wind_speed)
    print(f'At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_temperature:.2f}F')
    wind_speed=wind_speed+5
