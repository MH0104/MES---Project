class ProductionOrder:
    def __init__(self, order_number, product_name, quantity):
        self.__order_number = order_number
        self.__product_name = product_name
        self.__quantity = quantity
        self.__status = "created"
        self.__produced_units = 0

    def get_order_number(self):
        return self.__order_number

    def start(self):
        if self.__status == "created":
            self.__status = "in progress"
        else:
            raise ValueError("Order is not in a state that can be started")

    def finish(self):
        if self.__status == "in progress":
            self.__status = "finished"
        else:
            raise ValueError("Order is not in a state that can be finished")

    def produce(self, units):
        if self.__status != "in progress":
            raise ValueError("Order must be in progress to produce units")
        else:
            self.__produced_units += units

    def get_production_efficiency(self):
        return round((self.__produced_units / self.__quantity) * 100, 2)