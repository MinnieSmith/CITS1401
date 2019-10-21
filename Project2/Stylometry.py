import os
import math


def open_file(filename):

    # if file can't be opened
    if not os.path.isfile(filename):
        print("Unable to openfile")
        return None

    with open(filename, 'r') as file:
            text = file.read()

    file.close()
    return text


def text_punctuation(filename):
    text_string = open_file(filename)
    # Find commas and semicolons in text and update dictionary
    punctuations = ';,'
    text_punctuations = {';': 0, ',': 0, '-': 0, "'": 0}

    for char in text_string:
        if char in punctuations:
            text_punctuations[char] += 1

    #  Find apostrophes
    for i in range(len(text_string)):
        if text_string[i] == "'":
            if text_string[i+1].isalpha() and text_string[i-1].isalpha():
                text_punctuations["'"] += 1

    # Find hypens
    for i in range(len(text_string)):
        if text_string[i] == "-":
            if text_string[i+1].isalpha() and text_string[i-1].isalpha():
                text_punctuations["-"] += 1
    return text_punctuations


def text_unigrams(filename):
    # Open file and parse text removing capitals and punctuations storing in an array
    text_string = open_file(filename)
    text_length = len(text_string)

    # Replace all '--' with space
    for j in range(text_length):
        if text_string[j] == '-':
            if text_string[j+1] == '-':
                text_string = text_string[:j] + ' ' + ' ' + text_string[j+2:]

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text_without_punctuations = ""
    for char in text_string:
        if char not in punctuations:
            text_without_punctuations = text_without_punctuations + char
    text = text_without_punctuations.lower().split()

    # Loop through text and populate dictionary
    unigram_words = {}
    for word in text:
        if word in unigram_words:
            unigram_words[word] += 1
        else:
            unigram_words[word] = 1
    return unigram_words


def text_conjunctions(filename):
    # Open file and parse text removing capitals and punctuations storing in an array
    text_string = open_file(filename)
    text_length = len(text_string)

    # Replace all '--' with space
    for j in range(text_length):
        if text_string[j] == '-':
            if text_string[j+1] == '-':
                text_string = text_string[:j] + ' ' + ' ' + text_string[j+2:]

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text_without_punctuations = ""
    for char in text_string:
        if char not in punctuations:
            text_without_punctuations = text_without_punctuations + char
    text = text_without_punctuations.lower().split()

    # Create a dictionary with all the conjunction words as key and initiate all values to zero
    conjunction_words = {}
    conjunction_list = ["also", "although", "and", "as", "because", "before", "but", "for", "if", "nor", "of",
                        "or", "since", "that", "though", "until", "when", "whenever", "whereas",
                        "which", "while", "yet"]
    for i in range(len(conjunction_list)):
        conjunction_words[conjunction_list[i]] = 0

    # Loop through text find dictionary key and update count
    for word in text:
        if word in conjunction_words:
            conjunction_words[word] += 1
    return conjunction_words


def text_composite(filename):
    profile = text_conjunctions(filename)
    profile.update(text_punctuation(filename))
    num_of_sentences = 0
    num_of_paragraphs = 1

    # Find the average number of words per sentence
    text_string = open_file(filename)
    text_length = len(text_string)
    for i in range(text_length):
        if text_string[i] == '.' or text_string[i] == '!' or text_string[i] == '?':
            if text_string[i+1] == ' ' or text_string[i+1] == "'" or text_string[i+1] == "\""\
                    or text_string[i+1] == '\n':
                num_of_sentences += 1

    # Replace all '--' with space
    for j in range(text_length):
        if text_string[j] == '-':
            if text_string[j+1] == '-':
                text_string = text_string[:j] + ' ' + ' ' + text_string[j+2:]

    text = text_string.split()
    num_of_words = len(text)
    profile['avg_word_per_sentence'] = round(num_of_words/num_of_sentences, 4)

    # Find average sentences per paragraph
    for k in range(text_length):
        if text_string[k] == '\n' and text_string[k-1] == '\n':
            num_of_paragraphs += 1
    profile['avg_senteces_per_paragaph'] = round(num_of_sentences/num_of_paragraphs, 4)
    return profile


def calculate_distance(profile1, profile2):
    values1 = list(profile1.values())
    values2 = list(profile2.values())
    sum_of_distance = 0

    for i in range(len(values1)):
        sum_of_distance = sum_of_distance + math.pow((values1[i] - values2[i]), 2)

    distance = round(math.sqrt(sum_of_distance), 4)
    return distance


def main(textfile1, textfile2, feature):
    if feature == "unigrams":
        profile1 = text_unigrams(textfile1)
        profile2 = text_unigrams(textfile2)
        distance = calculate_distance(profile1, profile2)
        return distance, profile1, profile2

    elif feature == "punctuation":
        profile1 = text_punctuation(textfile1)
        profile2 = text_punctuation(textfile2)
        distance = calculate_distance(profile1, profile2)
        return distance, profile1, profile2

    elif feature == "conjunctions":
        profile1 = text_conjunctions(textfile1)
        profile2 = text_conjunctions(textfile2)
        distance = calculate_distance(profile1, profile2)
        return distance, profile1, profile2

    elif feature == "composite":
        profile1 = text_composite(textfile1)
        profile2 = text_composite(textfile2)
        distance = calculate_distance(profile1, profile2)
        return distance, profile1, profile2
    else:
        print("The argument does not contain correct parameters ")


main("sample1.txt", "sample2.txt", "composite")

