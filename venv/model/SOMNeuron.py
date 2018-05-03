from abstracts.AbstractNeuron import AbstractNeuron
from math import sqrt, exp
from utils.WinnerHolder import WinnerHolder


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

    @id.setter
    def id(self, id):
        self.__id = id

    @output.setter
    def output(self, output):
        self.__output = output

    def __init__(self, layer_id, id):
        self.__layer_id = layer_id
        self.__id = id
        self.input_synapses = []  # synapse
        self.output_synapses = []
        self.delta = 0
        self.winner_tag = ""
        self.__output = 0  # distance
        self.output_vector = [0,0,0]
        self.color = list()

    def update_weights(self,  gama,learning_factor =None):
        for synapse in self.input_synapses:
            synapse.synapse["weight"] = synapse.synapse["weight"] + self.delta * gama * (synapse.synapse["input_neuron"].output - synapse.synapse["weight"])

    def update(self, activation_fun=None, beta=None):
        temp_sum = 0
        for synapse in self.input_synapses:
            value= (synapse.synapse["input_neuron"].output * synapse.synapse["weight"])
            temp_sum += value*value
        self.__output = sqrt(temp_sum)

    def is_valid(self,sigma):
        winner_neuron = WinnerHolder.get_winner()
        distance = abs(self.__layer_id - winner_neuron.layer_id) + abs(self.__id - winner_neuron.id)
        return True if distance <= sigma else False

    def calculate_delta(self, sigma):
        winner_neuron = WinnerHolder.get_winner()
        distance = abs(self.__layer_id - winner_neuron.layer_id) + abs(self.__id - winner_neuron.id)
        self.delta = exp(-1 * (distance ^ distance) / (2 * (sigma * sigma)))

    def add_input_synapse(self, synapses_list):
        self.input_synapses.append(synapses_list)

    def add_output_synapse(self, synapses_list):
        self.output_synapses.append(synapses_list)

    def calculate_color(self):
        occureence=sum(self.output_vector)
        if occureence != 0:
            self.color=[self.output_vector[0]/occureence,self.output_vector[1]/occureence,self.output_vector[2]/occureence]
        else:
            self.color = None
        return self.color

    def __str__(self):
        print("layer_id:" + str(self.layer_id))
        print("id:" + str(self.id))
        print("output:" + str(self.output))
        print("delta:" + str(self.delta))
        print("is winner:" + str(self.winner_tag))
        print("INPUT CONNECTION")
        for synapse in self.input_synapses:
            synapse.print()
        print("OUTPUT CONNECTION")
        for synapse in self.output_synapses:
            synapse.print()
        return " /n"
