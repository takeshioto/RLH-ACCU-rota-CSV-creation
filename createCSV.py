import csv
import datetime
from datetime import timedelta

#CONSTANTS
sStart = '08:00'
sEnd = '17:00'
cStart = '08:00'
cEnd = '20:30'
lStart = '14:00'
lEnd = '22:00'
nStart = '20:00'
nEnd = '08:30'
shiftDescription = '#work'

# open the CSV file which has been renamed rotadata.csv
with open('rotadata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # Create a new CSV file with calendar suitable header
    with open('gCalendarImportFile.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Start date', 'Start time', 'End date', 'End time', 'Description'])

    # A function to add an entry into the calendar CSV
    def addShift (subject, startDate, startTime, endDate, endTime, description):
        with open('gCalendarImportFile.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([subject, startDate, startTime, endDate, endTime, description])

    # A funciton that takes a string inputDate in the format YYYY-MM-DD and returns
    # a string in format YYYY-MM-DD which is a day later than the input date
    # requires use of datetime for the adding of the singular day
    def addDay (inputDate):
        print(inputDate[6:10])
        print(inputDate[3:5])
        print(inputDate[0:2])
        outputDate = datetime.datetime(int(inputDate[0:4]), int(inputDate[5:7]), int(inputDate[8:10]))
        outputDate += timedelta(days=1)
        output = outputDate.strftime('%Y' + '-' + '%m' + '-' + '%d')
        print(output)
        return output

    # A loop to add the CSV calendar rows
    for row in readCSV:

        # Create a Date object
        # nb/ the date has to be in the format 2020-12-01 from the CSV file
        date = row[0]

        # Quirk of a mistake in the covid rota, doesnt change to 2021 when the new year starts
        # if month is jan or feb, changes year from 2020 to 2021
        if (date[5] == '0' and date[6] == '1') or (date[5] == '0' and date[6] == '2'):
            # In python strings are immutable. converting string to a list of individual characters
            listString = list(date)
            # Changing the year to 2021
            listString[3] = '1'
            # Rejoining the list as a string to be used for the addShift function
            date = "".join(listString)

        print(date)

        shiftType = row[1]

        # Initialise an endDate
        endDate = ''

        if shiftType == 'S':
            shiftType += ' Shift'
            startTime = sStart
            print(startTime)
            endTime = sEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'C':
            shiftType += ' Shift'
            startTime = cStart
            print(startTime)
            endTime = cEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'L':
            shiftType += ' Shift'
            startTime = lStart
            print(startTime)
            endTime = lEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'N':
            shiftType += ' Shift'
            startTime = nStart
            print(startTime)
            endTime = nEnd
            print(endTime)
            endDate = addDay(date)
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)