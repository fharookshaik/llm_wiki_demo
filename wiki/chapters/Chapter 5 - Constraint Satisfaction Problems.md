---
type: chapter
tags: [aima, chapter, constraint-satisfaction-problems]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 5
---

# Chapter 5 - Constraint Satisfaction Problems

## Summary

Chapter 5 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **constraint satisfaction problems**. This chapter is part of Part II: Problem-Solving. The chapter contains approximately 8,557 words and covers foundational concepts, algorithms, and frameworks central to understanding constraint satisfaction problems in the context of artificial intelligence.

## Key Points

- **Introduction**: 5
CHAPTER
CONSTRAINT SATISFACTION
PROBLEMS
Inwhichweseehowtreatingstatesasmorethanjustlittleblackboxesleadstonewsearch
methodsandadeeperunderstandingofproblemstructure.
Chapters3and4exploredtheideathatproblemscanbesolvedbysearchingthestatespace:
a graph where the nodes are states and the edges betwe...
- **5.1 Defining Constraint Satisfaction Problems**: Aconstraintsatisfactionproblemconsistsofthreecomponents,X,D,andC:
X isasetofvariables,{X ,...,X }.
1 n
D isasetofdomains,{D ,...,D },oneforeachvariable.
1 n
C isasetofconstraintsthatspecifyallowablecombinationsofvalues.
A domain, D, consists of a set of allowable values, {v ,...,v }, for variable X....
- **5.1.1 Example problem: Map coloring**: Supposethat,havingtiredofRomania,wearelookingatamapofAustraliashowingeachof
its states and territories (Figure 5.1(a)). We are given the task of coloring each region either
red, green, or blue in such a way that no two neighboring regions have the same color. To
formulatethisasaCSP,wedefinethevariab...
- **5.1.2 Example problem: Job-shop scheduling**: Factorieshavetheproblemofschedulingaday’sworthofjobs,subjecttovariousconstraints.
Inpractice,manyoftheseproblemsaresolvedwithCSPtechniques. Considertheproblemof
schedulingtheassemblyofacar. Thewholejobiscomposedoftasks,andwecanmodeleach
task as a variable, where the value of each variable is the tim...
- **5.1.3 Variations on the CSP formalism**: ThesimplestkindofCSPinvolvesvariablesthathavediscrete,finitedomains. Map-coloring Discretedomain
problemsandschedulingwithtimelimitsarebothofthiskind. The8-queensproblem(Fig- Finitedomain
ure4.3)canalsobeviewedasafinite-domainCSP,wherethevariablesQ ,...,Q correspond
1 8
to the queens in columns 1 to...

## Sections Overview

### Introduction

5
CHAPTER
CONSTRAINT SATISFACTION
PROBLEMS
Inwhichweseehowtreatingstatesasmorethanjustlittleblackboxesleadstonewsearch
methodsandadeeperunderstandingofproblemstructure.
Chapters3and4exploredtheideathatproblemscanbesolvedbysearchingthestatespace:
a graph where the nodes are states and the edges between them are actions. We saw that
domain-specific heuristics could estimate the cost of reaching the ...

### 5.1 Defining Constraint Satisfaction Problems

Aconstraintsatisfactionproblemconsistsofthreecomponents,X,D,andC:
X isasetofvariables,{X ,...,X }.
1 n
D isasetofdomains,{D ,...,D },oneforeachvariable.
1 n
C isasetofconstraintsthatspecifyallowablecombinationsofvalues.
A domain, D, consists of a set of allowable values, {v ,...,v }, for variable X. For exam-
i 1 k i
ple, a Boolean variable would have the domain {true,false}. Different variables c...

### 5.1.1 Example problem: Map coloring

Supposethat,havingtiredofRomania,wearelookingatamapofAustraliashowingeachof
its states and territories (Figure 5.1(a)). We are given the task of coloring each region either
red, green, or blue in such a way that no two neighboring regions have the same color. To
formulatethisasaCSP,wedefinethevariablestobetheregions:
X ={WA,NT,Q,NSW,V,SA,T}.
ThedomainofeveryvariableisthesetD ={red,green,blue}. The...

### 5.1.2 Example problem: Job-shop scheduling

