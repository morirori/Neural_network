class Neuron():
    
    def __init__(self, input_synapses, **opt):
        self.input_synapses=input_synapses  #synapse
        self.output_synapses=0
        self.weighted_sum=0
        self.delta=0
        self.normalized_input_data=[]


        if opt.keys() == "output":
            self.output=opt.get("output")

        if opt.keys() == "output_synapses":
            self.output_synapses=opt.get("output_synapes")



    def calucate_weights(self):
        synapses=self.input_synapses.get_synapses_list()
        temp_weight=0
        for synapse in synapses:
            temp_weight +=synapse["weight"]

        self.weighted_sum=temp_weight

    def normalize_data(self):
        unnormalized_data=self.input_synapses.get_raw_data()
        for i in range(len(unnormalized_data)):
            value=(unnormalized_data[i]-min(unnormalized_data))/(max(unnormalized_data)-min(unnormalized_data))
            self.normalized_input_data.append(value)

    def calculate_output(self):
        synapses_list=self.input_synapses.get_synapses_list()
        temp_normalized_data=self.normalized_input_data
        value=0
        for i in range((len(temp_normalized_data))):
            value+=temp_normalized_data[i]*synapses_list[i]["weight"]
            print(str(temp_normalized_data[i]) +"  "+ str(synapses_list[i]["weight"])+ "  " + str(value) )

        print()
        self.output=value

    def update(self):
        normalize_data()
        calculate_output()

    def get_output(self):
        return self.output

    def add_output_synapse(self):
        pass