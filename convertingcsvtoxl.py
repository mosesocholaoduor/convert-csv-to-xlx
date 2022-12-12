import csv
import openpyxl

# Open the CSV file and read in the data
with open('input.csv', 'r') as csv_file:
    csv_data = csv.reader(csv_file)

# Create a new Excel file and add a sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Iterate over the CSV data and write it to the Excel sheet
for row in csv_data:
    sheet.append(row)

# Save the Excel file
wb.save('output.xlsx')

