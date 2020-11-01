# RLH-ACCU-rota-CSV-creation
Creating a calendar CSV file from a formatted excel rota file that can be imported into google calendar

HOWTO
1. Format using Microsoft Excel your rota line into the format shown in the example rotadata.csv
2. Make sure to format the dates into YYYY-MM-DD (select the colum and press 'control'+'1' in Microsoft Excel)
3. Save said file as a .csv file named rotadata.csv
4. Install Python
5. Place the script and YOUR newly created .csv file into the same working directory
6. Make sure to delete the existing rotadata.csv file if you've downloaded it from GitHub as this is my rota, not yours
6. Run the script
7. Import the created gCalendarImportFile.csv into your Google Calendar. I recommend creating a new Google Calendar to import the file to

IMPORTANT: The second column in the .csv needs to be in the format of a single letter of S/C/L/N
