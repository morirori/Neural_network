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

    def update(self,beta):

        for neuron in self.neuron_vector:
            neuron.update("sigmoid",beta)
            # self.output_vector[counter] = neuron.output
            # delta=self.label[counter]-self.output_vector[counter]
            # neuron.calculate_delta(delta=delta)
            # neuron.update_weights()

    def update_weights(self,learning_factor):
        if self.tag != "output":
            for neuron in self.neuron_vector:
                neuron.calculate_delta()
                neuron.update_weights(learning_factor)
        else:
            for neuron in self.neuron_vector:
                neuron.update_weights(learning_factor)

    def get_layer_output(self):
        output=list()
        for neuron in self.neuron_vector:
            output.append(neuron.output)

        return output

    def print(self):
        for neuron in self.neuron_vector:
            print(neuron)
