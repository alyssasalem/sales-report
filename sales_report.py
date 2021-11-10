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

    # if: salesperson has already been added to list of salespeople:
    #   finds the index of that salesperson in the list
    #
    #   adds the melons they sold to their total melons sold
    #else: (if this is their first sale)
    #   adds saleperson's name to the list
    #   adds their melons sold as an index to melons_sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Prints the name of all salepeople as well as the total number of melons they sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')



#Perhaps a better way to store this information would be (code from solution, not by Lys)
# this is here so I can reference it for study
# I started making a class for all this, which def wasn't what the solution wanted, haha
"""Generate sales report showing total melons each salesperson sold."""


def get_melons_sold_by_salesperson(log_file_path):
    """Return a dictionary of {salesperson_name: melons_sold}.

    Arguments:
        log_file_path (str) - the path to a sales report log file

    Return:
        mels_by_sales (dict)
    """

    mels_by_sales = {}

    with open(log_file_path) as f:
        for line in f:
            line = line.rstrip()

            # Create a list of data and unpack its values
            salesperson_name, total_dollars, melons_sold = line.split('|')

            # Set or increment the salesperson's total melons sold
            if salesperson_name in mels_by_sales:
                mels_by_sales[salesperson_name] += int(melons_sold)
            else:
                mels_by_sales[salesperson_name] = int(melons_sold)

    return mels_by_sales


def print_sales_report(melons_sold_by_salesperson):
    """Print a report of salespeople and the total no. of melons they've sold.

    Arguments:
        melons_sold_by_salesperson (dict) - {salesperson_name: melons_sold}
    """

    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))