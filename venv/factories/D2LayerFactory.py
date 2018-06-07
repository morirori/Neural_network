from factories.NodeFactory import NodeFactory
from utils.Tags import NodesTags
from model.Layer.D2Layer import D2Layer


class D2LayerFactory:

    @staticmethod
    def create(layer_num,layer_num_x,layer_num_y):

        neuron_list=list()

        for i in range(layer_num_x):
            temp = list()
            for j in range(layer_num_y):
                    temp.append(NodeFactory.create(NodesTags.ConvNeuron,layer_num,{'row': i, 'column': j}))
            neuron_list.append(temp)

        # TODO implement layer creation
        layer = D2Layer(neuron_list, layer_num)
        return layer
