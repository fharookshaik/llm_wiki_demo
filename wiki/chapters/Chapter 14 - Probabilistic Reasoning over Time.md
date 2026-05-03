---
type: chapter
tags: [aima, chapter, probabilistic-reasoning-over-time]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 14
---

# Chapter 14 - Probabilistic Reasoning over Time

## Summary

Chapter 14 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **probabilistic reasoning over time**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 11,505 words and covers foundational concepts, algorithms, and frameworks central to understanding probabilistic reasoning over time in the context of artificial intelligence.

## Key Points

- **Introduction**: 14
CHAPTER
PROBABILISTIC REASONING OVER
TIME
Inwhichwetrytointerpretthepresent,understandthepast,andperhapspredictthefuture,
evenwhenverylittleiscrystalclear.
Agentsinpartiallyobservableenvironmentsmustbeabletokeeptrackofthecurrentstate,to
theextentthattheirsensorsallow. InSection4.4weshowedamethodo...
- **14.1 Time and Uncertainty**: Wehavedevelopedourtechniquesforprobabilisticreasoninginthecontextofstaticworlds,
in which each random variable has a single fixed value. For example, when repairing a car,
we assume that whatever is broken remains broken during the process of diagnosis; our job
istoinferthestateofthecarfromobservede...
- **14.1.1 States and observations**: Discretetime This chapter discusses discrete-time models, in which the world is viewed as a series of
Timeslice snapshots or time slices.1 We’ll just number the time slices 0, 1, 2, and so on, rather than
assigning specific times to them. Typically, the time interval ∆ between slices is assumed to
b...
- **14.1.2 Transition and sensor models**: With the set of state and evidence variables for a given problem decided on, the next step is
to specify how the world evolves (the transition model) and how the evidence variables get
theirvalues(thesensormodel).
The transition model specifies the probability distribution over the latest state vari...
- **14.2 Inference in Temporal Models**: Havingsetupthestructureofagenerictemporalmodel,wecanformulatethebasicinference
tasksthatmustbesolved:
• Filtering2 or state estimation is the task of computing the belief state P(X t |e 1:t )— Filtering
the posterior distribution over the most recent state given all evidence to date. In the Stateest...

## Sections Overview

### Introduction

14
CHAPTER
PROBABILISTIC REASONING OVER
TIME
Inwhichwetrytointerpretthepresent,understandthepast,andperhapspredictthefuture,
evenwhenverylittleiscrystalclear.
Agentsinpartiallyobservableenvironmentsmustbeabletokeeptrackofthecurrentstate,to
theextentthattheirsensorsallow. InSection4.4weshowedamethodologyfordoingthat: an
agentmaintainsabeliefstatethatrepresentswhichstatesoftheworldarecurrentlypossib...

### 14.1 Time and Uncertainty

Wehavedevelopedourtechniquesforprobabilisticreasoninginthecontextofstaticworlds,
in which each random variable has a single fixed value. For example, when repairing a car,
we assume that whatever is broken remains broken during the process of diagnosis; our job
istoinferthestateofthecarfromobservedevidence,whichalsoremainsfixed.
Now consider a slightly different problem: treating a diabetic patien...

### 14.1.1 States and observations

Discretetime This chapter discusses discrete-time models, in which the world is viewed as a series of
Timeslice snapshots or time slices.1 We’ll just number the time slices 0, 1, 2, and so on, rather than
assigning specific times to them. Typically, the time interval ∆ between slices is assumed to
bethesameforeveryinterval. Foranyparticularapplication, aspecificvalueof∆hastobe
chosen. Sometimesthi...

### 14.1.2 Transition and sensor models

With the set of state and evidence variables for a given problem decided on, the next step is
to specify how the world evolves (the transition model) and how the evidence variables get
theirvalues(thesensormodel).
The transition model specifies the probability distribution over the latest state variables,
given the previous values, that is, P(X |X ). Now we face a problem: the set X is
t 0:t−1 0:t...

