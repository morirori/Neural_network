from abc import ABCMeta, abstractmethod


class AbstractNetwork(metaclass=ABCMeta):

    @property
    @abstractmethod
    def layers_list(self):
        pass

    @property
    @abstractmethod
    def input_layer(self):
        pass

    @property
    @abstractmethod
    def output_layer(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    def set_feature_value(self,data):
        counter = 0
        input_neuron = self.layers_list[0].neuron_vector
        for neuron in input_neuron:
            neuron.output = data[counter]
            counter += 1
