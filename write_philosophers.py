def main():
    # open and create file object
    outfile = open("philosophers.txt", "w")

    # write names
    # John Locke, David Hume, and Edmund Burke
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    # close file
    outfile.close


def add_my_name():
    # open file
    outfile = open("philosophers.txt", "a")

    # append file
    outfile.write("Aidan Conom\n")

    # close file
    outfile.close


main()
add_my_name()
