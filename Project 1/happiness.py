import os

def open_file(filename):
    countries = []
    new_countries = []

    # if file can't be opened
    if not os.path.isfile(filename):
        print("Unable to openfile")
        return None

    with open(filename) as file:
        for line in file:
            countries.append(line.rstrip().split(","))
        del countries[0]

        l = len(countries[0])
        m = len(countries)

        for i in range(m):
            new_countries.append([])
            new_countries[i].insert(0, countries[i][0])
            for j in range(1, l):
                if countries[i][j]:
                    new_countries[i].append(float(countries[i][j]))

        print(new_countries)
        file.close()
        return new_countries

def normalise(new_countries):
    l = len(new_countries[0])
    m = len(new_countries)
    life_ladder = []

    for i in range(m):
        life_ladder.append(new_countries[i][1])

    x = min(life_ladder)
    y = max(life_ladder)

    for i in range(m):
        new_countries[i][1] = (new_countries[i][1] - x)/(y-x)
        print(new_countries[i][1])





    return





def find_min(action):
    return

def calculate_mean(action):
    return

def calculate_median(action):
    return

def calculate_harmonic_mean(action):
    return






def main():
    # filename = input("Enter name of file containing World Happiness data: ")
    coutries = open_file("WHR2018Chapter2_reduced (2).csv")
    # metric = input("Choose metric to be tested from: min, mean, median, harmonic_mean ")
    # action = input("Choose action to be performed on data using specified metric from: list, correlation list ")
    normalise(coutries)

main()
