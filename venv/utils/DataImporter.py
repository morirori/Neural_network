import pandas
from random import shuffle
class Data_importer():

    @staticmethod
    def import_data_to_list_of_dict(file,ret_rows_num,shufle_data=True ):
        data=[]
        file=pandas.read_excel(file)
        data=file.to_dict("records")
        to_return=[]
        if ret_rows_num <= len(data):
            for i in range(ret_rows_num):
                to_return.append(data[i])

        if shufle_data:
            shuffle(to_return)
        return to_return
