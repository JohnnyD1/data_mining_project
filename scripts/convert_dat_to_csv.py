import sys
import csv


def convert(dat_file):
    with open(dat_file, 'r') as dat_f, open(''.join(dat_file.rsplit('.',1)[0]) + '.csv', 'w') as csv_f:
        csv_writer = csv.writer(csv_f)

        for line in dat_f:
            row = line.split(' ')
            row[-1] = row[-1].strip()
            csv_writer.writerow(row)




if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert(sys.argv[1])
    else:
        print("need to supply argument")
        exit()
