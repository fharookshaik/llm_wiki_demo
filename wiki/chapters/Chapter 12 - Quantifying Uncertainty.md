---
type: chapter
tags: [aima, chapter, quantifying-uncertainty]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 12
---

# Chapter 12 - Quantifying Uncertainty

## Summary

Chapter 12 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **quantifying uncertainty**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 7,846 words and covers foundational concepts, algorithms, and frameworks central to understanding quantifying uncertainty in the context of artificial intelligence.

## Key Points

- **12.1 Acting under Uncertainty**: Agents in the real world need to handle uncertainty, whether due to partial observability, Uncertainty
nondeterminism,oradversaries. Anagentmayneverknowforsurewhatstateitisinnowor
whereitwillendupafterasequenceofactions.
Wehaveseenproblem-solvingandlogicalagentshandleuncertaintybykeepingtrackof
abel...
- **12.1.1 Summarizing uncertainty**: Let’s consider an example of uncertain reasoning: diagnosing a dental patient’s toothache.
Diagnosis—whether for medicine, automobile repair, or whatever—almost always involves
uncertainty. Letustrytowriterulesfordentaldiagnosisusingpropositionallogic,sothatwe
canseehowthelogicalapproachbreaksdown. ...
- **12.1.2 Uncertainty and rational decisions**: Consider again the A plan for getting to the airport. Suppose it gives us a 97% chance
90
of catching our flight. Does this mean it is a rational choice? Not necessarily: there might
be other plans, such as A , with higher probabilities. If it is vital not to miss the flight,
180
then it is worth ri...
- **12.2 Basic Probability Notation**: For our agent to represent and use probabilistic information, we need a formal language.
Thelanguageofprobabilitytheoryhastraditionallybeeninformal,writtenbyhumanmathe-
maticians for other human mathematicians. Appendix A includes a standard introduction to
elementaryprobabilitytheory;here,wetakeana...

## Sections Overview

### Introduction

12
CHAPTER
QUANTIFYING UNCERTAINTY
Inwhichweseehowtotameuncertaintywithnumericdegreesofbelief....

### 12.1 Acting under Uncertainty

Agents in the real world need to handle uncertainty, whether due to partial observability, Uncertainty
nondeterminism,oradversaries. Anagentmayneverknowforsurewhatstateitisinnowor
whereitwillendupafterasequenceofactions.
Wehaveseenproblem-solvingandlogicalagentshandleuncertaintybykeepingtrackof
abeliefstate—arepresentationofthesetofallpossibleworldstatesthatitmightbein—and
generating a contingency...

### 12.1.1 Summarizing uncertainty

Let’s consider an example of uncertain reasoning: diagnosing a dental patient’s toothache.
Diagnosis—whether for medicine, automobile repair, or whatever—almost always involves
uncertainty. Letustrytowriterulesfordentaldiagnosisusingpropositionallogic,sothatwe
canseehowthelogicalapproachbreaksdown. Considerthefollowingsimplerule:
Toothache ⇒ Cavity.
The problem is that this rule is wrong. Not all ...

### 12.1.2 Uncertainty and rational decisions

Consider again the A plan for getting to the airport. Suppose it gives us a 97% chance
90
of catching our flight. Does this mean it is a rational choice? Not necessarily: there might
be other plans, such as A , with higher probabilities. If it is vital not to miss the flight,
180
then it is worth risking the longer wait at the airport. What about A , a plan that involves
1440
leavinghome24hoursina...

### 12.2 Basic Probability Notation

For our agent to represent and use probabilistic information, we need a formal language.
Thelanguageofprobabilitytheoryhastraditionallybeeninformal,writtenbyhumanmathe-
maticians for other human mathematicians. Appendix A includes a standard introduction to
elementaryprobabilitytheory;here,wetakeanapproachmoresuitedtotheneedsofAIand
connectitwiththeconceptsofformallogic....

### 12.2.1 What probabilities are about

