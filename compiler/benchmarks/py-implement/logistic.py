import math

class Logistic(MLinterface):
    def gradient(self, input_row, output_row):
        mul = [a * b for a, b in zip(input_row, self.model)]
        h = 0
        for num in mult:
            h += num
        h = self.sigmoid(h)
        d = h - output_row
        gradient_row = [d * x for x in input_row]
        return gradient_row

    def sgd(self, gradient):
        gradient = [self.meta * g for g in gradient]
        self.model = [w - g for w, g in zip(self.model, gradient)]

    def logistic(self):
        for input_row, output_row in zip(self.model_input, self.model_output):
            gradient_row = self.gradient(input_row, output_row)
            self.sgd(gradient_row)

    def sigmoid(self, num):
        return 1 / (1 + math.exp(num))
