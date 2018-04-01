from utils.Data import  Data
from factories.NetworkFactory import NetworkFactory
from model.Network import Network

data=Data("resources/IrisDataTrain.xls",125)
layers=[data.def_input_neurons(),3,2,data.def_output_neurons()]
mlp = NetworkFactory.create(layers)
mlp.train(data.normalize_data(),data.label_iris_dat(),5000)
predict_data=Data("resources/IrisData.xls",150)
mlp.predict(predict_data.normalize_data(),predict_data.label_iris_dat())
