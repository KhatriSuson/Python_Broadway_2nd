with open("./N_File_Handling/example.txt", "a") as file:
    file.write(f"\nAppend the exmple.txt")


def write_log(n):

    with open("./N_File_Handling/example.txt", "r") as read_file:
        content = read_file.read()

        print(content, n)


for i in range(1, 10):
    print(write_log(i))
