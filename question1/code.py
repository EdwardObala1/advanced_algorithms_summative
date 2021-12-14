# for testing
import unittest


def get_total(value_range):
    # ÷initialise a variable that will be used which is o(1) storage even in the loop
    values_total = 0
    # initialise a counter that will have o(1) time and storage
    counter = 0
    # use a loop that will gor through all the elements
    while counter <= value_range:
        values_total += counter
        counter += 1
    return values_total

print(get_total(3), "total of 3")
print(get_total(8), "total of 8")
print(get_total(10), "total of 10")
print(get_total(10000), "total of 10000")
print(get_total(1000000), "total of 1000000")
print(get_total(1000000000), "total of 1000000000")

# observation as the  input grew then the time of executing the algoruthm aslos grew.
# the last element took more than a minute to execute
# using python date time you can observe this in seconds