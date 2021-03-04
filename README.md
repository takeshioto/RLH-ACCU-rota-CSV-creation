# RLH-ACCU-rota-CSV-creation
Creating a calendar CSV file from a formatted excel rota file that can be imported into google calendar

HOWTO
1. Format using Microsoft Excel your rota line into the format shown in the example rotadata.csv. This will require a little bit of work on your end but shouldnt take long.
3. Make sure to format the dates into YYYY-MM-DD (select the colum and press 'control'+'1' in Microsoft Excel)
4. Save said file as a .csv file named rotadata.csv
5. Install Python
6. Place the script and YOUR newly created .csv file into the same working directory
7. Make sure to delete the existing rotadata.csv file if you've downloaded it from GitHub as this is my rota, not yours
8. Run the script
9. Import the created gCalendarImportFile.csv into your Google Calendar. I recommend creating a new Google Calendar to import the file to

IMPORTANT: The second column in the .csv needs to be in the format of S/C/L/N/SL
Note it doesn't add AL as anything
Feel free to edit the script to your liking

If theres a problem with the dates it's probably Excel displaying the format in a UK local format DD-MM-YYY while the underlying data is in the universal YYY-MM-DD
