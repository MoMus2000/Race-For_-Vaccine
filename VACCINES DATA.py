from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from pprint import pprint
import time

ts = TimeSeries(key='' , output_format='pandas')
Moderna, meta_data = ts.get_daily(symbol = 'MRNA', outputsize = 'full')
Gillead, meta_data = ts.get_daily(symbol = 'GILD', outputsize = 'full')
Regeneron, meta_data = ts.get_daily(symbol = 'REGN', outputsize = 'full')
astraZeneka, meta_data = ts.get_daily(symbol = 'AZN', outputsize = 'full')
cansinoBiologic , meta_data = ts.get_daily(symbol = 'CASBF', outputsize = 'full')

# print(data)
# while True
Modernas  = Moderna['4. close']
Gilleads = Gillead['4. close']
Regenerons =Regeneron['4. close']
astraZenekas = astraZeneka['4. close']
cansinoBiologics = cansinoBiologic['4. close']
Moderna_change = Modernas.pct_change()
Gillead_changes = Gilleads.pct_change()
Regeneron_changes = Regenerons.pct_change()
cansinoBiologic_changes = cansinoBiologics.pct_change()
astraZenekas_changes = astraZenekas.pct_change()


print("FORE RUNNERS IN VACCINE RACE AND THEIR STOCKS \n")
print("Moderna")
print(Moderna_change[-1])
print("Gillead")
print(Gillead_changes[-1])
print("Regeneron")
print(Regeneron_changes[-1])
print("astraZeneka")
print(astraZenekas_changes[-1])
print("Chinese : cansinoBiologics")
print(cansinoBiologic_changes[-1])

stockData = pd.DataFrame(
{
'Moderna' : Moderna_change[-1],
'Gillead' : Gillead_changes[-1],
'Regeneron':Regeneron_changes[-1],
'astraZeneka':astraZenekas_changes[-1],
'Chinese: cansinoBiologics': cansinoBiologic_changes[-1],

},index=[0]
)
stockData.to_csv("stockDATA.csv",mode='a', header=False)

    # time.sleep(60)
