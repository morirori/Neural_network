import pandas 

class Data_importer():
    
    def __init__(self, file):
        self.file=file
        
    def import_data_to_list_of_dict(self,ret_rows_num):
        data=[]
        file=pandas.read_excel(self.file)
        data=file.to_dict("records")
        to_return=[]
        if ret_rows_num <= len(data):
            for i in range(ret_rows_num):
                to_return.append(data[i])
        return to_return