Factorieshavetheproblemofschedulingaday’sworthofjobs,subjecttovariousconstraints.
Inpractice,manyoftheseproblemsaresolvedwithCSPtechniques. Considertheproblemof
schedulingtheassemblyofacar. Thewholejobiscomposedoftasks,andwecanmodeleach
task as a variable, where the value of each variable is the time that the task starts, expressed
as an integer number of minutes. Constraints can assert that one t...

### 5.1.3 Variations on the CSP formalism

ThesimplestkindofCSPinvolvesvariablesthathavediscrete,finitedomains. Map-coloring Discretedomain
problemsandschedulingwithtimelimitsarebothofthiskind. The8-queensproblem(Fig- Finitedomain
ure4.3)canalsobeviewedasafinite-domainCSP,wherethevariablesQ ,...,Q correspond
1 8
to the queens in columns 1 to 8, and the domain of each variable specifies the possible row
numbersforthequeeninthatcolumn, D ={1...

### 5.2 Constraint Propagation: Inference in CSPs

An atomic state-space search algorithm makes progress in only one way: by expanding a
node to visit the successors. A CSP algorithm has choices. It can generate successors by
choosinganewvariableassignment,oritcandoaspecifictypeofinferencecalledconstraint
propagation: usingtheconstraintstoreducethenumberoflegalvaluesforavariable,which Constraint
propagation...

### 5.2.1 Node consistency

Nodeconsistency A single variable (corresponding to a node in the CSP graph) is node-consistent if all the
values in the variable’s domain satisfy the variable’s unary constraints. For example, in the
variant of the Australia map-coloring problem (Figure 5.1) where South Australians dislike
green, the variable SA starts with domain {red,green,blue}, and we can make it node con-
sistentby eliminati...

### 5.2.2 Arc consistency

Arcconsistency A variable in a CSP is arc-consistent1 if every value in its domain satisfies the variable’s
binary constraints. More formally, X is arc-consistent with respect to another variable X if
i j
for every value in the current domain D there is some value in the domain D that satisfies
i j
the binary constraint on the arc (X,X ). A graph is arc-consistent if every variable is arc-
i j
con...

### 5.2.3 Path consistency

Suppose we are to color the map of Australia with just two colors, red and blue. Arc con-
sistency does nothing because every constraint can be satisfied individually with red at one
end and blue at the other. But clearly there is no solution to the problem: because Western
Australia,NorthernTerritory,andSouthAustraliaalltoucheachother,weneedatleastthree
colorsforthemalone....

### 5.2.4 K-consistency

K-consistency Strongerformsofpropagationcanbedefinedwiththenotionofk-consistency. ACSPisk-
consistentif,foranysetofk−1variablesandforanyconsistentassignmenttothosevariables,
aconsistentvaluecanalwaysbeassignedtoanykthvariable. 1-consistencysaysthat, given
the empty set, we can make any set of one variable consistent: this is what we called node
consistency. 2-consistency is the same as arc consist...

### 5.2.5 Global constraints

Rememberthataglobalconstraintisoneinvolvinganarbitrarynumberofvariables(butnot
necessarily all variables). Global constraints occur frequently in real problems and can be
handledbyspecial-purposealgorithmsthataremoreefficientthanthegeneral-purposemeth-
ods described so far. For example, the Alldiff constraint says that all the variables involved
must have distinct values (as in the cryptarithmetic...

### 5.2.6 Sudoku

ThepopularSudokupuzzlehasintroducedmillionsofpeopletoconstraintsatisfactionprob- Sudoku
lems,althoughtheymaynotrealizeit. ASudokuboardconsistsof81squares,someofwhich
are initially filled with digits from 1 to 9. The puzzle is to fill in all the remaining squares
such that no digit appears twice in any row, column, or 3×3 box (see Figure 5.4). A row,
column,orboxiscalledaunit....

### 5.3 Backtracking Search for CSPs

Sometimes we can finish the constraint propagation process and still have variables with
multiple possible values. In that case we have to search for a solution. In this section we
cover backtracking search algorithms that work on partial assignments; in the next section
welookatlocalsearchalgorithmsovercompleteassignments.
Consider how a standard depth-limited search (from Chapter 3) could solve ...

### 5.3.1 Variable and value ordering

Thebacktrackingalgorithmcontainstheline
var←SELECT-UNASSIGNED-VARIABLE(csp,assignment).
The simplest strategy for SELECT-UNASSIGNED-VARIABLE is static ordering: choose the
variables in order, {X ,X ,...}. The next simplest is to choose randomly. Neither strategy
1 2
is optimal. For example, after the assignments for WA=red and NT=green in Figure 5.6,
thereisonlyonepossiblevalueforSA,soitmakessense...

### 5.3.2 Interleaving search and inference

We saw how AC-3 can reduce the domains of variables before we begin the search. But
inference can be even more powerful during the course of a search: every time we make
a choice of a value for a variable, we have a brand-new opportunity to infer new domain
reductionsontheneighboringvariables.
Forwardchecking Oneofthesimplestformsofinferenceiscalledforwardchecking. Wheneveravariable
X isassigned,t...

### 5.3.3 Intelligent backtracking: Looking backward

The BACKTRACKING-SEARCH algorithminFigure5.5hasaverysimplepolicyforwhatto
do when a branch of the search fails: back up to the preceding variable and try a different
value for it. This is called chronological backtracking because the most recent decision Chronological
backtracking
pointisrevisited. Inthissubsection,weconsiderbetterpossibilities.
Consider what happens when we apply simple backtrack...

### 5.3.4 Constraint learning

When we reach a contradiction, backjumping can tell us how far to back up, so we don’t
waste time changing variables that won’t fix the problem. But we would also like to avoid
running into the same problem again. When the search arrives at a contradiction, we know
Constraintlearning that some subset of the conflict set is responsible for the problem. Constraint learning is
the idea of finding a m...

### 5.4 Local Search for CSPs

Localsearchalgorithms(seeSection4.1)turnouttobeveryeffectiveinsolvingmanyCSPs.
They use a complete-state formulation (as introduced in Section 4.1.1) where each state as-
signsavaluetoeveryvariable,andthesearchchangesthevalueofonevariableatatime. As
anexample,we’llusethe8-queensproblem,asdefinedasaCSPonpage167. InFigure5.8
we start on the left with a complete assignment to the 8 variables; typical...

### 5.5 The Structure of Problems

In this section, we examine ways in which the structure of the problem, as represented by
theconstraintgraph,canbeusedtofindsolutionsquickly. Mostoftheapproachesherealso
applytootherproblemsbesidesCSPs,suchasprobabilisticreasoning.
Theonlywaywecanpossiblyhopetodealwiththevastrealworldistodecomposeitinto
subproblems. LookingagainattheconstraintgraphforAustralia(Figure5.1(b),repeatedas
Figure5.12(a)...

### 5.5.1 Cutset conditioning

Thefirstwaytoreduceaconstraintgraphtoatreeinvolvesassigningvaluestosomevariables
sothattheremainingvariablesformatree. ConsidertheconstraintgraphforAustralia,shown
again in Figure 5.12(a). Without South Australia, the graph would become a tree, as in (b).
Fortunately, we can delete South Australia (in the graph, not the country) by fixing a value
for SA and deleting from the domains of the other v...

### 5.5.2 Tree decomposition

Thesecondwaytoreduceaconstraintgraphtoatreeisbasedonconstructingatreedecom-
positionoftheconstraintgraph: atransformationoftheoriginalgraphintoatreewhereeach Treedecomposition
node in the tree consists of a set of variables, as in Figure 5.13. A tree decomposition must
satisfythesethreerequirements:
• Everyvariableintheoriginalproblemappearsinatleastoneofthetreenodes.
• Iftwovariablesareconnectedb...

### 5.5.3 Value symmetry

So far, we have looked at the structure of the constraint graph. There can also be important
structurein thevaluesof variables, or inthe structureof theconstraint relationsthemselves.
Consider the map-coloring problem with d colors. For every consistent solution, there is
actually a set of d! solutions formed by permuting the color names. For example, on the
Australia map we know that WA, NT, and ...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[A search]]
- [[Backtracking Search]]
- [[Local search]]
- [[H algorithm]]
- [[Plateau search]]
- [[Therearemorecomplexinference
algorithm]]
- [[Arc The algorithm]]
- [[T algorithm]]
- [[Interleaving search]]
- [[P algorithm]]

## Cross-References

- Previous: [[Chapter 4 - Search in Complex Environments]]
- Next: [[Chapter 6 - Adversarial Search and Games]]
- Part: Part II: Problem-Solving

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 5. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
