from fileinput import filename

from openpyxl import workdook as wb

wb = Workbook()
sheet = wb.active

sheet["A1"] = "Hello"
sheet["B1"] = "World"

wb.save(filename="Helo_world.xlsx")