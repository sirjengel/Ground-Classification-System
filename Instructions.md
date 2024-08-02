# FYP-2024---Ground-Classification-System
Ground Type Classification System for Automated Selection of Tunnel Boring Machines

Dear User,
The purpose of the following code is to determine the most suitable TBM for the ground type present on your project site. Due to limitations, only EPB and Mixed Shield TBM's are able to be selected for either soft and heterogeneous ground conditions, respectively. 

Please begin by downloading the Test Case - Tempaplate.xlsx file and filling in the data from your laboratory results. These results include: 
1. Mass retained on each seive size,
2. Liquid Limit and Plasticity Index,
3. Permeability, Consistency Index, Relative Density, Confinment Pressure, Swell Index, Abrasivity values. Please ensure the rows direclty underneath these specific titles are either Yes or No to indicate whether you are including them

Once the you have finished filling in your excel file, please rename to the following "GCS-LR.xlsx", and save to your device in a folder. Ensure you are aware of where this folder is located for later.

Next, download both Python and PyCharm to your device. Follow this tutorial if unsure: https://www.youtube.com/watch?v=mO6ONGkQk9Y

Once both Python and PyCharm are downloaded onto your device, download the following files and please place them into the same folder as the one used previously for your excel document.
1. Classification_System_New.py
2. PSDC_PlotFunction.py
3. PSDC_NewFunction.py
4. USCS_NewFunction.py
5. DAUB_NewFunction.py

With all required python codes downloaded, please open the Classification_System_New python file. Scroll down to line 22, and ensure that the correct file path leading to the GCS-LR.xlsx is chosen, ensuring that the file path has an apostrophe at either end. Your code should now read as follows:

  file_path = 'C:/Users/[Your File Path Here]/GCS-LR.xlsx'

With all of this now completed, please run the Classification_New_Function python code to generate results.
