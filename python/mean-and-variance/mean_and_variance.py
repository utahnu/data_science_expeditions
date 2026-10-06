import argparse as ap

def main(array):
    # Write the compute the variance and the mean of a given list of numbers
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.

    def array_sum(array):
        sum = 0
        for num in array:
            sum += num
        return sum

    def stdev_sum(array):
        sum = 0
        mean = mean_maker(array)
        for num in array:
            temp = (num - mean)**2
            sum += temp
        return sum

    def mean_maker(array):
        mean = array_sum(array)/len(array)
        return mean

    def variance_maker(array):
        variance = stdev_sum(array)/len(array)
        return variance

    print(f"mean = {mean_maker(array)}\nvariance = {variance_maker(array)}")

    return None

if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int, help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    main(parsedArgs.array)