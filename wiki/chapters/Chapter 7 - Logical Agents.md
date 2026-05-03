---
type: chapter
tags: [aima, chapter, logical-agents]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 7
---

# Chapter 7 - Logical Agents

## Summary

Chapter 7 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **logical agents**. This chapter is part of Part III: Knowledge, Reasoning, and Planning. The chapter contains approximately 12,579 words and covers foundational concepts, algorithms, and frameworks central to understanding logical agents in the context of artificial intelligence.

## Key Points

- **Introduction**: 7
CHAPTER
LOGICAL AGENTS
Inwhichwedesignagentsthatcanformrepresentationsofacomplexworld,useaprocess
ofinferencetoderivenewrepresentationsabouttheworld, andusethesenewrepresenta-
tionstodeducewhattodo.
Humans,itseems,knowthings;andwhattheyknowhelpsthemdothings. InAI,knowledge-
Knowledge-based based a...
- **7.1 Knowledge-Based Agents**: Thecentralcomponentofaknowledge-basedagentisitsknowledgebase,orKB.Aknowl- Knowledgebase
edge base is a set of sentences. (Here “sentence” is used as a technical term. It is related Sentence
but not identical to the sentences of English and other natural languages.) Each sentence is
Knowledge
express...
- **7.2 The Wumpus World**: Inthissectionwedescribeanenvironmentinwhichknowledge-basedagentscanshowtheir
Wumpusworld worth. Thewumpusworldisacaveconsistingofroomsconnectedbypassageways. Lurking
somewhere in the cave is the terrible wumpus, a beast that eats anyone who enters its room.
Thewumpuscanbeshotbyanagent,buttheagenthas...
- **7.3 Logic**: This section summarizes the fundamental concepts of logical representation and reasoning.
These beautiful ideas are independent of any of logic’s particular forms. We therefore post-
pone the technical details of those forms until the next section, using instead the familiar
exampleofordinaryarithme...
- **7.4 Propositional Logic: A Very Simple Logic**: Wenowpresentpropositionallogic. Wedescribeitssyntax(thestructureofsentences)and Propositionallogic
itssemantics(thewayinwhichthetruthofsentencesisdetermined). Fromthese,wederive
a simple, syntactic algorithm for logical inference that implements the semantic notion of
entailment. Everythingtakesplac...

## Sections Overview

### Introduction

7
CHAPTER
LOGICAL AGENTS
Inwhichwedesignagentsthatcanformrepresentationsofacomplexworld,useaprocess
ofinferencetoderivenewrepresentationsabouttheworld, andusethesenewrepresenta-
tionstodeducewhattodo.
Humans,itseems,knowthings;andwhattheyknowhelpsthemdothings. InAI,knowledge-
Knowledge-based based agents use a process of reasoning over an internal representation of knowledge to
agents
Reasoning de...

### 7.1 Knowledge-Based Agents

Thecentralcomponentofaknowledge-basedagentisitsknowledgebase,orKB.Aknowl- Knowledgebase
edge base is a set of sentences. (Here “sentence” is used as a technical term. It is related Sentence
but not identical to the sentences of English and other natural languages.) Each sentence is
Knowledge
expressed in a language called a knowledge representation language and represents some representation
langu...

### 7.2 The Wumpus World

