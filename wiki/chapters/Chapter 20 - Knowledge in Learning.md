---
type: chapter
tags: [aima, chapter, knowledge-in-learning]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 20
---

# Chapter 20 - Knowledge in Learning

## Summary

Chapter 20 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **knowledge in learning**. This chapter is part of Part V: Learning. The chapter contains approximately 8,122 words and covers foundational concepts, algorithms, and frameworks central to understanding knowledge in learning in the context of artificial intelligence.

## Key Points

- **Introduction**: 20
CHAPTER
KNOWLEDGE IN LEARNING
Inwhichweexaminetheproblemoflearningwhenyouknowsomethingalready.
Inalloftheapproachestolearningdescribedinthepreviouschapter,theideaistoconstruct
afunctionthathastheinput–outputbehaviorobservedinthedata. Ineachcase,thelearning
methodscanbeunderstoodassearchingahypoth...
- **20.1 A Logical Formulation of Learning**: Chapter 19 defined pure inductive learning as a process of finding a hypothesis that agrees
withtheobservedexamples. Here,wespecializethisdefinitiontothecasewherethehypoth-
esisisrepresentedbyasetoflogicalsentences. Exampledescriptionsandclassificationswill
also be logical sentences, and a new examp...
- **20.1.1 Examples and hypotheses**: RecallfromChapter19therestaurantlearningproblem: learningarulefordecidingwhether
to wait for a table. Examples were described by attributes such as Alternate, Bar, Fri/Sat,
and so on. In a logical setting, an example is described by a logical sentence; the attributes
become unary predicates. Let us ...
- **20.1.2 Current-best-hypothesis search**: The idea behind current-best-hypothesis search is to maintain a single hypothesis, and to Current-best-
hypothesis
adjust it as new examples arrive in order to maintain consistency. The basic algorithm was
describedbyJohnStuartMill(1843),andmaywellhaveappearedevenearlier.
Suppose we have some hypoth...
- **20.1.3 Least-commitment search**: Backtracking arises because the current-best-hypothesis approach has to choose a particular
hypothesis as its best guess even though it does not have enough data yet to be sure of the
choice. What we can do instead is to keep around all and only those hypotheses that are
consistent with all the data...

## Sections Overview

### Introduction

20
CHAPTER
KNOWLEDGE IN LEARNING
Inwhichweexaminetheproblemoflearningwhenyouknowsomethingalready.
Inalloftheapproachestolearningdescribedinthepreviouschapter,theideaistoconstruct
afunctionthathastheinput–outputbehaviorobservedinthedata. Ineachcase,thelearning
methodscanbeunderstoodassearchingahypothesisspacetofindasuitablefunction,starting
from only a very basic assumption about the form of the fu...

### 20.1 A Logical Formulation of Learning

Chapter 19 defined pure inductive learning as a process of finding a hypothesis that agrees
withtheobservedexamples. Here,wespecializethisdefinitiontothecasewherethehypoth-
esisisrepresentedbyasetoflogicalsentences. Exampledescriptionsandclassificationswill
also be logical sentences, and a new example can be classified by inferring a classification
sentence from the hypothesis and the example desc...

### 20.1.1 Examples and hypotheses

RecallfromChapter19therestaurantlearningproblem: learningarulefordecidingwhether
to wait for a table. Examples were described by attributes such as Alternate, Bar, Fri/Sat,
and so on. In a logical setting, an example is described by a logical sentence; the attributes
become unary predicates. Let us generically call the ith example X. For instance, the first
i
examplefromFigure19.3(page676)isdescri...

### 20.1.2 Current-best-hypothesis search

The idea behind current-best-hypothesis search is to maintain a single hypothesis, and to Current-best-
hypothesis
adjust it as new examples arrive in order to maintain consistency. The basic algorithm was
describedbyJohnStuartMill(1843),andmaywellhaveappearedevenearlier.
Suppose we have some hypothesis such as h , of which we have grown quite fond. As
r
longaseachnewexampleisconsistent,weneeddono...

### 20.1.3 Least-commitment search

Backtracking arises because the current-best-hypothesis approach has to choose a particular
hypothesis as its best guess even though it does not have enough data yet to be sure of the
choice. What we can do instead is to keep around all and only those hypotheses that are
consistent with all the data so far. Each new example will either have no effect or will get
rid of some of the hypotheses. Reca...

### 20.2 Knowledge in Learning

Theprecedingsectiondescribedthesimplestsettingforinductivelearning. Tounderstandthe
role of prior knowledge, we need to talk about the logical relationships among hypotheses,
example descriptions, and classifications. Let Descriptions denote the conjunction of all the
exampledescriptionsinthe trainingset, andletClassificationsdenotetheconjunctionof all
theexampleclassifications. ThenaHypothesistha...

### 20.2.1 Some simple examples

Letusconsidersomecommonsenseexamplesoflearningwithbackgroundknowledge. Many
apparently rational cases of inferential behavior in the face of observations clearly do not
followthesimpleprinciplesofpureinduction.
• Sometimes one leaps to general conclusions after only one observation. Gary Larson
once drew a cartoon in which a bespectacled caveman, Zog, is roasting his lizard on
the end of a pointed...

### 20.2.2 Some general schemes

