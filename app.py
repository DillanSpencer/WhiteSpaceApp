import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    output = open("output.txt", 'w')
    lines = file.readlines()
    for line in lines:
        output.write(line.replace('\t', " "))

    output.close()
    file.close()


main()
