import os, os.path, glob
import subprocess
import math
import sys

if __name__ == "__main__":
    
    #directory = "aqueductes/"
    directory = "test-greedy/"
 
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".in"):
            if filename == "secret-10.in":
                continue

            print(u"\n\u001b[36m-------- " + filename + u" --------\u001b[0m\n")

            #command = "./backtracking_recursive.py " + directory + filename
            command = "./greedy_recursive.py " + directory + filename
      
            result = subprocess.getoutput(command)
            
            filename = filename[:-3]
            s = open(directory + filename + ".ans", "r")
            comparar_resultado = s.readline()
            
            if result == "impossible":
                print(u"\n\u001b[33mResultado Calculado", "impossible", u"\u001b[0m")
                print(u"\u001b[32mResultado Correcto ", comparar_resultado, u"\u001b[0m")
                print(u"\u001b[32mOK\u001b[0m\n")
            else:
                print(u"\n\u001b[33mResultado Calculado", result, u"\u001b[0m")
                print(u"\u001b[32mResultado Correcto ", comparar_resultado, u"\u001b[0m")
                
                """if comparar_resultado == "impossible" or result == "impossible":
                    print("mal")
                else:
                    diff = int(float(result)) - int(comparar_resultado)
                    print(diff)
                    if diff == 0:"""
                    #    print(u"\u001b[32mOK\u001b[0m\n")
                    #else:
                    #    print(u"\u001b[31mMAL\u001b[0m\n")
                    