In each of the preceding examples, one can appeal to prior knowledge to try to justify the
generalizationschosen. Wewillnowlookatwhatkindsofentailmentconstraintsareoperat-
ing in each case. The constraints will involve the Background knowledge, in addition to the
HypothesisandtheobservedDescriptionsandClassifications.
In the case of lizard toasting, the cavemen generalize by explaining the success...

### 20.3 Explanation-Based Learning

Explanation-based learning is a method for extracting general rules from individual obser-
vations. As an example, consider the problem of differentiating and simplifying algebraic
expressions (Exercise 9.17). If we differentiate an expression such as X2 with respect to
X, we obtain 2X. (We use a capital letter for the arithmetic unknown X, to distinguish it
from the logical variable x.) In a logi...

### 20.3.1 Extracting general rules from examples

ThebasicideabehindEBLisfirsttoconstructanexplanationoftheobservationusingprior
knowledge, andthentoestablishadefinitionoftheclassofcasesforwhichthesameexpla-
nation structure can be used. This definition provides the basis for a rule covering all of the
casesintheclass. The“explanation”canbealogicalproof,butmoregenerallyitcanbeany
reasoningorproblem-solvingprocesswhosestepsarewelldefined. Thekeyis...

### 20.3.2 Improving efficiency

ThegeneralizedprooftreeinFigure20.7actuallyyieldsmorethanonegeneralizedrule. For
example, if we terminate, or prune, the growth of the right-hand branch in the proof tree
whenitreachesthePrimitivestep,wegettherule
Primitive(z) ⇒ Simplify(1×(0+z),z)....

### 20.4 Learning Using Relevance Information

OurtravelerinBrazilseemstobeabletomakeaconfidentgeneralizationconcerningthelan-
guagespokenbyotherBrazilians. Theinferenceissanctionedbyherbackgroundknowledge,
namely, that people in a given country (usually) speak the same language. We can express
thisinfirst-orderlogicasfollows:2
Nationality(x,n)∧Nationality(y,n)∧Language(x,l) ⇒ Language(y,l). (20.6)
(Literal translation: “If x and y have the sa...

### 20.4.1 Determining the hypothesis space

Although the determinations sanction general conclusions concerning all Brazilians, or all
pieces of copper at a given temperature, they cannot, of course, yield a general predictive
theory for all nationalities, or for all temperatures and materials, from a single example.
Theirmaineffectcanbeseenaslimitingthespaceofhypothesesthatthelearningagentneed
consider. In predicting conductance, for examp...

### 20.4.2 Learning and using relevance information

Aswestatedintheintroductiontothischapter,priorknowledgeisusefulinlearning;butittoo
hastobelearned. Inordertoprovideacompletestoryofrelevance-basedlearning,wemust
therefore provide a learning algorithm for determinations. The learning algorithm we now
present is based on a straightforward attempt to find the simplest determination consistent
withtheobservations. AdeterminationP(cid:31)Qsaysthatifan...

### 20.5 Inductive Logic Programming

Inductivelogicprogramming(ILP)combinesinductivemethodswiththepoweroffirst-order
representations, concentratinginparticularontherepresentationofhypothesesaslogicpro-
grams.3 It has gained popularity for three reasons. First, ILP offers a rigorous approach to
the general knowledge-based inductive learning problem. Second, it offers complete algo-
rithms for inducing general, first-order theories fro...

### 20.5.1 An example

RecallfromEquation(20.5)thatthegeneralknowledge-basedinductionproblemisto“solve”
theentailmentconstraint
Background∧Hypothesis∧Descriptions|=Classifications
for the unknown Hypothesis, given the Background knowledge and examples described by
DescriptionsandClassifications. Toillustratethis,wewillusetheproblemoflearningfam-
ily relationships from examples. The descriptions will consist of an extend...

### 20.5.2 Top-down inductive learning methods

ThefirstapproachtoILPworksbystartingwithaverygeneralruleandgraduallyspecializing
it so that it fits the data. This is essentially what happens in decision-tree learning, where a
decision tree is gradually grown until it is consistent with the observations. To do ILP we
usefirst-orderliteralsinsteadofattributes, andthehypothesisisasetofclausesinsteadofa
decisiontree. Thissectiondescribes FOIL(Quinl...

### 20.5.3 Inductive learning with inverse deduction

The second major approach to ILP involves inverting the normal deductive proof process.
Inverse resolution is based on the observation that if the example Classifications follow Inverseresolution
from Background∧Hypothesis∧Descriptions, then one must be able to prove this fact by
resolution(becauseresolutioniscomplete). Ifwecan“runtheproofbackward,”thenwecan
find a Hypothesis such that the proof g...

### 20.5.4 Making discoveries with inductive logic programming

An inverse resolution procedure that inverts a complete resolution strategy is, in principle,
a complete algorithm for learning first-order theories. That is, if some unknown Hypothesis
generates a set of examples, then an inverse resolution procedure can generate Hypothesis
from the examples. This observation suggests an interesting possibility: Suppose that the
availableexamplesincludeavarietyof...

## Key Entities Mentioned

- Bertrand Russell
- Patrick Winston

## Algorithms & Concepts

- [[Asketchofthecomplete
algorithm]]
- [[Thebasic
algorithm]]
- [[It search]]
- [[S
algorithm]]
- [[P algorithm]]
- [[G algorithm]]

## Cross-References

- Previous: [[Chapter 19 - Learning from Examples]]
- Next: [[Chapter 21 - Learning Probabilistic Models]]
- Part: Part V: Learning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 20. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
