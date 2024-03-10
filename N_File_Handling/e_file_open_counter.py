def write_counter(n):
    with open("counter.log", "a+") as file:
        file.write(f'{n}')

write_counter(1)

def read_counter():
    with open("counter.log", "r") as conter_file:
        content = conter_file.read()

        n = int(content)
        print(content)

def write_log():
    with open("daily_use.log", "a+") as file:
        n = read_counter()
        file.write(f"\nuser opened file{n} times")
        n = n + 1
        write_counter(n)