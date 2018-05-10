from sklearn.datasets import fetch_mldata

class DataHelper():

    def __init__(self):
        pass

    @staticmethod
    def label_iris_data(data):
        label=[]

        for row in data:

            if row["class"]=='Iris-setosa':
                label.append([1,0,0])
            if row["class"]=='Iris-versicolor':
                label.append([0, 1, 0])
            if row["class"]=='Iris-virginica':
                label.append([0, 0, 1])

        return label

    @staticmethod
    def prepare_digit_data():
        recived_data = fetch_mldata('MNIST original',  data_home='C:/Users/michal/PycharmProjects/untitled1/venv/resources/digit_data')
        data=list()
        label=list()
        for i in range(len(recived_data.data)):
            data.append(recived_data.data[i].reshape(28 , 28))
            label.append(recived_data.target[i])
        return data,label

    @staticmethod
    def mornalize_input_data(unnormalized_data):
        normalized_data=[]
        unnormalized_data = DataHelper.extract_data(unnormalized_data)
        for row in unnormalized_data:
            temp=[]
            for i in range(len(row)):
                value = (row[i] - min(row)) / (max(row) - min(row))
                temp.append(value)
            normalized_data.append(temp)
        return normalized_data

    def extract_data(data):
        to_return=list()
        for i in range(len(data)):
            temp_list=[]
            for key, value in data[i].items():
                if key != "class":
                    temp_list.append(value)

            to_return.append(temp_list)
        return to_return