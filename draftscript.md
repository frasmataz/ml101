# Intro to NN

## How do we think?

I'm not a neuroscientist, so please take this section with a grain of salt!

The short answer is we don't fully know.  We do have some ideas though.

There are two concepts to think about here, the _structure_ of the brain, and the signals travelling _through_ that structure.  We can look at the brain and observe its structure, we can even observe signals travelling through the brain, but understanding what those signals mean is another beast entirely.

So lets start with what we can observe.

_again, not a neuroscientist_

The brain is a big ball of brain cells.  We call these brain cells _neurons_.

<INSERT PICTURE OF NEURON>

Neurons have a body full of cell things, and have long reaching tendrils called _synapses_.  Neurons will tend to extend these synapses to touch other nearby neurons, forming a larger network.

<INSERT PICTURE OF NEURONS HANGIN OUT>

Synapses are electrically conductive, so a neuron can generate an electric pulse, and have that pulse propagate down it's synapses to it's neighbouring neurons.  Those neurons sense a pulse arriving, and, if the pulse is energetic enough, possibly send out another pulse of it's own to it's own neighbours.  This gives our brain cells a mechanism to talk to each other!

So how does a neuron decide when to fire?

When a neuron receives a pulse, it needs to decide whether or not it will fire in return.  Each neuron has an _activation threshold_ voltage.  If the sum of incoming pulses reaches this threshold, the neuron will fire.

Our neurons are not fixed.  As we grow and learn, our neurons will adapt their layout, growing new synapses to other neurons, and strengthening/weakening existing synapses.  This alters how signals will propagate through the brain.

On top of that, the neurons in the brain aren't laid out randomly.  The cerebral cortex is the outermost layer of the brain, and is divided into layers.  Signals don't randomly propagate through the mass of neurons, rather they will start to propagate from the outermost layer, and neurons will pass signals down through the layers.

<INSERT PICTURE OF NEURAL LAYERS>

So we can see the structure of the brain, and can see how signals propagate through the brain.  How does this result in conscious thought, memory, emotion and problem solving?

Well, we don't know fully.  This is where the real magic of neural networks, biological or artificial, lies.  We have a machine which takes in simple signals from sensors, propegates those signals through a hyper-complex network of billions of carefully interconnected neurons, and outputs simple signals to muscles in response.  We don't _need_ to understand what signals mean, or why parts of the brain are laid out the way they are, as the network will automatically adapt itself to better fit the tasks presented to it.  We don't need to understand how to structure the network, because it's not our job _to_ structure it.  Our job is to provide the network with a good training program so that it can structure _itself_ to better fit the task.  The fine detail of what each signal means, and why each neuron is connected the way it is isn't as important as the big picture.

## How does this differ from traditional computing?
 - PATTERNS
 - Allows behaviours to emerge from patterns
 - Has no definite behaviour

## How do we model this machine?

 - Simplify

### The feedforward network


## So, how do we make this learn?

#### Natural selection

#### Backpropagation


## So that's great, but there are limitations

 - For a trained network, a set of inputs match exactly one set of outputs.  It will always do the same thing for an input, with no regard for what came before.

 - Data points are isolated, each being treated completely separately to other data points.  We have no flexibility in input the structure or amount of input data.

## Other network models

#### LSTM - Long short-term memory

Temporal data

#### CNN - Convolutional neural networks

2D data

#### GAN - Generative adversarial networks

2D data.. but cooler