Inthissectionwedescribeanenvironmentinwhichknowledge-basedagentscanshowtheir
Wumpusworld worth. Thewumpusworldisacaveconsistingofroomsconnectedbypassageways. Lurking
somewhere in the cave is the terrible wumpus, a beast that eats anyone who enters its room.
Thewumpuscanbeshotbyanagent,buttheagenthasonlyonearrow. Someroomscontain
bottomlesspitsthatwilltrapanyonewhowandersintotheserooms(exceptforthe...

### 7.3 Logic

This section summarizes the fundamental concepts of logical representation and reasoning.
These beautiful ideas are independent of any of logic’s particular forms. We therefore post-
pone the technical details of those forms until the next section, using instead the familiar
exampleofordinaryarithmetic.
In Section 7.1, we said that knowledge bases consist of sentences. These sentences are
Syntax e...

### 7.4 Propositional Logic: A Very Simple Logic

Wenowpresentpropositionallogic. Wedescribeitssyntax(thestructureofsentences)and Propositionallogic
itssemantics(thewayinwhichthetruthofsentencesisdetermined). Fromthese,wederive
a simple, syntactic algorithm for logical inference that implements the semantic notion of
entailment. Everythingtakesplace,ofcourse,inthewumpusworld....

### 7.4.1 Syntax

The syntax of propositional logic defines the allowable sentences. The atomic sentences Atomicsentences
consist of a single proposition symbol. Each such symbol stands for a proposition that can Propositionsymbol
be true or false. We use symbols that start with an uppercase letter and may contain other
letters or subscripts, for example: P, Q, R, W and FacingEast. The names are arbitrary
1,3
butar...

### 7.4.2 Semantics

Having specified the syntax of propositional logic, we now specify its semantics. The se-
mantics defines the rules for determining the truth of a sentence with respect to a particular
Truthvalue model. Inpropositionallogic,amodelsimplysetsthetruthvalue—trueorfalse—forevery
proposition symbol. For example, if the sentences in the knowledge base make use of the
propositionsymbolsP ,P ,andP ,thenone...

### 7.4.3 A simple knowledge base

Nowthatwehavedefinedthesemanticsforpropositionallogic,wecanconstructaknowledge
base for the wumpus world. We focus first on the immutable aspects of the wumpus world,
leaving the mutable aspects for a later section. For now, we need the following symbols for
each[x,y]location:
P istrueifthereisapitin[x,y].
x,y
W istrueifthereisawumpusin[x,y],deadoralive.
x,y
B istrueifthereisabreezein[x,y].
x,y
S ...

### 7.4.4 A simple inference procedure

Our goal now is to decide whether KB |= α for some sentence α. For example, is ¬P
1,2
entailedbyourKB? Ourfirstalgorithmforinferenceisamodel-checkingapproachthatisa
direct implementation of the definition of entailment: enumerate the models, and check that
α is true in every model in which KB is true. Models are assignments of true or false to
everypropositionsymbol. Returningtoourwumpus-worldexam...

### 7.5 Propositional Theorem Proving

Sofar,wehaveshownhowtodetermineentailmentbymodelchecking: enumeratingmodels
and showing that the sentence must hold in all models. In this section, we show how entail-
Theoremproving mentcanbedonebytheoremproving—applyingrulesofinferencedirectlytothesentences
inourknowledgebasetoconstructaproofofthedesiredsentencewithoutconsultingmodels.
Ifthenumberofmodelsislargebutthelengthoftheproofisshort,then...

### 7.5.1 Inference and proofs

Thissectioncoversinferencerulesthatcanbeappliedtoderiveaproof—achainofconclu- Inferencerules
sionsthatleadstothedesiredgoal. Thebest-knownruleiscalledModusPonens(Latinfor Proof
modethataffirms)andiswritten ModusPonens
α ⇒ β, α
β
The notation means that, whenever any sentences of the form α⇒β and α are given, then
the sentence β can be inferred. For example, if (WumpusAhead∧WumpusAlive)⇒Shoot
and(W...

### 7.5.2 Proof by resolution

We have arguedthat the inference rules coveredso far aresound, but we havenot discussed
the question of completeness for the inference algorithms that use them. Search algorithms
such as iterative deepening search (page 99) are complete in the sense that they will find
any reachable goal, but if the available inference rules are inadequate, then the goal is not
reachable—noproofexiststhatusesonlyt...

### 7.5.3 Horn clauses and definite clauses

Thecompletenessofresolutionmakesitaveryimportantinferencemethod. Inmanypractical
situations, however, the full power of resolution is not needed. Some real-world knowledge
bases satisfy certain restrictions on the form of sentences they contain, which enables them
touseamorerestrictedandefficientinferencealgorithm.
Onesuchrestrictedformisthedefiniteclause,whichisadisjunctionofliteralsofwhich Defin...

### 7.5.4 Forward and backward chaining

Theforward-chainingalgorithmPL-FC-ENTAILS?(KB,q)determinesifasingleproposition
symbol q—the query—is entailed by a knowledge base of definite clauses. It begins from
knownfacts(positiveliterals)intheknowledgebase. Ifallthepremisesofanimplicationare
known,thenitsconclusionisaddedtothesetofknownfacts. Forexample,ifL andBreeze
1,1
areknownand(L ∧Breeze)⇒B isintheknowledgebase,thenB canbeadded. This
1...

### 7.6 Effective Propositional Model Checking

In this section, we describe two families of efficient algorithms for general propositional
inference based on model checking: one approach based on backtracking search, and one
onlocalhill-climbingsearch. Thesealgorithmsarepartofthe“technology”ofpropositional
logic. Thissectioncanbeskimmedonafirstreadingofthechapter.
The algorithms we describe are for checking satisfiability: the SAT problem. (As...

### 7.6.1 A complete backtracking algorithm

ThefirstalgorithmweconsiderisoftencalledtheDavis–Putnamalgorithm,afterthesem- Davis–Putnam
algorithm
inal paper by Martin Davis and Hilary Putnam (1960). The algorithm is in fact the version
described by Davis, Logemann, and Loveland (1962), so we will call it DPLL after the ini-
tials of all four authors. DPLL takes as input a sentence in conjunctive normal form—a set
of clauses. Like BACKTRACKIN...

### 7.6.2 Local search algorithms

Wehaveseenseverallocalsearchalgorithmssofarinthisbook,including HILL-CLIMBING
(page 129) and SIMULATED-ANNEALING (page 133). These algorithms can be applied di-
rectly to satisfiability problems, provided that we choose the right evaluation function. Be-
causethegoalistofindanassignmentthatsatisfieseveryclause,anevaluationfunctionthat
counts the number of unsatisfied clauses will do the job. In fa...

### 7.6.3 The landscape of random SAT problems

Some SAT problems are harder than others. Easy problems can be solved by any old algo-
rithm,butbecauseweknowthatSATisNP-complete,atleastsomeprobleminstancesmust
requireexponentialruntime. InChapter5,wesawsomesurprisingdiscoveriesaboutcertain
kindsofproblems. Forexample,then-queensproblem—thoughttobequitetrickyforback-
trackingsearchalgorithms—turnedouttobetriviallyeasyforlocalsearchmethods,suchas...

### 7.7 Agents Based on Propositional Logic

In this section, we bring together what we have learned so far in order to construct wumpus
worldagentsthatusepropositionallogic. Thefirststepistoenabletheagenttodeduce,tothe
extentpossible,thestateoftheworldgivenitspercepthistory. Thisrequireswritingdowna
completelogicalmodeloftheeffectsofactions. Wethenshowhowlogicalinferencecanbe
used by an agent in the wumpus world. We also show how the agent ...

### 7.7.1 The current state of the world

As stated at the beginning of the chapter, a logical agent operates by deducing what to do
from a knowledge base of sentences about the world. The knowledge base is composed of
axioms—general knowledge about how the world works—and percept sentences obtained
fromtheagent’sexperienceinaparticularworld. Inthissection,wefocusontheproblemof
deducingthecurrentstateofthewumpusworld—whereamI,isthatsquare...

### 7.7.2 A hybrid agent

Theabilitytodeducevariousaspectsofthestateoftheworldcanbecombinedfairlystraight-
forwardly with condition–action rules (see Section 2.4.2) and with problem-solving algo-
rithmsfromChapters3and4toproduceahybridagentforthewumpusworld. Figure7.20 Hybridagent
shows one possible way to do this. The agent program maintains and updates a knowledge
base as well as a current plan. The initial knowledge bas...

### 7.7.3 Logical state estimation

The agent program in Figure 7.20 works quite well, but it has one major weakness: as time
goesby,thecomputationalexpenseinvolvedinthecallstoASKgoesupandup. Thishappens
mainlybecausetherequiredinferenceshavetogobackfurtherandfurtherintimeandinvolve
more and more proposition symbols. Obviously, this is unsustainable—we cannot have an
agentwhosetimetoprocesseachperceptgrowsinproportiontothelengthofit...

### 7.7.4 Making plans by propositional inference

TheagentinFigure7.20useslogicalinferencetodeterminewhichsquaresaresafe,butuses
A∗ search to make plans. In this section, we show how to make plans by logical inference.
Thebasicideaisverysimple:
1. Constructasentencethatincludes
(a) Init0,acollectionofassertionsabouttheinitialstate;
(b) Transition1,...,Transitiont, the successor-state axioms for all possible actions at
eachtimeuptosomemaximumtimet...

## Key Entities Mentioned

- Allen Newell
- Aristotle
- George Boole
- John McCarthy

## Algorithms & Concepts

- [[Putnam
algorithm]]
- [[Putnam algorithm]]
- [[These algorithm]]
- [[L algorithm]]
- [[Search algorithm]]
- [[H algorithm]]
- [[T algorithm]]
- [[The algorithm]]
- [[Local search]]
- [[The
algorithm]]

## Cross-References

- Previous: [[Chapter 6 - Adversarial Search and Games]]
- Next: [[Chapter 8 - First-Order Logic]]
- Part: Part III: Knowledge, Reasoning, and Planning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 7. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
