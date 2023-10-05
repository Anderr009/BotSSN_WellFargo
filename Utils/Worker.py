
class Worker:
    def numThreads(num_hilos,request):
        hilos = []
    
        for i in range(num_hilos):
            # Crea un nuevo hilo y pasa el parámetro que desees
            hilo = threading.Thread(target=request, args=(i,))
            
            # Agrega el hilo a la lista
            hilos.append(hilo)
            
            # Inicia el hilo
            hilo.start()
    
        # Espera a que todos los hilos terminen
        for hilo in hilos:
            hilo.join()

    def dataDivisor(data, threads):
        dataProvider = round(len(data)/threads)
        # print(dataProvider)
        # if int(dataProvider) != 0:
        #     return False        
        dataThread = []
        dataTemp = []
        # print(dataProvider)
        # comprobando en caso de que sea impar se le añada el ultimo elemento o coworker
        # al ulitmo elemento
        # print(dataProvider * threads)
        if (dataProvider * threads) != len(data):
            restData =  len(data) - (dataProvider * threads) 
            # print(restData)
            for i in range(restData):
                i+=1
                dataTemp.append(data[-i])
                #--------
                     
        counter = 0
        for i in range(threads):
            for n in range(dataProvider):
                try:
                    dataTemp.append(data[counter])
                except IndexError:
                    pass
                counter += 1
            dataThread.append(dataTemp)
            dataTemp = []

        return dataThread

# test area




