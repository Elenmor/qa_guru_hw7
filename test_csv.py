import csv
from os_path_scripts import PROJECT_ROOT_PATH, resources
import os



def test_open_csv():

    csvfile_path = os.path.join(PROJECT_ROOT_PATH, resources, 'eggs.csv')

    with open(csvfile_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csvfile_path) as csvfile:
        csvreader = csv.reader(csvfile)
        save = []
        for row in csvreader:
            save.append(row)
            print(row)

    assert save[0] == ['Anna', 'Pavel', 'Peter']