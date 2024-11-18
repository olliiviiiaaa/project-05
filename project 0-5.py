import os

# Define the file to store authorized vehicles
vehicles_file = "AuthorizedVehicles.txt"

# Load the list of authorized vehicles from the file
def load_vehicles():
    if not os.path.exists(vehicles_file):
        with open(vehicles_file, "w") as file:  # Create the file if it doesn't exist
            file.write("Ford F-150\nChevrolet Silverado\nTesla CyberTruck\nToyota Tundra\nRivian R1T\nRam 1500\n")
    with open(vehicles_file, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save the list of authorized vehicles back to the file
def save_vehicles(vehicles_list):
    with open(vehicles_file, "w") as file:
        file.write("\n".join(vehicles_list) + "\n")

# Function to print the list of authorized vehicles
def print_vehicles(vehicles_list):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in vehicles_list:
        print(vehicle)

# Function to search for a vehicle in the allowed list
def search_vehicle(vehicles_list):
    vehicle_to_search = input("Please Enter the full Vehicle name: ").strip()
    if vehicle_to_search in vehicles_list:
        print(f"{vehicle_to_search} is an authorized vehicle")
    else:
        print(f"{vehicle_to_search} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Function to add a new vehicle to the allowed list
def add_vehicle(vehicles_list):
    vehicle_to_add = input("Please Enter the full Vehicle name you would like to add: ").strip()
    if vehicle_to_add in vehicles_list:
        print(f'"{vehicle_to_add}" is already in the authorized vehicles list.')
    else:
        vehicles_list.append(vehicle_to_add)
        save_vehicles(vehicles_list)
        print(f'You have added "{vehicle_to_add}" as an authorized vehicle')

# Function to remove a vehicle from the allowed list
def remove_vehicle(vehicles_list):
    vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ").strip()
    if vehicle_to_remove in vehicles_list:
        confirmation = input(f'Are you sure you want to remove "{vehicle_to_remove}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirmation == 'yes':
            vehicles_list.remove(vehicle_to_remove)
            save_vehicles(vehicles_list)
            print(f'You have REMOVED "{vehicle_to_remove}" as an authorized vehicle')
        else:
            print("Vehicle removal canceled.")
    else:
        print(f'"{vehicle_to_remove}" is not in the Authorized Vehicles List.')

# Function to display the main menu and handle user input
def menu():
    vehicles_list = load_vehicles()  # Load vehicles from file on program start
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")
        
        # Get user input
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ").strip()
        
        if choice == "1":
            print_vehicles(vehicles_list)
        elif choice == "2":
            search_vehicle(vehicles_list)
        elif choice == "3":
            add_vehicle(vehicles_list)
        elif choice == "4":
            remove_vehicle(vehicles_list)
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3, 4, or 5.")

# Start the program
menu()
