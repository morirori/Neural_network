from utils.Data import  Data
from factories.NetworkFactory import NetworkFactory
from utils.Tags import NetworkTags
from utils.WinnerHolder import WinnerHolder

data=Data("resources/IrisDataTrain.xls",125,shufle_data=True)
data.label_iris_dat()
normalized_data=data.normalize_data()
layers = [data.def_input_neurons(), 4,4,4,4]
som = NetworkFactory.create(NetworkTags.SOM, layers)
# som.print()
som.train(data.get_raw_data(), data.label_iris_dat(),2000)
# som.print()
# print("=============================================")
# print(WinnerHolder.get_winner())
# print("distance")
# print(som.layers_list[1].neuron_vector[0])
