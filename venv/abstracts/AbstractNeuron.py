from abc import ABCMeta, abstractmethod


class AbstractNeuron(metaclass=ABCMeta):

    @property
    @abstractmethod
    def output(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def layer_id(self):
        pass

    @abstractmethod
    def update_weights(self, learning_factor, activation_fun):
        pass

    @abstractmethod
    def update(self, activation_fun, beta):
        pass

    @abstractmethod
    def calculate_delta(self, activation_fun):
        pass
