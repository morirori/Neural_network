class Layer():

    def __init__(self,neuron_vector, **opt):
         self.neuron_vector=neuron_vector
         self.output_vector=[0,0,0]
         print(opt.keys())
         if opt.keys().__contains__("label") :
             self.label=opt.get("label")


    def add_neuron(self,vector):
        self.neuron_vector.append(neuron_vector)

    def update_label(self,label):
        self.label=label

    def update(self):
        temp=0

        for neuron in self.neuron_vector:
            neuron.update()
            self.output_vector[temp]=neuron.output
            temp+=1

    def train(self):
        for i in range(3):
            self.update()
#            print("iterartion")
#            print(self.label)
            counter=0
            if self.label != None:
                for neuron in self.neuron_vector:
                    delta=abs(self.label[counter]-self.output_vector[counter])
                    neuron.calculate_delta(delta=delta)
#                    print("delty")
#                    print(delta)
                    neuron.update_weights()
#                    print("updated weights")
#                    print(neuron.input_synapses.get_synapses_list())
                    counter+=1


class InputLayer():
    def __init__(self,neuron_vector):
        Layer.__init__(self,data)
        self.data=data

# class OutputLayer(neuron_vector,*opt):
#     def __init__(self):
#         self.neuron_vector = neuron_vector
#
#         if opt.keys() == "label":
#             self.label=opt.get("label")
#
#     def predict(self):
#         pass
#
#
#         # "predict" or