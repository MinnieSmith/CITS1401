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
                else:
                    new_countries[i].append("")

        file.close()
        return new_countries


def normalise(new_countries):
    l = len(new_countries[0])
    m = len(new_countries)

    for j in range(1, l):
        temp = []
        for i in range(m):
            if new_countries[i][j]:
                temp.append(new_countries[i][j])
        x = min(temp)
        y = max(temp)

        for i in range(m):
            if new_countries[i][j]:
                new_countries[i][j] = (new_countries[i][j] - x) / (y - x)

    return new_countries


def find_min(new_countries):
    l = len(new_countries[0])
    m = len(new_countries)
    min_countries = []
    for i in range(m):
        min_countries.append([])
        min_countries[i].insert(0, new_countries[i][0])
        temp = []
        for j in range(1, l):
            if new_countries[i][j] != "":
                temp.append(new_countries[i][j])
        x = min(temp)
        min_countries[i].append(x)

    return min_countries


def calculate_mean(new_countries):
    l = len(new_countries[0])
    m = len(new_countries)
    mean_countries = []
    for i in range(m):
        mean_countries.append([])
        mean_countries[i].insert(0, new_countries[i][0])
        temp = []
        n = 0
        for j in range(1, l):
            if new_countries[i][j] != "":
                temp.append(new_countries[i][j])
                n += 1
        mean = sum(temp) / n
        mean_countries[i].append(mean)

    return mean_countries


def calculate_median(new_countries):
    l = len(new_countries[0])
    m = len(new_countries)
    median_countries = []
    for i in range(m):
        median_countries.append([])
        median_countries[i].insert(0, new_countries[i][0])
        temp = []
        n = 0
        for j in range(1, l):
            if new_countries[i][j] != "":
                temp.append(new_countries[i][j])
                n += 1
        x = sorted(temp)
        lt = len(x)
        mt = int(lt / 2)
        if lt % 2 == 1:
            median = x[mt + 1]
        else:
            median = (x[mt] + x[mt + 1]) / 2
        median_countries[i].append(median)

    return median_countries


def calculate_harmonic_mean(new_countries):
    l = len(new_countries[0])
    m = len(new_countries)
    harmonic_mean_countries = []
    for i in range(m):
        harmonic_mean_countries.append([])
        harmonic_mean_countries[i].insert(0, new_countries[i][0])
        temp = []
        n = 0
        for j in range(1, l):
            if new_countries[i][j] != "" and new_countries[i][j] != 0.0:
                temp.append(1 / new_countries[i][j])
                n += 1
        x = sum(temp)
        harmonic_mean = n / x
        harmonic_mean_countries[i].append(harmonic_mean)

    return harmonic_mean_countries


def rank_list(country_list):
    m = len(country_list)
    country_list.sort(key=lambda x: x[1], reverse=True)
    return country_list


def correlation_list(new_countries, metric_list):
    l = len(new_countries[0])
    m = len(new_countries)
    life_ladder = []
    difference = []

    # calculate the rank for life ladder
    for i in range(m):
        life_ladder.append([])
        life_ladder[i].insert(0, new_countries[i][0])

    for i in range(m):
        life_ladder[i].append(new_countries[i][1])

    ranked_life_ladder = rank_list(life_ladder)

    for i in range(m):
        ranked_life_ladder[i].insert(0, (i + 1))

    # sort list alphabetically
    ranked_life_ladder.sort(key=lambda x: x[1], reverse=False)

    # calculate the rank for metric list
    ranked_metric_list = rank_list(metric_list)
    for i in range(m):
        ranked_metric_list[i].insert(0, (i + 1))

    # sort list alphabetically
    ranked_metric_list.sort(key=lambda x: x[1], reverse=False)

    # calculate the difference
    for i in range(m):
        difference.append([])
        difference[i].insert(0, new_countries[i][0])

    for i in range(m):
        d = abs(ranked_life_ladder[i][0] - ranked_metric_list[i][0])
        dsquared = d*d
        difference[i].append(dsquared)

    # sum the difference
    temp = []
    for i in range(m):
        temp.append(difference[i][1])
    sum_dsquared = sum(temp)

    # calculate Spearman Rank Correlation
    p = 1 - ((6*sum_dsquared)/(m*((m*m)-1)))
    print(p)
    return p


def main():
    filename = input("Enter name of file containing World Happiness data: ")
    metric = input("Choose metric to be tested from: min, mean, median, harmonic_mean ")
    action = input("Choose action to be performed on data using specified metric from: list, correlation list ")

    countries = open_file(filename)
    new_countries = normalise(countries)
    m = len(new_countries)

    if metric.lower() == "min" and action.lower() == "list":
        country_list = rank_list(find_min(new_countries))
        print("Ranked list of countries' happiness scores based on "
              "the min metric: ")
        for i in range(m):
            print('{} {}'.format(country_list[i][0], country_list[i][1]))
        return

    elif metric.lower() == "min" and action.lower() == "correlation list":
        print("The correlation coefficient between the study's ranking and "
              "the ranking using the min metric is: ")
        return correlation_list(new_countries, find_min(new_countries))

    elif metric.lower() == "mean" and action.lower() == "list":
        country_list = rank_list(calculate_mean(new_countries))
        print("Ranked list of countries' happiness scores based on "
              "the mean metric: ")
        for i in range(m):
            print('{} {}'.format(country_list[i][0], country_list[i][1]))
        return

    elif metric.lower() == "mean" and action.lower() == "correlation list":
        print("The correlation coefficient between the study's ranking and "
              "the ranking using the mean metric is: ")
        return correlation_list(new_countries, calculate_mean(new_countries))

    elif metric.lower() == "median" and action.lower() == "list":
        country_list = rank_list(calculate_median(new_countries))
        print("Ranked list of countries' happiness scores based on "
              "the median metric: ")
        for i in range(m):
            print('{} {}'.format(country_list[i][0], country_list[i][1]))
        return

    elif metric.lower() == "median" and action.lower() == "correlation list":
        print("The correlation coefficient between the study's ranking and "
              "the ranking using the median metric is: ")
        return correlation_list(new_countries, calculate_median(new_countries))

    elif metric.lower() == "harmonic_mean" and action.lower() == "list":
        country_list = rank_list(calculate_harmonic_mean(new_countries))
        print("Ranked list of countries' happiness scores based on "
              "the harmonic_mean metric: ")
        for i in range(m):
            print('{} {}'.format(country_list[i][0], country_list[i][1]))
        return

    elif metric.lower() == "harmonic_mean" and action.lower() == "correlation list":
        print("The correlation coefficient between the study's ranking and "
              "the ranking using the harmonic_mean metric is: ")
        return correlation_list(new_countries, calculate_harmonic_mean(new_countries))

    else:
        print("Unable to calculate value, please check selection entered")
        return


main()
