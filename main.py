from Pages.SsnPage import SsnPage
from Utils.TextProcessor import TextProcessor

#test area
txtProcessor = TextProcessor()
txt = '308285539|01/17/1931|'
data = txtProcessor.Preparate(txt)
ssn = SsnPage()
ssn.sendRequest(data)