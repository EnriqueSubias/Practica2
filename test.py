#! /usr/bin/env python3

"""Tests"""

import os
import os.path
import subprocess


if __name__ == "__main__":

    ALGORITHM = 1
    # 0 = BackTracking Recursivo
    # 1 = Greedy Recursivo

    if ALGORITHM == 0:
        print(u"\n\u001b[36m### BackTracking Recursivo ##\u001b[0m\n")
        FOLDER = "aqueductes/"

    if ALGORITHM == 1:
        print(u"\n\u001b[36m###### Greedy Recursivo #####\u001b[0m\n")
        FOLDER = "test-greedy/"

    for filename in sorted(os.listdir(FOLDER)):
        if filename.endswith(".in"):
            if ALGORITHM == 0:
                if filename in (
                    "secret-10.in",
                    "secret-13.in",
                    "secret-14.in",
                    "secret-15.in",
                    "secret-16.in",
                    "secret-17.in",
                    "secret-18.in",
                    "secret-19.in",
                    "secret-20.in",
                    "secret-21.in",
                    "secret-22.in",
                    "secret-23.in",
                    "secret-24.in",
                    "secret-25.in",
                    "secret-26.in",
                    "secret-27.in",
                    "secret-28.in",
                ):
                    continue

            print(u"\u001b[36m-- " + FOLDER + filename + u" --\u001b[0m\n")

            if ALGORITHM == 0:
                command = "./backtracking_recursive.py " + FOLDER + filename
            if ALGORITHM == 1:
                command = "./greedy_recursive.py " + FOLDER + filename

            result = subprocess.getoutput(command)

            filename = filename[:-3]
            s = open(FOLDER + filename + ".ans", "r")
            resultado_correcto = s.readline()

            if result == "impossible":
                print(u"\u001b[33mResultado Calculado", "impossible", u"\u001b[0m")
                if resultado_correcto.replace("\n", "") == "impossible":
                    print(u"\u001b[34mResultado Correcto ", "impossible", u"\u001b[0m")
                    print(u"\n\u001b[32mBIEN\u001b[0m\n")
                    continue

                print(
                    u"\u001b[34mResultado Correcto ", resultado_correcto, u"\u001b[0m"
                )
                print(u"\u001b[31m#### MAL ####\u001b[0m\n")
                continue

            print(u"\u001b[33mResultado Calculado", result, u"\u001b[0m")
            print(u"\u001b[34mResultado Correcto ", resultado_correcto, u"\u001b[0m")

            difference = int(result) - int(resultado_correcto)
            if difference == 0:
                print(u"\u001b[32mBIEN\u001b[0m\n")
                continue

            print(
                u"\u001b[31m#### MAL #### diferencia de:"
                + difference
                + "\u001b[0m\n"
            )
