from factories.NodeFactory import NodeFactory
from model.Layer.D1Layer import D1Layer
from utils.Tags import NodesTags


class D1LayerFactory:

    @staticmethod
    def create(network_tag,layer_num,number_of_neuron):
        neuron_list=[]

        for i in range(number_of_neuron):
            if network_tag == NodesTags.MLPNeuron:
                neuron_list.append(NodeFactory.create(NodesTags.MLPNeuron,layer_num,i))
            elif network_tag == NodesTags.SOMNeuron:
                neuron_list.append(NodeFactory.create(NodesTags.SOMNeuron,layer_num,i))

        layer = D1Layer(neuron_list, layer_num)
        return layer
