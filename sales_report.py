"""Generate sales report showing total melons each salesperson sold."""

# salespeople   = list of salesperson names
# melons_sold   = list of melons sold, parallel to salespeople 
salespeople = []
melons_sold = []


# f             = opened sales report file
f = open('sales-report.txt')

# For loop - for each line of the file:
#   splits each line of the file into entries:
#   entries = [salesperson,                     - name of salesperson
#             [index represents sale amount],   - total sale cost
#              melons]                          - number of melons sold
for line in f:
    line = line.rstrip()        # strips whitespace to right of line
    entries = line.split('|')   # splits line into list at '|'

    salesperson = entries[0]   
    melons = int(entries[2])

    # if salesperson has already been added to list of salespeople:
    #   finds the index of that salesperson in the list
    #   adds the melons they sold to their total melons sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
