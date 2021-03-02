import csv

from simple_salesforce import Salesforce
from pathlib import Path


def run_main():
    # 1. load CSV from file
    # 2. (optionally) do stuff to the data
    # 3. Upload stuff to Salesforce

    csv_dict = {}  # new dict
    csv_set = set()  # new set
    csv_tuple = ()  # new tuple

    # To open a file, we use the open()

    # Use "with" to ensure the file is closed again

    # old way to open a file

    file_path = Path('data/ContactReassign-2020-05-12.csv')

    # file = open(filename, 'r')

    # do stuff with file

    # file.close()

    # New way to deal with files

    # Step 1.
    header = []
    csv_data = [] # new list
    index = 0
    with open(file_path, 'r') as csv_file:
        # Do the stuff.
        reader = csv.reader(csv_file)

        # read the column headers
        # header = reader.next()

        for row in reader:
            if index == 0:
                header = row
                print(header)
            elif index == 21:
                break
            else:
                csv_data.append(row)
                print(f'{index} - Contact Id: {row[0]} - Owner Id: {row[1]}')

            index += 1

    # 2. Do stuff

    # 3. Salesforce
    client = Salesforce()




if __name__ == '__main__':
    run_main()

