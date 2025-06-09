                                #############################################################
                                #         TEAM MEMBER         |             QUID            #
                                #-----------------------------------------------------------#
                                #          Islam Hamdi        |           ........          #
                                #############################################################

# we need to import the module "functions" to gain access to all the functions
# that we need for our project.
# we imported the module as Fn for short form.                               
import functions as Fn

#defining the main function:
def main():    
    while True:
        #Formatting the output as the example
        print()
        print("\033[1m"+" COVID'19 tracking System"+"\033[0m")# for bold
        print("Please choose one of the following tasks:")
        print()
        print("\t[1] Add a record of a new country")
        print("\t[2] Display the informatiom of all countries")
        print("\t[3] Search for a specific country")
        print("\t[4] Display a report of all counties with total\n\tnumber of cases higher than a specified value from\n\tuser")
        print("\t[5] Classify the countries")
        print("\t[6] Exit")
        
        try:
            userInput = int(input("\033[1m   Enter your choice: \033[0m")) #we left some spaces before the sentence and make it in bold.
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        
        #We use if/elif/else to assign each number (choice) to a specific function (task).
        if userInput == 1:
            Fn.add_record()
        elif userInput == 2:
            Fn.display_all_info()
        elif userInput == 3:
            Fn.search()
        elif userInput == 4:
            Fn.display_report()
        elif userInput == 5:
            Fn.classification()
        elif userInput == 6:
            Fn.Exit()
            break
        else:
            print("Invalid input! The input should be between 1 and 6")

    #Bonus: show the chart
    Fn.bar_chart()

main()