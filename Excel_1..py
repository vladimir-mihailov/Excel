from fileinput import filename

from openpyxl import Workdook

workbook = Workdook()
sheet = workbook.active

sheet["A1"] = "Hello"
sheet["B1"] = "World"

workbook.save(filename="Helo_world.ODF")