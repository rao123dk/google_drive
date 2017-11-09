# @Dhhearj Kumar Rao
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import client

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("students").sheet1
print(sheet.title)
print(sheet.get_all_values())
print(sheet.row_count)
print(sheet.row_values(1));
sheet.update_cell(1, 1, "Name")
sheet.update_cell(4, 1, "Hello word!")
sheet.update_cell(4, 2, "google.com")
sheet.clear();

print(sheet.find("rao"))
print(sheet.findall("rao"))

cell_list = sheet.range('A1:C7')

for cell in cell_list:
    print(cell)

sht = client.open('students')
worksheet = sht.sheet('Annual')

# Extract and print all of the values
row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
index = 4
sheet.insert_row(row, index)

