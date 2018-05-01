from abstracts.AbstractNeuron import AbstractNeuron
from math import sqrt, exp


class SOMNeuron(AbstractNeuron):

    @property
    def output(self):
        return self.__output

    @property
    def id(self):
        return self.__id

    @property
    def layer_id(self):
        return self.__layer_id

    @layer_id.setter
    def layer_id(self, layer_id):
        self.__layer_id = layer_id

    def __init__(self, layer_id, id):
        self.__layer_id = layer_id
        self.__id = id
        self.input_synapses = []  # synapse
        self.output_synapses = []
        self.delta = 0
        self.__output = 0  # distance

    def update_weights(self, learning_factor, gama):
        for synapse in self.input_synapses:
            synapse.synapse["weight"] = synapse.synapse["weight"] + self.delta * gama * (synapse.synapse["input_neuron"].output - synapse.synapse["weight"])

    def update(self, activation_fun=None, beta=None):
        temp_sum = 0
        for synapse in self.input_synapses:
            temp_sum += synapse.synapse["input_neuron"].output * synapse.synapse["weight"]
        self.__output = sqrt(temp_sum)

    def calculate_delta(self, sigma):
        # TODO distance = ...
        # TODO self.delta=exp(-1 * (distance^ 2) / (2 * sigma ^ 2))
        pass

    def add_input_synapse(self, synapses_list):
        self.input_synapses.append(synapses_list)

    def add_output_synapse(self, synapses_list):
        self.output_synapses.append(synapses_list)

    def __str__(self):
        print("layer_id:" + str(self.layer_id))
        print("id:" + str(self.id))
        print("output:" + str(self.delta))
        print("delta:" + str(self.output))
        print("INPUT CONNECTION")
        for synapse in self.input_synapses:
            synapse.print()
        print("OUTPUT CONNECTION")
        for synapse in self.output_synapses:
            synapse.print()
        return " /n"
