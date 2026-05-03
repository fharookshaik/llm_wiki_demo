---
type: chapter
tags: [aima, chapter, adversarial-search-and-games]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 6
---

# Chapter 6 - Adversarial Search and Games

## Summary

Chapter 6 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **adversarial search and games**. This chapter is part of Part II: Problem-Solving. The chapter contains approximately 9,890 words and covers foundational concepts, algorithms, and frameworks central to understanding adversarial search and games in the context of artificial intelligence.

## Key Points

- **Introduction**: 6
CHAPTER
ADVERSARIAL SEARCH AND GAMES
Inwhichweexploreenvironmentswhereotheragentsareplottingagainstus.
Inthischapterwecovercompetitiveenvironments,inwhichtwoormoreagentshavecon-
Adversarialsearch flicting goals, giving rise to adversarial search problems. Rather than deal with the chaos
of real-wo...
- **6.1 Game Theory**: There are at least three stances we can take towards multi-agent environments. The first
stance, appropriate when there are a very large number of agents, is to consider them in the
Economy aggregate as an economy, allowing us to do things like predict that increasing demand will
causepricestorise,w...
- **6.1.1 Two-player zero-sum games**: ThegamesmostcommonlystudiedwithinAI(suchaschessandGo)arewhatgametheorists
call deterministic, two-player, turn-taking, perfect information, zero-sum games. “Perfect Perfectinformation
information”isasynonymfor“fullyobservable,”1 and“zero-sum”meansthatwhatisgood Zero-sumgames
foroneplayerisjustasbadf...
- **6.2 Optimal Decisions in Games**: MAX wants to find a sequence of actions leading to a win, but MIN has something to say
about it. This means that MAX’s strategy must be a conditional plan—a contingent strategy
specifyingaresponsetoeachof MIN’spossiblemoves. Ingamesthathaveabinaryoutcome
(win or lose), we could use AND–OR search (pa...
- **6.2.1 The minimax search algorithm**: Now that we can compute MINIMAX(s), we can turn that into a search algorithm that finds
the best move for MAX by trying all actions and choosing the one whose resulting state has
the highest MINIMAX value. Figure 6.3 shows the algorithm. It is a recursive algorithm
that proceeds all the way down to ...

## Sections Overview

### Introduction

6
CHAPTER
ADVERSARIAL SEARCH AND GAMES
Inwhichweexploreenvironmentswhereotheragentsareplottingagainstus.
Inthischapterwecovercompetitiveenvironments,inwhichtwoormoreagentshavecon-
Adversarialsearch flicting goals, giving rise to adversarial search problems. Rather than deal with the chaos
of real-world skirmishes, we will concentrate on games, such as chess, Go, and poker. For
AI researchers, the ...

### 6.1 Game Theory

There are at least three stances we can take towards multi-agent environments. The first
stance, appropriate when there are a very large number of agents, is to consider them in the
Economy aggregate as an economy, allowing us to do things like predict that increasing demand will
causepricestorise,withouthavingtopredicttheactionofanyindividualagent.
Second, we could consider adversarial agents as ...

### 6.1.1 Two-player zero-sum games

ThegamesmostcommonlystudiedwithinAI(suchaschessandGo)arewhatgametheorists
call deterministic, two-player, turn-taking, perfect information, zero-sum games. “Perfect Perfectinformation
information”isasynonymfor“fullyobservable,”1 and“zero-sum”meansthatwhatisgood Zero-sumgames
foroneplayerisjustasbadfortheother: thereisno“win-win”outcome. Forgamesweoften
usethetermmoveasasynonymfor“action”andpositio...

### 6.2 Optimal Decisions in Games

MAX wants to find a sequence of actions leading to a win, but MIN has something to say
about it. This means that MAX’s strategy must be a conditional plan—a contingent strategy
specifyingaresponsetoeachof MIN’spossiblemoves. Ingamesthathaveabinaryoutcome
(win or lose), we could use AND–OR search (page 143) to generate the conditional plan. In
fact, for such games, the definition of a winning strat...

### 6.2.1 The minimax search algorithm

Now that we can compute MINIMAX(s), we can turn that into a search algorithm that finds
the best move for MAX by trying all actions and choosing the one whose resulting state has
the highest MINIMAX value. Figure 6.3 shows the algorithm. It is a recursive algorithm
that proceeds all the way down to the leaves of the tree and then backs up the minimax
values through the tree as the recursion unwind...

### 6.2.2 Optimal decisions in multiplayer games

Manypopulargamesallowmorethantwoplayers. Letusexaminehowtoextendtheminimax
idea to multiplayer games. This is straightforward from the technical viewpoint, but raises
someinterestingnewconceptualissues.
First, we need to replace the single value for each node with a vector of values. For
example, in a three-player game with players A, B, andC, a vector (cid:104)v ,v ,v (cid:105) is associated
A B ...

### 6.2.4 Move ordering

Theeffectivenessofalpha–betapruningishighlydependentontheorderinwhichthestates
areexamined. Forexample,inFigure6.5(e)and(f),wecouldnotpruneanysuccessorsofD
atallbecausetheworstsuccessors(fromthepointofviewofMIN)weregeneratedfirst. Ifthe...

### 6.3.1 Evaluation functions

AheuristicevaluationfunctionEVAL(s,p)returnsanestimateoftheexpectedutilityofstate
stoplayer p,justastheheuristicfunctionsofChapter3returnanestimateofthedistanceto
thegoal. Forterminalstates,itmustbethatEVAL(s,p)=UTILITY(s,p)andfornonterminal
states, the evaluation must be somewhere between a loss and a win: UTILITY(loss,p) ≤
EVAL(s,p)≤UTILITY(win,p).
Beyondthoserequirements, whatmakesforagoodevalu...

### 6.3.2 Cutting off search

The next step is to modify ALPHA-BETA-SEARCH so that it will call the heuristic EVAL
function when it is appropriate to cut off the search. We replace the two lines in Figure 6.7
thatmention IS-TERMINALwiththefollowingline:
ifgame.IS-CUTOFF(state,depth)thenreturngame.EVAL(state,player),null
Wealsomustarrangeforsomebookkeepingsothatthecurrentdepthisincrementedoneach
recursive call. The most straigh...

### 6.3.3 Forward pruning

Alpha–betapruningprunesbranchesofthetreethatcanhavenoeffectonthefinalevaluation,
butforwardpruningprunesmovesthatappeartobepoormoves,butmightpossiblybegood Forwardpruning
ones. Thus,thestrategysavescomputationtimeattheriskofmakinganerror. InShannon’s
terms,thisisaTypeBstrategy. Clearly,mosthumanchessplayersdothis,consideringonly
afewmovesfromeachposition(atleastconsciously).
One approach to forwar...

### 6.3.4 Search versus lookup

Somehow it seems like overkill for a chess program to start a game by considering a tree of
a billion game states, only to conclude that it will play pawn to e4 (the most popular first
move). Booksdescribinggoodplayintheopeningandendgameinchesshavebeenavailable
for more than a century (Tattersall, 1911). It is not surprising, therefore, that many game-
playingprogramsusetablelookupratherthansearch...

### 6.4 Monte Carlo Tree Search

The game of Go illustrates two major weaknesses of heuristic alpha–beta tree search: First,
Gohasabranchingfactorthatstartsat361,whichmeansalpha–betasearchwouldbelimited
toonly4or5ply. Second,itisdifficulttodefineagoodevaluationfunctionforGobecause
material value is not a strong indicator and most positions are in flux until the endgame. In
response to these two challenges, modern Go programs have...

### 6.5 Stochastic Games

Stochasticgame Stochastic games bring us a little closer to the unpredictability of real life by including a
randomelement,suchasthethrowingofdice. Backgammonisatypicalstochasticgamethat
combinesluckandskill. InthebackgammonpositionofFigure6.12,Blackhasrolleda6–5
andhasfourpossiblemoves(eachofwhichmovesonepieceforward(clockwise)5positions,
andonepieceforward6positions)....

### 6.5.1 Evaluation functions for games of chance

As with minimax, the obvious approximation to make with expectiminimax is to cut the
searchoffatsomepointandapplyanevaluationfunctiontoeachleaf. Onemightthinkthat
evaluationfunctionsforgamessuchasbackgammonshouldbejustlikeevaluationfunctions
for chess—they just need to give higher values to better positions. But in fact, the presence
ofchancenodesmeansthatonehastobemorecarefulaboutwhatthevaluesmea...

### 6.6 Partially Observable Games

Bobby Fischer declared that “chess is war,” but chess lacks at least one major characteristic
of real wars, namely, partial observability. In the “fog of war,” the whereabouts of enemy
unitsisoftenunknownuntilrevealedbydirectcontact. Asaresult,warfareincludestheuse
ofscoutsandspiestogatherinformationandtheuseofconcealmentandblufftoconfusethe
enemy.
Partiallyobservablegamessharethesecharacteristics...

### 6.6.1 Kriegspiel: Partially observable chess

The rules of Kriegspiel are as follows: White and Black each see a board containing only
theirownpieces. Areferee,whocanseeallthepieces,adjudicatesthegameandperiodically
makes announcements that are heard by both players. First, White proposes to the referee
a move that would be legal if there were no black pieces. If the black pieces prevent the
move,therefereeannounces“illegal,”andWhitekeepsprop...

### 6.6.2 Card games

Card games such as bridge, whist, hearts, and poker feature stochastic partial observability,
wherethemissinginformationisgeneratedbytherandomdealingofcards.
Atfirstsight,itmightseemthatthesecardgamesarejustlikedicegames: thecardsare
dealtrandomlyanddeterminethemovesavailabletoeachplayer,butallthe“dice”arerolled
atthebeginning! Eventhoughthisanalogyturnsouttobeincorrect,itsuggestsanalgorithm:
trea...

### 6.7 Limitations of Game Search Algorithms

Because calculating optimal decisions in complex games is intractable, all algorithms must
makesomeassumptionsandapproximations. Alpha–betasearchusestheheuristicevaluation
function as an approximation, and Monte Carlo search computes an approximate average
over a random selection of playouts. The choice of which algorithm to use depends in part
on the features of each game: when the branching fact...

## Key Entities Mentioned

- Alan Turing
- Charles Babbage
- Claude Shannon
- John McCarthy
- Norbert Wiener
- Richard Bellman

## Algorithms & Concepts

- [[Carlotree
search]]
- [[Beta Tree Search]]
- [[Monte Carlo
search]]
- [[Gametree
search]]
- [[Suppose Black search]]
- [[No algorithm]]
- [[Monte Carlo search]]
- [[Monte Carlo]]
- [[Backpropagation]]
- [[Then search]]

## Cross-References

- Previous: [[Chapter 5 - Constraint Satisfaction Problems]]
- Next: [[Chapter 7 - Logical Agents]]
- Part: Part II: Problem-Solving

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 6. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
