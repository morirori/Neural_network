from abc import ABCMeta, abstractmethod


class AbstractNetwork(metaclass=ABCMeta):

    @property
    @abstractmethod
    def layers_list(self):
        pass

    @property
    @abstractmethod
    def input_layer(self):
        pass

    @property
    @abstractmethod
    def output_layer(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def set_feature_value(self):
        pass