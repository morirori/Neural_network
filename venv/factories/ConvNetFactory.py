from factories.D2LayerFactory import D2LayerFactory
from utils.Tags import NodesTags
from model.Networks.ConvNetwork import ConvNetwork
from utils.Tags import LayersTags
from factories.D1LayerFactory import D1LayerFactory
class ConvNetFactory():

    @staticmethod
    def create(layer_list):
        layers = list()
        i = 0
        # layer_list list is a list of dict,
        # layer_list[0]={"TAG": Conv_layer,"row": 2,"column":8 }

        for layer in layer_list:
            if layer["TAG"]==LayersTags.CONV_LAYER:
                    layers.append(D2LayerFactory.create(i, layer["row"],layer["column"]))
            elif layer["TAG"]==LayersTags.INPUT_LAYER:
                layers.append(D2LayerFactory.create(i, layer["row"], layer["column"]))
            elif layer["TAG"]==LayersTags.HIDDEN_LAYER:
                layers.append(D1LayerFactory.create(NodesTags.MLPNeuron,i, layer["neurons"]))
            elif layer["TAG"]==LayersTags.OUTPUT_LAYER:
                layers.append(D1LayerFactory.create(NodesTags.MLPNeuron,i, layer["neurons"]))

            i= i + 1
        #
        # for i in range(len(neuron_list)):
        #
        #     if i == 0:
        #         layers[i].tag=LayersTags.INPUT_LAYER
        #         layers[i].connect_to_next_layer(layers[i+1])
        #
        #     elif i == len(neuron_list)-1:
        #         layers[i].tag=LayersTags.OUTPUT_LAYER
        #         #already connected
        #
        #     else:
        #         layers[i].tag = LayersTags.HIDDEN_LAYER
        #         layers[i].add_bias(NodeFactory.create(NodesTags.Bias,i,"Bias"))
        #         layers[i].connect_to_next_layer(layers[i+1])

        return ConvNetwork(layers)
