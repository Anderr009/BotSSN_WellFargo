from datetime import date


def WriteOutput(data):
    today = date.today()
    file = open(f"./Output/{today}.txt", "a")
    file.write("\n" + data)
    file.close()
