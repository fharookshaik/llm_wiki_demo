---
type: chapter
tags: [aima, chapter, probabilistic-reasoning]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 13
---

# Chapter 13 - Probabilistic Reasoning

## Summary

Chapter 13 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **probabilistic reasoning**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 13,551 words and covers foundational concepts, algorithms, and frameworks central to understanding probabilistic reasoning in the context of artificial intelligence.

## Key Points

- **Introduction**: 13
CHAPTER
PROBABILISTIC REASONING
In which we explain how to build efficient network models to reason under uncertainty
according to the laws of probability theory, and how to distinguish between correlation
andcausality.
Chapter 12 introduced the basic elements of probability theory and noted the ...
- **13.1 Representing Knowledge in an Uncertain Domain**: InChapter12,wesawthatthefulljointprobabilitydistributioncanansweranyquestionabout
thedomain,butcanbecomeintractablylargeasthenumberofvariablesgrows. Furthermore,
specifyingprobabilitiesforpossibleworldsonebyoneisunnaturalandtedious.
We also saw that independence and conditional independence relation...
- **13.2 The Semantics of Bayesian Networks**: The syntax of a Bayes net consists of a directed acyclic graph with some local probability
information attached to each node. The semantics defines how the syntax corresponds to a
jointdistributionoverthevariablesofthenetwork.
Assume that the Bayes net contains n variables, X ,...,X . A generic entr...
- **13.2.1 Conditional independence relations in Bayesian networks**: From the semantics of Bayes nets as defined in Equation (13.2), we can derive a number of
conditional independence properties. We have already seen the property that a variable is
conditionally independent of its other predecessors, given its parents. It is also possible to
provethemoregeneral“non-d...
- **13.2.2 Efficient Representation of Conditional Distributions**: Evenifthemaximumnumberofparentsk issmallish, fillingintheCPTforanoderequires
uptoO(2k)numbersandperhapsagreatdealofexperiencewithallthepossibleconditioning
cases. Infact,thisisaworst-casescenarioinwhichtherelationshipbetweentheparentsand
the child is completely arbitrary. Usually, such relationships...

## Sections Overview

### Introduction

13
CHAPTER
PROBABILISTIC REASONING
In which we explain how to build efficient network models to reason under uncertainty
according to the laws of probability theory, and how to distinguish between correlation
andcausality.
Chapter 12 introduced the basic elements of probability theory and noted the importance of
independence andconditional independence relationshipsin simplifying probabilistic rep...

### 13.1 Representing Knowledge in an Uncertain Domain

InChapter12,wesawthatthefulljointprobabilitydistributioncanansweranyquestionabout
thedomain,butcanbecomeintractablylargeasthenumberofvariablesgrows. Furthermore,
specifyingprobabilitiesforpossibleworldsonebyoneisunnaturalandtedious.
We also saw that independence and conditional independence relationships among vari-
ables can greatly reduce the number of probabilities that need to be specified in ...

### 13.2 The Semantics of Bayesian Networks

The syntax of a Bayes net consists of a directed acyclic graph with some local probability
information attached to each node. The semantics defines how the syntax corresponds to a
jointdistributionoverthevariablesofthenetwork.
Assume that the Bayes net contains n variables, X ,...,X . A generic entry in the joint
1 n
distribution is then P(X =x ∧...∧X =x ), or P(x ,...,x ) for short. The semantics...

### 13.2.1 Conditional independence relations in Bayesian networks

From the semantics of Bayes nets as defined in Equation (13.2), we can derive a number of
conditional independence properties. We have already seen the property that a variable is
conditionally independent of its other predecessors, given its parents. It is also possible to
provethemoregeneral“non-descendants”propertythat:
Descendant Eachvariableisconditionallyindependentofitsnon-descendants,given...

### 13.2.2 Efficient Representation of Conditional Distributions

Evenifthemaximumnumberofparentsk issmallish, fillingintheCPTforanoderequires
uptoO(2k)numbersandperhapsagreatdealofexperiencewithallthepossibleconditioning
cases. Infact,thisisaworst-casescenarioinwhichtherelationshipbetweentheparentsand
the child is completely arbitrary. Usually, such relationships are describable by a canonical
Canonical distributionthatfitssomestandardpattern. Insuchcases,theco...

### 13.2.3 Bayesian nets with continuous variables

Manyreal-worldproblemsinvolvecontinuousquantities,suchasheight,mass,temperature,
and money. By definition, continuous variables have an infinite number of possible values,
so it is impossible to specify conditional probabilities explicitly for each value. One way to
Discretization handle continuous variables is with discretization—that is, dividing up the possible values
intoafixedsetofintervals. ...

### 13.2.4 Case study: Car insurance

A car insurance company receives an application from an individual to insure a specific ve-
hicleandmustdecideontheappropriateannualpremiumtocharge,basedontheanticipated
claims it will pay out for this applicant. The task is to build a Bayes net that captures the...

### 13.3 Exact Inference in Bayesian Networks

