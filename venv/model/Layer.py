from factories.SynapseFactory import SynapseFactory

class Layer():

    def __init__(self,neuron_vector ):
         self.neuron_vector=neuron_vector
         self.tag=""
    def add_neuron(self,vector):
        self.neuron_vector.append(neuron_vector)

    def connect_forward(self, layer):
        for neuron in self.neuron_vector:
            neuron.add_output_synapse(SynapseFactory.create(layer.neuron_vector))

    def connect_backward(self, layer):
        for neuron in self.neuron_vector:
            neuron.add_input_synapse(SynapseFactory.create(layer.neuron_vector))

    def update(self,activation_fun,beta):

        for neuron in self.neuron_vector:
            neuron.update(activation_fun,beta)

    def update_weights(self,activation_fun,learning_factor):
        if self.tag != "output":
            for neuron in self.neuron_vector:
                neuron.calculate_delta(activation_fun=activation_fun)
                neuron.update_weights(learning_factor=learning_factor,activation_fun=activation_fun)
        else:
            for neuron in self.neuron_vector:
                neuron.update_weights(learning_factor=learning_factor,activation_fun=activation_fun)

    def get_layer_output(self):
        output=list()
        for neuron in self.neuron_vector:
            output.append(neuron.output)

        return output

    def print(self):
        for neuron in self.neuron_vector:
            print(neuron)
