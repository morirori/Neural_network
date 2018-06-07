from math import exp
from utils.Functions import sigmoid
from utils.Functions import sigmoid_derivative
from utils.Functions import hiberbolic
from utils.Functions import hiperbolic_derivative
from utils.Functions import ActivaionFunction
from abstracts.AbstractNeuron import AbstractNeuron


class ConvNeuron(AbstractNeuron):


    def update_weights(self, learning_factor, activation_fun):
        pass

    def update(self, activation_fun, beta):
        pass

    def calculate_delta(self, activation_fun):
        pass

    def __init__(self,layer_id, id):
        self.__layer_id=layer_id
        self.__id=id
        self.input_synapses=[]  #synapse
        self.output_synapses=[]
        self.delta = 0
        self.__output = 0

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