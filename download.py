import pandas  as pd

class DownloadDataset:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def dowload(self):
        new_filename = input("\nEnter the filename you want: (Press  -1 to go back)")
        if new_filename == "-1":
            return
        new_filename = new_filename + ".csv"
        pd.DataFrame(self.dataframe).to_csv(new_filename, index = False)
        print("It's done")
        if input("\nDo you wan to exit not? (y/n)").lower() == "y":
            print("\nExiting")
            exit()
        else:
            return