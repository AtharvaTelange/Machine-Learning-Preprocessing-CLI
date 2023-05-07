from data_description import DataDescription
from imputation import DataImputation
from categorical  import EncodingCategoricalData
from feature_scaling  import FeatureScaling
from download import DownloadDataset
import argparse
import pandas as pd

class Main:

    tasks = [
        "Data Description",
        "Handling NULL Values",
        "Encoding Categorical Data",
        "Feature Scaling of the Dataset",
        "Download the Dataset"
    ]

    supported_file_extension = (
        ".csv"
    )

    def __init__(self, filename):
        print("Welcome to Machine  learning Preprocessor CLI!")
        self.filename = filename
        self.dataframe = []
        print("Verifying user input and converting...")
        self.accept_supported_file_extensions()
        self.convert_to_dataframe()
    
    def accept_supported_file_extensions(self):
        try:
            if not self.filename.endswith(self.supported_file_extension):
                raise SystemExit("Provide the dataset filename ending with" + self.supported_file_extension)
        except Exception as error:
            raise SystemExit(error)
    
    def convert_to_dataframe(self):
        try:
            self.dataframe = pd.read_csv(self.filename)
        except FileNotFoundError as error:
            raise SystemExit(error)
        except pd.errors.EmptyDataError as error:
            raise SystemExit(error)
        
    def column_rename_lowercase(self):
        for column in self.dataframe.columns.values:
            self.dataframe.rename(columns = {column : column.lower()}, inplace = True)

    def remove_target_dependent_variable(self):
        print("Columns\n")
        self.column_rename_lowercase()
        for column in self.dataframe.columns.values:
            print(column, end=" ")
        while True:
            column_name  = input("\nWhich is the target variable: (Press -1 to exit)").lower()
            if column_name == "-1":
                exit()
            choice = input("Are you sure? (y/n)").lower()
            if choice == "y":
                try:
                    self.dataframe.drop([column_name], axis = 1, inplace = True)
                except KeyError as error:
                    print(error)
                    continue
                print("Done!")
                break
            elif choice == "n":
                print("Select the target variable again!")
                continue
            else:
                print("Try again!")

    def handle_tasks(self):
        self.remove_target_dependent_variable()
        while True:
            print("\nTasks (Preprocessing)\n")
            for index, value in enumerate(self.tasks):
                print(f"{index + 1}. {value}")
            while True:
                try:
                    choice = int(input("\nWhat do you want to do? (Press -1 to exit): "))
                except ValueError as error:
                    print(error)
                    continue
                break

            if choice == -1:
                exit()
            
            elif choice == 1:
                DataDescription(self.dataframe).handle_tasks()
            
            elif choice == 2:
                self.dataframe = DataImputation(self.dataframe).handle_tasks()
            
            elif choice == 3:
                self .dataframe = EncodingCategoricalData(self.dataframe).handle_tasks()
            
            elif choice == 4:
                self.dataframe = FeatureScaling(self.dataframe).handle_tasks()
            
            elif choice == 5:
                DownloadDataset(self.dataframe).dowload()
            
            else:
                print("\nWrong Value! Try Again!!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    Main(args.filename).handle_tasks()
