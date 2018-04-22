from utils.Data import  Data
from factories.NetworkFactory import NetworkFactory
from model.Network import Network
from utils.Functions import ActivaionFunction
from model.AutoEncoder import AutoEncoder
from factories.AutoEncodersFactory import AutoEncoderFactory
from utils.NetworkHelper import NetworkHelper

data=Data("resources/IrisDataTrain.xls",125,shufle_data=True)
data.label_iris_dat()
normalized_data=data.normalize_data()
layers=[data.def_input_neurons(),3,data.def_input_neurons()]
encoder = AutoEncoderFactory.create(layers)
encoder.train(normalized_data,normalized_data,repetitions=500,activation_function=ActivaionFunction.HYPERBOLIC_TANGENT)
encoder.remove_unneeded_layers()

layers=[data.def_input_neurons(),15,7,data.def_output_neurons()]
mlp = NetworkFactory.create_with_contigious_connection(layers)
merged=NetworkHelper.merge_autoencoder_to_mlp(encoder,mlp)
finnal=NetworkHelper.add_neurons_to_first_hidden_layer(merged,6)
finnal.update_id()

finnal.train(data.normalize_data(),data.label_iris_dat(),repetitions=500,activation_function=ActivaionFunction.HYPERBOLIC_TANGENT)

predict_data=Data("resources/IrisData.xls",150,shufle_data=False)
returned_value=finnal.predict(predict_data.normalize_data(),predict_data.label_iris_dat(),activation_function=ActivaionFunction.HYPERBOLIC_TANGENT)
labels=predict_data.label_iris_dat()
counter=0

for i in range(len(returned_value)):
    print("label: {0}".format(labels[i]))
    print("output: {0}".format(returned_value[i]))
    max_value=max(returned_value[i])
    index=returned_value[i].index(max_value)
    if labels[i][index] == 1:
        counter+=1

percaentage =counter*100/len(labels)
print("Samples: {0}, predicted {1}  percentage: {2}% ".format(len(labels),counter,percaentage))
