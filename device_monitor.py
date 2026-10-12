"""
Laboratory Exercise 17
Simulated Device Monitoring and Alert System
"""


def get_initial_readings():
    """Return the initial temperature readings."""
    readings = [28, 31, 35, 37, 29]
    return readings


def display_menu():
    """Display the main menu."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Display every reading with its position number."""
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings):
    """Validate a new reading and add it if valid."""
    new_reading = input("Enter new reading: ")

    if new_reading == "":
        print("Invalid input. The reading cannot be empty.")

    elif not new_reading.isdigit():
        print("Invalid input. Enter a whole number only.")

    else:
        temperature = int(new_reading)

        if temperature < 0 or temperature > 100:
            print("Invalid reading. Enter a value from 0 to 100.")

        else:
            readings.append(temperature)
            print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the classification of a temperature reading."""
    if reading < warning_limit:
        return "NORMAL"

    elif reading <= critical_limit:
        return "WARNING"

    else:
        return "CRITICAL"


def classify_readings(readings):
    """Display the classification of every reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, 30, 35)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Calculate the total using a loop."""
    total = 0

    for reading in readings:
        total += reading

    return total


def compute_average(readings):
    """Calculate the average temperature."""
    total = compute_total(readings)
    average = total / len(readings)

    return average


def find_minimum(readings):
    """Find the lowest reading using a loop."""
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    """Find the highest reading using a loop."""
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Count readings belonging to a specified category."""
    count = 0

    for reading in readings:
        result = classify_reading(reading, warning_limit, critical_limit)

        if result == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    """Determine the overall monitoring status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"

    elif warning_count >= 1:
        return "MONITOR"

    else:
        return "NORMAL"


def display_summary(readings):
    """Calculate and display the complete monitoring summary."""
    number_of_readings = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    normal_percentage = normal_count / number_of_readings * 100
    warning_percentage = warning_count / number_of_readings * 100
    critical_percentage = critical_count / number_of_readings * 100

    overall_status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {number_of_readings}")
    print(f"Total of readings  : {total}")
    print(f"Average temperature: {average:.2f} °C")
    print(f"Minimum temperature: {minimum} °C")
    print(f"Maximum temperature: {maximum} °C")

    print()
    print(f"NORMAL   : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percentage:.2f}%)")

    print()
    print(f"Overall Status: {overall_status}")


def main():
    """Run the device monitoring system."""
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            classify_readings(readings)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


main()