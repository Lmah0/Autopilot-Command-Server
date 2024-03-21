from pymavlink import mavutil

import Operations.arm as arm
import Operations.initialize as initialize
import Operations.mode as mode
import Operations.takeoff as takeoff
import Operations.waypoint as waypoint

# Main.py to coordinate operations together

def main():
    vehicle_port = input("Enter your SITL or vehicle port (press enter to use default port): ")
    try:
        if vehicle_port == "":
            vehicle_connection, connection_status = initialize.connect_to_vehicle()
        else:
            vehicle_connection, connection_status = initialize.connect_to_vehicle(vehicle_port)
    except Exception as e:
        print("Connection failed. Exiting application. Error: ", e)
        exit(1)
    if connection_status:
        print("Vehicle connection established.")
    
    while True:
        print("1. Arm the vehicle")
        print("2. Disarm the vehicle")
        print("3. Set flight mode")
        print("4. Takeoff")
        print("5. Set waypoint")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            arm.arm(vehicle_connection)
        elif choice == "2":
            arm.disarm(vehicle_connection)
        elif choice == "3":
            mode_id = int(input("Enter the flight mode ID: "))
            mode.set_mode(vehicle_connection, mode_id)
        elif choice == "4":
            takeoff_height = float(input("Enter the takeoff height: "))
            takeoff.takeoff(vehicle_connection, takeoff_height)
        elif choice == "5":
            latitude = float(input("Enter the latitude: "))
            longitude = float(input("Enter the longitude: "))
            altitude = float(input("Enter the altitude: "))
            waypoint.set_waypoint(vehicle_connection, latitude, longitude, altitude)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    

if __name__ == "__main__":
    main()