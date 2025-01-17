#Write a program that asks the user for a number of a month and then prints out the corresponding season
#(spring,  summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define
#each season to last three months, December being the first month of winter.

seasons = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer","Summer", "Summer", "Autumn",
           "Autumn", "Autumn", "Winter")
month = int(input("Enter number of a month (1-12): "))
if 1 <= month <= 12:
    print(f"Month {month} corresponds to {seasons[month-1]}")

#Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether
# the name was entered for the first time. Finally, the program lists out the input names one by one,
# one below another in any order. Use the set data structure to store the names.

names_set = set()
while True:
    user_input = input("Enter a name (or press enter to exit): ")
    if user_input == "":
        break
    if user_input  in names_set:
        print("Existing name")
    else:
        print(f"New name {user_input}")
        names_set.add(user_input)
print("\n List of names entered:")
for name in names_set:
    print(name)

#Write a program for fetching and storing airport data. The program asks the user if they want to enter a
# new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new
# airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch
# airport information instead, the program asks for the ICAO code of the airport and prints out the
# corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new
# option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique
# to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the
# ICAO codes of different airports online.)

airport_data = {}
prompt = input("Type 'add' to add a new airport data, 'fetch' to view existing airport data, or 'quit' to quit: ")
while prompt != "quit":
    if prompt == "add":
        airport_name = input("Enter airport name: ")
        airport_ICAO = input("Enter airport ICAO code: ").upper()
        airport_data[airport_ICAO] = airport_name
    elif prompt == "fetch":
        airport_fetch = input("Enter airport ICAO code: ").upper()
        if airport_fetch in airport_data:
            print(f"The airport with ICAO code {airport_fetch} is {airport_data[airport_fetch]}.")
        else:
            print(f"The airport with ICAO code {airport_fetch} is not available.")
    else:
        print("Invalid input please try again.")
    prompt = input("Type 'add' to add a new airport data, 'fetch' to view existing airport data, 'quit' to quit: ")

