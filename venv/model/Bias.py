from abstracts.AbstractNeuron import AbstractNeuron


class Bias(AbstractNeuron):

    __id = "Bias"
    __output = 1

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

    def __init__(self, layer_id):
        self.__layer_id = layer_id

    def update_weights(self, learning_factor, activation_fun):
        pass

    def update(self, activation_fun, beta):
        pass

    def calculate_delta(self, activation_fun):
        pass

