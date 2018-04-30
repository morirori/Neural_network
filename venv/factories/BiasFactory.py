from model.Bias import Bias


class BiasFactory():
    @staticmethod
    def create(layer_id):
        bias=Bias(layer_id)
        return bias
