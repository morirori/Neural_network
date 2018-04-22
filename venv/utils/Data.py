from utils.DataImporter import  Data_importer
from utils.DataHelper import  DataHelper

class Data():

    def __init__(self,file,rows,shufle_data):
        self.data=Data_importer.import_data_to_list_of_dict(file,rows,shufle_data)
        self.labels=[]

    def label_iris_dat(self):
        self.labels=DataHelper.label_iris_data(self.data)
        return self.labels

    def get_raw_data(self):
        return DataHelper.extract_data(self.data)

    def normalize_data(self):
        return DataHelper.mornalize_input_data(self.data)

    def def_input_neurons(self):
        return len(self.data[-1])-1

    def def_output_neurons(self):
        return len(self.labels[-1])
