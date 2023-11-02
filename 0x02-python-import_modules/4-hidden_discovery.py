#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i, value in vars(hidden_4).items():
        if i[:2] != "__":
            print(i)
