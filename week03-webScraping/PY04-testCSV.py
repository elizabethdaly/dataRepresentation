## Elizabeth Daly
## Data Representation Lab 3 PY04-testCSV.py

# Import csv package.
import csv

# Open/create file in write mode.
employee_file = open('employee_file.csv', mode='w')

# set up pars.
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Write to the file.
employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# close the file.
employee_file.close()