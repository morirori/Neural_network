from utils.Data import  Data
from factories.NetworkFactory import NetworkFactory
from model.Network import Network

data=Data("resources/IrisDataTrain.xls",125,shufle_data=True)
data.label_iris_dat()
layers=[data.def_input_neurons(),15,8,data.def_output_neurons()]
mlp = NetworkFactory.create(layers)
mlp.train(data.normalize_data(),data.label_iris_dat(),500)
predict_data=Data("resources/IrisData.xls",150,shufle_data=False)
returned_value=mlp.predict(predict_data.normalize_data(),predict_data.label_iris_dat())

labels=predict_data.label_iris_dat()
counter=0

for i in range(len(returned_value)):
    print("label: {0}".format(labels[i]))
    print("output: {0}".format(returned_value[i]))
    max_value=max(returned_value[i])
    index=returned_value[i].index(max_value)
    if labels[i][index] == 1:
        counter+=1

print("Samples: {0}, predicted {1}".format(len(labels),format(counter)))
