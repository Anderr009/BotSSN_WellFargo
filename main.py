from Pages.SsnPage import SsnPage
from Utils.TextProcessor import TextProcessor
from Utils.SaveData import WriteOutput


# test area
txtProcessor = TextProcessor()
txt = '305367996|08/12/1936|'
data = txtProcessor.Preparate(txt)
ssn = SsnPage()
element = ssn.sendRequest(data)
if element[0] != "Eror" or element[0] != "Not rated":
    WriteOutput(element[0])
else:
    print("Malo")
