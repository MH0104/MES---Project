# Description: This file contains the ProductionLine class which is used to create a production line object. 
# The production line object contains a name and a list of orders. 
# The production line object is used to store orders that are assigned to a production line.
class ProductionLine:
    # Constructor
    def __init__(self, name):
        self.__production_line_name = name
        self.__orders = []

    # Adds an order to the production line
    def add_order(self, order):
        self.__orders.append(order)
        print("Added " + str(order) + " to the order list")

    # Returns the production line name
    def get_production_line_name(self):
        return self.__production_line_name
        
    # Returns a list of orders
    def get_orders(self):
        return self.__orders
    