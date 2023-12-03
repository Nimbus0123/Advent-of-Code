def main():
           
    calibration_values = [] #list for all calibration values

    #open and iterate through each line of document
    with open("day1_data.txt", "r") as file:

        for line in file:
            string = line.strip()

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