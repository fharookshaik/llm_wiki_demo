---
type: chapter
tags: [aima, chapter, solving-problems-by-searching]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 3
---

# Chapter 3 - Solving Problems by Searching

## Summary

Chapter 3 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **solving problems by searching**. This chapter is part of Part II: Problem-Solving. The chapter contains approximately 13,688 words and covers foundational concepts, algorithms, and frameworks central to understanding solving problems by searching in the context of artificial intelligence.

## Key Points

- **Introduction**: 3
CHAPTER
SOLVING PROBLEMS BY SEARCHING
Inwhichweseehowanagentcanlookaheadtofindasequenceofactionsthatwilleven-
tuallyachieveitsgoal.
When the correct action to take is not immediately obvious, an agent may need to plan
ahead: to consider a sequence of actions that form a path to a goal state. Such ...
- **3.1 Problem-Solving Agents**: Imagine an agent enjoying a touring vacation in Romania. The agent wants to take in the
sights, improve its Romanian, enjoy the nightlife, avoid hangovers, and so on. The decision
problem is a complex one. Now, suppose the agent is currently in the city of Arad and
has a nonrefundable ticket to fly ...
- **3.1.1 Search problems and solutions**: Asearchproblemcanbedefinedformallyasfollows: Problem
• Asetofpossiblestatesthattheenvironmentcanbein. Wecallthisthestatespace. States
• Theinitialstatethattheagentstartsin. Forexample: Arad. Statespace
• A set of one or more goal states. Sometimes there is one goal state (e.g., Bucharest), Initialst...
- **3.1.2 Formulating problems**: OurformulationoftheproblemofgettingtoBucharestisamodel—anabstractmathematical
description—andnottherealthing. ComparethesimpleatomicstatedescriptionAradtoan
actualcross-countrytrip,wherethestateoftheworldincludessomanythings: thetraveling
companions,thecurrentradioprogram,thesceneryoutofthewindow,th...
- **3.2 Example Problems**: Theproblem-solvingapproachhasbeenappliedtoavastarrayoftaskenvironments. Welist
someofthebestknownhere,distinguishingbetweenstandardizedandreal-worldproblems.
Standardized Astandardizedproblemisintendedtoillustrateorexercisevariousproblem-solvingmeth-
problem
ods. It can be given a concise, exact des...

## Sections Overview

### Introduction

3
CHAPTER
SOLVING PROBLEMS BY SEARCHING
Inwhichweseehowanagentcanlookaheadtofindasequenceofactionsthatwilleven-
tuallyachieveitsgoal.
When the correct action to take is not immediately obvious, an agent may need to plan
ahead: to consider a sequence of actions that form a path to a goal state. Such an agent is
calledaproblem-solvingagent,andthecomputationalprocessitundertakesiscalledsearch. Proble...

### 3.1 Problem-Solving Agents

Imagine an agent enjoying a touring vacation in Romania. The agent wants to take in the
sights, improve its Romanian, enjoy the nightlife, avoid hangovers, and so on. The decision
problem is a complex one. Now, suppose the agent is currently in the city of Arad and
has a nonrefundable ticket to fly out of Bucharest the following day. The agent observes
streetsignsandseesthattherearethreeroadsleadi...

### 3.1.1 Search problems and solutions

Asearchproblemcanbedefinedformallyasfollows: Problem
• Asetofpossiblestatesthattheenvironmentcanbein. Wecallthisthestatespace. States
• Theinitialstatethattheagentstartsin. Forexample: Arad. Statespace
• A set of one or more goal states. Sometimes there is one goal state (e.g., Bucharest), Initialstate
sometimes there is a small set of alternative goal states, and sometimes the goal is Goalstates
...

### 3.1.2 Formulating problems

OurformulationoftheproblemofgettingtoBucharestisamodel—anabstractmathematical
description—andnottherealthing. ComparethesimpleatomicstatedescriptionAradtoan
actualcross-countrytrip,wherethestateoftheworldincludessomanythings: thetraveling
companions,thecurrentradioprogram,thesceneryoutofthewindow,theproximityoflaw
enforcementofficers,thedistancetothenextreststop,theconditionoftheroad,theweather,
t...

