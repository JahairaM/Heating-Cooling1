def heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp:
        print("Run heat")
    elif actual_temp > desired_temp:
        print("Run A/C")
    else:
        print("Standby")

# Prompting the user for input
current_temp = float(input("Enter the current temperature: "))
desired_temp = float(input("Enter the desired temperature: "))
heating_cooling(current_temp, desired_temp)
