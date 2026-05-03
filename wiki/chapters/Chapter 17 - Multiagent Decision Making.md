---
type: chapter
tags: [aima, chapter, multiagent-decision-making]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 17
---

# Chapter 17 - Multiagent Decision Making

## Summary

Chapter 17 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **multiagent decision making**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 17,169 words and covers foundational concepts, algorithms, and frameworks central to understanding multiagent decision making in the context of artificial intelligence.

## Key Points

- **Introduction**: 17
CHAPTER
MULTIAGENT DECISION MAKING
Inwhichweexaminewhattodowhenmorethanoneagentinhabitstheenvironment....
- **17.1 Properties of Multiagent Environments**: Sofar,wehavelargelyassumedthatonlyoneagenthasbeendoingthesensing,planning,and
acting. Butthisrepresentsahugesimplifyingassumption, whichfailstocapturemanyreal-
world AI settings. In this chapter, therefore, we will consider the issues that arise when an
agentmustmakedecisionsinenvironmentsthatcontai...
- **17.1.1 One decision maker**: The first possibility is that while the environment contains multiple actors, it contains only
one decision maker. In such a case, the decision maker develops plans for the other agents,
and tells them what to do. The assumption that agents will simply do what they are told
is called the benevolent ...
- **17.1.2 Multiple decision makers**: The second possibility is that the other actors in the environment are also decision makers:
they each have preferences and choose and execute their own plan. We call them counter-
Counterparts parts. Inthiscase,wecandistinguishtwofurtherpossibilities.
• The first is that, although there are multipl...
- **17.1.3 Multiagent planning**: For the time being, we will treat the multieffector, multibody, and multiagent settings in the
same way, labeling them generically as multiactor settings, using the generic term actor to Multiactor
cover effectors, bodies, and agents. The goal of this section is to work out how to define Actor
trans...

## Sections Overview

### Introduction

17
CHAPTER
MULTIAGENT DECISION MAKING
Inwhichweexaminewhattodowhenmorethanoneagentinhabitstheenvironment....

### 17.1 Properties of Multiagent Environments

Sofar,wehavelargelyassumedthatonlyoneagenthasbeendoingthesensing,planning,and
acting. Butthisrepresentsahugesimplifyingassumption, whichfailstocapturemanyreal-
world AI settings. In this chapter, therefore, we will consider the issues that arise when an
agentmustmakedecisionsinenvironmentsthatcontainmultipleactors. Suchenvironments
are called multiagent systems, and agents in such a system face a ...

### 17.1.1 One decision maker

The first possibility is that while the environment contains multiple actors, it contains only
one decision maker. In such a case, the decision maker develops plans for the other agents,
and tells them what to do. The assumption that agents will simply do what they are told
is called the benevolent agent assumption. However, even in this setting, plans involving Benevolentagent
assumption
multiple...

### 17.1.2 Multiple decision makers

The second possibility is that the other actors in the environment are also decision makers:
they each have preferences and choose and execute their own plan. We call them counter-
Counterparts parts. Inthiscase,wecandistinguishtwofurtherpossibilities.
• The first is that, although there are multiple decision makers, they are all pursuing a
Commongoal commongoal. Thisisroughlythesituationofworkers...

### 17.1.3 Multiagent planning

For the time being, we will treat the multieffector, multibody, and multiagent settings in the
same way, labeling them generically as multiactor settings, using the generic term actor to Multiactor
cover effectors, bodies, and agents. The goal of this section is to work out how to define Actor
transition models, correct plans, and efficient planning algorithms for the multiactor setting.
Acorrectp...

### 17.1.4 Planning with multiple agents: Cooperation and coordination

Nowletusconsideratruemultiagentsettinginwhicheachagentmakesitsownplan. Tostart
with, let us assume that the goals and knowledge base are shared. One might think that this
reduces to the multibody case—each agent simply computes the joint solution and executes
its own part of that solution. Alas, the “the” in “the joint solution” is misleading. Here is a
secondplanthatalsoachievesthegoal:
PLAN 2: A...

### 17.2 Non-Cooperative Game Theory

Wewillnowintroducethekeyconceptsandanalyticaltechniquesofgametheory—thetheory
that underpins decision making in multiagent environments. Our tour will start with non-
cooperativegametheory....

### 17.2.1 Games with a single move: Normal form games

The first game model we will look at is one in which all players take action simultaneously
and the result of the game is based on the profile of actions that are selected in this way.
(Actually,itisnotcrucialthattheactionstakeplaceatthesametime;whatmattersisthatno
player has knowledge of the other players’ choices.) These games are called normal form
games. Anormalformgameisdefinedbythreecomponen...

### 17.2.2 Social welfare

The main perspective in game theory is that of players within the game, trying to obtain the
best outcomes for themselves that they can. However, it is sometimes instructive to adopt a
differentperspective. Supposeyouwereabenevolent,omnisciententitylookingdownonthe
game, and you were able to choose the outcome. Being benevolent, you want to choose the
best overall outcome—the outcome that would be...

### 17.2.3 Repeated games

