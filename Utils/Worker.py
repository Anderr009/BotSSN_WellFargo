
class Worker:
    def threadWorker(data):
        pass

    def dataDivisor(data, threads):
        dataProvider = round(len(data)/threads)
        dataThread = []
        dataTemp = []
        # comprobando en caso de que sea impar se le añada el ultimo elemento o coworker
        # al ulitmo elemento
        if dataProvider > len(data):
            dataTemp.append(data[-1])
        counter = 0
        for i in range(threads):
            for n in range(dataProvider):
                dataTemp.append(data[counter])
                counter += 1
            dataThread.append(dataTemp)
            dataTemp = []

        return dataThread

# test area


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print(Worker.dataDivisor(data, 6))
print(data[-1])
