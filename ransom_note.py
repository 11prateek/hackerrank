"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    # Cut and collect words from magazine
    envelope = dict()
    for word in magazine:
        envelope.update(
            {word: 1 + envelope.get(word, 0)}
        )

    # Pull words out of the envelope to create message
    found_all_words = True

    for word in note:
        if envelope.get(word, 0) > 0:
            envelope.update(
                            {word: envelope.get(word, 0) - 1}
            )
        else:
            print("No")
            found_all_words = False
            break

    if found_all_words:
        print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
