import csv

csv_name = input('Enter the name of the file (example.csv): ')

file_name_base = 'split'

rows_to_split = int(input('Enter the number of lines per file: '))

with open(csv_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Save the row header
    header = next(csv_reader)
    
    # Initializing new file lines writted
    lines = 0

    # The initial batch
    batch = 1

    file = open('split-' + '1.csv', 'w', newline='')
    writer = csv.writer(file)

    for row in csv_reader:
        if (lines == 0):
            writer.writerow(header)

        writer.writerow(row)
        lines += 1

        if (lines == rows_to_split):
            file.close()
            
            batch += 1

            file = open(file_name_base + '-' + str(batch) + '.csv', 'w', newline='')
            writer = csv.writer(file)

            # Initializing new file lines writted
            lines = 0
