from factories.D1LayerFactory import  D1LayerFactory
from model.Networks.AutoEncoder import AutoEncoder
from utils.Tags import LayersTags,NodesTags


class AutoEncoderFactory():

    @staticmethod
    def create(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(D1LayerFactory.create(NodesTags.MLPNeuron, i, neurons_num))
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

