from model.Layer import Layer
class Network:

    def __init__(self,layer):
        self.layers_list=layer
        self.activation_function="sigmoid"
        self.input_layer=layer[0]
        self.output_layer=layer[-1]
        self.beta = 0.5
        self.learning_rate = 0.2
        self.label=list()
    # TODO: offline trainifn
    # TODO: updating learinig rate


    def train(self,data,labels, repetitions):

        for i in range(len(data)):
            self.set_feature_value(data[i])
            self.set_label(labels[i])
            for i in range(repetitions):
                self.calculate(self.beta)
                self.backpropagetion(self.learning_rate)
            #self.print()

        # print("forward")
        # for layer in self.layers_list:
        #     layer.print()
        # print("backward")
        # for layer in reversed(self.layers_list):
        #     layer.print()

    def predict(self,data,labels):
        to_return=list()
        for i in range(len(data)):
            self.set_feature_value(data[i])
            self.set_label(labels[i])
            self.calculate(self.beta)
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


    def calculate(self,beta):
        for layer  in self.layers_list:
            if layer.tag != "input":
                layer.update(beta)


    def backpropagetion(self,learning_factor):
        for layer in reversed(self.layers_list):
            if layer.tag=="output":
                self.set_output_delta()
                layer.update_weights(learning_factor)
            elif layer.tag == "input":
                pass
            else:
                layer.update_weights(learning_factor)

    def set_output_delta(self):
        for i in range(len(self.output_layer.neuron_vector)):
            delta = self.label[i] - self.output_layer.neuron_vector[i].output
            self.output_layer.neuron_vector[i].delta=delta


    def print(self):
        print("label")
        print(self.label)
        toPrint=[]
        for neuron in self.output_layer.neuron_vector:
            toPrint.append(neuron.output)

        print("output")
        print(toPrint)