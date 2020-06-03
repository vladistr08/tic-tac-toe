from terminaltables import SingleTable
from fabulous.color import bold, bg256, fg256

print(bold('ana are text bold'), 'dar si text normal')
print(bg256('#DDD', 'dar si text pe fundal gri'))

data = [['X', 'O', 'X'], [' ', 'O', ' '], ['X', ' ', ' ']]
table = SingleTable(data)
table.inner_row_border = True

print(table.table)