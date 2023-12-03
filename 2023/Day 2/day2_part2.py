def main():

    #iterate throught all lines from the document
    with open("day2_data.txt", "r") as file:
        powers_list = []
        for lines in file:
            string = lines.strip()
            
            #convert everything from a line to a list
            input = string[string.index(":") + 2:]
            input = input.replace(";", "").replace(",", "").split()

            #make a dictionary for all highest scores
            scores = {}
            for i in range(1, len(input), 2):                           
                if input[i] in scores:
                    scores[input[i]] = max(scores[input[i]], int(input[i - 1]))
                else:
                    scores[input[i]] = int(input[i - 1])
                
            #append powers to a list
            power = scores["blue"] * scores["red"] * scores["green"]
            powers_list.append(power)

        #sum powers of each game
        print(f"The sum of all powers of mininum possible cubes for each game is {sum(powers_list)}")

if __name__ == "__main__":
    main()