# Title: Final Year Project - Ground Condition Classification System
# Name: Jordan Engel
# ID: 32479050
# Start Date: 24/04/24
# Finish Date: 11/05/24

import pandas as pd

print("Please Ensure Excel Document Is Of The Same Format Of Template.")

epb_from_tests = 0
mixed_shield_from_test = 0

while True:
    proceed = input('Would You Like To Proceed? ')
    if proceed == 'Yes' or proceed == 'yes':
        # First we should import the excel file that the user will give us. For now, let us
        # assume that the user has given us the following excel file.

        pd.set_option('display.max_columns', None)
        file_path = 'C:/Users/jteng/Documents/Monash/Year 4/FYP/Test Cases/Test Case - Mixed Shield Case 1.xlsx'
        df1 = pd.read_excel(file_path)

        # 1. PSDC
        #Plotting the sample on the graph for visulisation
        from PSDC.PSDC_PlotFunction import particle_size_distribution_curve_plot
        particle_size_distribution_curve_plot(df1)

        #Determining from sample the ground type
        from PSDC.PSDC_NewFunction import particle_size_distribution_curve
        tbm_type_from_psdc = particle_size_distribution_curve(df1)

        # 2. USCS
        from USCS.USCS_NewFunction import unified_soil_classification_system
        tbm_type_from_uscs = unified_soil_classification_system(df1)

        if tbm_type_from_psdc == "epb" and tbm_type_from_uscs == "epb":
            print("\nOverall, the type of TBM that should be used for your project is the EPB TBM.")
            epb_from_tests += 1
        elif tbm_type_from_psdc == "mixed shield" and tbm_type_from_uscs == "mixed shield":
            print("\nOverall, the type of TBM that should be used for your project is the Mixed Shield TBM.")
            mixed_shield_from_test += 1
        #After all checks are finished, and ground type has been determined, we can break out of the loop
        break

    elif proceed == 'No' or proceed == 'no':
        print("\nAlright, Good Bye.")
        break
    else:
        print("\nSorry, Please Ensure You Enter Either 'Yes' or 'No'.")
        continue



# 3. DAUB Table Check

from DAUB.DAUB_NewFunction import daub_tables_check
daub_check = daub_tables_check(df1)

if daub_check == "epb" and epb_from_tests == 1:
    print("\nFrom Testing and DAUB Tables, the recommended TBM to be used is EPB.")
elif daub_check == "mixed shield" and mixed_shield_from_test == 1:
    print("\nFrom Testing and DAUB Tables, the recommended TBM to be used is Mixed Shield.")
else:
    print("\nSorry, but manual selection may be required.")


