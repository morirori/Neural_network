from builtins import len

from utils.Tags import LayersTags
from utils.Functions import ActivaionFunction
from utils.Functions import ActivationFunctionDoesntExist
from abstracts.AbstractNetwork import AbstractNetwork


class MLPNetwork(AbstractNetwork):

    def __init__(self, layer):
        self.__layers_list = layer
        self.activation_function = None
        self.__input_layer = layer[0]
        self.__output_layer = layer[-1]
        self.beta = 0.8
        self.learning_rate = 0.2
        self.label = list()

    # TODO: offline trainifn
    # TODO: updating learinig rate

    def train(self, data, labels, repetitions, activation_function):
        self.set_activation_fun(activation_function)
        for j in range(repetitions):
            for i in range(len(data)):
                self.set_feature_value(data[i])
                self.set_label(labels[i])
                self.calculate(beta=self.beta, activation_function=self.activation_function)
                #  print("label")
                #  print(self.label)
                #
                #  print("output")
                #  print(self.get_output())
                self.backpropagation(learning_factor=self.learning_rate, activation_function=self.activation_function)
            self.update_learning_rate()

    def predict(self, data, labels, activation_function):
        self.set_activation_fun(activation_function)
        to_return = list()
        for i in range(len(data)):
            self.set_feature_value(data[i])
            self.set_label(labels[i])
            self.calculate(beta=self.beta, activation_function=self.activation_function)
            to_return.append(self.get_output())
        return to_return

    def get_output(self):
        to_return = []
        for neuron in self.output_layer.neuron_vector:
            to_return.append(neuron.output)
        return to_return

    def check_corretnes(self):
        to_compare = []
        for neuron in self.output_layer.neuron_vector:
            to_compare.append(neuron.output)

    def set_label(self, label):
        self.label = label

    def calculate(self, beta, activation_function):
        for layer in self.layers_list:
            if layer.tag != LayersTags.INPUT_LAYER:
                layer.update(activation_function, beta)

    def backpropagation(self, learning_factor, activation_function):
        for layer in reversed(self.layers_list):
            if layer.tag == LayersTags.OUTPUT_LAYER:
                self.set_output_delta()
                layer.update_weights(activation_fun=activation_function, learning_factor=learning_factor)
            elif layer.tag == LayersTags.INPUT_LAYER or layer.tag == LayersTags.ENCODER:
                pass
            else:
                layer.update_weights(activation_fun=self.activation_function, learning_factor=learning_factor)

    def set_output_delta(self):
        for i in range(len(self.output_layer.neuron_vector)):
            delta = self.label[i] - self.output_layer.neuron_vector[i].output
            self.output_layer.neuron_vector[i].delta = delta

    def set_activation_fun(self, activation_fun):
        if ActivaionFunction(activation_fun) is not None:
            self.activation_function = activation_fun
        else:
            raise ActivationFunctionDoesntExist()

    def update_id(self):
        for i in range(len(self.layers_list)):
            self.layers_list[i].id = i
            self.layers_list[i].update_neuron_ids()

    def print(self):
        print(self.label)
        toPrint = []
        for layer in self.layers_list:
            layer.print()
        print("output")

    def update_learning_rate(self):
        self.beta = 0.99 * self.beta

    @property
    def layers_list(self):
        return self.__layers_list

    @property
    def input_layer(self):
        return self.__input_layer

    @property
    def output_layer(self):
        return self.__output_layer

    #
    # @layers_list.setter
    # def layers_list(self, layer_list):
    #     self.__layers_list = layer_list
    #
    # @output_layer.setter
    # def output_layer(self, output_layer):
    #     self.__output_layer = output_layer
    #
    # @input_layer.setter
    # def input_layer(self, input_layer):
    #     pass
