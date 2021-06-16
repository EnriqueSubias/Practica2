#! /usr/bin/env python3


def test():
    rows, cols = (10,10)
    dynamic_results = [[0]*cols]*rows
    print(dynamic_results)

    print(dynamic_results[0][7])


if __name__ == "__main__":
    test()