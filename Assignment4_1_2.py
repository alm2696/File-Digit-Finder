def check_digits(infile):
    try:
        with open(infile, 'r') as file:
            contents = file.read()
            if any(char.isdigit() for char in contents):
                print("Digit present in the file")
            else:
                print("Digit not present in the file")
    except FileNotFoundError:
        print("File not found")

check_digits(r'C:\Users\angel\Downloads\input.txt')