### 14.2 Inference in Temporal Models

Havingsetupthestructureofagenerictemporalmodel,wecanformulatethebasicinference
tasksthatmustbesolved:
• Filtering2 or state estimation is the task of computing the belief state P(X t |e 1:t )— Filtering
the posterior distribution over the most recent state given all evidence to date. In the Stateestimation
umbrella example, this would mean computing the probability of rain today, given all Beliefs...

### 14.2.1 Filtering and prediction

As we pointed out in Section 7.7.3, a useful filtering algorithm needs to maintain a current
stateestimateandupdateit,ratherthangoingbackovertheentirehistoryofperceptsforeach
update. (Otherwise,thecostofeachupdateincreasesastimegoesby.) Inotherwords,given
theresultoffilteringuptotimet,theagentneedstocomputetheresultfort+1fromthenew
evidencee . Sowehave
t+1
P(X |e )= f(e ,P(X |e ))
t+1 1:t+1 t+1 t ...

### 14.2.2 Smoothing

As we said earlier, smoothing is the process of computing the distribution over past states
given evidence up to the present—that is, P(X |e ) for 0≤k <t. (See Figure 14.3.) In
k 1:t
anticipation of another recursive message-passing approach, we can split the computation
intotwoparts—theevidenceuptokandtheevidencefromk+1tot,
P(X |e ) = P(X |e ,e )
k 1:t k 1:k k+1:t
= αP(X |e )P(e |X ,e ) (usingBay...

### 14.2.3 Finding the most likely sequence

Suppose that [true,true,false,true,true] is the observed umbrella sequence for the security
guard’sfirstfivedaysonthejob. Whatweathersequenceismostlikelytoexplainthis? Does
the absence of the umbrella on day 3 mean that it wasn’t raining, or did the director forget
to bring it? If it didn’t rain on day 3, perhaps (because weather tends to persist) it didn’t
rain on day 4 either, but the director b...

### 14.3 Hidden Markov Models

Theprecedingsectiondevelopedalgorithmsfortemporalprobabilisticreasoningusingagen-
eralframeworkthatwasindependentofthespecificformofthetransitionandsensormodels
and independent of the nature of the state and evidence variables. In this and the next two
sections, we discuss more concrete models and applications that illustrate the power of the
basicalgorithmsandinsomecasesallowfurtherimprovements.
...

### 14.3.1 Simplified matrix algorithms

With a single, discrete state variable X, we can give concrete form to the representations of
t
thetransitionmodel,thesensormodel,andtheforwardandbackwardmessages. Letthestate
variableX havevaluesdenotedbyintegers1,...,S,whereSisthenumberofpossiblestates.
t
ThetransitionmodelP(X |X )becomesanS×SmatrixT,where
t t−1
T =P(X =j|X =i).
ij t t−1
Thatis,T istheprobabilityofatransitionfromstateitostate j....

### 14.3.2 Hidden Markov model example: Localization

Onpage151,weintroducedasimpleformofthelocalizationproblemforthevacuumworld.
In that version, the robot had a single nondeterministic Move action and its sensors reported
perfectly whether or not obstacles lay immediately to the north, south, east, and west; the
robot’sbeliefstatewasthesetofpossiblelocationsitcouldbein.
Here we make the problem slightly more realistic by allowing for noise in the s...

### 14.4 Kalman Filters

Imagine watching a small bird flying through dense jungle foliage at dusk: you glimpse
brief,intermittentflashesofmotion;youtryhardtoguesswherethebirdisandwhereitwill
appear next so that you don’t lose it. Or imagine that you are a World War II radar operator
peeringatafaint,wanderingblipthatappearsonceevery10secondsonthescreen. Or,going
back further still, imagine you are Kepler trying to reconst...

### 14.4.1 Updating Gaussian distributions

In Chapter 13 on page 441, we alluded to a key property of the linear–Gaussian family of
distributions: it remains closed under Bayesian updating. (That is, given any evidence, the
posteriorisstillinthelinear–Gaussianfamily.) Herewemakethisclaimpreciseinthecontext
of filtering in a temporal probability model. The required properties correspond to the two-
stepfilteringcalculationinEquation(14.5):
...

### 14.4.2 A simple one-dimensional example

We have said that the FORWARD operator for the Kalman filter maps a Gaussian into a new
Gaussian. Thistranslatesintocomputinganewmeanandcovariancefromthepreviousmean
and covariance. Deriving the update rule in the general (multivariate) case requires rather a
lotoflinearalgebra, sowewillsticktoaverysimpleunivariatecasefornow, andlatergive
the results for the general case. Even for the univariate c...

### 14.4.3 The general case

The preceding derivation illustrates the key property of Gaussian distributions that allows
Kalmanfilteringtowork: thefactthattheexponentisaquadraticform. Thisistruenotjust
fortheunivariatecase;thefullmultivariateGaussiandistributionhastheform
−1 (cid:16) (x−µ)(cid:62)Σ−1 (x−µ) (cid:17)
N(x;µ,Σ)=αe 2 .
Multiplyingoutthetermsintheexponent,weseethattheexponentisalsoaquadraticfunc-
tionofthevaluesx i...

### 14.4.4 Applicability of Kalman filtering

TheKalmanfilteranditselaborationsareusedinavastarrayofapplications. The“classical”
applicationisinradartrackingofaircraftandmissiles. Relatedapplicationsincludeacoustic
tracking of submarines and ground vehicles and visual tracking of vehicles and people. In a
slightly more esoteric vein, Kalman filters are used to reconstruct particle trajectories from
bubble-chamber photographs and ocean current...

### 14.5 Dynamic Bayesian Networks

DynamicBayesiannetworks,orDBNs,extendthesemanticsofstandardBayesiannetworks DynamicBayesian
network
tohandletemporalprobabilitymodelsofthekinddescribedinSection14.1. Wehavealready
seenexamplesofDBNs: theumbrellanetworkinFigure14.2andtheKalmanfilternetwork
in Figure 14.9. In general, each slice of a DBN can have any number of state variables X
t
andevidencevariablesE . Forsimplicity,weassumethatthe...

### 14.5.1 Constructing DBNs

ToconstructaDBN,onemustspecifythreekindsofinformation: thepriordistributionover
thestatevariables,P(X );thetransitionmodelP(X |X );andthesensormodelP(E |X ).
0 t+1 t t t
To specify the transition and sensor models, one must also specify the topology of the con-
nections between successive slices and between the state and evidence variables. Because
thetransitionandsensormodelsareassumedtobetime-ho...

### 14.5.2 Exact inference in DBNs

HavingsketchedsomeideasforrepresentingcomplexprocessesasDBNs,wenowturntothe
questionofinference. Inasense,thisquestionhasalreadybeenanswered: dynamicBayesian
networks are Bayesian networks, and we already have algorithms for inference in Bayesian
networks. Givenasequenceofobservations,onecanconstructthefullBayesiannetworkrep-...

### 14.5.3 Approximate inference in DBNs

described two approximation algorithms: likelihood weighting (Figure 13.18)
andMarkovchainMonteCarlo(MCMC,Figure13.20). Ofthetwo,theformerismosteasily
adaptedtotheDBNcontext. (AnMCMCfilteringalgorithmisdescribedbrieflyinthenotes
attheendofthischapter.) Wewillsee,however,thatseveralimprovementsarerequiredover
thestandardlikelihoodweightingalgorithmbeforeapracticalmethodemerges.
Recall that likeliho...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[M algorithm]]
- [[Monte Carlo]]
- [[Viterbi algorithm]]
- [[C
algorithm]]
- [[The algorithm]]
- [[Viterbi
algorithm]]
- [[Koller algorithm]]

## Cross-References

- Previous: [[Chapter 13 - Probabilistic Reasoning]]
- Next: [[Chapter 15 - Making Simple Decisions]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 14. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
