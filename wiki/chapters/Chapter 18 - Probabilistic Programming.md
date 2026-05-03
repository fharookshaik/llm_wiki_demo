---
type: chapter
tags: [aima, chapter, probabilistic-programming]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 18
---

# Chapter 18 - Probabilistic Programming

## Summary

Chapter 18 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **probabilistic programming**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 7,826 words and covers foundational concepts, algorithms, and frameworks central to understanding probabilistic programming in the context of artificial intelligence.

## Key Points

- **Introduction**: 18
CHAPTER
PROBABILISTIC PROGRAMMING
Inwhichweexplaintheideaofuniversallanguagesforprobabilisticknowledgerepresen-
tationandinferenceinuncertaindomains.
The spectrum of representations—atomic, factored, and structured—has been a persistent
theme in AI. For deterministic models, search algorithms ass...
- **18.1 Relational Probability Models**: Recall from Chapter 12 that a probability model defines a set Ω of possible worlds with
a probability P(ω) for each world ω. For Bayesian networks, the possible worlds are as-
signments of values to variables; for the Boolean case in particular, the possible worlds are
identicaltothoseofpropositiona...
- **18.1.1 Syntax and semantics**: Let us begin with a simple example: suppose that an online book retailer would like to pro-
videoverallevaluationsofproductsbasedonrecommendationsreceivedfromitscustomers.
Theevaluationwilltaketheformofaposteriordistributionoverthequalityofthebook,given
theavailableevidence. Thesimplestsolutionistob...
- **18.1.2 Example: Rating player skill levels**: Manycompetitivegameshaveanumericalmeasureofplayers’skilllevels,sometimescalled
Rating arating. Perhapsthebest-knownistheEloratingforchessplayers,whichratesatypicalbe-
ginnerataround800andtheworldchampionusuallysomewhereabove2800. AlthoughElo
ratingshaveastatisticalbasis, theyhavesomeadhocelements. W...
- **18.1.3 Inference in relational probability models**: ThemoststraightforwardapproachtoinferenceinRPMsissimplytoconstructtheequivalent
Bayesiannetwork,giventheknownconstantsymbolsbelongingtoeachtype. WithBbooks
andCcustomers,thebasicmodelgivenpreviouslycouldbeconstructedwithsimpleloops:4
forb=1toBdo
addnodeQuality withnoparents,prior(cid:104)0.05,0.2,0....

## Sections Overview

### Introduction

18
CHAPTER
PROBABILISTIC PROGRAMMING
Inwhichweexplaintheideaofuniversallanguagesforprobabilisticknowledgerepresen-
tationandinferenceinuncertaindomains.
The spectrum of representations—atomic, factored, and structured—has been a persistent
theme in AI. For deterministic models, search algorithms assume only an atomic represen-
tation; CSPs and propositional logic provide factored representations; ...

### 18.1 Relational Probability Models

Recall from Chapter 12 that a probability model defines a set Ω of possible worlds with
a probability P(ω) for each world ω. For Bayesian networks, the possible worlds are as-
signments of values to variables; for the Boolean case in particular, the possible worlds are
identicaltothoseofpropositionallogic.
Forafirst-orderprobabilitymodel,then,itseemsweneedthepossibleworldstobethose
offirst-orderlo...

### 18.1.1 Syntax and semantics

Let us begin with a simple example: suppose that an online book retailer would like to pro-
videoverallevaluationsofproductsbasedonrecommendationsreceivedfromitscustomers.
Theevaluationwilltaketheformofaposteriordistributionoverthequalityofthebook,given
theavailableevidence. Thesimplestsolutionistobasetheevaluationontheaveragerecom-
mendation,perhapswithavariancedeterminedbythenumberofrecommendati...

### 18.1.2 Example: Rating player skill levels

Manycompetitivegameshaveanumericalmeasureofplayers’skilllevels,sometimescalled
Rating arating. Perhapsthebest-knownistheEloratingforchessplayers,whichratesatypicalbe-
ginnerataround800andtheworldchampionusuallysomewhereabove2800. AlthoughElo
ratingshaveastatisticalbasis, theyhavesomeadhocelements. WecandevelopaBayesian
ratingschemeasfollows: eachplayerihasanunderlyingskilllevelSkill(i);ineachgameg...

### 18.1.3 Inference in relational probability models

ThemoststraightforwardapproachtoinferenceinRPMsissimplytoconstructtheequivalent
Bayesiannetwork,giventheknownconstantsymbolsbelongingtoeachtype. WithBbooks
andCcustomers,thebasicmodelgivenpreviouslycouldbeconstructedwithsimpleloops:4
forb=1toBdo
addnodeQuality withnoparents,prior(cid:104)0.05,0.2,0.4,0.2,0.15(cid:105)
b
forc=1toCdo
addnodeHonest withnoparents,prior(cid:104)0.99,0.01(cid:105)
c
add...

### 18.2 Open-Universe Probability Models

