from abstracts.AbstractNetwork import AbstractNetwork
from numpy import array
from matplotlib import pyplot


class ConvNetwork(AbstractNetwork):

    def __init__(self, layer):
        self.__layers_list = layer
        self.activation_function = None
        self.__input_layer = layer[0]
        self.__output_layer = layer[-1]
        self.beta = 0.8
        self.learning_rate = 0.2
        self.label = list()

    @property
    def layers_list(self):
        pass

    @property
    def input_layer(self):
        pass

    @property
    def output_layer(self):
        pass

    def train(self):
        pass

    def predict(self):
        pass

    def set_feature_value(self, data):
        i = 0
        for neuron in self.__layers_list[0].neuron_vector:
            j = 0
            for inner_neuron in neuron:
                inner_neuron.output = data[i][j]
                j += 1
            i += 1
        #     neuron.output = data[counter]
        #     counter += 1

    def print(self):
        for layer in self.__layers_list:
            layer.print()
        print("output")

    def plot(self):
        to_plot = list()
        for sublayer in self.__layers_list[0].neuron_vector:
            temp = list()
            for neuron in sublayer:
                temp.append(neuron.output)
            to_plot.append(temp)
        to_plot=array(to_plot)
        print(to_plot)
        pyplot.matshow(to_plot)
        pyplot.show()
