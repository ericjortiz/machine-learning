import nn

class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        return nn.DotProduct(self.w, x)
    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        if nn.as_scalar(self.run(x)) >= 0:
            return 1
        return -1
    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        while True:
            numMistakes = 0
            for x, y in dataset.iterate_once(1):
                pred = self.get_prediction(x)
                if pred != nn.as_scalar(y):
                    numMistakes += 1
                    self.w.update(x, nn.as_scalar(y))
            if numMistakes == 0:
                break


class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.learningRate = -0.01
        self.batch_size   = 5
        self.w1, self.w2  = nn.Parameter(1, 100), nn.Parameter(100, 1)
        self.b1, self.b2  = nn.Parameter(1, 100), nn.Parameter(1, 1)

        self.w3, self.w4  = nn.Parameter(1, 100), nn.Parameter(100, 1)
        self.b3, self.b4  = nn.Parameter(1, 100), nn.Parameter(1, 1)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        xw1 = nn.Linear(x, self.w1)
        inter = nn.AddBias(xw1, self.b1)
        layer1 = nn.ReLU(inter)
        xw2 = nn.Linear(layer1, self.w2)
        layer2 = nn.AddBias(xw2, self.b2)

        xw3 = nn.Linear(x, self.w1)
        inter2 = nn.AddBias(xw1, self.b1)
        layer3 = nn.ReLU(inter2)
        xw4 = nn.Linear(layer1, self.w2)
        layer4 = nn.AddBias(xw2, self.b2)
        return nn.Add(layer4, layer2)
    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SquareLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        threshold = 0.01
        loss = 1000
        while loss > threshold:
            for x, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(x, y)
                grad_w1, grad_w2, grad_w3, grad_w4, grad_b1, grad_b2, grad_b3, grad_b4 = nn.gradients(loss, [self.w1, self.w2, self.w3, self.w4, self.b1, self.b2, self.b3, self.b4])

                self.w1.update(grad_w1, self.learningRate)
                self.w2.update(grad_w2, self.learningRate)
                self.w3.update(grad_w3, self.learningRate)
                self.w4.update(grad_w4, self.learningRate)
                self.b1.update(grad_b1, self.learningRate)
                self.b2.update(grad_b2, self.learningRate)
                self.b3.update(grad_b3, self.learningRate)
                self.b4.update(grad_b4, self.learningRate)
                loss = nn.as_scalar(loss)

class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.learningRate = -0.2
        self.batch_size  = 25
        self.w1, self.w2 = nn.Parameter(784, 100), nn.Parameter(100, 10)
        self.b1, self.b2 = nn.Parameter(1, 100), nn.Parameter(1, 10)

        self.w3, self.w4 = nn.Parameter(784, 100), nn.Parameter(100, 10)
        self.b3, self.b4 = nn.Parameter(1, 100), nn.Parameter(1, 10)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        xw1 = nn.Linear(x, self.w1)
        inter = nn.AddBias(xw1, self.b1)
        layer1 = nn.ReLU(inter)
        xw2 = nn.Linear(layer1, self.w2)
        layer2 = nn.AddBias(xw2, self.b2)

        xw3 = nn.Linear(x, self.w1)
        inter2 = nn.AddBias(xw1, self.b1)
        layer3 = nn.ReLU(inter2)
        xw4 = nn.Linear(layer1, self.w2)
        layer4 = nn.AddBias(xw2, self.b2)
        return nn.Add(layer4, layer2)

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SoftmaxLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"

        accuracy = 0.0
        currCount = 0
        while True:
            for x, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(x, y)
                grad_w1, grad_w2, grad_w3, grad_w4, grad_b1, grad_b2, grad_b3, grad_b4 = nn.gradients(loss, [self.w1, self.w2, self.w3, self.w4, self.b1, self.b2, self.b3, self.b4])

                self.w1.update(grad_w1, self.learningRate)
                self.w2.update(grad_w2, self.learningRate)
                self.w3.update(grad_w3, self.learningRate)
                self.w4.update(grad_w4, self.learningRate)
                self.b1.update(grad_b1, self.learningRate)
                self.b2.update(grad_b2, self.learningRate)
                self.b3.update(grad_b3, self.learningRate)
                self.b4.update(grad_b4, self.learningRate)

                currCount += 1
                if currCount % 100 == 0: #only do every 100 times through
                    accuracy = dataset.get_validation_accuracy()
                if accuracy >= 0.975:
                    break
            if accuracy >= 0.975:
                break

class LanguageIDModel(object):
    """
    A model for language identification at a single-word granularity.

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Our dataset contains words from five different languages, and the
        # combined alphabets of the five languages contain a total of 47 unique
        # characters.
        # You can refer to self.num_chars or len(self.languages) in your code
        self.num_chars = 47
        self.languages = ["English", "Spanish", "Finnish", "Dutch", "Polish"]

        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.hiddenSize = 400
        self.batch_size = 100
        self.learningRate = -0.15
        self.W = nn.Parameter(self.num_chars, self.hiddenSize)
        self.hidden_W = nn.Parameter(self.hiddenSize, self.hiddenSize)
        self.W_matcher = nn.Parameter(self.hiddenSize, len(self.languages))
    def run(self, xs):
        """
        Runs the model for a batch of examples.

        Although words have different lengths, our data processing guarantees
        that within a single batch, all words will be of the same length (L).

        Here `xs` will be a list of length L. Each element of `xs` will be a
        node with shape (batch_size x self.num_chars), where every row in the
        array is a one-hot vector encoding of a character. For example, if we
        have a batch of 8 three-letter words where the last word is "cat", then
        xs[1] will be a node that contains a 1 at position (7, 0). Here the
        index 7 reflects the fact that "cat" is the last word in the batch, and
        the index 0 reflects the fact that the letter "a" is the inital (0th)
        letter of our combined alphabet for this task.

        Your model should use a Recurrent Neural Network to summarize the list
        `xs` into a single node of shape (batch_size x hidden_size), for your
        choice of hidden_size. It should then calculate a node of shape
        (batch_size x 5) containing scores, where higher scores correspond to
        greater probability of the word originating from a particular language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
        Returns:
            A node with shape (batch_size x 5) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        f_initial = nn.Linear(xs[0], self.W)
        f_initial = nn.ReLU(f_initial)
        h = f_initial
        for i in range(1, len(xs)):
            linear_W = nn.Linear(xs[i], self.W)
            linear_hidden_W = nn.Linear(h, self.hidden_W)
            addition = nn.Add(linear_W, linear_hidden_W)
            h = nn.ReLU(addition)
        return nn.Linear(h, self.W_matcher)
    def get_loss(self, xs, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 5). Each row is a one-hot vector encoding the correct
        language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
            y: a node with shape (batch_size x 5)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SoftmaxLoss(self.run(xs), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"

        accuracy = 0.0
        currCount = 0
        while True:
            for x, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(x, y)
                grad_w, grad_hidden_w, grad_matcher= nn.gradients(loss, [self.W, self.hidden_W, self.W_matcher])

                self.W.update(grad_w, self.learningRate)
                self.hidden_W.update(grad_hidden_w, self.learningRate)
                self.W_matcher.update(grad_matcher, self.learningRate)

                currCount += 1
                if currCount % 100 == 0: #only do every 100 times through
                    accuracy = dataset.get_validation_accuracy()

                if accuracy >= 0.86:
                    break
                elif accuracy >= 0.83:
                    self.learningRate = -0.05
                elif accuracy >= 0.75:
                    self.learningRate = -0.1
            if accuracy >= 0.86:
                break
