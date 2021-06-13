#! /usr/bin/env python3
"""Tests"""

import os
import os.path
import sys
import subprocess

todo_bien = True
count_acierto = 0
count_fallo = 0

if __name__ == "__main__":

    for alg in range(6):

        ALGORITHM = alg

        # 0 = Greedy Recursivo
        # 1 = Greedy Iterativo

        # 2 = BackTracking Recursivo
        # 3 = BackTracking Iterativo

        # 4 = Dynamic Programming Recursivo
        # 5 = Dynamic Programing Iterativo
        print(u"\n\u001b[32m######################################\u001b[0m")
        if ALGORITHM == 0:
            print(u"\u001b[32m########## Greedy Recursivo ##########\u001b[0m")
            FOLDER = "test-greedy/"

        if ALGORITHM == 1:
            print(u"\u001b[32m########## Greedy Iterativo ##########\u001b[0m")
            FOLDER = "test-greedy/"

        if ALGORITHM == 2:
            print(u"\u001b[32m####### BackTracking Recursivo #######\u001b[0m")
            FOLDER = "aqueductes/"

        if ALGORITHM == 3:
            print(u"\u001b[32m####### BackTracking Iterativo #######\u001b[0m")
            FOLDER = "aqueductes/"

        if ALGORITHM == 4:
            print(u"\u001b[32m### Dynamic Programming Recursivo ####\u001b[0m")
            FOLDER = "aqueductes/"

        if ALGORITHM == 5:
            print(u"\u001b[32m### Dynamic Programming Iterativo ####\u001b[0m")
            FOLDER = "aqueductes/"
        print(u"\u001b[32m######################################\u001b[0m\n")

        for filename in sorted(os.listdir(FOLDER)):
            if filename.endswith(".in"):
                if ALGORITHM == 2:
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
                    ):  # Lista de archivos a omitir
                        continue

                print(u"\u001b[36m-- " + FOLDER + filename + u" --\u001b[0m\n")

                if ALGORITHM == 0:
                    command = "./greedy_recursive.py " + FOLDER + filename
                if ALGORITHM == 1:
                    command = "./greedy_iterative.py " + FOLDER + filename
                if ALGORITHM == 2:
                    command = "./backtracking_recursive.py " + FOLDER + filename
                if ALGORITHM == 3:
                    command = "./backtracking_iterative.py " + FOLDER + filename
                if ALGORITHM == 4:
                    command = "./dynamic_programming_recursive.py " + FOLDER + filename
                if ALGORITHM == 5:
                    command = "./dynamic_programming_iterative.py " + FOLDER + filename

                result = subprocess.getoutput(command)

                filename = filename[:-3]
                s = open(FOLDER + filename + ".ans", "r")
                resultado_correcto = s.readline()

                if result == "":
                    print(
                        u"\u001b[31mNo se ha obtenido un resultado, programa sin print\u001b[0m\n"
                    )

                if result == "impossible":
                    print(u"\u001b[33mResultado Calculado", "impossible",
                          u"\u001b[0m")
                    if resultado_correcto.replace("\n", "") == "impossible":
                        print(u"\u001b[34mResultado Correcto ", "impossible",
                              u"\u001b[0m")
                        count_acierto += 1
                        print(u"\n\u001b[32mBIEN\u001b[0m\n")
                        continue

                    print(u"\u001b[34mResultado Correcto ", resultado_correcto,
                          u"\u001b[0m")
                    todo_bien = False
                    count_fallo += 1
                    print(u"\u001b[31m#### MAL ####\u001b[0m\n")
                    continue

                print(u"\u001b[33mResultado Calculado", result, u"\u001b[0m")
                print(u"\u001b[34mResultado Correcto ", resultado_correcto,
                      u"\u001b[0m")

                difference = int(result) - int(resultado_correcto)
                if difference == 0:
                    count_acierto += 1
                    print(u"\u001b[32mBIEN\u001b[0m\n")
                    continue

                todo_bien = False
                count_fallo += 1
                print(u"\u001b[31m#### MAL #### diferencia de:" +
                      str(difference) + "\u001b[0m\n")
    if todo_bien:
        print(
            u"\u001b[32m¡Enhorabuena, todos los resultados han dado correctamente!\u001b[0m\n"
        )

    else:
        print(u"\u001b[31mVaya, algún resultado ha fallado :(\u001b[0m\n")

    print(
        str(count_acierto) + " aciertos y " + str(count_fallo) +
        " fallos de " + str(count_acierto + count_fallo) + " pruebas\n")
