"""Codes that allow me to modify my spreadsheet(reworking) as well as looking up the new stock price"""
import warnings
warnings.filterwarnings("ignore") #Suppress Future warning from pandas.util.testing
"""Other packages"""
import yfinance as yf   # downloading data from yahoo finance
import generalfunction
import glob, os
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr


#theFile = openpyxl.load_workbook("stock portfolio.xlsx")
#allSheetNames = theFile.sheetnames
#currentSheet = 0


#for sheet in allSheetNames:
 #   if sheet == "stock portfolio":
  #      currentSheet = theFile[sheet]


#def find_specific_cell(str):
 #   for row in range(1, currentSheet.max_row + 1):
  #      for column in "ABCDE":
   #         cell_name = "{}{}".format(column, row)
    #        if currentSheet[cell_name].value == str:
     #           return cell_name
    #return 0

#def get_column_letter(specificCellLetter):
 #   if specificCellLetter == 0:
  #      return 0
   # letter = specificCellLetter[0:-1]
    #return letter

#def get_role_value(specificCellLetter):
 #   if specificCellLetter == 0:
  #      return 0
   # number = specificCellLetter[1:2]
    #return number

#def get_all_values_by_cell_letter(letter):
 #   for row in range(1, currentSheet.max_row + 1):
  #      for column in letter:
   #         cell_name = "{}{}".format(column, row)
    #        #print(cell_name)
     #       print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))


def main():
    yf.pdr_override()
    sp500 = pdr.get_data_yahoo('^GSPC',period = ('30d'))
    sp500.head()
    print(sp500)
    fig = sp500['Close'].plot(title=str('sp500' + " stock price"))
    plt.show(block=False)
    action = 1
    while action != 0:
        print("What do you want to do today\n")
        action = generalfunction.getnumber("\npress 1 to search current and historic stock price \npress 2 to download data about a stock \npress 3 to view downloaded data \npress 4 to show s&p 500 index \npress 5 to use the calculator \npress 0 to quit ")
        #if action == 1:
            #Whattofind = input("What you want to find? ")
            #specificCellletter = (find_specific_cell(Whattofind))
            #value = get_role_value(specificCellletter)
            #newvalue = input("What the new value? ")
            #currentSheet['C' + str(value)] = float(newvalue)
            #theFile.save('stock portfolio.xlsx')
            #print("The stock " + Whattofind + " value has changed to " +newvalue)
        #elif action == 2:
            #Whattofind = input("What you want to find? ")
            #specificCellletter = (find_specific_cell(Whattofind))
            #value = get_role_value(specificCellletter)
            #price = currentSheet['C' + str(value)].value
            #print("\nThe value of the stock "+ Whattofind +" is "+ str(price) +"\n")

        if action == 1:     #A function to show stock price by asking the user to input the stock symbol, also provide the user the ability to choose the time period
            Whattofind = input("Which stock price are you interested? ")
            whattofindprice = yf.Ticker(Whattofind)
            pricehistory = whattofindprice.history(period="10d")
            print("The price of " + Whattofind + " is\n" + str(pricehistory))
            plt.clf()
            fig = pricehistory['Close'].plot(title = str(Whattofind + " stock price"))
            plt.show(block=False)
            print("Power by yahoo finance")
            option = input("Would you want more data? \npress y for yes \npress n for no \n")
            if option == "y":
                period = generalfunction.getnumber("How many days of data do you want? ")
                plt.clf()
                pricehistory = whattofindprice.history(period=(str(period) +"d"))
                fig = pricehistory['Close'].plot(title=str(Whattofind + " stock price"))
                print("The price of " + Whattofind + " is\n" + str(pricehistory))
                plt.show(block=False)

        elif action == 2:    #A function allows the user to download stock data by asking the user to input the stock symbol and the start and end date then save the data into a csv file
            Whattofind = input("Which stock/stocks price are you interested? (You can enter one or more stocks just separate the stock symbol with space)")
            startdate = input("Startdate (format: YYYY-MM-DD): ")
            enddate = input("Enddate (format: YYYY-MM-DD): ")
            data = yf.download(str(Whattofind), start=str(startdate), end=str(enddate)).to_csv(str(Whattofind) + ".csv")
            print("The data have been saved in the directory "+str(os.getcwd()))

        elif action == 3:   #A function to allow user to open csv files
            print("Which csv do you want to open? (Please type the full name): ")
            currentpathnote = os.getcwd()
            os.chdir(str(currentpathnote))
            for file in glob.glob("*.csv"):
                print(file)
            filename = input("")
            try:
                df = pd.read_csv(filename, header =0, index_col = 'Date', parse_dates=True)
                print(df)
            except ValueError:
                df = pd.read_csv(filename, skiprows= 1)
                print(df)

        elif action == 4: #A function allows the user to search up s&p 500 index history
            plt.clf()
            sp500 = pdr.get_data_yahoo('^GSPC', period=('30d'))
            sp500.head()
            print(sp500)
            fig = sp500['Close'].plot(title=str('sp500' + " stock price"))
            plt.show(block=False)

        elif action == 5: #A function that allow the user to use the calculator
            calc = input("Type Calculation: \n")
            print("Answer: " + str(eval(calc)))




