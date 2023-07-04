from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
mt5.initialize(login=5002557002, server="MetaQuotes-Demo", password="bkidk4ea")
print(mt5.account_info())
print("------------------------------------------------------------")
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
from_date=datetime(2020,1,1)
to_date=datetime.now()
deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*USD*")
if deals == None:
    print("No deals, error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =", len(deals))
    # display all obtained deals 'as is'
    for deal in deals:
        print("  ",deal)
    print()
    # display these deals as a table using pandas.DataFrame
    df=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)
print("---------------------------------------------------------------")
symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0
# display the first five ones
for s in symbols:
    count+=1
    print("{}. {}".format(count,s.name))
    if count==5: break
print("---------------------------------------------------------------")
selected = mt5.symbol_select("EURCAD", True)
if not selected:
    print("Failed to select EURCAD, error code =", mt5.last_error())
else:
    symbol_info = mt5.symbol_info("EURCAD")
    print(symbol_info)
    print("EURCAD: currency_base =", symbol_info.currency_base, "  currency_profit =", symbol_info.currency_profit,
          "  currency_margin =", symbol_info.currency_margin)
    print()

    # get symbol properties in the form of a dictionary
    print("Show symbol_info()._asdict():")
    symbol_info_dict = symbol_info._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))
    print()

    # convert the dictionary into DataFrame and print
    df = pd.DataFrame(list(symbol_info_dict.items()), columns=['property', 'value'])
    print("symbol_info_dict() as dataframe:")
    print(df)
print("---------------------------------------------------------------")


mt5.shutdown()