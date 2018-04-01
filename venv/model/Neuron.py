from math import exp

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

    def calucate_weights(self):
        synapses=self.input_synapses.get_synapses_list()
        temp_weight=0
        for synapse in synapses:
            temp_weight +=synapse["weight"]

        self.weighted_sum=temp_weight


    def calculate_output(self,  activation_fun,beta=1):

        if activation_fun == "sigmoid":
            synapses_list=self.input_synapses.get_synapses_list()
            value=0
            for i in range((len(synapses_list))):
                value+=synapses_list[i]["neuron"].output*synapses_list[i]["weight"]

            value=1/(1+exp(-1*beta*value))
            self.output=value

    def update_weights(self,learning_factor=0.01 ):
        synapses=self.input_synapses.get_synapses_list()
        for synapse in synapses:
            weight_delta=learning_factor*self.delta*(1-self.output)*self.output*synapse["neuron"].output
            synapse["weight"]=synapse["weight"]+weight_delta


    #TODO backpropagationn delta
    def calculate_delta(self):
        synapses = self.output_synapses.get_synapses_list()
        delta=0
        for synapse in synapses:
            delta+=synapse["neuron"].delta*synapse["weight"]*(1-synapse["neuron"].output)*synapse["neuron"].output
        self.delta=delta

    def update(self,activation_fun):
        self.calculate_output(activation_fun)

    def get_output(self):
        return self.output

    def __str__(self):
        print("layer_id:" +str(self.layer_id) )
        print("id:" +str(self.id ))

        if self.input_synapses != "":
            print("input:" +self.input_synapses.print() )

        if self.output_synapses != "":
            print("output:" +self.output_synapses.print() )

        return " /n"