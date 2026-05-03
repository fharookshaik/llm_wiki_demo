---
type: chapter
tags: [aima, chapter, deep-learning]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 22
---

# Chapter 22 - Deep Learning

## Summary

Chapter 22 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **deep learning**. This chapter is part of Part V: Learning. The chapter contains approximately 12,315 words and covers foundational concepts, algorithms, and frameworks central to understanding deep learning in the context of artificial intelligence.

## Key Points

- **Introduction**: 22
CHAPTER
DEEP LEARNING
In which gradient descent learns multistep programs, with significant implications for the
majorsubfieldsofartificialintelligence.
Deep learning is a broad family of techniques for machine learning in which hypotheses Deeplearning
take the form of complex algebraic circuits ...
- **22.1 Simple Feedforward Networks**: Feedforwardnetwork Afeedforwardnetwork,asthenamesuggests,hasconnectionsonlyinonedirection—that
is,itformsadirectedacyclicgraphwithdesignatedinputandoutputnodes. Eachnodecom-
putesafunctionofitsinputsandpassestheresulttoitssuccessorsinthenetwork. Information
flows through the network from the input n...
- **22.1.1 Networks as complex functions**: Unit Eachnodewithinanetworkiscalledaunit. Traditionally,followingthedesignproposedby
McCullochandPitts,aunitcalculatestheweightedsumoftheinputsfrompredecessornodes...
- **22.1.2 Gradients and learning**: In Section 19.6, we introduced an approach to supervised learning based on gradient de-
scent: calculate the gradient of the loss function with respect to the weights, and adjust the
weights along the gradient direction to reduce the loss. (If you have not already read Sec-
tion 19.6, we recommend s...
- **22.2 Computation Graphs for Deep Learning**: We have established the basic ideas of deep learning: represent hypotheses as computation
graphs with tunable weights and compute the gradient of the loss function with respect to
thoseweightsinordertofitthetrainingdata. Nowwelookathowtoputtogethercomputation
graphs. We begin with the input layer, w...

## Sections Overview

### Introduction

22
CHAPTER
DEEP LEARNING
In which gradient descent learns multistep programs, with significant implications for the
majorsubfieldsofartificialintelligence.
Deep learning is a broad family of techniques for machine learning in which hypotheses Deeplearning
take the form of complex algebraic circuits with tunable connection strengths. The word
“deep” refers to the fact that the circuits are typicall...

### 22.1 Simple Feedforward Networks

Feedforwardnetwork Afeedforwardnetwork,asthenamesuggests,hasconnectionsonlyinonedirection—that
is,itformsadirectedacyclicgraphwithdesignatedinputandoutputnodes. Eachnodecom-
putesafunctionofitsinputsandpassestheresulttoitssuccessorsinthenetwork. Information
flows through the network from the input nodes to the output nodes, and there are no loops.
Recurrentnetwork Arecurrentnetwork,ontheotherhand,...

### 22.1.1 Networks as complex functions

Unit Eachnodewithinanetworkiscalledaunit. Traditionally,followingthedesignproposedby
McCullochandPitts,aunitcalculatestheweightedsumoftheinputsfrompredecessornodes...

### 22.1.2 Gradients and learning

In Section 19.6, we introduced an approach to supervised learning based on gradient de-
scent: calculate the gradient of the loss function with respect to the weights, and adjust the
weights along the gradient direction to reduce the loss. (If you have not already read Sec-
tion 19.6, we recommend strongly that you do so before continuing.) We can apply exactly
the same approach to learning the we...

### 22.2 Computation Graphs for Deep Learning

We have established the basic ideas of deep learning: represent hypotheses as computation
graphs with tunable weights and compute the gradient of the loss function with respect to
thoseweightsinordertofitthetrainingdata. Nowwelookathowtoputtogethercomputation
graphs. We begin with the input layer, which is where the training or test example x is
encodedasvaluesoftheinputnodes. Thenweconsidertheout...

### 22.2.1 Input encoding

Theinputandoutputnodesofacomputationalgrapharetheonesthatconnectdirectlytothe
input data x and the output data y. The encoding of input data is usually straightforward, at
least for the case of factored data where each training example contains values for n input
1 Automaticdifferentiationmethodswereoriginallydevelopedinthe1960sand1970sforoptimizingthepa-
rametersofsystemsdefinedbylarge,complexFor...

### 22.2.2 Output layers and loss functions

On the output side of the network, the problem of encoding the raw data values into actual
values y for the output nodes of the graph is much the same as the input encoding problem.
Forexample,ifthenetworkistryingtopredicttheWeathervariablefromChapter12,which
hasvalues{sun,rain,cloud,snow},wewoulduseaone-hotencodingwithfourbits.
So much for the data values y. What about the prediction yˆ? Ideally,...

### 22.2.3 Hidden layers

Duringthetrainingprocess,aneuralnetworkisshownmanyinputvaluesxandmanycorre-
sponding output values y. While processing an input vector x, the neural network performs
severalintermediatecomputationsbeforeproducingtheoutputy. Wecanthinkofthevalues
computed at each layer of the network as a different representation for the input x. Each
layer transforms the representation produced by the preceding la...

### 22.3 Convolutional Networks

WementionedinSection22.2.1thatanimagecannotbethoughtofasasimplevectorofin-
putpixelvalues,primarilybecauseadjacencyofpixelsreallymatters. Ifweweretoconstruct
a network with fully connected layers and an image as input, we would get the same result
whetherwetrainedwithunperturbedimagesorwithimagesallofwhosepixelshadbeenran-
domlypermuted. Furthermore,supposetherearenpixelsandnunitsinthefirsthiddenl...

### 22.3.1 Pooling and downsampling

A pooling layer in a neural network summarizes a set of adjacent units from the preceding Pooling
layerwithasinglevalue. Poolingworksjustlikeaconvolutionlayer,withakernelsizel and
strides,buttheoperationthatisappliedisfixedratherthanlearned. Typically,noactivation
functionisassociatedwiththepoolinglayer. Therearetwocommonformsofpooling:
• Average-pooling computes the average value of its l inputs....

### 22.3.2 Tensor operations in CNNs

WesawinEquations(22.1)and(22.3)thattheuseofvectorandmatrixnotationcanbehelpful
inkeepingmathematicalderivationssimpleandelegantandprovidingconcisedescriptionsof
computationgraphs. Vectorsandmatricesareone-dimensionalandtwo-dimensionalspecial
Tensor cases of tensors, which (in deep learning terminology) are simply multidimensional arrays
ofanydimension.5
ForCNNs,tensorsareawayofkeepingtrackofthe“sh...

### 22.3.3 Residual networks

Residual networks are a popular and successful approach to building very deep networks Residualnetwork
thatavoidtheproblemofvanishinggradients.
Typicaldeepmodelsuselayersthatlearnanewrepresentationatlayeribycompletelyre-
placingtherepresentationatlayeri−1. Usingthematrix–vectornotationthatweintroduced
inEquation(22.3),withz(i) beingthevaluesoftheunitsinlayeri,wehave
z(i)= f(z(i−1))=g(i)(W(i)z(i−1)...

### 22.4 Learning Algorithms

Traininganeuralnetworkconsistsofmodifyingthenetwork’sparameterssoastominimize
the loss function on the training set. In principle, any kind of optimization algorithm could
beused. Inpractice,modernneuralnetworksarealmostalwaystrainedwithsomevariantof
stochasticgradientdescent(SGD).
WecoveredstandardgradientdescentanditsstochasticversioninSection19.6.2. Here,
thegoalistominimizethelossL(w),wherewre...

### 22.4.1 Computing gradients in computation graphs

On page 806, we derived the gradient of the loss function with respect to the weights in a
specific (and very simple) network. We observed that the gradient could be computed by
back-propagatingerrorinformationfromtheoutputlayerofthenetworktothehiddenlayers.
We also said that this result holds in general for any feedforward computation graph. Here,
weexplainhowthisworks.
Figure22.6showsagenericnod...

### 22.4.2 Batch normalization

Batchnormalizationisacommonlyusedtechniquethatimprovestherateofconvergenceof Batchnormalization
SGDbyrescalingthevaluesgeneratedattheinternallayersofthenetworkfromtheexamples
within each minibatch. Although the reasons for its effectiveness are not well understood at
thetimeofwriting,weincludeitbecauseitconferssignificantbenefitsinpractice. Tosome
extent,batchnormalizationseemstohaveeffectssimilar...

### 22.5 Generalization

Sofarwehavedescribedhowtofitaneuralnetworktoitstrainingset,butinmachinelearn-
ing the goal is to generalize to new data that has not been seen previously, as measured by
performanceonatestset. Inthissection,wefocusonthreeapproachestoimprovinggener-
alizationperformance: choosingtherightnetworkarchitecture,penalizinglargeweights,and
randomlyperturbingthevaluespassingthroughthenetworkduringtraining....

### 22.5.1 Choosing a network architecture

A great deal of effort in deep learning research has gone into finding network architectures
that generalize well. Indeed, for each particular kind of data—images, speech, text, video,
and so on—a good deal of the progress in performance has come from exploring different
kinds of network architectures and varying the number of layers, their connectivity, and the
typesofnodeineachlayer.6
Someneural...

### 22.5.2 Neural architecture search

Unfortunately,wedon’tyethaveaclearsetofguidelinestohelpyouchoosethebestnetwork
architectureforaparticularproblem. Successindeployingadeeplearningsolutionrequires
experienceandgoodjudgment.
Fromtheearliestdaysofneuralnetworkresearch,attemptshavebeenmadetoautomate
theprocessofarchitectureselection. Wecanthinkofthisasacaseofhyperparametertuning
(Section 19.4.4), where the hyperparameters determine th...

### 22.5.3 Weight decay

InSection19.4.3wesawthatregularization—limitingthecomplexityofamodel—canaid
generalization. Thisistruefordeeplearningmodelsaswell. Inthecontextofneuralnetworks
Weightdecay weusuallycallthisapproachweightdecay.
Weightdecayconsistsofaddingapenaltyλ∑ W2 tothelossfunctionusedtotrainthe
i,j i,j
neural network, where λ is a hyperparameter controlling the strength of the penalty and the
sum is usually ta...

### 22.5.4 Dropout

Another way that we can intervene to reduce the test-set error of a network—at the cost of
making it harder to fit the training set—is to use dropout. At each step of training, dropout Dropout
appliesonestepofback-propagationlearningtoanewversionofthenetworkthatiscreated
by deactivating a randomly chosen subset of the units. This is a rough and very low-cost
approximationtotrainingalargeensembleof...

### 22.6 Recurrent Neural Networks

Recurrentneuralnetworks(RNNs)aredistinctfromfeedforwardnetworksinthattheyallow
cycles in the computation graph. In all the cases we will consider, each cycle has a delay,
so that units may take as input a value computed from their own output at an earlier step in...

### 22.6.1 Training a basic RNN

The basic model we will consider has an input layer x, a hidden layer z with recurrent con-
nections,andanoutputlayery,asshowninFigure22.8(a). Weassumethatbothxandyare
observedinthetrainingdataateachtimestep. Theequationsdefiningthemodelrefertothe
valuesofthevariablesindexedbytimestept:
z = f (z ,x )=g (W z +W x )≡g (in )
t w t−1 t z z,z t−1 x,z t z z,t
yˆ = g (W z )≡g (in ), (22.13)
t y z,y t y y...

### 22.6.2 Long short-term memory RNNs

SeveralspecializedRNNarchitectureshavebeendesignedwiththegoalofenablinginforma-
tion to be preserved over many time steps. One of the most popular is the long short-term
Longshort-term memoryorLSTM.Thelong-termmemorycomponentofanLSTM,calledthememorycell
memory
Memorycell anddenotedbyc,isessentiallycopiedfromtimesteptotimestep. (Incontrast,thebasicRNN
multipliesitsmemory byaweight matrixateverytime...

### 22.7 Unsupervised Learning and Transfer Learning

Thedeeplearningsystemswehavediscussedsofararebasedonsupervisedlearning,which
requires each training example to be labeled with a value for the target function. Although
such systems can reach a high level of test-set accuracy—as shown by the ImageNet com-
petition results, for example—they often require far more labeled data than a human would
for the same task. For example, a child needs to see o...

### 22.7.1 Unsupervised learning

Supervised learning algorithms all have essentially the same goal: given a training set of
inputs x and corresponding outputs y=f(x), learn a function h that approximates f well.
Unsupervised learning algorithms, on the other hand, take a training set of unlabeled exam-
ples x. Here we describe two things that such an algorithm might try to do. The first is to
learn new representations—for example...

### 22.7.2 Transfer learning and multitask learning

Transferlearning Intransferlearning,experiencewithonelearningtaskhelpsanagentlearnbetteronanother
task. Forexample,apersonwhohasalreadylearnedtoplaytenniswilltypicallyfinditeasier
tolearnrelatedsportssuchasracquetballandsquash;apilotwhohaslearnedtoflyonetype
of commercial passenger airplane will very quickly learn to fly another type; a student who
hasalreadylearnedalgebrafindsiteasiertolearncalcu...

### 22.8 Applications

DeeplearninghasbeenappliedsuccessfullytomanyimportantproblemareasinAI.Forin-
depth explanations, we refer the reader to the relevant chapters: Chapter 23 for the use of
deeplearninginreinforcementlearningsystems,Chapter25fornaturallanguageprocessing,
Chapter27(particularlySection27.4)forcomputervision,andChapter26forrobotics....

### 22.8.1 Vision

Webeginwithcomputervision,whichistheapplicationareathathasarguablyhadthebiggest
impactondeeplearning,andviceversa. Althoughdeepconvolutionalnetworkshadbeenin
usesincethe1990sfortaskssuchashandwritingrecognition,andneuralnetworkshadbegun
to surpass generative probability models for speech recognition by around 2010, it was the
successoftheAlexNetdeeplearningsysteminthe2012ImageNetcompetitionthatpro...

### 22.8.2 Natural language processing

Deeplearninghasalsohadahugeimpactonnaturallanguageprocessing(NLP)applications
such as machine translation and speech recognition. Some advantages of deep learning for
these applications include the possibility of end-to-end learning, the automatic generation
of internal representations for the meanings of words, and the interchangeability of learned
encodersanddecoders.
End-to-endlearningreferstot...

### 22.8.3 Reinforcement learning

In reinforcement learning (RL), a decision-making agent learns from a sequence of reward
signalsthatprovidesomeindicationofthequalityofitsbehavior. Thegoalistooptimizethe
sum of future rewards. This can be done in several ways: in the terminology of Chapter 16,...

## Key Entities Mentioned

- Alan Turing
- Frank Rosenblatt
- John McCarthy
- Norbert Wiener
- Yann LeCun

## Algorithms & Concepts

- [[Learning Algorithm]]
- [[M algorithm]]
- [[Monte Carlo]]
- [[Evolutionary algorithm]]
- [[Neuralarchitecture
search]]
- [[This algorithm]]
- [[Efficient Neural
Architecture Search]]
- [[The algorithm]]
- [[Nmodelsand
algorithm]]

## Cross-References

- Previous: [[Chapter 21 - Learning Probabilistic Models]]
- Next: [[Chapter 23 - Reinforcement Learning]]
- Part: Part V: Learning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 22. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
