import argparse
import numpy as np

def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    documentsTxt = documentsTxt.lower()

    split = documentsTxt.split("\n")
    word_keys = []
    matrix_list = []

    for element in split:
        ssplit = element.split(" ")
        for word in ssplit:
            if word not in word_keys:
                word_keys.append(word)
    
    sorted_word_keys = sorted(word_keys)
    sorted_word_values = np.zeros(len(word_keys), dtype=int)
    word_frequency = dict(zip(sorted_word_keys, sorted_word_values))

    for element in split:
        temp_frequency = word_frequency.copy()
        ssplit = element.split(" ")
        for word in ssplit:
            temp_frequency[word]+=1
        element_values = [*temp_frequency.values()]
        matrix_list.append(element_values)
    
    matrix = np.array(matrix_list)
    print(matrix)
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())