from factories.D1LayerFactory import  D1LayerFactory
from utils.Tags import LayersTags,NodesTags
from model.Networks.SOMNetwork import SOMNetwork


class SOMFactory():

    @staticmethod
    def create(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(D1LayerFactory.create(NodesTags.SOMNeuron, i, neurons_num))
            i=i+1

        for i in range(len(neuron_list)):
            if i == 0:
                for j in range(1, len(neuron_list)):
                    layers[0].tag = LayersTags.INPUT_LAYER
                    layers[0].connect_to_next_layer(layers[j])
            else:
                layers[i].tag = LayersTags.SOM

        return SOMNetwork(layers)
