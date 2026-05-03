---
type: chapter
tags: [aima, chapter, search-in-complex-environments]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 4
---

# Chapter 4 - Search in Complex Environments

## Summary

Chapter 4 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **search in complex environments**. This chapter is part of Part II: Problem-Solving. The chapter contains approximately 9,204 words and covers foundational concepts, algorithms, and frameworks central to understanding search in complex environments in the context of artificial intelligence.

## Key Points

- **Introduction**: 4
CHAPTER
SEARCH IN COMPLEX
ENVIRONMENTS
In which we relax the simplifying assumptions of the previous chapter, to get closer to the
realworld.
Chapter3addressedproblemsinfullyobservable,deterministic,static,knownenvironments
where the solution is a sequence of actions. In this chapter, we relax tho...
- **4.1 Local Search and Optimization Problems**: InthesearchproblemsofChapter3wewantedtofindpathsthroughthesearchspace,suchas
apathfromAradtoBucharest. Butsometimeswecareonlyaboutthefinalstate,notthepath
to get there. For example, in the 8-queens problem (Figure 4.3), we care only about finding
a valid final configuration of 8 queens (because if y...
- **4.1.1 Hill-climbing search**: Thehill-climbingsearchalgorithmisshowninFigure4.2. Itkeepstrackofonecurrentstate Hillclimbing
and on each iteration moves to the neighboring state with highest value—that is, it heads in
thedirectionthatprovidesthesteepestascent. Itterminateswhenitreachesa“peak”where Steepestascent
no neighbor has a...
- **4.1.2 Simulated annealing**: Ahill-climbingalgorithmthatnevermakes“downhill”movestowardstateswithlowervalue
(orhighercost)isalwaysvulnerabletogettingstuckinalocalmaximum. Incontrast,apurely
random walk that moves to a successor state without concern for the value will eventually
stumble upon the global maximum, but will be extr...
- **4.1.3 Local beam search**: Keeping just one node in memory might seem to be an extreme reaction to the problem of
memory limitations. The local beam search algorithm keeps track of k states rather than Localbeamsearch
justone. Itbeginswithk randomlygeneratedstates. Ateachstep, allthesuccessorsofallk
statesaregenerated. Ifanyo...

## Sections Overview

### Introduction

4
CHAPTER
SEARCH IN COMPLEX
ENVIRONMENTS
In which we relax the simplifying assumptions of the previous chapter, to get closer to the
realworld.
Chapter3addressedproblemsinfullyobservable,deterministic,static,knownenvironments
where the solution is a sequence of actions. In this chapter, we relax those constraints. We
begin with the problem of finding a good state without worrying about the path to...

### 4.1 Local Search and Optimization Problems

InthesearchproblemsofChapter3wewantedtofindpathsthroughthesearchspace,suchas
apathfromAradtoBucharest. Butsometimeswecareonlyaboutthefinalstate,notthepath
to get there. For example, in the 8-queens problem (Figure 4.3), we care only about finding
a valid final configuration of 8 queens (because if you know the configuration, it is trivial to
reconstructthestepsthatcreatedit). Thisisalsotrueformany...

### 4.1.1 Hill-climbing search

Thehill-climbingsearchalgorithmisshowninFigure4.2. Itkeepstrackofonecurrentstate Hillclimbing
and on each iteration moves to the neighboring state with highest value—that is, it heads in
thedirectionthatprovidesthesteepestascent. Itterminateswhenitreachesa“peak”where Steepestascent
no neighbor has a higher value. Hill climbing does not look ahead beyond the immediate
neighbors of the current state...

### 4.1.2 Simulated annealing

Ahill-climbingalgorithmthatnevermakes“downhill”movestowardstateswithlowervalue
(orhighercost)isalwaysvulnerabletogettingstuckinalocalmaximum. Incontrast,apurely
random walk that moves to a successor state without concern for the value will eventually
stumble upon the global maximum, but will be extremely inefficient. Therefore, it seems
reasonable to try to combine hill climbing with a random walk...

### 4.1.3 Local beam search

Keeping just one node in memory might seem to be an extreme reaction to the problem of
memory limitations. The local beam search algorithm keeps track of k states rather than Localbeamsearch
justone. Itbeginswithk randomlygeneratedstates. Ateachstep, allthesuccessorsofallk
statesaregenerated. Ifanyoneisagoal,thealgorithmhalts. Otherwise,itselectsthek best
successorsfromthecompletelistandrepeats.
A...

### 4.1.4 Evolutionary algorithms

Evolutionaryalgorithmscanbeseenasvariantsofstochasticbeamsearchthatareexplicitly Evolutionary
algorithms
motivatedbythemetaphorofnaturalselectioninbiology: thereisapopulationofindividuals
(states), in which the fittest (highest value) individuals produce offspring (successor states)
that populate the next generation, a process called recombination. There are endless forms Recombination
ofevolution...

### 4.2 Local Search in Continuous Spaces

In Chapter 2, we explained the distinction between discrete and continuous environments,
pointing out that most real-world environments are continuous. A continuous action space
hasaninfinitebranchingfactor,andthuscan’tbehandledbymostofthealgorithmswehave
coveredsofar(withtheexceptionoffirst-choicehillclimbingandsimulatedannealing).
This section provides a very brief introduction to some local sea...

### 4.3 Search with Nondeterministic Actions

In Chapter3, we assumed a fullyobservable, deterministic, known environment. Therefore,
anagentcanobservetheinitialstate,calculateasequenceofactionsthatreachthegoal,and
executetheactionswithits“eyesclosed,”neverhavingtouseitspercepts.
Whentheenvironmentispartiallyobservable, however, theagentdoesn’tknowforsure
what state it is in; and when the environment is nondeterministic, the agent doesn’t kno...

### 4.3.1 The erratic vacuum world

The vacuum world from Chapter 2 has eight states, as shown in Figure 4.9. There are three
actions—Right,Left,andSuck—andthegoalistocleanupallthedirt(states7and8). Ifthe
environment is fully observable, deterministic, and completely known, then the problem is
easytosolvewithanyofthealgorithmsinChapter3,andthesolutionisanactionsequence.
Forexample,iftheinitialstateis1,thentheactionsequence[Suck,Righ...

### 4.3.3 Try, try again

Consider a slippery vacuum world, which is identical to the ordinary (non-erratic) vacuum
world except that movement actions sometimes fail, leaving the agent in the same location.
For example, moving Right in state 1 leads to the belief state {1,2}. Figure 4.12 shows
part of the search graph; clearly, there are no longer any acyclic solutions from state 1, and
AND-OR-SEARCH wouldreturnwithfailure...

### 4.4 Search in Partially Observable Environments

Wenowturntotheproblemofpartialobservability,wheretheagent’sperceptsarenotenough
to pin down the exact state. That means that some of the agent’s actions will be aimed at
reducinguncertaintyaboutthecurrentstate....

### 4.4.1 Searching with no observation

Sensorless Whentheagent’sperceptsprovidenoinformationatall,wehavewhatiscalledasensorless
Conformant problem (or a conformant problem). At first, you might think the sensorless agent has no
hopeofsolvingaproblemifithasnoideawhatstateitstartsin,butsensorlesssolutionsare
surprisinglycommonanduseful,primarilybecausetheydon’trelyonsensorsworkingprop-
erly. Inmanufacturingsystems, forexample, manyingeni...

### 4.4.2 Searching in partially observable environments

Many problems cannot be solved without sensing. For example, the sensorless 8-puzzle is
impossible. On the other hand, a little bit of sensing can go a long way: we can solve 8-
puzzles if we can see just the upper-left corner square. The solution involves moving each
tileinturnintotheobservablesquareandkeepingtrackofitslocationfromthenon.
Forapartiallyobservableproblem,theproblemspecificationwill...

### 4.4.3 Solving partially observable problems

The preceding section showed how to derive the RESULTS function for a nondeterministic
belief-stateproblemfromanunderlyingphysicalproblem,giventhePERCEPTfunction. With
this formulation, the AND–OR search algorithm of Figure 4.11 can be applied directly to
derive a solution. Figure 4.16 shows part of the search tree for the local-sensing vacuum
world,assuminganinitialpercept[L,Dirty]. Thesolutionis...

### 4.4.4 An agent for partially observable environments

An agent for partially observable environments formulates a problem, calls a search algo-
rithm(suchasAND-OR-SEARCH)tosolveit,andexecutesthesolution. Therearetwomain
differences between this agent and the one for fully observable deterministic environments.
First,thesolutionwillbeaconditionalplanratherthanasequence;toexecuteanif–then–else
expression,theagentwillneedtotesttheconditionandexecutethea...

### 4.5 Online Search Agents and Unknown Environments

Offlinesearch So far we have concentrated on agents that use offline search algorithms. They compute
Onlinesearch a complete solution before taking their first action. In contrast, an online search8 agent
interleaves computation and action: first it takes an action, then it observes the environment
and computes the next action. Online search is a good idea in dynamic or semi-dynamic
environments, ...

### 4.5.1 Online search problems

An online search problem is solved by interleaving computation, sensing, and acting. We’ll
startbyassumingadeterministicandfullyobservableenvironment(Chapter16relaxesthese
assumptions)andstipulatethattheagentknowsonlythefollowing:
• ACTIONS(s),thelegalactionsinstates;
• c(s,a,s(cid:48)),thecostofapplyingactionainstatestoarriveatstates(cid:48). Notethatthiscannot
beuseduntiltheagentknowsthats(cid:4...

### 4.5.2 Online search agents

After each action, an online agent in an observable environment receives a percept telling it
what state it has reached; from this information, it can augment its map of the environment.
The updated map is then used to plan where to go next. This interleaving of planning and
action means that online search algorithms are quite different from the offline search algo-
rithms we have seen previously:...

### 4.5.3 Online local search

Like depth-first search, hill-climbing search has the property of locality in its node expan-
sions. In fact, because it keeps just one current state in memory, hill-climbing search is
already an online search algorithm! Unfortunately, the basic algorithm is not very good for
explorationbecauseitleavestheagentsittingatlocalmaximawithnowheretogo. Moreover,
randomrestartscannotbeused,becausetheagent...

### 4.5.4 Learning in online search

Theinitialignoranceofonlinesearchagentsprovidesseveralopportunitiesforlearning. First,
theagentslearna“map”oftheenvironment—moreprecisely,theoutcomeofeachactionin
each state—simply by recording each of their experiences. Second, the local search agents
acquiremore accurate estimatesofthecost ofeachstate byusinglocalupdating rules, asin
LRTA∗. In Chapter 23, we show that these updates eventually co...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[Historical Notes
Local search]]
- [[Evolutionary algorithm]]
- [[Online search]]
- [[Stochasticbeam
search]]
- [[Localsearch Local search]]
- [[Severalstochasticlocal
search]]
- [[Thissuggeststhatsuccessfuluseofgenetic
algorithm]]
- [[Online Search]]
- [[Itisnotclearhowmuchoftheappealofgenetic
algorithm]]
- [[Genetic algorithm]]

## Cross-References

- Previous: [[Chapter 3 - Solving Problems by Searching]]
- Next: [[Chapter 5 - Constraint Satisfaction Problems]]
- Part: Part II: Problem-Solving

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 4. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
