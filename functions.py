import matplotlib.pyplot as plt

###############################################################################################################################
# if the userInput was equal to 1:
# The function "add_record" appends a new country record to the covid19_information.txt file.

def add_record():
    with open('covid19_information.txt', 'a') as Covid19Info_file:
        Covid19Info_file.write("\n")  # Ensure a new line before new entry
        country_code = input("Enter Country Code: ")
        country = input("Enter Country Name: ")
        total_cases = input("Enter Total Cases: ")
        new_cases = input("Enter New Cases (24 hours): ")
        deaths = input("Enter Deaths: ")
        new_deaths = input("Enter New Deaths: ")
        
        Covid19Info_file.write(f"{country_code}\t{country}\t{total_cases}\t{new_cases}\t{deaths}\t{new_deaths}")
    print("Record successfully added!")


###############################################################################################################################
# if the userInput was equal to 2:
# The function "display_all_info" reads the information of all countries(from the text file: covid19_information.txt )
# and display it in a tabular format .

###############################################################################################################################
# if the userInput was equal to 2:
# The function "display_all_info" reads the information of all countries(from the text file: covid19_information.txt )
# and display it in a tabular format .

def display_all_info():
    Covid19Info_file = open('covid19_information.txt', 'r')
    print("The information of all countries:")
    print(f"{'Country Code':<13} | {'Country':<12} | {'Total Cases':<12} | {'New Cases (24 hours)':<22} | {'Deaths':<10} | {'New Deaths'}")
    print('----------------------------------------------------------------------------------------------------------')
    for line in Covid19Info_file:
        elements = line.strip().split()
        if len(elements) == 6:
            print(f"{elements[0]:<13} | {elements[1]:<12} | {elements[2]:<12} | {elements[3]:<22} | {elements[4]:<10} | {elements[5]}")
    Covid19Info_file.close()


###############################################################################################################################
# if the userInput was equal to 3:
# The function "search" recieves a country_code from the user, then check if that code exists or not
# by reading all the country codes (in the text file: covid19_information.txt ).
# After that, it displays the country record if it exists, otherwise the user recieves a message
# that tells him/her that the country_code does not exist.

def search():
    country_code = input('Enter Country Code: ')
    found = False
    Covid19Info_file = open('covid19_information.txt','r')
    for country in Covid19Info_file:
        elements = country.strip().split()
        if elements[0] == country_code:
            print(f"{'Country Code':<13} | {'Country':<12} | {'Total Cases':<12} | {'New Cases (24 hours)':<22} | {'Deaths':<10} | {'New Deaths'}")
            print('----------------------------------------------------------------------------------------------------------')
            print(f"{elements[0]:<13} | {elements[1]:<12} | {elements[2]:<12} | {elements[3]:<22} | {elements[4]:<10} | {elements[5]}")
            found = True
            break
    Covid19Info_file.close()

    if  found == False:
        print("The Country Code doesn't exist in the file \n")

###############################################################################################################################
# if the userInput was equal to 4:
#  The function "display_report" displays a report of all countries with total number of cases higher than or equal to a  
# specified value entered by the user.

def display_report():
    Covid19Info_file = open('covid19_information.txt', 'r')
    total_cases = int(input('enter total cases :'))
    print("Country records based on the Total Cases:")
    found = False
    for line in Covid19Info_file:
        elements = line.strip().split()
        if int(elements[2]) >= total_cases:
            if not found:
                print(f"{'Country Code':<13} | {'Country':<12} | {'Total Cases':<12} | {'New Cases (24 hours)':<22} | {'Deaths':<10} | {'New Deaths'}")
                print('----------------------------------------------------------------------------------------------------------')
                found = True
            print(f"{elements[0]:<13} | {elements[1]:<12} | {elements[2]:<12} | {elements[3]:<22} | {elements[4]:<10} | {elements[5]}")
    Covid19Info_file.close()

    if not found:
        print("There is no country that has total cases higher than or equal to the enterd value:", total_cases)

###############################################################################################################################
# if the userInput was equal to 5:
# The function "classification" categorizes countries into severity levels based on total cases.

###############################################################################################################################
# if the userInput was equal to 5:
# The function "classification" categorizes countries into severity levels based on total cases.

def classification():
    Covid19Info_file = open('covid19_information.txt', 'r')
    print("Country Classification (based on total cases):")
    print("------------------------------------------------")
    for line in Covid19Info_file:
        elements = line.strip().split()
        country = elements[1]
        total_cases = int(elements[2])

        # Determine classification and color
        if total_cases > 1000000:
            status = "\033[91mSeverely Affected\033[0m"    # Red
        elif total_cases > 100000:
            status = "\033[93mModerately Affected\033[0m"  # Yellow
        else:
            status = "\033[92mLess Affected\033[0m"        # Green

        print(f"{country:<12}: {status}")
    Covid19Info_file.close()


###############################################################################################################################
# if the userInput was equal to 6:
# ----> the program exits

def Exit():
    print("\033[1m Bye, see you again later!\033[0m")    #the closing sentence is in bold

###############################################################################################################################
# Bonus Question:
# Draw a bar chart of country names vs. total cases from the file.

# Bonus Question:
# Draw a bar chart of country names vs. total cases from the file.

def bar_chart():
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    country_name = []
    total_cases = []
    Covid19Info_file = open('covid19_information.txt', 'r')
    for line in Covid19Info_file:
        elements = line.split()
        country_name.append(elements[1])
        total_cases.append(int(elements[2]))
    Covid19Info_file.close()

    plt.figure(figsize=(10, 6))
    plt.bar(country_name, total_cases, color='steelblue')
    plt.title("COVID'19 Tracking System")
    plt.xlabel('Countries')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()
