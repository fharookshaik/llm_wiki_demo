---
type: chapter
tags: [aima, chapter, learning-probabilistic-models]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 21
---

# Chapter 21 - Learning Probabilistic Models

## Summary

Chapter 21 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **learning probabilistic models**. This chapter is part of Part V: Learning. The chapter contains approximately 8,684 words and covers foundational concepts, algorithms, and frameworks central to understanding learning probabilistic models in the context of artificial intelligence.

## Key Points

- **Introduction**: 21
CHAPTER
LEARNING PROBABILISTIC MODELS
Inwhichweviewlearningasaformofuncertainreasoningfromobservations,anddevise
modelstorepresenttheuncertainworld.
Chapter12pointedouttheprevalenceofuncertaintyinrealenvironments. Agentscanhandle
uncertaintybyusingthemethodsofprobabilityanddecisiontheory,butfirst...
- **21.1 Statistical Learning**: The key concepts in this chapter, just as in Chapter 19, are data and hypotheses. Here, the
dataareevidence—thatis,instantiationsofsomeoralloftherandomvariablesdescribingthe
domain. The hypotheses in this chapter are probabilistic theories of how the domain works,
includinglogicaltheoriesasaspecialc...
- **21.2 Learning with Complete Data**: Thegeneraltaskoflearningaprobabilitymodel,givendatathatareassumedtobegenerated
from that model, is called density estimation. (The term applied originally to probability Densityestimation
density functions for continuous variables, but it is used now for discrete distributions too.)
Densityestimatio...
- **21.2.1 Maximum-likelihood parameter learning: Discrete models**: Supposewebuyabagoflimeandcherrycandyfromanewmanufacturerwhoseflavorpro-
portionsarecompletelyunknown;thefractionofcherrycouldbeanywherebetween0and1.
In that case, we have a continuum of hypotheses. The parameter in this case, which we
call θ, is the proportion of cherry candies, and the hypothesis i...
- **21.2.2 Naive Bayes models**: Probably the most common Bayesian network model used in machine learning is the naive
Bayesmodelfirstintroducedonpage420. Inthismodel, the“class”variableC (whichisto
bepredicted)istherootandthe“attribute”variablesX aretheleaves. Themodelis“naive”
i
because it assumes that the attributes are conditio...

## Sections Overview

### Introduction

21
CHAPTER
LEARNING PROBABILISTIC MODELS
Inwhichweviewlearningasaformofuncertainreasoningfromobservations,anddevise
modelstorepresenttheuncertainworld.
Chapter12pointedouttheprevalenceofuncertaintyinrealenvironments. Agentscanhandle
uncertaintybyusingthemethodsofprobabilityanddecisiontheory,butfirsttheymustlearn
their probabilistic theories of the world from experience. This chapter explains how t...

### 21.1 Statistical Learning

The key concepts in this chapter, just as in Chapter 19, are data and hypotheses. Here, the
dataareevidence—thatis,instantiationsofsomeoralloftherandomvariablesdescribingthe
domain. The hypotheses in this chapter are probabilistic theories of how the domain works,
includinglogicaltheoriesasaspecialcase.
Consider a simple example. Our favorite surprise candy comes in two flavors: cherry
(yum)andlim...

### 21.2 Learning with Complete Data

Thegeneraltaskoflearningaprobabilitymodel,givendatathatareassumedtobegenerated
from that model, is called density estimation. (The term applied originally to probability Densityestimation
density functions for continuous variables, but it is used now for discrete distributions too.)
Densityestimationisaformofunsupervisedlearning. Thissectioncoversthesimplestcase,
where we have complete data. Data ...

### 21.2.1 Maximum-likelihood parameter learning: Discrete models

Supposewebuyabagoflimeandcherrycandyfromanewmanufacturerwhoseflavorpro-
portionsarecompletelyunknown;thefractionofcherrycouldbeanywherebetween0and1.
In that case, we have a continuum of hypotheses. The parameter in this case, which we
call θ, is the proportion of cherry candies, and the hypothesis is h . (The proportion of lime
θ
candies is just 1−θ.) If we assume that all proportions are equally ...

### 21.2.2 Naive Bayes models

