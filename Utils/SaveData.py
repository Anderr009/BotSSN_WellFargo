from datetime import date


def WriteOutput(data,num):
    today = date.today()
    file = open(f"./Output/{today}-HiloNum{num}.txt", "a")
    file.write("\n" + data)
    file.close()
