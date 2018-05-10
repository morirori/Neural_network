from factories.D1LayerFactory import  D1LayerFactory
from model.Networks.MLPNetwork import MLPNetwork
from utils.Tags import LayersTags,NodesTags
from factories.NodeFactory import NodeFactory


class MLPNetworkFactory():

    @staticmethod
    def create_with_contigious_connection(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(D1LayerFactory.create(NodesTags.MLPNeuron, i, neurons_num))
            i=i+1

        for i in range(len(neuron_list)):

            if i == 0:
                layers[i].tag=LayersTags.INPUT_LAYER
                layers[i].connect_to_next_layer(layers[i+1])

            elif i == len(neuron_list)-1:
                layers[i].tag=LayersTags.OUTPUT_LAYER
                #already connected

            else:
                layers[i].tag = LayersTags.HIDDEN_LAYER
                layers[i].add_bias(NodeFactory.create(NodesTags.Bias,i,"Bias"))
                layers[i].connect_to_next_layer(layers[i+1])

        return MLPNetwork(layers)

    @staticmethod
    def create_with_each_layer_connection(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(D1LayerFactory.create(NodesTags.MLPNeuron, i, neurons_num))
            i=i+1

        for i in range(len(neuron_list)):
            for j in range(len(neuron_list)):
                if i == 0:
                    layers[i].tag=LayersTags.INPUT_LAYER
                    if j > i:
                        layers[i].connect_to_next_layer(layers[j])

                elif i == (len(neuron_list)-1):
                    layers[i].tag=LayersTags.OUTPUT_LAYER

                elif 0 < i < (len(neuron_list) - 1):
                    layers[i].tag = LayersTags.HIDDEN_LAYER
                    if j > i:
                        layers[i].add_bias(NodeFactory.create(NodesTags.Bias, i, "Bias"))
                        layers[i].connect_to_next_layer(layers[j])

        return MLPNetwork(layers)

