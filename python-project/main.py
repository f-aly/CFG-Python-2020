import csv
import os


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def get_total_sales():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    header = "\n=================== TOTAL SALES ==================\n"
    msg = '{}* Total sales: {} sales'.format(header, total)
    print(msg)
def write_total_sales():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    header = "\n=================== TOTAL SALES ==================\n"
    msg = '{}* Total sales: {} sales'.format(header, total)
    print(msg, file=open('summary.txt', 'a'))

def get_monthly_changes():
    data = read_data()
    months = []
    sales = []
    percentages = []
    msgs = []
    index = 0
    for row in data:
        month = str(row['month'])
        months.append(month)
        sale = int(row['sales'])
        sales.append(sale)
        amount_of_change = sales[index] - sales[index - 1]
        months_msg = '**** from {} to {} ****'.format(months[index - 1], months[index])
        # print(months_msg)
        change_msg = '* Amount of change: {} - {} = {}'.format(sales[index], sales[index - 1], amount_of_change)
        # print(change_msg)
        last_months_measurement = amount_of_change / sales[index - 1]
        last_meas_msg = '* Last months measurement: {} / {} = {}'.format(amount_of_change, sales[index - 1], last_months_measurement)
        # print(last_meas_msg)
        percentage = last_months_measurement * 100
        percentage_msg = '* Difference percentage: {} x 100 = {}%\n'.format(last_months_measurement, int(percentage))
        # print(percentage_msg)
        percentages.append(percentage)
        index = index + 1
        msg = '{}\n{}\n{}\n{}'.format(months_msg,change_msg,last_meas_msg,percentage_msg)
        msgs.append(msg)
    header = '\n================ MONTHLY CHANGES =================\n'
    print(header + '\n'.join(msgs))
    # return changes
def write_monthly_changes():
    data = read_data()
    months = []
    sales = []
    percentages = []
    msgs = []
    index = 0
    for row in data:
        month = str(row['month'])
        months.append(month)
        sale = int(row['sales'])
        sales.append(sale)
        amount_of_change = sales[index] - sales[index - 1]
        months_msg = '**** from {} to {} ****'.format(months[index - 1], months[index])
        # print(months_msg)
        change_msg = '* Amount of change: {} - {} = {}'.format(sales[index], sales[index - 1], amount_of_change)
        # print(change_msg)
        last_months_measurement = amount_of_change / sales[index - 1]
        last_meas_msg = '* Last months measurement: {} / {} = {}'.format(amount_of_change, sales[index - 1],
                                                                       last_months_measurement)
        # print(last_meas_msg)
        percentage = last_months_measurement * 100
        percentage_msg = '* Difference percentage: {} x 100 = {}%\n'.format(last_months_measurement, int(percentage))
        # print(percentage_msg)
        percentages.append(percentage)
        index = index + 1
        msg = '{}\n{}\n{}\n{}'.format(months_msg, change_msg, last_meas_msg, percentage_msg)
        msgs.append(msg)
    header = '\n================ MONTHLY CHANGES =================\n'
    print(header + '\n'.join(msgs), file=open('summary.txt', 'a'))

def get_average():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total_sales = sum(sales)
    total_average = total_sales / len(sales)
    total_average = int(total_average)
    msg = '* Sales Average: {} sales'.format(total_average)
    header = '\n================= SALES AVERAGE ==================\n'
    print(header + msg)
def write_average():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total_sales = sum(sales)
    total_average = total_sales / len(sales)
    total_average = int(total_average)
    msg = '* Sales Average: {} sales'.format(total_average)
    print("\n================= SALES AVERAGE ==================\n" + msg, file=open('summary.txt', 'a'))

