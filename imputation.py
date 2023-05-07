import pandas as pd
from data_description import DataDescription

class DataImputation:

    tasks = [
        "Show number of Null Values",
        "Remove Columns",
        "Fill Null Values (with mean)",
        "Fill Null Values (with median)",
        "Fill Null Values (with mode)",
        "Show the Dataset"
    ]

    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def show_columns(self):
        for column in self.dataframe.columns.values:
            print(column, end=" ")

    def show_null_value_count(self):
        print("\nNull Values for each column:")
        for column in self.dataframe.columns.values:
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.dataframe[column]))))
        print("")
    
    def remove_columns(self):
        self.show_columns()
        while True:
            columns = input("\nEnter all the column/s you want to delete (Press -1 to go back) ").lower()

            if columns == "-1":
                break

            choice = input("Are  you sure? (y/n)").lower()
            if choice == 'y':
                try:
                    self.dataframe.drop(columns.split(" "), axis = 1, inplace  = True)
                except KeyError as error:
                    print(error)
                    continue
                print("Done")
                break
            else:
                print("Not deleting")
                
    def fill_null_value_mean(self):
        self.show_columns()
        while True:
            column = input("\nEnter the column name: (Press -1 to go  back)").lower()

            if column == "-1":
                break
            choice = input("Are  you sure? (y/n)").lower()
            if  choice == "y":
                try:
                    self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].mean())
                except KeyError as error:
                    print(error)
                    continue
                except TypeError as error:
                    print(error)
                    continue
                print("Done")
                break
            else:
                print("Not Changing")

    def fill_null_value_median(self):
        self.show_columns()
        while True:
            column = input("\nEnter the column name: (Press -1 to go  back)").lower()

            if column == "-1":
                break
            choice = input("Are  you sure? (y/n)").lower()
            if  choice == "y":
                try:
                    self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median())
                except KeyError as error:
                    print(error)
                    continue
                except TypeError as error:
                    print(error)
                    continue
                print("Done")
                break
            else:
                print("Not Changing")

    def fill_null_values_mode(self):
        self.show_columns()
        while True:
            column = input("\nEnter the column name: (Press -1 to go  back)").lower()

            if column == "-1":
                break
            choice = input("Are  you sure? (y/n)").lower()
            if  choice == "y":
                try:
                    self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].mode()[0])
                except KeyError as error:
                    print(error)
                    continue
                except TypeError as error:
                    print(error)
                    continue
                print("Done")
                break
            else:
                print("Not Changing")

    def handle_tasks(self):
        while True:
            print("\nImputation Tasks")
            for index, value in enumerate(self.tasks):
                print(f"{index + 1}. {value}")
            while True:
                try:
                    choice = int(input("\nWhat you want to do? (Press -1 to go back)"))
                except ValueError as error:
                    print(error)
                    continue
                break
            if choice == -1:
                break
            elif choice == 1:
                self.show_null_value_count()
            elif choice == 2:
                self.remove_columns()
            elif choice == 3:
                self.fill_null_value_mean()
            elif choice  == 4:
                self.fill_null_value_median()
            elif choice == 5:
                self.fill_null_values_mode()
            elif choice == 6:
                DataDescription.show_dataset(self)
            else:
                print("\nWrong Value! Try Again!!")
        return self.dataframe