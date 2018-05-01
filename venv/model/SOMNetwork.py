from abstracts.AbstractNetwork import AbstractNetwork


class SOMNetwork(AbstractNetwork):

    def __init__(self,layers):
        self.__layers_list = layers
        self.__input_layer = layers[0]
        self.__output_layer = layers[-1]
        self.sigma = 1
        self.alfa = 1000
        self.gama=0

    def train(self,data):
        for i in range(len(data)):
            self.set_feature_value(data[i])
            self.calculate()

    def calculate(self):
        for layer in self.layers_list:
                layer.update(activation_function=None, beta=None)

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
