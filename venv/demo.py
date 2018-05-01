from utils.Data import  Data
from factories.NetworkFactory import NetworkFactory
from utils.Tags import NetworkTags

from utils.Functions import ActivaionFunction
import time

time_start=time.time()

data=Data("resources/IrisDataTrain.xls",125,shufle_data=True)
data.label_iris_dat()
normalized_data=data.normalize_data()
print(normalized_data[0])

layers=[data.def_input_neurons(),10,7,data.def_output_neurons()]
mlp = NetworkFactory.create(NetworkTags.MLPWithContiguousConnection,layers)

mlp.train(data.normalize_data(),data.label_iris_dat(),repetitions=500,activation_function=ActivaionFunction.SIGMOID)
predict_data=Data("resources/IrisData.xls",150,shufle_data=False)
returned_value=mlp.predict(predict_data.normalize_data(),predict_data.label_iris_dat(),activation_function=ActivaionFunction.SIGMOID)
labels=predict_data.label_iris_dat()
counter=0

for i in range(len(returned_value)):
     print("label: {0}".format(labels[i]))
     print("output: {0}".format(returned_value[i]))
     max_value = max(returned_value[i])
     index = returned_value[i].index(max_value)
     if labels[i][index] == 1:
        counter+=1

percaentage =counter*100/len(labels)
print("Samples: {0}, predicted {1}  percentage: {2}% ".format(len(labels),counter,percaentage))
print("first input data")
time_end=time.time()
print(time_end-time_start)