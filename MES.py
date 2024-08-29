import ProductionOrder,  ProductionLine, mes_utils

class MES:
    def __init__(self):
        self.__production_lines = []
    # Besprechungsbedarf, da redundanter Code
    def add_production_line(self, name):
        i = 0
        while True:
            try:
                new_production_line_name = str(name)
                if len(self.__production_lines) > 0:
                    for production_lines in self.__production_lines:
                        production_line = self.__production_lines[i]
                        comparison_name = production_line.get_production_line_name()
                        if new_production_line_name == comparison_name:
                            raise ValueError(f"Production line '{comparison_name}' already exist. Please enter a different name.")
                        i += 1
                break
            except TypeError:
                print(f"'{name}' is invalid. Name must be a string. Please try again.")
        new_production_line = ProductionLine(new_production_line_name)
        self.__production_lines.add(new_production_line)
        print(f"New production line '{new_production_line_name}' was successfully created.")

    def create_production_order(self, production_line_name:str, order_number:int, product_name, quantity):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = ProductionOrder(order_number, product_name, quantity)
        production_line.add_order(order)

    def start_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.start()
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def finish_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.finish()
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    def produce_units(self, production_line_name, order_number, units):
        production_line = self.get_production_line(production_line_name)
        if not production_line:
            raise ValueError(f"Production line '{production_line_name}' does not exist")
        order = mes_utils.get_order_by_number(production_line, order_number)
        if order:
            order.produce(units)
        else:
            raise ValueError(f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

    
    def get_production_lines(self):
        i = 0
        for production_lines in self.__production_lines:
            production_line = self.__production_lines[i]
            production_line_name = production_line.get_production_line_name()
            i+=1
            print(f"Production line No. {i}: {production_line_name}")

    def get_production_line(self, name):
        i = 0
        return_counter = False
        for production_lines in self.__production_lines:
            production_line = self.__production_lines[i]
            comparison_name = production_line.get_production_line_name()
            if name == comparison_name:
                return_counter = True
                return production_line
            i += 1
        if return_counter == False:
            answer = input(f'''No production line called "{name}" exists. Do you want to create this production line?
                Press "Y" to create this production line or press any other key to cancel: ''')
            answer = answer.upper()
            if answer == "Y":
                self.add_production_line(name)
            else:
                print("Draining was stopped.")
        return

#from mes import MES, ProductionOrder, ProductionLine, mes_utils

# Erstelle eine MES-Instanz
mes = MES()

# Füge eine Produktionslinie hinzu
mes.add_production_line("ProductionLine 1")

# Erstelle eine Bestellung
mes.create_production_order("ProductionLine 1", 1001, "Product 1", 100)

# Starte den Produktionsauftrag
mes.start_production_order("ProductionLine 1", 1001)

# Produziere Einheiten für einen Auftrag
mes.produce_units("ProductionLine 1", 1001, 50)

# Beende den Produktionsauftrag
mes.finish_production_order("ProductionLine 1", 1001)

# Berechne die Produktionseffizienz des Produktionsauftrags
#order = mes_utils.get_order_by_number(mes.production_lines["Produktionslinie 2"], 1001)
order = mes_utils.get_order_by_number(mes.get_production_line("ProductionLine 1"), 1001)
efficiency = mes_utils.calculate_production_efficiency(order)

print(f"The efficiency is {efficiency}%.")