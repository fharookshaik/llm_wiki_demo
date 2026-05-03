---
type: chapter
tags: [aima, chapter, deep-learning-for-natural-language-processing]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 25
---

# Chapter 25 - Deep Learning for Natural Language Processing

## Summary

Chapter 25 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **deep learning for natural language processing**. This chapter is part of Part VI: Communicating, Perceiving, and Acting. The chapter contains approximately 7,088 words and covers foundational concepts, algorithms, and frameworks central to understanding deep learning for natural language processing in the context of artificial intelligence.

## Key Points

- **Introduction**: 25
CHAPTER
DEEP LEARNING FOR NATURAL
LANGUAGE PROCESSING
Inwhichdeepneuralnetworksperformavarietyoflanguagetasks,capturingthestructure
ofnaturallanguageaswellasitsfluidity.
Chapter24explainedthekeyelementsofnaturallanguage,includinggrammarandsemantics.
Systems based on parsing and semantic analysis ...
- **25.1 Word Embeddings**: Wewouldlikearepresentationofwordsthatdoesnotrequiremanualfeatureengineering,but
allows for generalization between related words—words that are related syntactically (“col-
orless” and “ideal” are both adjectives), semantically (“cat” and “kitten” are both felines),
topically (“sunny” and “sleet” are...
- **25.2 Recurrent Neural Networks for NLP**: We now have a good representation for single words in isolation, but language consists of
an ordered sequence of words in which the context of surrounding words is important. For
simple tasks like part of speech tagging, a small, fixed-size window of perhaps five words
usuallyprovidesenoughcontext.
...
- **25.2.1 Language models with recurrent neural networks**: We’llstartwiththeproblemofcreatingalanguagemodelwithsufficientcontext. Recallthat
alanguagemodelisaprobabilitydistributionoversequencesofwords. Itallowsustopredict
thenextwordinatextgivenallthepreviouswords,andisoftenusedasabuildingblockfor
morecomplextasks.
Buildingalanguagemodelwitheitherann-gramm...
- **25.2.2 Classification with recurrent neural networks**: It is also possible to use RNNs for other language tasks, such as part of speech tagging or
coreference resolution. In both cases the input and hidden layers will be the same, but for
a POS tagger the output will be a softmax distribution over POS tags, and for coreference
resolutionitwillbeasoftmax...

## Sections Overview

### Introduction

25
CHAPTER
DEEP LEARNING FOR NATURAL
LANGUAGE PROCESSING
Inwhichdeepneuralnetworksperformavarietyoflanguagetasks,capturingthestructure
ofnaturallanguageaswellasitsfluidity.
Chapter24explainedthekeyelementsofnaturallanguage,includinggrammarandsemantics.
Systems based on parsing and semantic analysis have demonstrated success on many tasks,
but their performance is limited by the endless complexity ...

### 25.1 Word Embeddings

Wewouldlikearepresentationofwordsthatdoesnotrequiremanualfeatureengineering,but
allows for generalization between related words—words that are related syntactically (“col-
orless” and “ideal” are both adjectives), semantically (“cat” and “kitten” are both felines),
topically (“sunny” and “sleet” are both weather terms), in terms of sentiment (“awesome”
hasoppositesentimentto“cringeworthy”),orother...

### 25.2 Recurrent Neural Networks for NLP

We now have a good representation for single words in isolation, but language consists of
an ordered sequence of words in which the context of surrounding words is important. For
simple tasks like part of speech tagging, a small, fixed-size window of perhaps five words
usuallyprovidesenoughcontext.
More complex tasks such as question answering or reference resolution may require
dozens of words as...

### 25.2.1 Language models with recurrent neural networks

We’llstartwiththeproblemofcreatingalanguagemodelwithsufficientcontext. Recallthat
alanguagemodelisaprobabilitydistributionoversequencesofwords. Itallowsustopredict
thenextwordinatextgivenallthepreviouswords,andisoftenusedasabuildingblockfor
morecomplextasks.
Buildingalanguagemodelwitheitherann-grammodel(asinSection24.1)orafeedfor-
ward network with a fixed window of n words can run into difficulty...

### 25.2.2 Classification with recurrent neural networks

It is also possible to use RNNs for other language tasks, such as part of speech tagging or
coreference resolution. In both cases the input and hidden layers will be the same, but for
a POS tagger the output will be a softmax distribution over POS tags, and for coreference
resolutionitwillbeasoftmaxdistributionoverthepossibleantecedents. Forexample,when
the network gets to the input him in “Eduard...

### 25.2.3 LSTMs for NLP tasks

WesaidthatRNNssometimessolvethelimitedcontextproblem. Intheory,anyinformation
could be passed along from one hidden layer to the next for any number of time steps. But
inpracticetheinformationcangetlostordistorted,justasinplayingthegameoftelephone,
in which players stand in line and the first player whispers a message to the second, who
repeats it to the third, and so on down the line. Usually, th...

### 25.3 Sequence-to-Sequence Models

One of the most widely studied tasks in NLP is machine translation (MT), where the goal Machinetranslation
(MT)
is to translate a sentence from a source language to a target language—for example, from Sourcelanguage
SpanishtoEnglish. WetrainanMTmodelwithalargecorpusofsource/targetsentencepairs. Targetlanguage
Thegoalistothenaccuratelytranslatenewsentencesthatarenotinourtrainingdata.
CanweuseRNNsto...

### 25.3.1 Attention

WhatifthetargetRNNwereconditionedonallofthehiddenvectorsfromthesourceRNN,
ratherthanjustthelastone? Thiswouldmitigatetheshortcomingsofnearbycontextbiasand
fixed context size limits, allowing the model to access any previous word equally well. One
waytoachievethisaccessistoconcatenateallofthesourceRNNhiddenvectors. However,...

### 25.3.2 Decoding

Attrainingtime,asequence-to-sequencemodelattemptstomaximizetheprobabilityofeach
word in the target training sentence, conditioned on the source and all of the previous target
words. Oncetrainingiscomplete,wearegivenasourcesentence,andourgoalistogenerate
the corresponding target sentence. As shown in Figure 25.7, we can generate the target one
word at a time, and then feed back in the word that we ...

### 25.4 The Transformer Architecture

Theinfluentialarticle“Attentionisallyouneed”(Vaswanietal.,2018)introducedthetrans-
former architecture, which uses a self-attention mechanism that can model long-distance Transformer
contextwithoutasequentialdependency. Self-attention...

### 25.4.1 Self-attention

Previously, in sequence-to-sequence models, attention was applied from the target RNN to
the source RNN. Self-attention extends this mechanism so that each sequence of hidden Self-attention
statesalsoattendstoitself—thesourcetothesource,andthetargettothetarget. Thisallows
themodeltoadditionallycapturelong-distance(andnearby)contextwithineachsequence....

### 25.4.2 From self-attention to transformer

Self-attentionisonlyonecomponentofthetransformermodel. Eachtransformerlayercon-
sistsofseveralsub-layers. Ateachtransformerlayer, self-attentionisappliedfirst. Theout-
put of the attention module is fed through feedforward layers, where the same feedforward
weightmatricesareappliedindependentlyateachposition. Anonlinearactivationfunction,
typically ReLU, is applied after the first feedforward laye...

### 25.5 Pretraining and Transfer Learning

Getting enough data to build a robust model can be a challenge. In computer vision (see
Chapter27),thatchallengewasaddressedbyassemblinglargecollectionsofimages(suchas
ImageNet)andhand-labelingthem.
For natural language, it is more common to work with text that is unlabeled. The dif-
ference is in part due to the difficulty of labeling: an unskilled worker can easily label an
imageas“cat”or“sunset...

### 25.5.1 Pretrained word embeddings

In Section 25.1, we briefly introduced word embeddings. We saw that how similar words
like banana and apple end up with similar vectors, and we saw that we can solve analogy...

### 25.5.2 Pretrained contextual representations

Wordembeddingsarebetterrepresentationsthanatomicwordtokens, butthereisanimpor-
tant issue with polysemous words. For example, the word rose can refer to a flower or the
pasttenseofrise. Thus,weexpecttofindatleasttwoentirelydistinctclustersofwordcon-
texts for rose: one similar to flower names such as dahlia, and one similar to upsurge. No
singleembeddingvectorcancapturebothofthesesimultaneously. R...

### 25.5.3 Masked language models

Aweaknessofstandardlanguagemodelssuchasn-grammodelsisthatthecontextualization
ofeachwordisbasedonlyonthepreviouswordsofthesentence. Predictionsaremadefrom
lefttoright. Butsometimescontextfromlaterinasentence—forexample,feetinthephrase
rosefivefeet—helpstoclarifyearlierwords....

### 25.6 State of the art

DeeplearningandtransferlearninghavemarkedlyadvancedthestateoftheartforNLP—so
muchsothatonecommentatorin2018declaredthat“NLP’sImageNetmomenthasarrived”
(Ruder, 2018). The implication is that just as a turning point occurred in 2012 for computer
visionwhendeeplearningsystemsproducedsurprisinggoodresultsintheImageNetcompe-
tition,aturningpointoccurredin2018forNLP.Theprincipalimpetusforthisturningpoin...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[Beam search]]

## Cross-References

- Previous: [[Chapter 24 - Natural Language Processing]]
- Next: [[Chapter 26 - Robotics]]
- Part: Part VI: Communicating, Perceiving, and Acting

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 25. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
