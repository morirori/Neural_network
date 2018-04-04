from model.Layer import Layer
from utils.Functions import ActivaionFunction
from utils.Functions import ActivationFunctionDoesntExist
class Network:

    def __init__(self,layer):
        self.layers_list=layer
        self.activation_function=""
        self.input_layer=layer[0]
        self.output_layer=layer[-1]
        self.beta = 0.1
        self.learning_rate = 0.15
        self.label=list()
    # TODO: offline trainifn
    # TODO: updating learinig rate


    def train(self,data,labels, repetitions,activation_function):
        self.set_activation_fun(activation_function)
        for i in range(len(data)):
            self.set_feature_value(data[i])

            self.set_label(labels[i])
            for i in range(repetitions):
                self.calculate(beta=self.beta,activation_function=self.activation_function)
                self.backpropagetion(learning_factor=self.learning_rate,activation_function=self.activation_function)
            #self.print()

        # print("forward")
        # for layer in self.layers_list:
        #     layer.print()
        # print("backward")
        # for layer in reversed(self.layers_list):
        #     layer.print()

    def predict(self,data,labels,activation_function):
        self.set_activation_fun(activation_function)
        to_return=list()
        for i in range(len(data)):
            self.set_feature_value(data[i])
            self.set_label(labels[i])
            self.calculate(beta=self.beta,activation_function=self.activation_function)
#           self.print()
            to_return.append(self.get_output())
        return to_return

    def get_output(self):
        to_return=[]
        for neuron in self.output_layer.neuron_vector:
            to_return.append(neuron.output)
        return to_return

    def check_corretnes(self):
        to_compare=[]
        for neuron in self.output_layer.neuron_vector:
            to_compare.append(neuron.output)


    def set_label(self,label):
        self.label=label


    def set_feature_value(self,data):
        counter=0
        input_neuron=self.layers_list[0].neuron_vector
        for neuron in input_neuron :
            neuron.output=data[counter]
            counter += 1


    def calculate(self,beta,activation_function):
        for layer  in self.layers_list:
            if layer.tag != "input":
                layer.update(activation_function,beta)


    def backpropagetion(self,learning_factor,activation_function):
        for layer in reversed(self.layers_list):
            if layer.tag=="output":
                self.set_output_delta()
                layer.update_weights(activation_fun=activation_function,learning_factor=learning_factor)
            elif layer.tag == "input":
                pass
            else:
                layer.update_weights(activation_fun=self.activation_function,learning_factor=learning_factor)

    def set_output_delta(self):
        for i in range(len(self.output_layer.neuron_vector)):
            delta = self.label[i] - self.output_layer.neuron_vector[i].output
            self.output_layer.neuron_vector[i].delta=delta

    def set_activation_fun(self,activation_fun):
        if ActivaionFunction(activation_fun)!= None:
            self.activation_function=activation_fun
        else:
            raise ActivationFunctionDoesntExist()

    def print(self):
        print("label")
        print(self.label)
        toPrint=[]
        for neuron in self.output_layer.neuron_vector:
            toPrint.append(neuron.output)

        print("output")
        print(toPrint)