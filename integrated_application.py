
'''
########################################################################################

                    Main test file for automatic html processing

    Version:            v1.0 
    Author:             Mingrui Yang
    Functionality:      This is a test file of the module that automates the process 
                        from parsing an html career page, to finding the input fields 
                        that requires information, and finally to apply separately for 
                        the users inside the csv file. 
    ! Important !       The current supported fields are : 
                        firstname, lastname, email, phone 
    Files for this demo: 
        1. integrated_application.py (this) 
        2. auto_fill.py
        3. auto_extract.py 
        4. test_data.csv 
        5. index2.html

########################################################################################
'''
import time 
from auto_fill import Application 
import csv

# Apply for an indivudual user 
def applyForUnit(url, rowDict): 
    print("######################################################")
    print(f"Applying for {rowDict['firstname']}")
    app_instance = Application(url, rowDict)
    app_instance.apply()
    print("######################################################")

# Running Tests 
def main(): 
    with open("test_data.csv", mode='r') as user_file: 
        csv_reader = csv.DictReader(user_file) 
        cur_line = 0 
        for row in csv_reader: 
            if cur_line == 0: 
                print(f"Column names are {', '.join(row)}") 
            cur_line += 1
            applyForUnit("https://carnegierobotics.applytojob.com/apply/BjE7MVB8og/2020-Fall-Electrical-Engineer-Internship-Coop", row)
        print(f"Processed {cur_line} applications.")


if __name__ == '__main__': 
    main() 
