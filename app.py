#!/usr/bin/env python

def greetings():
    """salut les amis"""
    print("helloo resif people 3")

def repeat(x, callback):
    """call x times callback"""
    for _ in range(x):
        callback()

if __name__ == "__main__":
    repeat(3, greetings)
