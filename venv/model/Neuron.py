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
        self.input_synapses=""  #synapse
        self.output_synapses=""
        self.weighted_sum=0
        self.delta=0
        self.data=[]
        self.output=0

    def add_input_synapse(self,synapse):
        self.input_synapses=synapse

    def add_output_synapse(self,synapse):
        self.output_synapses=synapse

    def calucate_weighted_sum(self):
        synapses_list=self.input_synapses.get_synapses_list()
        temp_weight=0
        for i in range((len(synapses_list))):
            temp_weight+=synapses_list[i]["neuron"].output*synapses_list[i]["weight"]

        self.weighted_sum=temp_weight


    def calculate_output(self,  activation_fun,beta):
        synapses_list=self.input_synapses.get_synapses_list()
        value=0
        # for i in range((len(synapses_list))):
        #     value+=synapses_list[i]["neuron"].output*synapses_list[i]["weight"]
        self.calucate_weighted_sum()
        if activation_fun == ActivaionFunction.SIGMOID:
            self.output=sigmoid(beta,self.weighted_sum)
        if activation_fun == ActivaionFunction.HYPERBOLIC_TANGENT:
            self.output=hiberbolic(beta,self.weighted_sum)


    def update_weights(self,learning_factor,activation_fun ):
        synapses=self.input_synapses.get_synapses_list()
        for synapse in synapses:

            if activation_fun ==ActivaionFunction.SIGMOID:
                derivative=sigmoid_derivative(self.output)

            elif activation_fun == ActivaionFunction.HYPERBOLIC_TANGENT:
                derivative=hiperbolic_derivative(self.output)

            weight_delta=learning_factor*self.delta*derivative*synapse["neuron"].output
            synapse["weight"]=synapse["weight"]+weight_delta


    def calculate_delta(self,activation_fun):
        synapses = self.output_synapses.get_synapses_list()
        delta=0
        for synapse in synapses:

            if activation_fun == ActivaionFunction.SIGMOID:
                derivative=sigmoid_derivative(synapse["neuron"].output)

            elif activation_fun == ActivaionFunction.HYPERBOLIC_TANGENT:
                derivative=hiperbolic_derivative(synapse["neuron"].output)

            delta+=synapse["neuron"].delta*synapse["weight"]*derivative
        self.delta=delta



    def update(self,activation_fun,beta):
        self.calculate_output(activation_fun,beta)

    def get_output(self):
        return self.output

    def __str__(self):
        print("layer_id:" +str(self.layer_id) )
        print("id:" +str(self.id ))
        print("output:" +str(self.delta ))
        print("delta:" +str(self.output ))

        if self.input_synapses != "":
            print("input_synapse:" +self.input_synapses.print() )

        if self.output_synapses != "":
            print("output_synapse:" +self.output_synapses.print() )

        return " /n"