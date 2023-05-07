import pandas as pd

class DataDescription:

    tasks = [
        "Describe a specific column",
        "Show properties of Each Column",
        "Show the Dataset"
    ]

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def describe_all_columns(self):
        print(self.dataframe.describe())
        print("\n\n")
        print(self.dataframe.info())

    def describe_specific_column(self):
        for column in self.dataframe.columns.values:
            print(column, end=" ")
        while True:
            column_name = input("\nWhich Column? ").lower()
            try:
                print(self.dataframe[column_name].describe())
            except KeyError as error:
                print(error)
                continue
            break

    def show_dataset(self):
        while True:
            try:
                row_number = int(input("\n How many rows(>0) to print? (Press -1  to go back) "))
                if row_number == -1:
                    break
                if row_number <= 0:
                    print("Number of rows must be greater than zero")
                    continue
                print(self.dataframe.head(row_number))
            except ValueError as error:
                print(error)
                continue
            break
        return

    def handle_tasks(self):
        while True:
            print("\nTasks (Data Description)")
            for index, value in enumerate(self.tasks):
                print(f"{index + 1}. {value}")
            while True:
                try:
                    choice = int(input("\nWhat do you want to do? (Press -1 to go back) "))
                except ValueError as error:
                    print(error)
                    continue
                break
            if choice == -1:
                break
            elif choice == 1:
                self.describe_specific_column()
            elif choice == 2:
                self.describe_all_columns()
            elif choice == 3:
                self.show_dataset()
            else:
                print("\nWrong Value! Try Again!!")