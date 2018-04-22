from math import exp
from utils.Functions import sigmoid
from utils.Functions import sigmoid_derivative
from utils.Functions import hiberbolic
from utils.Functions import hiperbolic_derivative
from utils.Functions import ActivaionFunction

class Neuron():
    
    def __init__(self,layer_id, id):
        self.layer_id=layer_id
        self.id=id
        self.input_synapses=[]  #synapse
        self.output_synapses=[]
        self.weighted_sum=0
        self.delta=0
        self.data=[]
        self.output=0

    def add_input_synapse(self,synapses_list):
            self.input_synapses.append(synapses_list)

    def add_output_synapse(self, synapses_list):
            self.output_synapses.append(synapses_list)

    def calculate_weighted_sum(self):
        temp_weight=0
        for synapse in self.input_synapses:
            temp_weight+=synapse.synapse["input_neuron"].output*synapse.synapse["weight"]

        self.weighted_sum=temp_weight

    def calculate_output(self,  activation_fun,beta):
        self.calculate_weighted_sum()
        if activation_fun == ActivaionFunction.SIGMOID:
            self.output=sigmoid(beta,self.weighted_sum)
        if activation_fun == ActivaionFunction.HYPERBOLIC_TANGENT:
            self.output=hiberbolic(beta,self.weighted_sum)

    def update_weights(self,learning_factor,activation_fun ):
        for synapse in self.input_synapses:

            if activation_fun == ActivaionFunction.SIGMOID:
                derivative=sigmoid_derivative(self.output)

            elif activation_fun == ActivaionFunction.HYPERBOLIC_TANGENT:
                derivative=hiperbolic_derivative(self.output)

            weight_delta = learning_factor*self.delta*derivative*synapse.synapse["input_neuron"].output
            synapse.synapse["weight"]=synapse.synapse["weight"]+weight_delta

    def calculate_delta(self,activation_fun):
        delta=0
        for synapse in self.output_synapses:

            if activation_fun == ActivaionFunction.SIGMOID:
                derivative=sigmoid_derivative(synapse.synapse["output_neuron"].output)

            elif activation_fun == ActivaionFunction.HYPERBOLIC_TANGENT:
                derivative=hiperbolic_derivative(synapse.synapse["output_neuron"].output)

            delta+=synapse.synapse["output_neuron"].delta*synapse.synapse["weight"]*derivative
        self.delta=delta

    def update(self,activation_fun,beta):
        self.calculate_output(activation_fun,beta)

    def get_output(self):
        return self.output

    def __str__(self):
        print("layer_id:" +str(self.layer_id ))
        print("id:" +str(self.id ))
        print("output:" +str(self.delta ))
        print("delta:" +str(self.output ))
        print("INPUT CONNECTION")
        for synapse in self.input_synapses:
                synapse.print()
        print("OUTPUT CONNECTION")
        for synapse in self.output_synapses:
                synapse.print()
        return " /n"