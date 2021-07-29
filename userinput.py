def weather_conditions(temperature):
    if temperature>7:
        return "warm"
    else:
        return "cold"

user_input = int(input("Enter temperature "))
print(weather_conditions(user_input))