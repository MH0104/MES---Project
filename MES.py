from ProductionOrder import *
from ProductionLine import *
from mes_utils import *

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
        self.__production_lines.append(new_production_line)
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


# Erstelle eine MES-Instanz
mes = MES()

print("Welcome to MES")

while True:
    try:
        line = input("Type in your new production line: ")
        mes.add_production_line(line)
        print(f"Production line '{line}' added successfully.")
        break  # Erfolgreich hinzugefügt, verlässt die Schleife
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        continue  # Schleife fortsetzen bei Fehler

while True:
    try:
        orderline = input("Which production line do you want to create your order on?: ")
        ordernumb = input("What's the order number?: ")
        ordername = input("What's the product name?: ")
        quantity = int(input("Tell me the quantity: "))  # Annahme: Die Menge ist eine Ganzzahl

        mes.create_production_order(orderline, ordernumb, ordername, quantity)
        print(f"Order {ordernumb} for product '{ordername}' with quantity {quantity} added to line '{orderline}'.")
        break  # Erfolgreich erstellt, verlässt die Schleife
    except ValueError as e:
        print(f"Error: {e}. Please enter valid data.")
    except KeyError as e:
        print(f"Error: Production line not found: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        continue  # Schleife fortsetzen bei Fehler


start = input("Type (1) if you want to start the order, (2) to create a new production line, or (3) to create a new order: ")

if start == "1":
    try:
        # Starte den Produktionsauftrag
        mes.start_production_order(orderline, ordernumb)

        # Produziere Einheiten für einen Auftrag
        mes.produce_units(orderline, ordernumb, quantity)

        # Beende den Produktionsauftrag
        mes.finish_production_order(orderline, ordernumb)

        # Berechne die Produktionseffizienz des Produktionsauftrags
        order = mes_utils.get_order_by_number(mes.get_production_line(orderline), ordernumb)
        efficiency = mes_utils.calculate_production_efficiency(order)

        print(f"The efficiency is {efficiency}%.")
    except KeyError as e:
        print(f"Error: Order or production line not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

elif start == "2":
    while True:
        try:
            line = input("Type in your new production line: ")
            mes.add_production_line(line)
            print(f"Production line '{line}' added successfully.")
            break  # Erfolgreich hinzugefügt, verlässt die Schleife
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue  # Schleife fortsetzen bei Fehler

elif start == "3":
    while True:
        try:
            orderline = input("Which production line do you want to create your order on?: ")
            ordernumb = input("What's the order number?: ")
            ordername = input("What's the product name?: ")
            quantity = int(input("Tell me the quantity: "))  # Annahme: Die Menge ist eine Ganzzahl

            mes.create_production_order(orderline, ordernumb, ordername, quantity)
            print(f"Order {ordernumb} for product '{ordername}' with quantity {quantity} added to line '{orderline}'.")
            break  # Erfolgreich erstellt, verlässt die Schleife
        except ValueError as e:
            print(f"Error: {e}. Please enter valid data.")
        except KeyError as e:
            print(f"Error: Production line not found: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue  # Schleife fortsetzen bei Fehler

else:
    print("Invalid option selected.")