Probably the most common Bayesian network model used in machine learning is the naive
Bayesmodelfirstintroducedonpage420. Inthismodel, the“class”variableC (whichisto
bepredicted)istherootandthe“attribute”variablesX aretheleaves. Themodelis“naive”
i
because it assumes that the attributes are conditionally independent of each other, given the
class. (The model in Figure 21.2(b) is a naive Bayes mode...

### 21.2.3 Generative and discriminative models

Wecandistinguishtwokindsofmachinelearningmodelsusedforclassifiers: generativeand
Generativemodel discriminative. A generative model models the probability distribution of each class. For
example,thenaiveBayestextclassifierfromSection12.6.1createsaseparatemodelforeach
possible category of text—one for sports, one for weather, and so on. Each model includes
the prior probability of the category—for ...

### 21.2.4 Maximum-likelihood parameter learning: Continuous models

Continuousprobabilitymodelssuchasthelinear–Gaussianmodelwereshownonpage440.
Because continuous variables are ubiquitous in real-world applications, it is important to
know how to learn the parameters of continuous models from data. The principles for
maximum-likelihoodlearningareidenticalinthecontinuousanddiscretecases.
Let us begin with a very simple case: learning the parameters of a Gaussian de...

### 21.2.5 Bayesian parameter learning

Maximum-likelihoodlearninggivesrisetosimpleprocedures,butithasseriousdeficiencies
with small data sets. For example, after seeing one cherry candy, the maximum-likelihood
hypothesisisthatthebagis100%cherry(i.e.,θ=1.0). Unlessone’shypothesisprioristhat
bagsmustbeeitherallcherryoralllime,thisisnotareasonableconclusion. Itismorelikely
that the bag is a mixture of lime and cherry. The Bayesian approac...

### 21.2.6 Bayesian linear regression

Here we illustrate how to apply a Bayesian approach to a standard statistical task: linear
regression. TheconventionalapproachwasdescribedinSection19.6asminimizingthesum
of squared errors and reinterpreted in Section 21.2.4 as maximizing likelihood assuming a
Gaussian error model. These produce a single best hypothesis: a straight line with specific
values for the slope and intercept and a fixed v...

### 21.2.7 Learning Bayes net structures

Sofar,wehaveassumedthatthestructureoftheBayesnetisgivenandwearejusttryingto
learn the parameters. The structure of the network represents basic causal knowledge about
the domain that is often easy for an expert, or even a naive user, to supply. In some cases,
however, the causal model may be unavailable or subject to dispute—for example, certain
corporations have long claimed that smoking does not...

### 21.2.8 Density estimation with nonparametric models

Itispossibletolearnaprobabilitymodelwithoutmakinganyassumptionsaboutitsstructure
and parameterization by adopting the nonparametric methods of Section 19.7. The task of
nonparametric density estimation is typically done in continuous domains, such as that Nonparametric
densityestimation
showninFigure21.8(a). Thefigureshowsaprobabilitydensityfunctiononaspacedefined
by two continuous variables. In F...

### 21.3 Learning with Hidden Variables: The EM Algorithm

The preceding section dealt with the fully observable case. Many real-world problems have
Latentvariable hiddenvariables(sometimescalledlatentvariables),whicharenotobservableinthedata.
Forexample,medicalrecordsoftenincludetheobservedsymptoms,thephysician’sdiagno-
sis,thetreatmentapplied,andperhapstheoutcomeofthetreatment,buttheyseldomcontain
a direct observation of the disease itself! (Note that t...

### 21.3.1 Unsupervised clustering: Learning mixtures of Gaussians

Unsupervised clustering is the problem of discerning multiple categories in a collection of Unsupervised
clustering
objects. Theproblemisunsupervisedbecausethecategorylabelsarenotgiven. Forexample,
suppose we record the spectra of a hundred thousand stars; are there different types of stars
revealedbythespectra,and,ifso,howmanytypesandwhataretheircharacteristics? Weare
allfamiliarwithtermssuchas“r...

### 21.3.2 Learning Bayes net parameter values for hidden variables

To learn a Bayesian network with hidden variables, we apply the same insights that worked
formixturesofGaussians. Figure21.14(a)representsasituationinwhichtherearetwobags
ofcandythathavebeenmixedtogether. Candiesaredescribedbythreefeatures: inaddition
to the Flavor and the Wrapper, some candies have a Hole in the middle and some do not.
The distribution of candies in each bag is described by a nai...

### 21.3.3 Learning hidden Markov models

Our final application of EM involves learning the transition probabilities in hidden Markov
models (HMMs). Recall from that a hidden Markov model can be represented
by a dynamic Bayes net with a single discrete state variable, as illustrated in Figure 21.15.
Each data point consists of an observation sequence of finite length, so the problem is to
learn the transition probabilities from a set of o...

### 21.3.4 The general form of the EM algorithm

We have seen several instances of the EM algorithm. Each involves computing expected
valuesofhiddenvariablesforeachexampleandthenrecomputingtheparameters, usingthe
expected values as if they were observed values. Let x be all the observed values in all the
examples, let Z denote all the hidden variables for all the examples, and let θ be all the
parametersfortheprobabilitymodel. ThentheEMalgorithm...

### 21.3.5 Learning Bayes net structures with hidden variables

In Section 21.2.7, we discussed the problem of learning Bayes net structures with complete
data. When unobserved variables influence observed data, things get more difficult. In the
simplestcase, ahumanexpertmighttellthelearningalgorithmthatcertainhiddenvariables
exist,leavingittothealgorithmtofindaplacefortheminthenetworkstructure. Forexample,
analgorithmmighttrytolearnthestructureshowninFigure21...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[M algorithm]]
- [[M Algorithm]]
- [[The algorithm]]

## Cross-References

- Previous: [[Chapter 20 - Knowledge in Learning]]
- Next: [[Chapter 22 - Deep Learning]]
- Part: Part V: Learning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 21. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
