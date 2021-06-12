
if __name__ == "__main__":
    main()
    exit(0)

    directory = "aqueductes/"

    debug = True
    superDebug = True
    if superDebug == True:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".in"):
                if filename == "secret-10.in":
                    continue

        #os.chdir("/mydir")
            #for file in glob.glob("*.txt"):

                #DIR = 'testing/'
                #for name in os.listdir(DIR):
                    #if os.path.isfile(os.path.join(DIR, name)):
                       # print(name)

                print(u"\n\u001b[36m-------- " + filename+ " --------\u001b[0m\n")
                #print(os.path.join(filename))

                #list = os.listdir("testing/") # dir is your directory path
                #number_files = len(list)
                #print (number_files)

                filename = filename[:-3]

                f = open(directory + filename + ".in", "r")
                valores = f.readline().split(" ")

                s = open(directory + filename + ".ans", "r")
                comparar_resultado = s.readline()

                n_points = int(valores[0])
                h_max = int(valores[1])
                alpha = int(valores[2])
                beta = int(valores[3])
                
                calcular = calcul(n_points,h_max,alpha,beta)
                if calcular.is_valid():         
                    # Y segunda columna
                    if calcular.read_terrain(f):  

                        #f.close # pylint dice que es innecesario ponerlo
                        #result = [0, 0]
                        #result = check_overlap_and_calculate_cost_multiple_arches()
                        #result[1] = calculate_cost_one_arch()
                        print("Calculando ...")
                        #print(calcular.get_n_points())
                        #print(calcular.get_posX())
                        #print(calcular.get_posY())
                        result = rec_func(calcular.get_n_points(), calcular.get_posX(), calcular.get_posY())
                        if result != "impossible":
                            result = result + (calcular.get_h_max() - calcular.get_posY()[-1] ) * alpha


                        #print(int(result))

                        #result = int(result)
                        if debug == True:
                            print(u"\u001b[32mDebug Enabled\u001b[0m")
                            #print(pos_x)
                            #print(pos_y)
                            if result == "impossible":
                                print ("impossible")
                                print (comparar_resultado)
                            else:
                                print(u"\n\u001b[33mResultado Calculado", int(result) , u"\u001b[0m")
                                print(u"\u001b[32mResultado Correcto ", comparar_resultado , u"\u001b[0m")
                                comparar_resultado2 = " " + comparar_resultado
                                diff = int(result) - int(comparar_resultado)
                                print(diff)
                                #if int(result) == comparar_resultado or int(result) == comparar_resultado2:
                                if diff == 0:
                                    print(u"\u001b[32mOK\u001b[0m\n")
                                else:
                                    print(u"\u001b[31mMAL\u001b[0m\n")

                            #print(u"\u001b[36m" , pos_x , u"\u001b[0m")
                    else:
                        print("impossible")
                else:
                    print("impossible")
        exit(0)

    if debug == True:
        filename = "secret-08"

        f = open("aqueductes/" + filename +".in", "r")
        valores = f.readline().split(" ")

        s = open("aqueductes/" + filename + ".ans", "r")
        comparar_resultado = s.readline()

    if debug == False:

        if len(sys.argv) != 2:
            print(u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n")
            exit(0)
        f = open(sys.argv[1], "r")
        valores = f.readline().split(" ")

    n_points = int(valores[0])
    h_max = int(valores[1])
    alpha = int(valores[2])
    beta = int(valores[3])

    calcular = calcul(n_points,h_max,alpha,beta)

    if is_valid():
        pos_x = [0]              # X primera columna
        pos_y = [0]              # Y segunda columna
        if read_terrain():

            #f.close # pylint dice que es innecesario ponerlo
            #result = [0, 0]
            #result = check_overlap_and_calculate_cost_multiple_arches()
            #result[1] = calculate_cost_one_arch()

            result = rec_func(n_points, pos_x, pos_y)

            #print(" " + str(int(result)))
            #print(int(result))
            print("\n")
            print(result)
            print("\n")

            #result = int(result)
            if debug == True:
                print(u"\u001b[32mDebug Enabled\u001b[0m")
                print(pos_x)
                print(pos_y)
                print(u"\n\u001b[33mResultado Calculado", int(result) , u"\u001b[0m")
                print(u"\u001b[32mResultado Correcto ", comparar_resultado , u"\u001b[0m")
                comparar_resultado2 = " " + comparar_resultado
                diff = int(result) - int(comparar_resultado)
                print(diff)
                #if int(result) == comparar_resultado or int(result) == comparar_resultado2:
                if diff == 0:
                    print(u"\u001b[32mOK\u001b[0m\n")
                else:
                    print(u"\u001b[31mMAL\u001b[0m\n")

                print(u"\u001b[36m" , pos_x , u"\u001b[0m")
        else:
            print("impossible")
    else:
        print("impossible")
