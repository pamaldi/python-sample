class Node(object):
    def __init__(self, bias, label, weights):
        self.bias = bias;
        self.label = label;
        self.weights = weights;

    def getBias(self):
        return self.bias;

    def getWeights(self):
        return self.weights;
