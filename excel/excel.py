from openpyxl import *
from openpyxl.styles.colors import *
from ExampleResults import *
from openpyxl.styles import *
from openpyxl.utils import *



wb = Workbook()

ws = wb.active
ws.title = '"' + searchString + '" Profile Search'

for x in range(1, profileCount + 2):
    for y in range(1, 9):
        ws.cell(row=x, column=y)

# ws.append(names title currco loc)

for i in range(9):
    aCell = chr(65 + i) + str(1)
    ws[aCell].font = Font(color = "00FFFFFF", bold=True)
    ws[aCell].fill = PatternFill(bgColor=BLACK, fill_type="solid")

wb.save("test.xlsx")
