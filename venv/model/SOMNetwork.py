from abstracts.AbstractNetwork import AbstractNetwork
from utils.Tags import LayersTags
from math import exp
from utils.WinnerHolder import WinnerHolder
import matplotlib.pyplot as plt
import matplotlib
import time

class SOMNetwork(AbstractNetwork):

    def __init__(self, layers):
        self.__layers_list = layers
        self.__input_layer = layers[0]
        self.__output_layer = layers[-1]
        self.__sigma_initial = 1
        self.sigma=0
        self.__gama_initial=1
        self.label = list()
        self.alfa = 100
        self.gama = 0

    def train(self, data,label):
        self.calculate_initial_sigma()
        for i in range(len(data)):
                self.set_feature_value(data[i])
                self.set_label(label[i])
                self.calculate()
                self.set_winner_neuron_label(label[i])
                self.adapt_neurons(i)
                plt.title("iteration {}".format(i))
                self.plot_network()

    def adapt_neurons(self, i):
        self.calculate_radius(i)
        self.calculate_learning_rate(i)

        # print("sigma : = {}".format(self.sigma))
        # print("gama := {}".format(self.gama))

        for layer in self.layers_list:
            if layer.tag != LayersTags.INPUT_LAYER:
                layer.update_weights(self.sigma, self.gama)

    def calculate_learning_rate(self,iteration):
        self.gama = self.__gama_initial * exp(-(iteration/self.alfa))

    # sigma
    def calculate_radius(self,iteration):
        self.sigma = self.__sigma_initial * exp(-(iteration/self.alfa))

    def calculate(self):
        for layer in self.layers_list:
            if layer.tag != LayersTags.INPUT_LAYER:
                layer.update(activation_fun=None, beta=None)

    def set_label(self, label):
        self.label = label

    def predict(self):
        pass

    @property
    def layers_list(self):
        return self.__layers_list

    @property
    def input_layer(self):
        return self.__input_layer

    @property
    def output_layer(self):
        return self.__output_layer

    def print(self):
        toPrint = []
        for layer in self.layers_list:
            layer.print()
        print("output")

    def set_feature_value(self,data):
        counter = 0
        input_neuron = self.layers_list[0].neuron_vector
        for neuron in input_neuron:
            neuron.output = data[counter]
            counter += 1

    def calculate_initial_sigma(self):
        self.__sigma_initial=len(self.layers_list)/exp(1/self.alfa)

    def set_winner_neuron_label(self, label):
        winner=WinnerHolder.get_winner()
        if label==[1,0,0]:
            winner.output_vector[0] += 1
        elif label==[0,1,0]:
            winner.output_vector[1] += 1
        elif label==[0,0,1]:
            winner.output_vector[2] += 1

    def plot_network(self):
        for i in range(1,len(self.layers_list)):
            for j in range(len(self.layers_list[i].neuron_vector)):
                color=self.layers_list[i].neuron_vector[j].calculate_color()
                tag = self.layers_list[i].neuron_vector[j].winner_tag
                if color is None:
                    plt.scatter(i, j, color ='k',marker='v')
                elif color is not None and tag == "winner":
                    plt.scatter(i, j,  c=color, marker='*' )
                else:
                    plt.scatter(i, j,  c=color, marker='s' )

        plt.show()
        time.sleep(1/2)