Like logical assertions, probabilistic assertions are about possible worlds. Whereas logical
assertionssaywhichpossibleworldsarestrictlyruledout(allthoseinwhichtheassertionis
false),probabilisticassertionstalkabouthowprobablethevariousworldsare. Inprobability
Samplespace theory, the set of all possible worlds is called the sample space. The possible worlds are
mutually exclusive and exhaustive—two...

### 12.2.2 The language of propositions in probability assertions

Inthischapterandthenext,propositionsdescribingsetsofpossibleworldsareusuallywrit-
ten in a notation that combines elements of propositional logic and constraint satisfaction
notation. In the terminology of Section 2.4.7, it is a factored representation, in which a
possibleworldisrepresentedbyasetofvariable/valuepairs. Amoreexpressivestructured
representationisalsopossible,asshowninChapter18.
Rando...

### 12.2.3 Probability axioms and their reasonableness

The basic axioms of probability (Equations (12.1) and (12.2)) imply certain relationships
amongthedegreesofbeliefthatcanbeaccordedtologicallyrelatedpropositions. Forexam-
ple, we can derive the familiar relationship between the probability of a proposition and the
probabilityofitsnegation:
P(¬a) = ∑ P(ω) byEquation(12.2)
ω∈¬a
= ∑ P(ω)+∑ P(ω)−∑ P(ω)
ω∈¬a ω∈a ω∈a
= ∑ P(ω)−∑ P(ω) groupingthefirsttwot...

### 12.3 Inference Using Full Joint Distributions

Inthissectionwedescribeasimplemethodforprobabilisticinference—thatis,thecompu- Probabilistic
inference
tationofposteriorprobabilitiesforquerypropositionsgivenobservedevidence. Weusethe Query
fulljointdistributionasthe“knowledgebase”fromwhichanswerstoallquestionsmaybede-
rived. Alongthewaywealsointroduceseveralusefultechniquesformanipulatingequations
involvingprobabilities.
Webeginwithasimpleexampl...

### 12.4 Independence

Let us expand thefull joint distribution in Figure 12.3 byadding a fourth variable, Weather.
ThefulljointdistributionthenbecomesP(Toothache,Catch,Cavity,Weather),whichhas2×
2×2×4 = 32 entries. It contains four “editions” of the table shown in Figure 12.3, one
for each kind of weather. What relationship do these editions have to each other and to the
originalthree-variabletable? HowisthevalueofP(to...

### 12.6 Naive Bayes Models

The dentistry example illustrates a commonly occurring pattern in which a single cause di-
rectly influences a number of effects, all of which are conditionally independent, given the
cause. Thefulljointdistributioncanbewrittenas
P(Cause,Effect ,...,Effect )=P(Cause)∏P(Effect |Cause). (12.20)
1 n i
i
NaiveBayes Such a probability distribution is called a naive Bayes model—“naive” because it is oft...

### 12.6.1 Text classification with naive Bayes

Let’s see how a naive Bayes model can be used for the task of text classification: given a Textclassification
text,decidewhichofapredefinedsetofclassesorcategoriesitbelongsto. Herethe“cause”
istheCategoryvariable,andthe“effect”variablesarethepresenceorabsenceofcertainkey
words,HasWord . Considerthesetwoexamplesentences,takenfromnewspaperarticles:
i
1. Stocks rallied on Monday, with major indexes g...

### 12.7 The Wumpus World Revisited

We can combine the ideas in this chapter to solve probabilistic reasoning problems in the
wumpusworld. (SeeChapter7foracompletedescriptionofthewumpusworld.) Uncertainty
arises in the wumpus world because the agent’s sensors give only partial information about
the world. For example, Figure 12.5 shows a situation in which each of the three unvisited
but reachable squares—[1,3], [2,2], and [3,1]—mig...

## Key Entities Mentioned

- George Boole

## Algorithms & Concepts

- To be identified on detailed review

## Cross-References

- Previous: [[Chapter 11 - Automated Planning]]
- Next: [[Chapter 13 - Probabilistic Reasoning]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 12. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
