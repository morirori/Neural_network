from model.Neurons.MLPNeuron import MLPNeuron
from model.Neurons.SOMNeuron import SOMNeuron
from model.Neurons.ConvNeuron import ConvNeuron
from utils.Tags import NodesTags
from model.Neurons.Bias import Bias


class NodeFactory:

    @staticmethod
    def create(node_tag, layer_id, id):
        if node_tag == NodesTags.MLPNeuron:
            neuron = MLPNeuron(layer_id, id)
        elif node_tag == NodesTags.ConvNeuron:
            neuron = ConvNeuron(layer_id, id)
        elif node_tag == NodesTags.SOMNeuron:
            neuron=SOMNeuron(layer_id, id)

        elif node_tag == NodesTags.Bias:
            neuron = Bias(layer_id)

        return neuron