def get_highest_and_lowest():
    contents = 'something'
    highest_month = 'something'
    highest = 0
    sales = []
    with open("sales.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            highest = lines['sales']
            sales.append(highest)
            highest_sale = max(sales)
            lowest_sale = min(sales)
            if lines['sales'] == highest_sale:
                highest_month = '* Month with highest sales: {}'.format(lines['month'])
                highest_sale_print = '* Highest sale: {} sales'.format(lines['sales'])

            if lines['sales'] == lowest_sale:
                lowest_month = '* Month with lowest sales: {}'.format(lines['month'])
                lowest_sale_print = '* Lowest sale: {} sales'.format(lines['sales'])
    high_msg = '{}\n{}'.format(highest_month, highest_sale_print)
    low_msg = '{}\n{}'.format(lowest_month, lowest_sale_print)
    msg = '{}\n{}'.format(high_msg, low_msg)
    header = '\n============ HIGHEST AND LOWEST SALES ============\n'
    print(header + msg)
    # return msg
def write_highest_and_lowest():
    contents = 'something'
    highest_month = 'something'
    highest = 0
    sales = []
    with open("sales.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            highest = lines['sales']
            sales.append(highest)
            highest_sale = max(sales)
            lowest_sale = min(sales)
            if lines['sales'] == highest_sale:
                highest_month = '* Month with highest sales: {}'.format(lines['month'])
                highest_sale_print = '* Highest sale: {} sales'.format(lines['sales'])

            if lines['sales'] == lowest_sale:
                lowest_month = '* Month with lowest sales: {}'.format(lines['month'])
                lowest_sale_print = '* Lowest sale: {} sales'.format(lines['sales'])
    high_msg = '{}\n{}'.format(highest_month, highest_sale_print)
    low_msg = '{}\n{}'.format(lowest_month, lowest_sale_print)
    msg = '{}\n{}'.format(high_msg, low_msg)
    header = '\n============ HIGHEST AND LOWEST SALES ============\n'
    print(header + msg, file=open('summary.txt', 'a'))

def read_write_txt(to_add):
    with open('./summary.txt', 'r') as summary_file:
        contents = summary_file.read()
    with open('./summary.txt', 'w+') as summary_file:
        summary_file.write(
            contents + to_add)
def generate_txt():
    file_path = 'summary.txt'
    if os.stat(file_path).st_size == 0:
        sales = []
        with open("sales.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            read_write_txt('==================================================\n'
                           '=============== 2018 SALES SUMMARY ===============\n'
                           '==================================================\n\n'
                           'Year | Month | Sales | Expenditure\n')
            for lines in csv_reader:
                highest = lines['sales']
                sales.append(highest)
                highest_sale = max(sales)
                # print(lines['year'], lines['month'], lines['sales'], lines['expenditure'])
                read_write_txt(lines['year'] + ' | ' + lines['month'] + '   | ' + lines['sales'] + '  | '
                               + lines['expenditure'] + '\n')
                if lines['sales'] == highest_sale:
                    highest_month = 'Months with highest sales: {}'.format(lines['month'])
                    highest_sale_print = 'Highest sale: {} sales'.format(lines['sales'])

        write_total_sales()
        write_average()
        write_highest_and_lowest()
        write_monthly_changes()
        print('Done! File saved as summary.txt')
    else:
        print('summary.txt already has a generated summary!')

def run():
    print('====================================')
    print('======= SPREADSHEET ANALYSER =======')
    print('====================================')

    # getInfo()
    print('Options available: '
          '\n    A) Get Total Sales'
          '\n    B) Get Monthly Changes (%)'
          '\n    C) Get Average'
          '\n    D) Get Months with the highest and lowest sales'
          '\n    E) Generate Summary')
    my_choice = input('\nSelect an option: ')

    option_a = my_choice == "A" or my_choice == "a"
    option_b = my_choice == "B" or my_choice == "b"
    option_c = my_choice == "C" or my_choice == "c"
    option_d = my_choice == "D" or my_choice == "d"
    option_e = my_choice == "E" or my_choice == "e"
    if option_a:
        get_total_sales()
        repeat()
    elif option_b:
        get_monthly_changes()
        repeat()
    elif option_c:
        get_average()
        repeat()
    elif option_d:
        get_highest_and_lowest()
        repeat()
    elif option_e:
        generate_txt()
        repeat()
    else:
        print('Sorry - this option is not available.')
        repeat()
def repeat():
    print('\n--------------------------------------------------')
    my_choice = input('\nWould you like to start over? [Y/N] : ')
    start_again = my_choice == 'Y' or my_choice == 'y' or my_choice == 'Yes' or my_choice == 'YES' or my_choice == 'yes'
    if start_again:
        print('\n--------------------------------------------------\n')
        run()
    else:
        print('Goodbye!')

run()
