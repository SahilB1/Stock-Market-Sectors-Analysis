# Importing all needed modules including the alpaca api
import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Keys and url needed to make calls to the alpaca api
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
API_KEY = "PKEZS7GSPAVR3P1UT195"
SECRET_KEY = "iifNp8Qug1lCKyvPWy4e0LSpAdEr4V7NEEVplDME"

class Stock_Market:
    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')
        self.data = pd.read_csv("companylist.csv")

        self.health_care_short_term = []
        self.health_care_long_term = []
        self.health_care_current = []

        self.miscellaneous_short_term = []
        self.miscellaneous_long_term = []
        self.miscellaneous_current = []

        self.basic_industries_long_term = []
        self.basic_industries_short_term = []
        self.basic_industries_current = []

        self.capital_goods_long_term = []
        self.capital_goods_short_term = []
        self.capital_goods_current = []

        self.public_utilities_long_term = []
        self.public_utilities_short_term = []
        self.public_utilities_current = []

        self.consumer_services_long_term = []
        self.consumer_services_short_term = []
        self.consumer_services_current = []

        self.consumer_non_durables_long_term = []
        self.consumer_non_durables_short_term = []
        self.consumer_non_durables_current = []

        self.transportation_long_term = []
        self.transportation_short_term = []
        self.transportation_current = []

        self.consumer_durables_long_term = []
        self.consumer_durables_short_term = []
        self.consumer_durables_current = []

        self.energy_long_term = []
        self.energy_short_term = []
        self.energy_current = []

        self.technology_long_term = []
        self.technology_short_term = []
        self.technology_current = []

        self.finance_short_term = []
        self.finance_long_term = []
        self.finance_current = []

    def health_care(self):
        health_care = np.array((self.data[self.data["Sector"] == "Health Care"]["Symbol"]))

        length = 365
        for index in range(0, int(len(health_care)/7)):
            bars = self.alpaca.get_barset(health_care[index], 'day', limit=length)
            stock_bars = bars[health_care[index]]
            self.health_care_short_term.append(stock_bars[-12].o)
            self.health_care_long_term.append(stock_bars[0].o)
            self.health_care_current.append(stock_bars[-1].c)

        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.health_care_short_term))
        plt.scatter(x, self.health_care_short_term, c='red')
        plt.scatter(x, self.health_care_long_term, c='blue')
        plt.scatter(x, self.health_care_current, c='green')

        plt.plot(x, self.health_care_short_term, c='red', label="health-care-12-days-ago")
        plt.plot(x, self.health_care_long_term, c='blue', label="health-care-365-days-ago")
        plt.plot(x, self.health_care_current, c='green', label="health-care-current")

        plt.legend()
        plt.show()

    def miscellaneous(self):
        miscellaneous = np.array((self.data[self.data["Sector"] == "Miscellaneous"]["Symbol"]))

        length = 365
        for index in range(0, int(len(miscellaneous))):
            bars = self.alpaca.get_barset(miscellaneous[index], 'day', limit=length)
            stock_bars = bars[miscellaneous[index]]
            self.miscellaneous_short_term.append(stock_bars[-12].o)
            self.miscellaneous_long_term.append(stock_bars[0].o)
            self.miscellaneous_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.miscellaneous_short_term))
        plt.scatter(x, self.miscellaneous_short_term, c='red')
        plt.scatter(x, self.miscellaneous_long_term, c='blue')
        plt.scatter(x, self.miscellaneous_current, c='green')

        plt.plot(x, self.miscellaneous_short_term, c='red', label="miscellaneous-12-days-ago")
        plt.plot(x, self.miscellaneous_long_term, c='blue', label="miscellaneous-365-days-ago")
        plt.plot(x, self.miscellaneous_current, c='green', label="miscellaneous-current")

        plt.legend()
        plt.show()

    def basic_industries(self):
        basic_industries = np.array((self.data[self.data["Sector"] == "Basic Industries"]["Symbol"]))

        length = 365
        for index in range(0, int(len(basic_industries))):
            bars = self.alpaca.get_barset(basic_industries[index], 'day', limit=length)
            stock_bars = bars[basic_industries[index]]
            self.basic_industries_short_term.append(stock_bars[-12].o)
            self.basic_industries_long_term.append(stock_bars[0].o)
            self.basic_industries_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.basic_industries_short_term))
        plt.scatter(x, self.basic_industries_short_term, c='red')
        plt.scatter(x, self.basic_industries_long_term, c='blue')
        plt.scatter(x, self.basic_industries_current, c='green')

        plt.plot(x, self.basic_industries_short_term, c='red', label="basic-industries-12-days-ago")
        plt.plot(x, self.basic_industries_long_term, c='blue', label="basic-industries-365-days-ago")
        plt.plot(x, self.basic_industries_current, c='green', label="basic-industries-current")

        plt.legend()
        plt.show()

    def capital_goods(self):
        capital_goods = np.array((self.data[self.data["Sector"] == "Capital Goods"]["Symbol"]))

        length = 365
        for index in range(0, int(len(capital_goods)/2)):
            bars = self.alpaca.get_barset(capital_goods[index], 'day', limit=length)
            stock_bars = bars[capital_goods[index]]
            self.capital_goods_short_term.append(stock_bars[-12].o)
            self.capital_goods_long_term.append(stock_bars[0].o)
            self.capital_goods_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.capital_goods_short_term))
        plt.scatter(x, self.capital_goods_short_term, c='red')
        plt.scatter(x, self.capital_goods_long_term, c='blue')
        plt.scatter(x, self.capital_goods_current, c='green')

        plt.plot(x, self.capital_goods_short_term, c='red', label="capital-goods-12-days-ago")
        plt.plot(x, self.capital_goods_long_term, c='blue', label="capital-goods-365-days-ago")
        plt.plot(x, self.capital_goods_current, c='green', label="capital-goods-current")

        plt.legend()
        plt.show()

    def public_utilities(self):
        public_utilities = np.array((self.data[self.data["Sector"] == "Public Utilities"]["Symbol"]))

        length = 365
        for index in range(0, int(len(public_utilities))):
            bars = self.alpaca.get_barset(public_utilities[index], 'day', limit=length)
            stock_bars = bars[public_utilities[index]]
            self.public_utilities_short_term.append(stock_bars[-12].o)
            self.public_utilities_long_term.append(stock_bars[0].o)
            self.public_utilities_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.public_utilities_short_term))
        plt.scatter(x, self.public_utilities_short_term, c='red')
        plt.scatter(x, self.public_utilities_long_term, c='blue')
        plt.scatter(x, self.public_utilities_current, c='green')

        plt.plot(x, self.public_utilities_short_term, c='red', label="public-utilities-12-days-ago")
        plt.plot(x, self.public_utilities_long_term, c='blue', label="public-utilities-365-days-ago")
        plt.plot(x, self.public_utilities_current, c='green', label="public-utilities-current")

        plt.legend()
        plt.show()

    def consumer_services(self):
        consumer_services = np.array((self.data[self.data["Sector"] == "Consumer Services"]["Symbol"]))

        length = 365
        for index in range(0, int(len(consumer_services)/7)):
            bars = self.alpaca.get_barset(consumer_services[index], 'day', limit=length)
            stock_bars = bars[consumer_services[index]]
            self.consumer_services_short_term.append(stock_bars[-12].o)
            self.consumer_services_long_term.append(stock_bars[0].o)
            self.consumer_services_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.consumer_services_short_term))
        plt.scatter(x, self.consumer_services_short_term, c='red')
        plt.scatter(x, self.consumer_services_long_term, c='blue')
        plt.scatter(x, self.consumer_services_current, c='green')

        plt.plot(x, self.consumer_services_short_term, c='red', label="consumer-services-12-days-ago")
        plt.plot(x, self.consumer_services_long_term, c='blue', label="consumer-services-365-days-ago")
        plt.plot(x, self.consumer_services_current, c='green', label="consumer-services-current")

        plt.legend()
        plt.show()

    def consumer_non_durables(self):
        consumer_non_durables = np.array((self.data[self.data["Sector"] == "Consumer Non-Durables"]["Symbol"]))

        length = 365
        for index in range(0, int(len(consumer_non_durables))):
            bars = self.alpaca.get_barset(consumer_non_durables[index], 'day', limit=length)
            stock_bars = bars[consumer_non_durables[index]]
            self.consumer_non_durables_short_term.append(stock_bars[-12].o)
            self.consumer_non_durables_long_term.append(stock_bars[0].o)
            self.consumer_non_durables_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.consumer_non_durables_short_term))
        plt.scatter(x, self.consumer_non_durables_short_term, c='red')
        plt.scatter(x, self.consumer_non_durables_long_term, c='blue')
        plt.scatter(x, self.consumer_non_durables_current, c='green')

        plt.plot(x, self.consumer_non_durables_short_term, c='red', label="consumer-non-durables-12-days-ago")
        plt.plot(x, self.consumer_non_durables_long_term, c='blue', label="consumer-non-durables-365-days-ago")
        plt.plot(x, self.consumer_non_durables_current, c='green', label="consumer-non-durables-current")

        plt.legend()
        plt.show()

    def transportation(self):
        transportation = np.array((self.data[self.data["Sector"] == "Transportation"]["Symbol"]))

        length = 365
        for index in range(0, int(len(transportation))):
            bars = self.alpaca.get_barset(transportation[index], 'day', limit=length)
            stock_bars = bars[transportation[index]]
            self.transportation_short_term.append(stock_bars[-12].o)
            self.transportation_long_term.append(stock_bars[0].o)
            self.transportation_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.transportation_short_term))
        plt.scatter(x, self.transportation_short_term, c='red')
        plt.scatter(x, self.transportation_long_term, c='blue')
        plt.scatter(x, self.transportation_current, c='green')

        plt.plot(x, self.transportation_short_term, c='red', label="transportation-12-days-ago")
        plt.plot(x, self.transportation_long_term, c='blue', label="transportation-365-days-ago")
        plt.plot(x, self.transportation_current, c='green', label="transportation-current")
        plt.bar

        plt.legend()
        plt.show()

    def consumer_durables(self):
        consumer_durables = np.array((self.data[self.data["Sector"] == "Consumer Durables"]["Symbol"]))

        length = 365
        for index in range(0, int(len(consumer_durables))):
            bars = self.alpaca.get_barset(consumer_durables[index], 'day', limit=length)
            stock_bars = bars[consumer_durables[index]]
            self.consumer_durables_short_term.append(stock_bars[-12].o)
            self.consumer_durables_long_term.append(stock_bars[0].o)
            self.consumer_durables_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.consumer_durables_short_term))
        plt.scatter(x, self.consumer_durables_short_term, c='red')
        plt.scatter(x, self.consumer_durables_long_term, c='blue')
        plt.scatter(x, self.consumer_durables_current, c='green')

        plt.plot(x, self.consumer_durables_short_term, c='red', label="consumer-durables-12-days-ago")
        plt.plot(x, self.consumer_durables_long_term, c='blue', label="consumer-durables-365-days-ago")
        plt.plot(x, self.consumer_durables_current, c='green', label="consumer-durables-current")

        plt.legend()
        plt.show()

    def energy(self):
        energy = np.array((self.data[self.data["Sector"] == "Energy"]["Symbol"]))

        length = 365
        for index in range(0, int(len(energy)/2)):
            bars = self.alpaca.get_barset(energy[index], 'day', limit=length)
            stock_bars = bars[energy[index]]
            self.energy_short_term.append(stock_bars[-24].o)
            self.energy_long_term.append(stock_bars[0].o)
            self.energy_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.energy_short_term))
        plt.scatter(x, self.energy_short_term, c='red')
        plt.scatter(x, self.energy_long_term, c='blue')
        plt.scatter(x, self.energy_current, c='green')

        plt.plot(x, self.energy_short_term, c='red', label="energy-24-days-ago")
        plt.plot(x, self.energy_long_term, c='blue', label="energy-365-days-ago")
        plt.plot(x, self.energy_current, c='green', label="energy-current")

        plt.legend()
        plt.show()

    def technology(self):
        technology = np.array((self.data[self.data["Sector"] == "Technology"]["Symbol"]))

        length = 365
        for index in range(0, int(len(technology)/7)):
            bars = self.alpaca.get_barset(technology[index], 'day', limit=length)
            stock_bars = bars[technology[index]]
            self.technology_short_term.append(stock_bars[-12].o)
            self.technology_long_term.append(stock_bars[0].o)
            self.technology_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.technology_short_term))
        plt.scatter(x, self.technology_short_term, c='red')
        plt.scatter(x, self.technology_long_term, c='blue')
        plt.scatter(x, self.technology_current, c='green')

        plt.plot(x, self.technology_short_term, c='red', label="technology-12-days-ago")
        plt.plot(x, self.technology_long_term, c='blue', label="technology-365-days-ago")
        plt.plot(x, self.technology_current, c='green', label="technology-current")

        plt.legend()
        plt.show()

    def finance(self):
        finance = np.array((self.data[self.data["Sector"] == "Finance"]["Symbol"]))

        length = 365
        for index in range(0, int(len(finance)/7)):
            bars = self.alpaca.get_barset(finance[index], 'day', limit=length)
            stock_bars = bars[finance[index]]
            self.finance_short_term.append(stock_bars[-12].o)
            self.finance_long_term.append(stock_bars[0].o)
            self.finance_current.append(stock_bars[-1].c)
        print("Done!")

        plt.figure(figsize=(15,5))
        x = np.arange(0, len(self.finance_short_term))
        plt.scatter(x, self.finance_short_term, c='red')
        plt.scatter(x, self.finance_long_term, c='blue')
        plt.scatter(x, self.finance_current, c='green')

        plt.plot(x, self.finance_short_term, c='red', label="finance-12-days-ago")
        plt.plot(x, self.finance_long_term, c='blue', label="finance-365-days-ago")
        plt.plot(x, self.finance_current, c='green', label="finance-current")

        plt.legend()
        plt.show()
