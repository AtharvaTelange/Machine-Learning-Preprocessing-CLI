import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:

    tasks = [
        "Perform Normalization (MinMax Scaler)",
        "Perform Standardization (Standard Scaler)",
        "Show the Dataset"
    ]

    tasks_normalization = [
        "Normalize a specific column",
        "Normalize the whole dataset",
        "Show the Dataset"
    ]

    tasks_standardization = [
        "Standardize a specific column",
        "Standardize the whole dataset",
        "Show the Dataset"
    ]

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def perform_normailzation(self):
        while True:
            print("\nTasks (Normalization)")
            for index, value in self.tasks_normalization:
                print(f"{index + 1}. {value}")
            while True:
                try:
                    choice = int(input("\nWhta you want to do? (Press -1 to go back)"))
                except ValueError as error:
                    print(error)
                    continue
                break

            if choice == -1:
                break
            elif choice == 1:
                print(self.dataframe.dtypes)
                columns = input("Enter all the column/s you want  to normalize (Press  -1 to go back)").lower()
                if columns == "-1":
                    break
                for column in columns.split(" "):
                    try:
                        min_value = self.dataframe[column].min()
                        max_value = self.dataframe[column].max()
                        self.dataframe[column] = (self.dataframe[column] - min_value)/(max_value - min_value)
                    except:
                        print("\nNot possible")
                print("Done")
            elif choice == 2:
                try:
                    self.dataframe = pd.DataFrame(MinMaxScaler().fit_transform(self.dataframe))
                except:
                    print("\nNot possible as string columns are present")
            elif choice == 3:
                DataDescription.show_dataset(self)
            else:
                print("Try again. Wrong Value")

    def perform_standardization(self):
        while True:
            print("\nTasks (Standardization)")
            for index, value in self.tasks_standardization:
                print(f"{index + 1}. {value}")
            while True:
                try:
                    choice = int(input("\nWhta you want to do? (Press -1 to go  back)"))
                except ValueError as error:
                    print(error)
                    continue
                break
            if choice == -1:
                break
            elif choice == 1:
                print(self.dataframe.dtypes)
                columns = input("Enter the column/s you want to standardize: (Press -1 to go back)").lower()
                if columns == "-1":
                    break
                for column in columns.split(" "):
                    try:
                        mean = self.data[column].mean()
                        standard_deviation = self.dataframe[column].std()
                        self.data[column] = (self.dataframe[column] - mean)/standard_deviation
                    except:
                        print("\nNot Possible")
                print("\nDone")
            
            elif choice == 2:
                try:
                    self.dataframe = pd.DataFrame(StandardScaler().fit_transform(self.dataframe))
                    print("\nDone")
                except:
                    print("\nString columns are present. Not possible!")
            else:
                print("Wrong value. Try again")

    def handle_tasks(self):
        while True:
            print("\nTasks (Feature Scaling)")
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
                self.perform_normailzation()
            elif choice == 2:
                self.perform_standardization()
            elif choice == 3:
                DataDescription.show_dataset(self)
            else:
                print("Wrong Value. Try Again")
        return self.dataframe
