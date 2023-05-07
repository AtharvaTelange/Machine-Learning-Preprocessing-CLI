import pandas as pd
from data_description import DataDescription

class EncodingCategoricalData:

    tasks = [
        "Show Categorical Columns",
        "Performing One Hot Encoding",
        "Show the Dataset"
    ]

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def show_categorical_columns(self):
        print("\n{0: <20}".format("Categorica Column") + "{0: <5}".format("Unique Values"))
        for column in self.dataframe.select_dtypes(include="onject"):
            print('{0: <20}'.format(column) + '{0: <5}'.format(self.dataframe[column].nuinque()))

    def performing_one_hot_encoding(self):
        categorical_columns = self.dataframe.select_dtypes(include="object")
        while True:
            column = input('\nWhich column would you like to one hot encode? (Press -1 to go back)').lower()
            if column == "-1":
                break
            if column in categorical_columns:
                self.dataframe = pd.get_dummies(data = self.dataframe, columns = [column])
                print("Encoding is done")

                choice = input("Do you  want more columns to be encoded? (y/n)").lower()
                if choice == "y":
                    continue
                else:
                    self.show_categorical_columns()
                    break
            else:
                print("Wrong column name. Try Again")

    def handle_tasks(self):
        while True:
            print("\nTasks")
            for index, value in enumerate(self.tasks):
                print(f"{index + 1}. {value}")
            while True:
                try:
                    choice = int(input("\Whta you want to do? (Press -1 to go back)"))
                except ValueError as error:
                    print(error)
                    continue
                break
            if choice == "-1":
                break
            elif choice == 1:
                self.show_categorical_columns()
            elif choice == 2:
                self.show_categorical_columns()
                self.performing_one_hot_encoding()
            elif choice == 3:
                DataDescription.show_dataset(self)
            else:
                print("Wrong Value! Try Again!")
        return self.dataframe