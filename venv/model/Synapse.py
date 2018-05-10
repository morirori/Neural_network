class Synapse():

    def __init__(self):
        self.synapse = {}

    def add_connection(self, input_neuron, weight, output_neuron):
        self.synapse["input_neuron"] = input_neuron
        self.synapse["weight"] = weight
        self.synapse["output_neuron"] = output_neuron

    def print(self):
        print("input_neuron id: {0} layer id:  {1} output{2} weight {3}  /n" \
              " output_neuron id: {4} layer id:  {5} output{6}" \
              "".format(str(self.synapse["input_neuron"].id),
                        str(self.synapse["input_neuron"].layer_id),
                        str(self.synapse["input_neuron"].output),
                        str(self.synapse["weight"]),
                        str(self.synapse["output_neuron"].id),
                        str(self.synapse["output_neuron"].layer_id),
                        str(self.synapse["output_neuron"].output)))
