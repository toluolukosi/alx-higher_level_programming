#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
Footer
© 2023 GitHub, Inc.
Footer navigation
Term
