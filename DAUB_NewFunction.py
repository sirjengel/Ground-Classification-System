# Title: Final Year Project - DAUB Table Function
# Name: Jordan Engel
# ID: 32479050
# Start Date: 11/05/24
# Finish Date: 11/04/24


def daub_tables_check(df1):


    permeability_given = df1['Permeability (m/s)'].iloc[0]
    permeability = df1['Permeability (m/s)'].iloc[1]
    #print(f"Permeability given? {permeability_given}")
    #print(f"Permeability value? {permeability}")

    consistency_given = df1['Consistency Index'].iloc[0]
    consistency = df1['Consistency Index'].iloc[1]
    #print(f"Consistency Index given? {consistency_given}")
    #print(f"Consistency Index value? {consistency}")

    rel_density_given = df1['Relative Density (%)'].iloc[0]
    rel_density = df1['Relative Density (%)'].iloc[1]*100
    #print(f"Relative Density given? {rel_density_given}")
    #print(f"Relative Density value? {rel_density}%")

    conf_pressure_given = df1['Confinment Pressure (kPa)'].iloc[0]
    conf_pressure = df1['Confinment Pressure (kPa)'].iloc[1]
    #print(f"Confinment Pressure given? {conf_pressure_given}")
    #print(f"Confinment Pressure value? {conf_pressure}")

    swel_potential_given = df1['Swell Index (%)'].iloc[0]
    swel_potential = df1['Swell Index (%)'].iloc[1]*100
    #print(f"Swelling Potential given? {swel_potential_given}")
    #print(f"Swelling Potential value? {swel_potential}%")

    abrasivity_given = df1['Abrasivity (%)'].iloc[0]
    abrasivity = df1['Abrasivity (%)'].iloc[1]*100
    #print(f"Abrasivity given? {abrasivity_given}")
    #print(f"Abrasivity value? {abrasivity}%")

    index_for_percentage_finer_on_size_0_075 = df1[df1['Sieve Size (mm)'] == 0.075]
    total_percentage_finer_on_size_0_075 = index_for_percentage_finer_on_size_0_075["Percentage Finer (%)"] * 100

    epb = 0
    mixed_shield = 0


    # Fines Check
    if total_percentage_finer_on_size_0_075.item() < 5:
        print("\nFines Content Classified as Very Low.")
        print("Main Field of Application for Mixed Shield, Limited Application for EPB.")
        mixed_shield += 1
    elif 5 < total_percentage_finer_on_size_0_075.item() < 15:
        print("\nFines Content Classified as Low.")
        print("Main Field of Application for Mixed Shield, Extended Application for EPB.")
        mixed_shield += 1
        epb += 0.5
    elif 15 < total_percentage_finer_on_size_0_075.item() < 40:
        print("\nFines Content Classified as Intermediate.")
        print("Main Field of Application for Mixed, Extended Application for EPB.")
        mixed_shield += 1
        epb += 0.5
    elif total_percentage_finer_on_size_0_075.item() > 50:
        print("\nFines Content Classified as High.")
        print("Extended Application for Mixed, Main Field of Application for EPB.")
        mixed_shield += 0.5
        epb += 1

    # Permeability Check
    if permeability_given == 1:
        if permeability < 10**(-6):
            print("\nPermeability Classified as Low.")
            print("Extended Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 0.5
        elif 10**(-6) <= permeability < 10**(-4):
            print("\nPermeability Classified as Permeable.")
            print("Main Field of Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 1
        elif 10**(-4) <= permeability < 10**(-2):
            print("\nPermeability Classified as High.")
            print("Extended Application for Mixed Shield, Limited Application for EPB.")
            mixed_shield += 0.5
        elif permeability >= 10**(-2):
            print("\nPermeability Classified as Very High.")
            print("Limited Application for Mixed Shield and EPB.")
    elif permeability_given == 0:
        print("\nNo Permeability Provided.")

    # Consistency Check
    if consistency_given == 1:
        if 0 <= consistency < 0.5:
            print("\nConsistency Classified as Very Soft.")
            print("Limited Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
        elif 0.5 <= consistency < 0.75:
            print("\nConsistency Classified as Soft.")
            print("Extended Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 0.5
        elif 0.75 <= consistency < 1:
            print("\nConsistency Classified as Stiff.")
            print("Extended Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 0.5
        elif 1 <= consistency < 1.25:
            print("\nConsistency Classified as Very Stiff.")
            print("Extended Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 0.5
        elif 1.25 <= consistency <= 1.5:
            print("\nConsistency Classified as Hard.")
            print("Extended Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 0.5
    elif consistency_given == 0:
        print("\nNo Consistency Provided.")

    # Relative Density Check
    if rel_density_given == 1:
        if 15 <= rel_density < 35:
            print("\nRelative Density Classified as Loose.")
            print("Extended Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 0.5
        elif 35 <= rel_density < 65:
            print("\nRelative Density Classified as Medium Dense.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
        elif 65 <= rel_density <= 85:
            print("\nRelative Density Classified as Dense.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
    elif rel_density_given == 0:
        print("\nNo Relative Density Provided.")

    #Confinment Pressure Check
    if conf_pressure_given == 1:
        if 0 <= conf_pressure < 100:
            print("\nConfinment Pressure Classified as Low.")
            print("Extended Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 0.5
        elif 100 <= conf_pressure < 400:
            print("\nConfinment Pressure Classified as Medium.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
        elif 400 <= conf_pressure < 700:
            print("\nConfinment Pressure Classified as High.")
            print("Main Field of Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 1
        elif 700 <= conf_pressure <= 1500:
            print("\nConfinment Pressure Classified as Very High.")
            print("Main Field of Application for Mixed Shield, Limited Application for EPB.")
            mixed_shield += 1
    elif conf_pressure_given == 0:
        print("\nNo Confinment Pressure Provided.")

    # Swelling Potential Check
    if swel_potential_given == 1:
        if 0 <= swel_potential <= 20:
            print("\nSwelling Potential Classified as Very Low.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
        elif 21 <= swel_potential <= 50:
            print("\nSwelling Potential Classified as Low.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
        elif 51 <= swel_potential <= 90:
            print("\nSwelling Potential Classified as Medium.")
            print("Extended Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 0.5
        elif 91 <= swel_potential <= 130:
            print("\nSwelling Potential Classified as High.")
            print("Limited Application for Mixed Shield, Limited Application for EPB.")
    elif swel_potential_given == 0:
        print("\nNo Swelling Potential Provided.")

    # Abrasivity Check
    if abrasivity_given == 1:
        if 0 <= abrasivity < 5:
            print("\nAbrasivity Classified as Very Low.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
        elif 5 <= abrasivity < 15:
            print("\nAbrasivity Classified as Low.")
            print("Main Field of Application for Mixed Shield, Main Field of Application for EPB.")
            epb += 1
            mixed_shield += 1
        elif 15 <= abrasivity < 35:
            print("\nAbrasivity Classified as Intermediate.")
            print("Main Field of Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 1
        elif 35 <= abrasivity < 75:
            print("\nAbrasivity Classified as High.")
            print("Extended Application for Mixed Shield, Extended Application for EPB.")
            epb += 0.5
            mixed_shield += 0.5
        elif 75 <= abrasivity <= 100:
            print("\nAbrasivity Classified as Very High.")
            print("Extended Application for Mixed Shield, Limited Application for EPB.")
            mixed_shield += 0.5
    elif abrasivity_given == 0:
        print("\nNo Abrasivity Provided.")

    # Final TBM Check
    if epb < mixed_shield:
        print("\nFrom the DAUB Tables, the TBM that should be used is Mixed Shield.")
        return "mixed shield"
    elif epb > mixed_shield:
        print("\nFrom the DAUB Tables, the TBM that should be used is EPB.")
        return "epb"
    else:
        print("\nFrom the DAUB Tables, the recommendation is inconclusive.")
        return "inconclusive"  # Or handle it in a way that fits your application







