---
type: chapter
tags: [aima, chapter, making-simple-decisions]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 15
---

# Chapter 15 - Making Simple Decisions

## Summary

Chapter 15 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **making simple decisions**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 10,193 words and covers foundational concepts, algorithms, and frameworks central to understanding making simple decisions in the context of artificial intelligence.

## Key Points

- **Introduction**: 15
CHAPTER
MAKING SIMPLE DECISIONS
In which we see how an agent should make decisions so that it gets what it wants in an
uncertainworld—atleastasmuchaspossibleandonaverage.
Inthischapter,wefillinthedetailsofhowutilitytheorycombineswithprobabilitytheoryto
yieldadecision-theoreticagent—anagentthatcan...
- **15.1 Combining Beliefs and Desires under Uncertainty**: We begin with an agent that, like all agents, has to make a decision. It has available some
actions a. There may be uncertainty about the current state, so we’ll assume that the agent
assigns a probability P(s) to each possible current state s. There may also be uncertainty
about the action outcomes...
- **15.2 The Basis of Utility Theory**: Intuitively, the principle of Maximum Expected Utility (MEU) seems like a reasonable way
to make decisions, but it is by no means obvious that it is the only rational way. After all,
why should maximizing the average utility be so special? What’s wrong with an agent that
maximizes the weighted sum o...
- **15.2.1 Constraints on rational preferences**: Thesequestionscanbeansweredbywritingdownsomeconstraintsonthepreferencesthata
rationalagentshouldhaveandthenshowingthattheMEUprinciplecanbederivedfromthe
constraints. Weusethefollowingnotationtodescribeanagent’spreferences:
A(cid:31)B theagentprefersAoverB.
A∼B theagentisindifferentbetweenAandB.
(cid...
- **15.2.2 Rational preferences lead to utility**: Noticethattheaxiomsofutilitytheoryarereallyaxiomsaboutpreferences—theysaynothing
about a utility function. But in fact from the axioms of utility we can derive the following
consequences(fortheproof,seevonNeumannandMorgenstern,1944):
• ExistenceofUtilityFunction: Ifanagent’spreferencesobeytheaxiomso...

## Sections Overview

### Introduction

15
CHAPTER
MAKING SIMPLE DECISIONS
In which we see how an agent should make decisions so that it gets what it wants in an
uncertainworld—atleastasmuchaspossibleandonaverage.
Inthischapter,wefillinthedetailsofhowutilitytheorycombineswithprobabilitytheoryto
yieldadecision-theoreticagent—anagentthatcanmakerationaldecisionsbasedonwhatit
believesandwhatitwants. Suchanagentcanmakedecisionsincontextsinwh...

### 15.1 Combining Beliefs and Desires under Uncertainty

We begin with an agent that, like all agents, has to make a decision. It has available some
actions a. There may be uncertainty about the current state, so we’ll assume that the agent
assigns a probability P(s) to each possible current state s. There may also be uncertainty
about the action outcomes; the transition model is given by P(s(cid:48)|s,a), the probability that
actionainstatesreachesstat...

### 15.2 The Basis of Utility Theory

Intuitively, the principle of Maximum Expected Utility (MEU) seems like a reasonable way
to make decisions, but it is by no means obvious that it is the only rational way. After all,
why should maximizing the average utility be so special? What’s wrong with an agent that
maximizes the weighted sum of the cubes of the possible utilities, or tries to minimize the
worst possible loss? Could an agent ...

### 15.2.1 Constraints on rational preferences

Thesequestionscanbeansweredbywritingdownsomeconstraintsonthepreferencesthata
rationalagentshouldhaveandthenshowingthattheMEUprinciplecanbederivedfromthe
constraints. Weusethefollowingnotationtodescribeanagent’spreferences:
A(cid:31)B theagentprefersAoverB.
A∼B theagentisindifferentbetweenAandB.
(cid:31)
A∼B theagentprefersAoverBorisindifferentbetweenthem.
Now the obvious question is, what sorts of...

### 15.2.2 Rational preferences lead to utility

Noticethattheaxiomsofutilitytheoryarereallyaxiomsaboutpreferences—theysaynothing
about a utility function. But in fact from the axioms of utility we can derive the following
consequences(fortheproof,seevonNeumannandMorgenstern,1944):
• ExistenceofUtilityFunction: Ifanagent’spreferencesobeytheaxiomsofutility,then
thereexistsafunctionU suchthatU(A)>U(B)ifandonlyifAispreferredtoB, and
U(A)=U(B)ifando...

### 15.3 Utility Functions

Utility functions map from lotteries to real numbers. We know they must obey the axioms
oforderability,transitivity,continuity,substitutability,monotonicity,anddecomposability. Is
thatallwecansayaboututilityfunctions? Strictlyspeaking,thatisit: anagentcanhaveany
preferencesitlikes. Forexample,anagentmightprefertohaveaprimenumberofdollarsin
itsbankaccount; inwhichcase,ifithad$16itwouldgiveaway$3. T...

### 15.3.1 Utility assessment and utility scales

Ifwewanttobuildadecision-theoreticsystemthathelpsahumanmakedecisionsoractson
his or her behalf, we must first work out what the human’s utility function is. This process,
often called preference elicitation, involves presenting choices to the human and using the Preferenceelicitation
observedpreferencestopindowntheunderlyingutilityfunction.
Equation(15.2)saysthatthereisnoabsolutescaleforutilities,...

### 15.3.2 The utility of money

Utility theory has its roots in economics, and economics provides one obvious candidate
for a utility measure: money (or more specifically, an agent’s total net assets). The almost
universal exchangeability of money for all kinds of goods and services suggests that money
playsasignificantroleinhumanutilityfunctions.
Itwillusuallybethecasethatanagentprefersmoremoneytoless,allotherthingsbeing
Monoto...

### 15.3.3 Expected utility and post-decision disappointment

Therationalwaytochoosethebestaction,a∗,istomaximizeexpectedutility:
a∗=argmaxEU(a).
a
Ifwehavecalculatedtheexpectedutilitycorrectlyaccordingtoourprobabilitymodel,andif
the probability model correctly reflects the underlying stochastic processes that generate the
outcomes,then,onaverage,wewillgettheutilityweexpectifthewholeprocessisrepeated
manytimes.
Inreality,however,ourmodelusuallyoversimplifies...

### 15.3.4 Human judgment and irrationality

Normativetheory Decision theory is a normative theory: it describes how a rational agent should act. A
Descriptivetheory descriptivetheory,ontheotherhand,describeshowactualagents—forexample,humans—
really do act. The application of economic theory would be greatly enhanced if the two
coincided,butthereappearstobesomeexperimentalevidencetothecontrary. Theevidence
suggeststhathumansare“predictablyir...

### 15.4 Multiattribute Utility Functions

Decision making in the field of public policy involves high stakes, in both money and lives.
For example, in deciding what levels of harmful emissions to allow from a power plant,
policy makers must weigh the prevention of death and disability against the benefit of the
powerandtheeconomicburdenofmitigatingtheemissions. Pickingasiteforanewairport
requiresconsiderationofthedisruptioncausedbyconstru...

### 15.4.1 Dominance

SupposethatairportsiteS costsless,generateslessnoisepollution,andissaferthansiteS .
1 2
Strictdominance One would not hesitate to reject S 2 . We then say that there is strict dominance of S 1 over
S . Ingeneral, ifanoptionisoflowervalueonallattributesthansomeotheroption, itneed
2
not be considered further. Strict dominance is often very useful in narrowing down the field
of choices to the real co...

### 15.4.2 Preference structure and multiattribute utility

Suppose we have n attributes, each of which has d distinct possible values. To specify the
complete utility functionU(x ,...,x ), we need dn values in the worst case. Multiattribute
1 n
utility theory aims to identify additional structure in human preferences so that we don’t
need to specify all dn values individually. Having identified some regularity in preference
behavior,wethenderiverepresenta...

### 15.5 Decision Networks

In this section, we look at a general mechanism for making rational decisions. The notation
Influencediagram is often called an influence diagram (Howard and Matheson, 1984), but we will use the
Decisionnetwork more descriptive term decision network. Decision networks combine Bayesian networks...

### 15.5.1 Representing a decision problem with a decision network

Initsmostgeneralform,adecisionnetworkrepresentsinformationabouttheagent’scurrent
state, its possible actions, the state that will result from the agent’s action, and the utility of
that state. It therefore provides a substrate for implementing utility-based agents of the type
firstintroduced inSection2.4.5. Figure15.6 showsadecisionnetwork fortheairport-siting
problem. Itillustratesthethreetypesof...

### 15.5.2 Evaluating decision networks

Actionsareselectedbyevaluatingthedecisionnetworkforeachpossiblesettingofthedeci-
sionnode. Oncethedecisionnodeisset,itbehavesexactlylikeachancenodethathasbeen
setasanevidencevariable. Thealgorithmforevaluatingdecisionnetworksisthefollowing:...

### 15.6 The Value of Information

Intheprecedinganalysis,wehaveassumedthatallrelevantinformation,oratleastallavail-
able information, is provided to the agent before it makes its decision. In practice, this is (cid:74)
hardly ever the case. One of the most important parts of decision making is knowing what
questions to ask. For example, a doctor cannot expect to be provided with the results of all
possible diagnostic tests and que...

### 15.6.1 A simple example

Supposeanoilcompanyishopingtobuyoneofnindistinguishableblocksofocean-drilling
rights. Letusassumefurtherthatexactlyoneoftheblockscontainsoilthatwillgeneratenet
profits of C dollars, while the others are worthless. The asking price of each block is C/n
dollars. Ifthecompanyisrisk-neutral,thenitwillbeindifferentbetweenbuyingablockand
notbuyingonebecausetheexpectedprofitiszeroinbothcases.
Now suppose...

### 15.6.2 A general formula for perfect information

Itissimpletoderiveageneralmathematicalformulaforthevalueofinformation. Weassume
that exact evidence can be obtained about the value of some random variable E (that is, we
j
Valueofperfect learnE =e ),sothephrasevalueofperfectinformation(VPI)isused.8
information j j
In the agent’s initial information state, the value of the current best action α is, from
Equation(15.1),
EU(α)=max∑P(RESULT(a)=s(cid:...

### 15.6.3 Properties of the value of information

One might ask whether it is possible for information to be deleterious: can it actually have
negative expected value? Intuitively, one should expect this to be impossible. After all, one
could in the worst case just ignore the information and pretend that one has never received
it. Thisisconfirmedbythefollowingtheorem,whichappliestoanydecision-theoreticagent
usinganydecisionnetworkwithpossibleobse...

### 15.6.4 Implementation of an information-gathering agent

A sensible agent should ask questions in a reasonable order, should avoid asking questions
that are irrelevant, should take into account the importance of each piece of information in
relation to its cost, and should stop asking questions when that is appropriate. All of these
capabilitiescanbeachievedbyusingthevalueofinformationasaguide.
Figure15.9showstheoveralldesignofanagentthatcangatherinform...

### 15.6.5 Nonmyopic information gathering

The fact that the value of a sequence of observations is invariant under permutations of the
sequence is intriguing but doesn’t, by itself, lead to efficient algorithms for optimal infor-
mation gathering. Even if we restrict ourselves to choosing in advance a fixed subset of
observations to collect, there are 2n possible such subsets from n potential observations. In
the general case, we face an ...

### 15.6.6 Sensitivity analysis and robust decisions

Sensitivityanalysis The practice of sensitivity analysis is widespread in technological disciplines: it means an-
alyzing how much the output of a process changes as the model parameters are tweaked.
Sensitivity analysis in probabilistic and decision-theoretic systems is particularly important
because the probabilities used are typically either learned from data or estimated by human
experts, whic...

### 15.7 Unknown Preferences

In this section we discuss what happens when there is uncertainty about the utility function
whose expected value is to be optimized. There are two versions of this problem: one in
whichanagent(machineorhuman)isuncertainaboutitsownutilityfunction,andanotherin
whichamachineissupposedtohelpahumanbutisuncertainaboutwhatthehumanwants.
15.7.1 Uncertainty about one’s own preferences
Imagine that you are...

### 15.7.2 Deference to humans

Now let’s turn to the second case mentioned above: a machine that is supposed to help a
humanbutisuncertainaboutwhatthehumanwants. Thefulltreatmentofthiscasemustbe
deferredtoChapter17,wherewediscussdecisionsinvolvingmorethanoneagent. Here,we
askonesimplequestion: underwhatcircumstanceswillsuchamachinedefertothehuman?...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- To be identified on detailed review

## Cross-References

- Previous: [[Chapter 14 - Probabilistic Reasoning over Time]]
- Next: [[Chapter 16 - Making Complex Decisions]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 15. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