The basic task for any probabilistic inference system is to compute the posterior probability
distributionforasetofqueryvariables,givensomeobservedevent—usually,someassign- Event
mentofvaluestoasetofevidencevariables.5 Tosimplifythepresentation,wewillconsider
onlyonequeryvariableatatime;thealgorithmscaneasilybeextendedtoquerieswithmul-
tiplevariables. (Forexample, wecansolvethequeryP(U,V|e)bymulti...

### 13.3.1 Inference by enumeration

Chapter 12 explained that any conditional probability can be computed by summing terms
from the full joint distribution. More specifically, a query P(X|e) can be answered using
Equation(12.9),whichwerepeathereforconvenience:
P(X|e)=αP(X,e)=α∑P(X,e,y).
y
5 Anotherwidelystudiedtaskisfindingthemostprobableexplanationforsomeobservedevidence.Thisand
othertasksarediscussedinthenotesattheendofthechapter....

### 13.3.2 The variable elimination algorithm

The enumeration algorithm can be improved substantially by eliminating repeated calcula-
tions of the kind illustrated in Figure 13.10. The idea is simple: do the calculation once
and save the results for later use. This is a form of dynamic programming. There are sev-
Variableelimination eral versions of this approach; we present the variable elimination algorithm, which is the
simplest. Variable...

### 13.3.3 The complexity of exact inference

The complexity of exact inference in Bayes nets depends strongly on the structure of the
network. The burglary network of Figure 13.2 belongs to the family of networks in which
there is at most one undirected path (i.e., ignoring the direction of the arrows) between any
two nodes in the network. These are called singly connected networks or polytrees, and Singlyconnected
they have a particularly n...

### 13.3.4 Clustering algorithms

Thevariableeliminationalgorithmissimpleandefficientforansweringindividualqueries. If
wewanttocomputeposteriorprobabilitiesforallthevariablesinanetwork,however,itcan
be less efficient. For example, in a polytree network, one would need to issue O(n) queries
Clustering costing O(n) each, for a total of O(n2) time. Using clustering algorithms (also known as
Jointree jointreealgorithms),thetimecanbere...

### 13.4 Approximate Inference for Bayesian Networks

Given the intractability of exact inference in large networks, we will now consider approxi-
mateinferencemethods. Thissectiondescribesrandomizedsamplingalgorithms,alsocalled
Monte Carlo algorithms, that provide approximate answers whose accuracy depends on MonteCarlo
the number of samples generated. They work by generating random events based on the
probabilities in the Bayes net and counting up ...

### 13.4.1 Direct sampling methods

Theprimitiveelementinanysamplingalgorithmisthegenerationofsamplesfromaknown
probability distribution. For example, an unbiased coin can be thought of as a random vari-
able Coin with values (cid:104)heads,tails(cid:105) and a prior distribution P(Coin)=(cid:104)0.5,0.5(cid:105). Sampling
fromthisdistributionisexactlylikeflippingthecoin: withprobability0.5itwillreturnheads,
and with probability 0.5...

### 13.4.2 Inference by Markov chain simulation

MarkovchainMonteCarlo(MCMC)algorithmsworkdifferentlyfromrejectionsampling MarkovchainMonte
Carlo
andlikelihoodweighting. Insteadofgeneratingeachsamplefromscratch,MCMCalgorithms
generateasamplebymakingarandomchangetotheprecedingsample. ThinkofanMCMC
algorithm as being in a particular current state that specifies a value for every variable and
generatinganextstatebymakingrandomchangestothecurrentsta...

### 13.4.3 Compiling approximate inference

ThesamplingalgorithmsinFigures13.17,13.18, and13.20shareacommonproperty: they
operate on a Bayes net represented as a data structure. This seems quite natural: after all, a
Bayesnetisadirectedacyclicgraph,sohowelsecoulditberepresented? Theproblemwith
thisapproachisthattheoperationsrequiredtoaccessthedatastructure—forexampletofind
anode’sparents—arerepeatedthousandsormillionsoftimesasthesamplingalg...

### 13.5 Causal Networks

We have discussed several advantages of keeping node ordering in Bayes nets compatible
withthedirectionofcausation. Inparticular,wenotedtheeasewithwhichconditionalprob-
abilities can be assessed if such ordering is maintained, as well as the compactness of the
resultant network structure. We noted however that, in principle, any node ordering permits...

### 13.5.1 Representing actions: The do-operator

ConsideragaintheSprinklerstoryofFigure13.23(a). Accordingtothestandardsemanticsof
Bayesnets,thejointdistributionofthefivevariablesisgivenbyaproductoffiveconditional
distributions:
P(c,r,s,w,g)=P(c)P(r|c)P(s|c)P(w|r,s)P(g|w) (13.14)
where we have abbreviated each variable name by its first letter. As a system of structural
equations,themodellookslikethis:
C = f (U )
C C
R = f (C,U )
R R
S = f (C,U ...

### 13.5.2 The back-door criterion

The ability to predict the effect of any intervention is a remarkable result, but it does re-
quireaccurateknowledgeofthenecessaryconditionaldistributionsinthemodel,particularly
P(x |parents(X )). Inmanyreal-worldsettings,however,thisistoomuchtoask. Forexam-
j j
ple, we know that “genetic factors” play a role in obesity, but we do not know which genes
play a role or the precise nature of their eff...

## Key Entities Mentioned

- Judea Pearl

## Algorithms & Concepts

- [[Metropolis algorithm]]
- [[Monte Carlo algorithm]]
- [[L algorithm]]
- [[C algorithm]]
- [[K algorithm]]
- [[Monte Carlo]]
- [[C
algorithm]]
- [[R search]]
- [[This algorithm]]
- [[The algorithm]]

## Cross-References

- Previous: [[Chapter 12 - Quantifying Uncertainty]]
- Next: [[Chapter 14 - Probabilistic Reasoning over Time]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 13. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