Sofar,wehavelookedonlyatgamesthatlastasinglemove. Thesimplestkindofmultiple-
Repeatedgame movegameistherepeatedgame(alsocalledaniteratedgame),inwhichplayersrepeatedly
Stagegame play rounds of a single-move game, called the stage game. A strategy in a repeated game
specifies an action choice for each player at each time step for every possible history of
previouschoicesofplayers.
First,let’slookatt...

### 17.2.4 Sequential games: The extensive form

Inthegeneralcase,agameconsistsofasequenceofturnsthatneednotbeallthesame. Such
gamesarebestrepresentedbyagametree,whichgametheoristscalltheextensiveform. The Extensiveform
tree includes all the same information we saw in Section 6.1: an initial state S , a function
0
PLAYER(s) that tells which player has the move, a function ACTIONS(s) enumerating the
possible actions, a function RESULT(s,a) that d...

### 17.2.5 Uncertain payoffs and assistance games

In Chapter 1 (page 22), we noted the importance of designing AI systems that can operate
underuncertaintyaboutthetruehumanobjective. Chapter15(page543)introducedasimple
modelforuncertaintyaboutone’sownpreferences,usingtheexampleofdurian-flavoredice
cream. By the simple device of adding a new latent variable to the model to represent the
unknownpreferences,togetherwithanappropriatesensormodel(e.g.,...

### 17.3 Cooperative Game Theory

Recall that cooperative games capture decision making scenarios in which agents can form
bindingagreementswithoneanothertocooperate. Theycanthenbenefitfromreceivingextra
valuecomparedtowhattheywouldgetbyactingalone.
Westartbyintroducingamodelforaclassofcooperativegames. Formally,thesegames
are called “cooperative games with transferable utility in characteristic function form.” The
idea of the mod...

### 17.3.1 Coalition structures and outcomes

Coalition It is conventional to refer to a subset of playersC as a coalition. In everyday use the term
“coalition”impliesacollectionofpeoplewithsomecommoncause(suchastheCoalitionto
Stop Gun Violence), but we will refer to any subset of players as a coalition. The set of all
Grandcoalition playersN isknownasthegrandcoalition.
In our model, every player must choose to join exactly one coalition (whi...

### 17.3.2 Strategy in cooperative games

Thebasicassumptionincooperativegametheoryisthatplayerswillmakestrategicdecisions
about who they will cooperate with. Intuitively, players will not desire to work with unpro-
ductiveplayers—theywillnaturallyseekoutplayersthatcollectivelyyieldahighcoalitional
value. Butthesesought-afterplayerswillbedoingtheirownstrategicreasoning. Beforewe
candescribethisreasoning,weneedsomefurtherdefinitions.
Animp...

### 17.3.3 Computation in cooperative games

From a theoretical point of view, we now have a satisfactory solution. But from a computa-
tional point of view, we need to know how to compactly represent cooperative games, and
howtoefficientlycomputesolutionconceptssuchasthecoreandtheShapleyvalue.
Theobviousrepresentationforacharacteristicfunctionwouldbeatablelistingthevalue
ν(C) for all 2n coalitions. This is infeasible for large n. A number o...

### 17.4 Making Collective Decisions

We will now turn from agent design to mechanism design—the problem of designing the
rightgameforacollectionofagentstoplay. Formally,amechanismconsistsof
1. Alanguagefordescribingthesetofallowablestrategiesthatagentsmayadopt.
Center 2. A distinguished agent, called the center, that collects reports of strategy choices from
theagentsinthegame. (Forexample,theauctioneeristhecenterinanauction.)
3. An ...

### 17.4.1 Allocating tasks with the contract net

Contractnet The contract net protocol is probably the oldest and most important multiagent problem-
protocol
solving technique studied in AI. It is a high-level protocol for task sharing. As the name
suggests,thecontractnetwasinspiredfromthewaythatcompaniesmakeuseofcontracts.
The overall contract net protocol has four main phases—see Figure 17.8. The process
starts with an agent identifying the ne...

### 17.4.2 Allocating scarce resources with auctions

One of the most important problems in multiagent systems is that of allocating scarce re-
sources; butwemayaswellsimplysay“allocatingresources,” sinceinpracticemostuseful
Auction resources are scarce in some sense. The auction is the most important mechanism for allo-
cating resources. The simplest setting for an auction is where there is a single resource and
Bidder therearemultiplepossiblebidder...

### 17.4.3 Voting

Thenextclassofmechanismsthatwelookatarevotingprocedures,ofthetypethatareused
forpoliticaldecisionmakingindemocraticsocieties. Thestudyofvotingproceduresderives
Socialchoicetheory fromthedomainofsocialchoicetheory....

### 17.4.4 Bargaining

Bargaining, or negotiation, is another mechanism that is used frequently in everyday life. It
has been studied in game theory since the 1950s and more recently has become a task for
automated agents. Bargaining is used when agents need to reach agreement on a matter of
commoninterest. Theagentsmakeoffers(alsocalledproposalsordeals)toeachotherunder
specificprotocols,andeitheracceptorrejecteachoffer...

## Key Entities Mentioned

- John von Neumann

## Algorithms & Concepts

- [[L algorithm]]
- [[Minimax]]

## Cross-References

- Previous: [[Chapter 16 - Making Complex Decisions]]
- Next: [[Chapter 18 - Probabilistic Programming]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 17. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
