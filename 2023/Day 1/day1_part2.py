def main():

    calibration_values = [] #list for all calibration values
    numbers = {
        "oneight": "18",
        "twone": "21", 
        "threeight": "38", 
        "fiveight": "58", 
        "sevenine": "79", 
        "eightwo": "82", 
        "eighthree": "83", 
        "nineight": "98", 
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
    } #dictionary for all possible spelled out digits

    #open and iterate through each line of document
    with open("day1_data.txt", "r") as file:

        for line in file:
            string = line.strip()
            
            #change all spelled out numbers to digits
            for key, value in numbers.items():
                string = string.replace(key, value)

            #get first digit
            for char in string:
                if char.isdigit():
                    first_digit = char
                    break

            #get last digit
            for char in string[::-1]:
                if char.isdigit():
                    last_digit = char
                    break

            #combine digits to int and append to calibration values
            two_digit_number = int(first_digit + last_digit)
            calibration_values.append(two_digit_number)

    #sum all calibration values
    print(f"The sum of all calibration values is {sum(calibration_values)}.")

if __name__ == "__main__":
    main()