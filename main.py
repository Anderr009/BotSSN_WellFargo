from Pages.SsnPage import SsnPage
from Utils.TextProcessor import TextProcessor
from Utils.SaveData import WriteOutput
from Utils.Worker import Worker
import threading

# test area
# txtProcessor = TextProcessor()
# txt = '305367996|08/12/1936|'
# data = txtProcessor.Preparate(txt)
# ssn = SsnPage()
# element = ssn.sendRequest(data)

#

def requestComplete(request,data,num):
    for i in data:
        print(i)
        element = request.sendRequest(i)
        print("Aqui")
        print(element)
        if element[0] != "Not rated" :
            WriteOutput(str(element[0]),num)
        else:
            print("Malo")

if __name__ == "__main__":
    #declaracion de clases
    txtProc = TextProcessor()
    ssnPage = SsnPage()

    num_hilos = 3
    data = txtProc.extractDataTxt("./Data/DataSet.txt")
    dataDivided = Worker.dataDivisor(data,num_hilos)
    
    print(dataDivided)  
    hilos = []
    counter = 1
    for i in range(len(dataDivided)):
        print(i)
        # Crea un nuevo hilo y pasa el parámetro que desees
        hilo = threading.Thread(target=requestComplete, args=(ssnPage,dataDivided[i], i))
        counter = counter + 1
        # Agrega el hilo a la lista
        hilos.append(hilo)
        
        # Inicia el hilo
        hilo.start()

    # Espera a que todos los hilos terminen
    # for hilo in hilos:
    #     hilo.join()
    