We argued earlier that database semantics was appropriate for situations in which we know
exactlythesetofrelevantobjectsthatexistandcanidentifythemunambiguously. (Inpartic-
ular, all observations about an object are correctly associated with the constant symbol that
names it.) In many real-world settings, however, these assumptions are simply untenable.
Forexample, abookretailermightuseanISBN(Inte...

### 18.2.1 Syntax and semantics

ThebasicideaistounderstandhowordinaryBayesiannetworksandRPMsmanagetodefine
a unique probability model and to transfer that insight to the first-order setting. In essence,
a Bayes net generates each possible world, event by event, in the topological order defined
by the network structure, where each event is an assignment of a value to a variable. An
RPMextendsthistoentiresetsofevents,definedbythep...

### 18.2.2 Inference in open-universe probability models

BecauseofthepotentiallyhugeandsometimesunboundedsizeoftheimplicitBayesnetthat
corresponds to a typical OUPM, unrolling it fully and performing exact inference is quite
impractical. Instead, we must consider approximate inference algorithms such as MCMC
(seeSection13.4.2).
Roughlyspeaking,anMCMCalgorithmforanOUPMisexploringthespaceofpossible
worldsdefinedbysetsofobjectsandrelationsamongthem,asillus...

### 18.2.3 Examples

The standard “use case” for an OUPM has three elements: the model, the evidence (the
known facts in a given scenario), and the query, which may be any expression, possibly
with free logical variables. The answer is a posterior joint probability for each possible set
of substitutions for the free variables, given the evidence, according to the model.7 Every
model includes type declarations, type si...

### 18.3 Keeping Track of a Complex World

Chapter 14 considered the problem of keeping track of the state of the world, but covered
only the case of atomic representations (HMMs) and factored representations (DBNs and
Kalman filters). This makes sense for worlds with a single object—perhaps a single patient
intheintensivecareunitorasinglebirdflyingthroughtheforest. Inthissection,weseewhat
happenswhentwoormoreobjectsgeneratetheobservations...

### 18.3.1 Example: Multitarget tracking

The data association problem was studied originally in the context of radar tracking of mul-
tiple targets, where reflected pulses are detected at fixed time intervals by a rotating radar
antenna. At each time step, multiple blips may appear on the screen, but there is no direct
observation of which blips at timet correspond to which blips at timet−1. Figure 18.8(a)
showsasimpleexamplewithtwoblips...

### 18.3.2 Example: Traffic monitoring

Figure 18.10 shows two images from widely separated cameras on a California freeway. In
this application, we are interested in two goals: estimating the time it takes, under current
traffic conditions, to go from one place to another in the freeway system; and measuring
demand—thatis,howmanyvehiclestravelbetweenanytwopointsinthesystematparticular
times of the day and on particular days of the week...

### 18.4 Programs as Probability Models

Many probabilistic programming languages have been built on the insight that probability
modelscanbedefinedusingexecutablecodeinanyprogramminglanguagethatincorporates
a source of randomness. For such models, the possible worlds are execution traces and the
probability of any such trace is the probability of the random choices required for that trace
tohappen. PPLscreatedinthiswayinheritalloftheexp...

### 18.4.1 Example: Reading text

Weillustratethisapproachtoprobabilisticmodelingandinferenceviatheproblemofwriting
a program that reads degraded text. These kinds of models can be built for reading text that
has been smudged or blurred due to water damage, or spotted due to aging of the paper on
whichitisprinted. TheycanalsobebuiltforbreakingsomekindsofCAPTCHAs.
Figure 18.11 shows a generative program containing two components: (...

### 18.4.2 Syntax and semantics

A generative program is an executable program in which every random choice defines a Generativeprogram
random variable in an associated probability model. Let us imagine unrolling the execution
of a program that makes random choices, step by step. Let X be the random variable corre-
i
spondingtotheithrandomchoicemadebytheprogram;asusual,x denotesapossiblevalue
i
ofX i . Letuscallω={x i }anexecutio...

### 18.4.3 Inference results

Let’s apply this model to interpret images of letters that have been degraded with additive
noise. Figure 18.13 shows a degraded image, along with results from three independent
MCMC runs. For each run, we show a rendering of the letters contained in the trace after
stoppingtheMarkovchain. Inallthreecasestheresultisthelettersequenceuncertainty,
suggestingthattheposteriordistributionishighlyconcent...

### 18.4.4 Improving the generative program to incorporate a Markov model

Probabilistic programming languages are modular in a way that makes it easy to explore
improvements to the underlying model. Figure 18.15 shows the generative program for an
improvedmodelthatgeneratesletterssequentiallyratherthanindependently. Thisgenerative
programusesaMarkovmodelthatdrawseachlettergiventhepreviousletter,withtransition
probabilitiesestimatedfromareferencelistofEnglishwords.
Figur...

### 18.4.5 Inference in generative programs

As with OUPMs, exact inference in generative programs is usually prohibitively expensive
orimpossible. Ontheotherhand,itiseasytoseehowtoperformrejectionsampling: runthe
program, keep just the traces that agree with the evidence, and count the different query an-
swersfoundinthosetraces. Likelihoodweightingisalsostraightforward: foreachgenerated
trace, keep track of the weight of the trace by multi...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[Monte Carlo]]
- [[T algorithm]]

## Cross-References

- Previous: [[Chapter 17 - Multiagent Decision Making]]
- Next: [[Chapter 19 - Learning from Examples]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 18. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
