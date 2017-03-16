#!/usr/bin/env python

def greetings():
    print("helloo resif people")

def repeat(x, callback):
    for _ in range(x):
        callback()

if __name__ == "__main__":
    repeat(3, greetings)
