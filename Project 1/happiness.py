import os

def open_file(filename):
    countries = []

    # if file can't be opened
    if not os.path.isfile(filename):
        print("Unable to openfile")
        return None

    with open(filename) as file:
        for line in file:
            countries.append(line.split(","))
        del countries[0]

        print(countries)
        file.close()
        return

def normalise(countries):
    normalised_countries = []

    for i in range:
        for j in range:
            countries[i][j]





def find_min(action):
    return

def calculate_mean(action):
    return

def calculate_median(action):
    return

def calculate_harmonic_mean(action):
    return






def main():
    filename = input("Enter name of file containing World Happiness data: ")
    open_file(filename)
    metric = input("Choose metric to be tested from: min, mean, median, harmonic_mean ")
    action = input("Choose action to be performed on data using specified metric from: list, correlation list ")


main()
