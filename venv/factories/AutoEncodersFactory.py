from factories.LayerFactory import  LayerFactory
from model.AutoEncoder import AutoEncoder
from utils.LayersTags import LayersTags
class AutoEncoderFactory():

    @staticmethod
    def create(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(LayerFactory.create(i,neurons_num))
            i=i+1

        for i in range(len(neuron_list)):
            if i == 0:
                layers[i].tag=LayersTags.INPUT_LAYER
                layers[i].connect_to_next_layer(layers[i + 1])

            elif i == len(neuron_list)-1:
                layers[i].tag=LayersTags.OUTPUT_LAYER

            elif i <= round((len(neuron_list)-1)/2):
                layers[i].tag = LayersTags.ENCODER
                layers[i].connect_to_next_layer(layers[i + 1])

            elif i > round((len(neuron_list)-1)/2):
                layers[i].tag = LayersTags.DECODER
                layers[i].connect_to_next_layer(layers[i + 1])

        return AutoEncoder(layers)