### 3.2 Example Problems

Theproblem-solvingapproachhasbeenappliedtoavastarrayoftaskenvironments. Welist
someofthebestknownhere,distinguishingbetweenstandardizedandreal-worldproblems.
Standardized Astandardizedproblemisintendedtoillustrateorexercisevariousproblem-solvingmeth-
problem
ods. It can be given a concise, exact description and hence is suitable as a benchmark for
Real-worldproblem researcherstocomparetheperforman...

### 3.2.1 Standardized problems

Gridworld Agridworldproblemisatwo-dimensionalrectangulararrayofsquarecellsinwhichagents
canmovefromcelltocell. Typicallytheagentcanmovetoanyobstacle-freeadjacentcell—
horizontallyorverticallyandinsomeproblemsdiagonally. Cellscancontainobjects,which
4 SeeSection11.4....

### 3.2.2 Real-world problems

We have already seen how the route-finding problem is defined in terms of specified lo-
cations and transitions along edges between them. Route-finding algorithms are used in a
variety of applications. Some, such as Web sites and in-car systems that provide driving
directions, are relatively straightforward extensions of the Romania example. (The main
complications are varying costs due to traffic...

### 3.3 Search Algorithms

Asearchalgorithmtakesasearchproblemasinputandreturnsasolution,oranindicationof Searchalgorithm
failure. Inthischapterweconsideralgorithmsthatsuperimposeasearchtreeoverthestate-
space graph, forming various paths from the initial state, trying to find a path that reaches a
goalstate. Eachnodeinthesearchtreecorrespondstoastateinthestatespaceandtheedges Node
inthesearchtreecorrespondtoactions. Theroo...

### 3.3.1 Best-first search

How do we decide which node from the frontier to expand next? A very general approach
is called best-first search, in which we choose a node, n, with minimum value of some Best-firstsearch
evaluation function, f(n). Figure 3.7 shows the algorithm. On each iteration we choose Evaluationfunction
a node on the frontier with minimum f(n) value, return it if its state is a goal state, and
otherwise app...

### 3.3.2 Search data structures

Searchalgorithmsrequireadatastructuretokeeptrackofthesearchtree. Anodeinthetree
isrepresentedbyadatastructurewithfourcomponents:
• node.STATE: thestatetowhichthenodecorresponds;
• node.PARENT: thenodeinthetreethatgeneratedthisnode;
• node.ACTION: theactionthatwasappliedtotheparent’sstatetogeneratethisnode;
• node.PATH-COST: thetotalcostofthepathfromtheinitialstatetothisnode. Inmath-
ematicalformul...

### 3.3.3 Redundant paths

ThesearchtreeshowninFigure3.4(bottom)includesapathfromAradtoSibiuandbackto
Repeatedstate Aradagain. WesaythatAradisarepeatedstateinthesearchtree,generatedinthiscaseby
Cycle acycle(alsoknownasaloopypath). Soeventhoughthestatespacehasonly20states,the
Loopypath completesearchtreeisinfinitebecausethereisnolimittohowoftenonecantraversealoop.
Redundantpath Acycleisaspecialcaseofaredundantpath. Forexampl...

### 3.3.4 Measuring problem-solving performance

Beforewegetintothedesignofvarioussearchalgorithms,wewillconsiderthecriteriaused
tochooseamongthem. Wecanevaluateanalgorithm’sperformanceinfourways:
• Completeness: Isthealgorithmguaranteedtofindasolutionwhenthereisone,andto Completeness
correctlyreportfailurewhenthereisnot?
• Costoptimality: Doesitfindasolutionwiththelowestpathcostofallsolutions?7 Costoptimality
• Time complexity: How long does it...

### 3.4 Uninformed Search Strategies

An uninformed search algorithm is given no clue about how close a state is to the goal(s).
Forexample,considerouragentinAradwiththegoalofreachingBucharest. Anuninformed
agent with no knowledge of Romanian geography has no clue whether going to Zerind or
Sibiuisabetterfirststep. Incontrast,aninformedagent(Section3.5)whoknowsthelocation
of each city knows that Sibiu is much closer to Bucharest and t...

### 3.4.1 Breadth-first search

Breadth-firstsearch Whenallactionshavethesamecost,anappropriatestrategyisbreadth-firstsearch,inwhich
the root node is expanded first, then all the successors of the root node are expanded next,
then their successors, and so on. This is a systematic search strategy that is therefore com-
plete even on infinite state spaces. We could implement breadth-first search as a call to
BEST-FIRST-SEARCH wher...

### 3.4.3 Depth-first search and the problem of memory

Depth-firstsearch Depth-first search always expands the deepest node in the frontier first. It could be imple-
mented as a call to BEST-FIRST-SEARCH where the evaluation function f is the negative
of the depth. However, it is usually implemented not as a graph search but as a tree-like
search that does not keep a table of reached states. The progress of the search is illustrated
inFigure3.11;searc...

### 3.4.4 Depth-limited and iterative deepening search

To keep depth-first search from wandering down an infinite path, we can use depth-limited
Depth-limitedsearch search,aversionofdepth-firstsearchinwhichwesupplyadepthlimit,(cid:96),andtreatallnodes
at depth (cid:96) as if they had no successors (see Figure 3.12). The time complexity is O(b(cid:96)) and
the space complexity is O(b(cid:96)). Unfortunately, if we make a poor choice for (cid:96) the al...

### 3.4.5 Bidirectional search

Thealgorithmswehavecoveredsofarstartataninitialstateandcanreachanyoneofmultiple
Bidirectionalsearch possible goal states. An alternative approach called bidirectional search simultaneously
searches forward from the initial state and backwards from the goal state(s), hoping that the
twosearcheswillmeet. Themotivationisthatbd/2+bd/2 ismuchlessthanbd (e.g.,50,000
timeslesswhenb=d=10)....

### 3.4.6 Comparing uninformed search algorithms

Figure3.15comparesuninformedsearchalgorithmsintermsofthefourevaluationcriteriaset
forthinSection3.3.4. Thiscomparisonisfortree-likesearchversionswhichdon’tcheckfor
repeatedstates. Forgraphsearcheswhichdocheck, themaindifferencesarethatdepth-first
search is complete for finite state spaces, and the space and time complexities are bounded
bythesizeofthestatespace(thenumberofverticesandedges,|V|+|E|)...

### 3.5.1 Greedy best-first search

Greedy best-first search is a form of best-first search that expands first the node with the Greedybest-first
search
lowest h(n) value—the node that appears to be closest to the goal—on the grounds that this
islikelytoleadtoasolutionquickly. Sotheevaluationfunction f(n)=h(n).
Let us see how this works for route-finding problems in Romania; we use the straight-
line distance heuristic, which we wil...

### 3.5.3 Search contours

Ausefulwaytovisualizeasearchistodrawcontoursinthestatespace,justlikethecontours Contour
in a topographic map. Figure 3.20 shows an example. Inside the contour labeled 400, all
nodeshave f(n)=g(n)+h(n)≤400,andsoon. Then,becauseA∗expandsthefrontiernode
of lowest f-cost, we can see that an A∗ search fans out from the start node, adding nodes in
concentricbandsofincreasing f-cost.
With uniform-cost se...

### 3.5.5 Memory-bounded search

ThemainissuewithA∗isitsuseofmemory. Inthissectionwe’llcoversomeimplementation
tricksthatsavespace,andthensomeentirelynewalgorithmsthattakebetteradvantageofthe
availablespace.
Memory is split between the frontier and the reached states. In our implementation of
best-firstsearch,astatethatisonthefrontierisstoredintwoplaces: asanodeinthefrontier
(so we can decide what to expand next) and as an entry ...

### 3.5.6 Bidirectional heuristic search

Withunidirectionalbest-firstsearch,wesawthatusing f(n)=g(n)+h(n)astheevaluation
functiongivesusanA∗ searchthatisguaranteedtofindoptimal-costsolutions(assumingan
admissibleh)whilebeingoptimallyefficientinthenumberofnodesexpanded.
With bidirectional best-first search we could also try using f(n)=g(n)+h(n), but un-
fortunately there is no guarantee that this would lead to an optimal-cost solution, no...

### 3.6 Heuristic Functions

Inthissection,welookathowtheaccuracyofaheuristicaffectssearchperformance,andalso
considerhowheuristicscanbeinvented. Asourmainexamplewe’llreturntothe8-puzzle. As
mentionedinSection3.2,theobjectofthepuzzleistoslidethetileshorizontallyorvertically
intotheemptyspaceuntiltheconfigurationmatchesthegoalconfiguration(Figure3.25).
There are 9!/2=181,400 reachable states in an 8-puzzle, so a search could e...

### 3.6.1 The effect of heuristic accuracy on performance

Effectivebranching Onewaytocharacterizethequalityofaheuristicistheeffectivebranchingfactorb∗. Ifthe
factor
totalnumberofnodesgeneratedbyA∗ foraparticularproblemisN andthesolutiondepthis
d, then b∗ is the branching factor that a uniform tree of depth d would have to have in order
tocontainN+1nodes. Thus,
N+1=1+b∗+(b∗)2+···+(b∗)d.
For example, if A∗ finds a solution at depth 5 using 52 nodes, then t...

### 3.6.2 Generating heuristics from relaxed problems

We have seen that both h (misplaced tiles) and h (Manhattan distance) are fairly good
1 2
heuristics for the 8-puzzle and that h is better. How might one have come up with h ? Is it
2 2
possibleforacomputertoinventsuchaheuristicmechanically?
h and h are estimates of the remaining path length for the 8-puzzle, but they are also
1 2
perfectlyaccuratepathlengthsforsimplifiedversionsofthepuzzle. Ifthe...

### 3.6.3 Generating heuristics from subproblems: Pattern databases

Subproblem Admissibleheuristicscanalsobederivedfromthesolutioncostofasubproblemofagiven
problem. For example, Figure 3.27 shows a subproblem of the 8-puzzle instance in Fig-
ure 3.25. The subproblem involves getting tiles 1, 2, 3, 4, and the blank into their correct
positions. Clearly, the cost of the optimal solution of this subproblem is a lower bound on
14 InChapters8and11,wedescribeformallangu...

### 3.6.4 Generating heuristics with landmarks

Thereareonlineservicesthathostmapswithtensofmillionsofverticesandfindcost-optimal
drivingdirectionsinmilliseconds(Figure3.28). Howcantheydothat,whenthebestsearch
algorithmswehaveconsideredsofarareaboutamilliontimesslower? Therearemanytricks,
Precomputation but the most important one is precomputation of some optimal path costs. Although the
precomputationcanbetime-consuming,itneedonlybedoneonce,an...

### 3.6.5 Learning to search better

We have presented several fixed search strategies—breadth-first, A∗, and so on—that have
been carefully designed and programmed by computer scientists. Could an agent learn how
tosearchbetter? Theanswerisyes,andthemethodrestsonanimportantconceptcalledthe
metalevel state space. Each state in a metalevel state space captures the internal (compu- Metalevelstate
space
tational) state of a program that...

### 3.6.6 Learning heuristics from experience

We have seen that one way to invent a heuristic is to devise a relaxed problem for which an
optimalsolutioncanbefoundeasily. Analternativeistolearnfromexperience. “Experience”
here means solving lots of 8-puzzles, for instance. Each optimal solution to an 8-puzzle
problemprovidesanexample(goal,path)pair. Fromtheseexamples,alearningalgorithmcan
beusedtoconstructafunctionhthatcan(withluck)approximat...

## Key Entities Mentioned

- Richard Bellman

## Algorithms & Concepts

- [[A search]]
- [[Uninformed Search]]
- [[Beamsearch Beam search]]
- [[Two algorithm]]
- [[Search Algorithm]]
- [[Search algorithm]]
- [[Informed search]]
- [[H algorithm]]
- [[Warshall algorithm]]
- [[Bidirectional search]]

## Cross-References

- Previous: [[Chapter 2 - Intelligent Agents]]
- Next: [[Chapter 4 - Search in Complex Environments]]
- Part: Part II: Problem-Solving

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 3. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
