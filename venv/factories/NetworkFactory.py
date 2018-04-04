from factories.LayerFactory import  LayerFactory
from model.Network import Network

class NetworkFactory():

    @staticmethod
    def create_with_contigious_connection(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(LayerFactory.create(i,neurons_num))
            i=i+1

        for i in range(len(neuron_list)):
            if i == 0:
                layers[i].tag="input"
                layers[i].connect_forward(layers[i+1])

            elif i == len(neuron_list)-1:
                layers[i].tag="output"
                layers[i].connect_backward(layers[i-1])

            else:
                layers[i].tag = "hidden"
                layers[i].connect_forward(layers[i+1])
                layers[i].connect_backward(layers[i-1])

        return Network(layers)

    @staticmethod
    def create_with_each_layer_connection(neuron_list):
        layers= list()
        i=0
        for neurons_num in neuron_list:
            layers.append(LayerFactory.create(i,neurons_num))
            i=i+1

        for i in range(len(neuron_list)):
            for j in range(len(neuron_list)):
                if i == 0 and j !=0 :
                    layers[i].tag="input"
                    layers[i].connect_forward(layers[j])

                elif i == (len(neuron_list)-1) and j != (len(neuron_list)-1) :
                    layers[i].tag="output"
                    layers[i].connect_backward(layers[j])

                elif i != (len(neuron_list)-1) and i < j:
                    layers[i].tag = "hidden"
                    layers[i].connect_forward(layers[j])

                elif i != 0  and i > j:
                    layers[i].tag = "hidden"
                    layers[i].connect_backward(layers[j])

        return Network(layers)

