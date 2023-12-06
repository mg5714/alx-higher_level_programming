#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_k = None
    best_v = 0

    for k, v in a_dictionary.items():
        if v > best_v:
            best_k = k
            best_v = v
    return best_k
