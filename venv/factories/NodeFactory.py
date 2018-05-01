from model.MLPNeuron import MLPNeuron
from model.SOMNeuron import SOMNeuron
from utils.Tags import NodesTags
from model.Bias import Bias


class NodeFactory:

    @staticmethod
    def create(node_tag, layer_id, id):
        if node_tag == NodesTags.MLPNeuron:
            neuron=MLPNeuron(layer_id, id)

        elif node_tag == NodesTags.SOMNeuron:
            neuron=SOMNeuron(layer_id, id)

        elif node_tag == NodesTags.Bias:
            neuron = Bias(layer_id)

        return neuron

