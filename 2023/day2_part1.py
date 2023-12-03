def main():

    #iterate throught all lines from the document
    with open("day2_data.txt", "r") as file:
        ID_list = []
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
                
            #gather game IDs to a list
            ID = int(string[5:string.index(":")])
            if scores["red"] <= 12 and scores["green"] <=13 and scores["blue"] <= 14:
                ID_list.append(ID)

        #sum of game IDs
        print(f"The sum of all possible game IDs is {sum(ID_list)}")

if __name__ == "__main__":
    main()