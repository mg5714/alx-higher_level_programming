#!/usr/bin/python3

def best_score(a_dictionary):
    best = {v: k for k, v in a_dictionary.items()} if a_dictionary else None
    return max(best)
