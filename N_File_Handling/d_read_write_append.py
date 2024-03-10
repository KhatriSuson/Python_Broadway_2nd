from counter import write_counter
def read_counter():
    with open("./N_File_Handling/counter.log", "r") as file:
        content = file.read()
        n = int(content)
        print(n)
    return n

read_counter()

def write_log():
    with open("./N_File_Handling/daily_use.log", "a") as file:
        n = read_counter()
        file.write(f"\nUser opened file {n} times")
        n = n + 1
        write_counter(n)

write_log()
