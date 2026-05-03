---
type: chapter
tags: [aima, chapter, automated-planning]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 11
---

# Chapter 11 - Automated Planning

## Summary

Chapter 11 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **automated planning**. This chapter is part of Part III: Knowledge, Reasoning, and Planning. The chapter contains approximately 13,083 words and covers foundational concepts, algorithms, and frameworks central to understanding automated planning in the context of artificial intelligence.

## Key Points

- **Introduction**: 11
CHAPTER
AUTOMATED PLANNING
Inwhichweseehowanagentcantakeadvantageofthestructureofaproblemtoefficiently
constructcomplexplansofaction.
Planningacourseofactionisakeyrequirementforanintelligentagent. Therightrepresen-
tation for actions and states and the right algorithms can make this easier. In Se...
- **11.1 Definition of Classical Planning**: Classicalplanning Classical planning is defined as the task of finding a sequence of actions to accomplish a
goal in a discrete, deterministic, static, fully observable environment. We have seen two ap-
proaches to this task: the problem-solving agent of Chapter 3 and the hybrid propositional
logica...
- **11.1.1 Example domain: Air cargo transport**: Figure11.1showsanaircargotransportprobleminvolvingloadingandunloadingcargoand
flyingitfromplacetoplace. Theproblemcanbedefinedwiththreeactions: Load, Unload,
and Fly. The actions affect two predicates: In(c,p) means that cargo c is inside plane p,
and At(x,a) means that object x (either plane or car...
- **11.1.2 Example domain: The spare tire problem**: Consider the problem of changing a flat tire (Figure 11.2). The goal is to have a good spare
tireproperlymountedontothecar’saxle,wheretheinitialstatehasaflattireontheaxleand
a good spare tire in the trunk. To keep it simple, our version of the problem is an abstract
one, with no sticky lug nuts or o...
- **11.1.3 Example domain: The blocks world**: Oneofthemostfamousplanningdomainsistheblocksworld. Thisdomainconsistsofaset
of cube-shaped blocks sitting on an arbitrarily-large table.1 The blocks can be stacked, but
onlyoneblockcanfitdirectlyontopofanother. Arobotarmcanpickupablockandmoveit
toanotherposition,eitheronthetableorontopofanotherblock...

## Sections Overview

### Introduction

11
CHAPTER
AUTOMATED PLANNING
Inwhichweseehowanagentcantakeadvantageofthestructureofaproblemtoefficiently
constructcomplexplansofaction.
Planningacourseofactionisakeyrequirementforanintelligentagent. Therightrepresen-
tation for actions and states and the right algorithms can make this easier. In weintroduceageneralfactoredrepresentationlanguageforplanningproblemsthatcannat-
urally and succinctly ...

### 11.1 Definition of Classical Planning

Classicalplanning Classical planning is defined as the task of finding a sequence of actions to accomplish a
goal in a discrete, deterministic, static, fully observable environment. We have seen two ap-
proaches to this task: the problem-solving agent of Chapter 3 and the hybrid propositional
logicalagentofChapter7. Bothsharetwolimitations. First,theybothrequireadhocheuris-
tics for each new domai...

### 11.1.1 Example domain: Air cargo transport

Figure11.1showsanaircargotransportprobleminvolvingloadingandunloadingcargoand
flyingitfromplacetoplace. Theproblemcanbedefinedwiththreeactions: Load, Unload,
and Fly. The actions affect two predicates: In(c,p) means that cargo c is inside plane p,
and At(x,a) means that object x (either plane or cargo) is at airport a. Note that some care...

### 11.1.2 Example domain: The spare tire problem

Consider the problem of changing a flat tire (Figure 11.2). The goal is to have a good spare
tireproperlymountedontothecar’saxle,wheretheinitialstatehasaflattireontheaxleand
a good spare tire in the trunk. To keep it simple, our version of the problem is an abstract
one, with no sticky lug nuts or other complications. There are just four actions: removing
the spare from the trunk, removing the fla...

### 11.1.3 Example domain: The blocks world

Oneofthemostfamousplanningdomainsistheblocksworld. Thisdomainconsistsofaset
of cube-shaped blocks sitting on an arbitrarily-large table.1 The blocks can be stacked, but
onlyoneblockcanfitdirectlyontopofanother. Arobotarmcanpickupablockandmoveit
toanotherposition,eitheronthetableorontopofanotherblock. Thearmcanpickuponly
one block at a time, so it cannot pick up a block that has another one on top ...

### 11.2 Algorithms for Classical Planning

The description of a planning problem provides an obvious way to search from the initial
state through the space of states, looking for a goal. A nice advantage of the declarative
representationofactionschemasisthatwecanalsosearchbackwardfromthegoal,looking
fortheinitialstate(Figure11.5comparesforwardandbackwardsearches). Athirdpossibility
is to translate the problem description into a set of logi...

### 11.2.1 Forward state-space search for planning

We can solve planning problems by applying any of the heuristic search algorithms from
Chapter 3 or Chapter 4. The states in this search state space are ground states, where every
fluent is either true or not. The goal is a state that has all the positive fluents in the prob-
lem’sgoalandnoneofthenegativefluents. Theapplicableactionsinastate,Actions(s),are
grounded instantiations of the action sch...

### 11.2.2 Backward search for planning

Regressionsearch Inbackwardsearch(alsocalledregressionsearch)westartatthegoalandapplytheactions
backward until we find a sequence of steps that reaches the initial state. At each step we
Relevantaction consider relevant actions (in contrast to forward search, which considers actions that are
applicable). This reduces the branching factor significantly, particularly in domains with
manypossibleacti...

### 11.2.3 Planning as Boolean satisfiability

In Section 7.7.4 we showed how some clever axiom-rewriting could turn a wumpus world
problem into a propositional logic satisfiability problem that could be handed to an efficient
satisfiability solver. SAT-based planners such as SATPLAN operate by translating a PDDL
problemdescriptionintopropositionalform. Thetranslationinvolvesaseriesofsteps:
• Propositionalizetheactions: foreachactionschema,for...

### 11.2.4 Other classical planning approaches

The three approaches we covered above are not the only ones tried in the 50-year history of
automatedplanning. Webrieflydescribesomeothershere.
Planninggraph An approach called Graphplan uses a specialized data structure, a planning graph, to
encodeconstraintsonhowactionsarerelatedtotheirpreconditionsandeffects,andonwhich
thingsaremutuallyexclusive.
Situationcalculus Situation calculus is a method...

### 11.3 Heuristics for Planning

Neither forward nor backward search is efficient without a good heuristic function. Recall
from Chapter 3 that a heuristic function h(s) estimates the distance from a state s to the
goal, and that if we can derive an admissible heuristic for this distance—one that does not
overestimate—thenwecanuseA∗ searchtofindoptimalsolutions.
By definition, there is no way to analyze an atomic state, and thus ...

### 11.3.1 Domain-independent pruning

Factoredrepresentationsmakeitobviousthatmanystatesarejustvariantsofotherstates. For
example, suppose we have a dozen blocks on a table, and the goal is to have block A on top
ofathree-blocktower. Thefirststepinasolutionistoplacesomeblockxontopofblocky
(wherex,y,andAarealldifferent). Afterthat,placeAontopofxandwe’redone. Thereare
11choicesforx, andgivenx, 10choicesfory, andthus110statestoconsider. ...

### 11.3.2 State abstraction in planning

A relaxed problem leaves us with a simplified planning problem just to calculate the value
of the heuristic function. Many planning problems have 10100 states or more, and relaxing
the actions does nothing to reduce the number of states, which means that it may still be
expensive to compute the heuristic. Therefore, we now look at relaxations that decrease the
numberofstatesbyformingastateabstract...

### 11.4 Hierarchical Planning

Theproblem-solvingandplanningmethodsoftheprecedingchaptersalloperatewithafixed
set of atomic actions. Actions can be strung together, and state-of-the-art algorithms can
generatesolutionscontainingthousandsofactions. That’sfineifweareplanningavacation
and the actions are at the level of “fly from San Francisco to Honolulu,” but at the motor-
control level of “bend the left knee by 5 degrees” we wo...

### 11.4.1 High-level actions

Thebasicformalismweadopttounderstandhierarchicaldecompositioncomesfromthearea
ofhierarchicaltasknetworksorHTNplanning. Fornowweassumefullobservabilityand Hierarchicaltask
network
determinismandasetofactions,nowcalledprimitiveactions,withstandardprecondition– Primitiveaction
effect schemas. The key additional concept is the high-level action or HLA—for example, High-levelaction
the action “Go to Sa...

### 11.4.2 Searching for primitive solutions

HTNplanningisoftenformulatedwithasingle“toplevel”actioncalledAct, wheretheaim
istofindanimplementationofActthatachievesthegoal. Thisapproachisentirelygeneral.
Forexample,classicalplanningproblemscanbedefinedasfollows: foreachprimitiveaction
a,provideonerefinementofActwithsteps[a,Act]. ThatcreatesarecursivedefinitionofAct
i i
thatletsusaddactions. Butweneedsomewaytostoptherecursion;wedothatbyprovid...

### 11.4.3 Searching for abstract solutions

ThehierarchicalsearchalgorithmintheprecedingsectionrefinesHLAsallthewaytoprimi-
tiveactionsequencestodetermineifaplanisworkable. Thiscontradictscommonsense: one
shouldbeabletodeterminethatthetwo-HLAhigh-levelplan
[Drive(Home,SFOLongTermParking),Shuttle(SFOLongTermParking,SFO)]
gets one to the airport without having to determine a precise route, choice of parking spot,
and so on. The solution is to...

### 11.5 Planning and Acting in Nondeterministic Domains

In this section we extend planning to handle partially observable, nondeterministic, and un-
knownenvironments. ThebasicconceptsmirrorthoseinChapter4,buttherearedifferences
arising from the use of factored representations rather than atomic representations. This af-
fects the way we represent the agent’s capability for action and observation and the way
we represent belief states—the sets of possi...

### 11.5.1 Sensorless planning

Section 4.4.1 (page 144) introduced the basic idea of searching in belief-state space to find
asolutionforsensorlessproblems. Conversionofasensorlessplanningproblemtoabelief-
state planning problem works much the same way as it did in Section 4.4.1; the main dif-
ferences are that the underlying physical transition model is represented by a collection of
action schemas, and the belief state can be...

### 11.5.2 Contingent planning

We saw in Chapter 4 that contingency planning—the generation of plans with conditional
branchingbasedonpercepts—isappropriateforenvironmentswithpartialobservability,non-
determinism,orboth. Forthepartiallyobservablepaintingproblemwiththeperceptschemas
givenearlier,onepossibleconditionalsolutionisasfollows:
[LookAt(Table),LookAt(Chair),
ifColor(Table,c)∧Color(Chair,c)thenNoOp
else[RemoveLid(Can ),L...

### 11.5.3 Online planning

Imaginewatchingaspot-weldingrobotinacarplant. Therobot’sfast,accuratemotionsare
repeated over and over again as each car passes down the line. Although technically im-
pressive, the robot probably does not seem at all intelligent because the motion is a fixed,
preprogrammedsequence; therobotobviouslydoesn’t“knowwhatit’sdoing”inanymean-
ingful sense. Now suppose that a poorly attached door falls of...

### 11.6 Time, Schedules, and Resources

Classical planning talks about what to do, in what order, but does not talk about time: how
longanactiontakesandwhenitoccurs. Forexample,intheairportdomainwecouldproduce
aplansayingwhatplanesgowhere,carryingwhat,butcouldnotspecifydepartureandarrival
Scheduling times. Thisisthesubjectmatterofscheduling.
Resourceconstraint The real world also imposes resource constraints: an airline has a limited nu...

### 11.6.1 Representing temporal and resource constraints

A typical job-shop scheduling problem (see Section 5.1.2), consists of a set of jobs, each Job-shopscheduling
problem
ofwhichhas acollectionofactionswithorderingconstraints amongthem. Each actionhas Job
a duration and a set of resource constraints required by the action. A constraint specifies Duration
a type of resource (e.g., bolts, wrenches, or pilots), the number of that resource required,
and...

### 11.6.2 Solving scheduling problems

Webeginbyconsideringjustthetemporalschedulingproblem,ignoringresourceconstraints.
Tominimizemakespan(planduration),wemustfindtheearlieststarttimesforalltheactions
consistentwiththeorderingconstraintssuppliedwiththeproblem. Itishelpfultoviewthese
orderingconstraintsasadirectedgraphrelatingtheactions,asshowninFigure11.14. Wecan
Criticalpathmethod apply the critical path method (CPM) to this graph to...

### 11.7 Analysis of Planning Approaches

Planning combines the two major areas of AI we have covered so far: search and logic. A
plannercanbeseeneitherasaprogramthatsearchesforasolutionorasonethat(construc-
tively)provestheexistenceofasolution. Thecross-fertilizationofideasfromthetwoareas
has allowed planners to scale up from toy problems where the number of actions and states
was limited to around a dozen, to real-world industrial appli...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[A search]]
- [[Backward search]]
- [[Fortunatelyasimplegreedy
algorithm]]
- [[Planning Algorithm]]
- [[Forward search]]
- [[Bidirectional search]]
- [[An algorithm]]
- [[Heuristic Search]]

## Cross-References

- Previous: [[Chapter 10 - Knowledge Representation]]
- Next: [[Chapter 12 - Quantifying Uncertainty]]
- Part: Part III: Knowledge, Reasoning, and Planning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 11. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
