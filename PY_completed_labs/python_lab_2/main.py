import json
import string
import argparse
import os

def main(inputString):
    punctuation = string.punctuation
    #print(punctuation)

    puncstrippedString = inputString.translate(str.maketrans('', '', punctuation))
    #print(puncstrippedString)

    lowerString = puncstrippedString.lower()
    #print(lowerString)

    splitString = lowerString.split()
    #print(splitString)

    output_dict = {}
    for word in splitString:
        if word not in output_dict.keys():
            output_dict[word] = 0
        output_dict[word] += 1
    #print(output_dict)

    with open('./word-counts.json', 'w') as ff:
        json.dump(output_dict, ff)




    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"


    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    