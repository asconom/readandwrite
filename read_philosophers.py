def main():
    # Open file to read
    infile = open("philosophers.txt", "r")

    # read file
    # file_contents = infile.read()
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")

    # close file
    infile.close

    # print(file_contents)
    print(line1)
    print(line2)
    print(line3)


main()
