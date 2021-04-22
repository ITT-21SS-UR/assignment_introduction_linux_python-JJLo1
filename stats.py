import math
import sys

if __name__ == "__main__":
    file = sys.argv[1]


# If stdin didnt give a value we use the file given through args

with open(file,'r') as file:
	string = "".join(file.read())


# Replace all "," decimal points with "."
string_list = string.replace(",",".").split(" ")
# Build a list with all values from the string as float
float_list = list(map(float,string_list))
# Sort the list
sorted_list = sorted(float_list)
# save the list length
list_length = len(float_list)
# Calculate the mean
mean = sum(sorted_list)/list_length
# Calculate the median
if list_length % 2 == 0:
    firstNumber = int(list_length / 2 - 1)
    secondNumber = int(list_length/2)
    median = (sorted_list[firstNumber] + sorted_list[secondNumber]) / 2
else:
    median = sorted_list[int(list_length / 2)]

    
sum_of_squares = 0
for value in sorted_list:
    currentValue = abs(value - mean)
    sum_of_squares += currentValue**2
 
standard_deviation = math.sqrt(sum_of_squares/list_length)
print ("mean: %.4f. median: %.4f. standard deviation: %.4f." % (mean, median, standard_deviation))
