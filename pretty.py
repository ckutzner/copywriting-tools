""" pretty-printing functions """

def print_matches(heading, dict):
    """ Pretty-print matches from a dictionary.
    :returns: a pretty printout of a dictionary where the values are a list.

    """
    print(" +++ {}: +++ ".format(heading))
    for k, v in dict.items():
        print("{}:\t{} mal gefunden in folgenden Ausdrücken: {}".format(k, v[0], ", ".join(v[1:])))

def print_filtered_matches(heading, dict):
    """ Pretty-print matches from a dictionary where the count is not zero.
    :returns: a pretty printout of a dictionary where the first item of the 
    values list is not zero.

    """
    print(" +++ {}: +++ ".format(heading))
    for k, v in dict.items():
        if v[0] != 0:
            print("{}:\t{} mal gefunden".format(k, v[0]))

