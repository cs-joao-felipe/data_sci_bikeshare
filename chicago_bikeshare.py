# coding: utf-8

# Here goes the imports
import csv

import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

print(data_list[:20])

input("Press Enter to continue...")
# TASK 2
print("\nTASK 2: Printing the genders of the first 20 samples")

for sample in data_list[:20]:
    print(sample[6])

input("Press Enter to continue...")
# TASK 3


def column_to_list(data: list, index: int) -> list:
    """
    Function to extract a data set column as list
    Args:
      data: Data set in question.
      index: Column of the the given data set to extract.
    Returns:
      List of values

    """
    list_to_return = []
    for entry in data:
        list_to_return.append(entry[index])
    return list_to_return


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", \
    "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
male = 0
female = 0
for sample in data_list:
    if sample[6] == 'Male':
        male = male + 1
    elif sample[6] == 'Female':
        female = female + 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")


# Why don't we create a function to do that?
# TASK 5


def count_gender(list_to_handle: list) -> [str, str]:
    """
    Function to count data entries based on gender
    Args:
      list_to_handle: Data set in question.
    Returns:
      Tuple with genders count
    """
    male_count = 0
    female_count = 0
    for entry in list_to_handle:
        if entry[6] == 'Male':
            male_count = male_count + 1
        elif entry[6] == 'Female':
            female_count = female_count + 1
    return [male_count, female_count]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong length returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")


# Now we can count the users, which gender use it the most?
# TASK 6


def most_popular_gender(list_to_handle: list) -> str:
    """
    Function to return most popular gender.
    Args:
      list_to_handle: Data set in question.
    Returns:
      Most popular gender.
    """
    genders = count_gender(list_to_handle)
    if genders[0] > genders[1]:
        return 'Male'
    elif genders[0] < genders[1]:
        return 'Female'
    else:
        return 'Equal'


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")


# TASK 7


def count_types(list_to_handle: list) -> [int, int]:
    """
    Function to count data entries based on user types
    Args:
      list_to_handle: Data set in question.
    Returns:
      List of user types count
    """
    subscriber = 0
    customer = 0
    for entry in list_to_handle:
        if entry[5] == 'Subscriber':
            subscriber = subscriber + 1
        elif entry[5] == 'Customer':
            customer = customer + 1
    return [subscriber, customer]


print("\nTASK 7: Check the chart!")
types = ["Subscriber", "Customer"]
quantity = count_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "There are users that did not fill in gender information"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")


# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9


def get_trip_values(list_to_handle: list) -> list:
    """
    Function to convert data entries str to int
    Args:
      list_to_handle: Data set in question.
    Returns:
      List of trip durations
    """
    return list(map(int, list_to_handle))


def mean_trip_value(int_list: list) -> float:
    """
    Function to calculate trip durations mean value.
    Args:
      int_list: Trip durations list.
    Returns:
      Trip duration mean value
    """
    total_sum = 0.
    for entry in int_list:
        total_sum = total_sum + entry
    return total_sum / len(int_list)


def min_trip_value(int_list: list) -> int:
    """
    Function to calculate trip durations minimum value.
    Args:
      int_list: Trip durations list.
    Returns:
      Trip duration minimum value
    """
    min_value = int_list[0]
    for entry in int_list:
        if entry < min_value:
            min_value = entry
    return min_value


def max_trip_value(int_list: list) -> int:
    """
    Function to calculate trip durations maximum value.
    Args:
      int_list: Trip durations list.
    Returns:
      Trip duration maximum value
    """
    max_value = int_list[0]
    for entry in int_list:
        if entry > max_value:
            max_value = entry
    return max_value


def median_trip_value(int_list):
    """
    Function to calculate trip durations median value.
    Args:
      int_list: Trip durations list.
    Returns:
      Trip duration median value
    """
    sorted_list = int_list
    sorted_list.sort()
    list_len = len(sorted_list)
    if list_len % 2 == 0:
        return (sorted_list[list_len / 2] + sorted_list[list_len - 1]) / 2
    else:
        return sorted_list[round(list_len / 2)]


trip_duration_values = get_trip_values(column_to_list(data_list, 2))
min_trip = min_trip_value(trip_duration_values)
max_trip = max_trip_value(trip_duration_values)
mean_trip = mean_trip_value(trip_duration_values)
median_trip = median_trip_value(trip_duration_values)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
start_stations = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(start_stations))
print(start_stations)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(start_stations) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
print("Will you face it?")
answer = "yes"


def count_items(list_to_handle: list) -> [list, list]:
    """
    Function to extract a column set value and count it's items.
    Args:
      list_to_handle: List to be worked on.
    Returns:
      A tuple containing the column set and it's respective entries count
    """
    items_dict = {}
    keys = set(list_to_handle)
    for x in keys:
        items_dict[x] = 0

    for x in column_list:
        items_dict[x] = items_dict[x] + 1

    return list(items_dict.keys()), list(items_dict.values())


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
