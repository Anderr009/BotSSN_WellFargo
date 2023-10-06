from dateutil.parser import parse


class TextProcessor:
    def dateFormatter(self, dateStr):
        # Intenta adivinar el formato de la fecha
        try:
            fecha = parse(dateStr, dayfirst=True)
        except ValueError:
            fecha = None

        # Reformatea la fecha en "mes-día-año" si se pudo adivinar el formato
        if fecha:
            fecha_formateada = fecha.strftime("%m-%d-%Y")
            print(fecha_formateada)
            return fecha_formateada
        else:
            print("No se pudo adivinar el formato de la fecha")

    def extractDataTxt(self, urlDataSet):
        dataSet = open(urlDataSet)
        # data set es el archivo de datos separados por |
        # verified data es para separar los ssn de los birth verified data consta de una lista anidada
        verifiedData = []
        # iteracion para sacar el dataSet
        for line in dataSet:
            verifiedData.append(self.Preparate(line))
            # leemos de nuevo
        return verifiedData

    def Preparate(self, text):
        ssn = ""
        birthDate = ""
        # validacion por si ya paso la parte del SSN
        passedSsn = False
        for t in text:
            if t != "|":
                if passedSsn == False:
                    ssn += t
                else:
                    birthDate += t
            else:
                if passedSsn:
                    break
                else:
                    passedSsn = True
        # end
        # asignacion a data
        data = [ssn, self.dateFormatter(birthDate)]
        return data

# | |

# test area
