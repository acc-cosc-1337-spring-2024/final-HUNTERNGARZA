#write functions here, don't add input('') statements here!

class Stock:

    def __init__(self, symbol, company_name) -> None:
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    

def stock_purchase_history():
    appl_stock = Stock("APPL", "Apple Inc")
    cat_stock = Stock("CAT", "Caterpillar")
    ek_stock = Stock("EK", "Eastman Kodak")
    goog_stock = Stock("GOOG", "Google")
    msft_stock = Stock("MSFT", "Microsoft")

    stock_dictionary = {
        "Apple Stock": appl_stock,
        "Caterpillar Stock": cat_stock,
        "Eastman Kodak Stock": ek_stock,
        "Google Stock": goog_stock,
        "Microsoft Stock": msft_stock
    }

    print("Stock list")
    print("Symbol | Company Name")
    for i in stock_dictionary:
        stock = stock_dictionary[i]
        print(f"{stock.get_symbol()} | {stock.get_company_name()}")
