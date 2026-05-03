---
type: chapter
tags: [aima, chapter, making-complex-decisions]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 16
---

# Chapter 16 - Making Complex Decisions

## Summary

Chapter 16 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **making complex decisions**. This chapter is part of Part IV: Uncertain Knowledge and Reasoning. The chapter contains approximately 10,609 words and covers foundational concepts, algorithms, and frameworks central to understanding making complex decisions in the context of artificial intelligence.

## Key Points

- **Introduction**: 16
CHAPTER
MAKING COMPLEX DECISIONS
Inwhichweexaminemethodsfordecidingwhattodotoday,giventhatwemayfaceanother
decisiontomorrow.
Inthischapter,weaddressthecomputationalissuesinvolvedinmakingdecisionsinastochas-
ticenvironment. WhereasChapter15wasconcernedwithone-shotorepisodicdecisionprob-
lems, in w...
- **16.1 Sequential Decision Problems**: Supposethatanagentissituatedinthe4×3environmentshowninFigure16.1(a). Beginning
inthestartstate,itmustchooseanactionateachtimestep. Theinteractionwiththeenviron-
ment terminates when the agent reaches one of the goal states, marked +1 or –1. Just as for
search problems, the actions available to the a...
- **16.1.1 Utilities over time**: IntheMDPexampleinFigure16.1,theperformanceoftheagentwasmeasuredbyasumof
rewardsforthetransitionsexperienced. Thischoiceofperformancemeasureisnotarbitrary,
but it is not the only possibility for the utility function2 on environment histories, which we
writeasU ([s ,a ,s ,a ...,s ]).
h 0 0 1 1 n
2 Int...
- **16.1.2 Optimal policies and the utilities of states**: Having decided that the utility of a given history is the sum of discounted rewards, we can
compare policies by comparing the expected utilities obtained when executing them. We
assumetheagentisinsomeinitialstatesanddefineS (arandomvariable)tobethestatethe
t
agentreachesattimet whenexecutingaparticu...
- **16.1.3 Reward scales**: Chapter15notedthatthescaleofutilitiesisarbitrary: anaffinetransformationleavestheop-
timaldecisionunchanged. WecanreplaceU(s)byU(cid:48)(s)=mU(s)+bwheremandbareany
constantssuchthatm>0. Itiseasytosee,fromthedefinitionofutilitiesasdiscountedsums
ofrewards, thatasimilartransformationofrewardswillleave...

## Sections Overview

### Introduction

16
CHAPTER
MAKING COMPLEX DECISIONS
Inwhichweexaminemethodsfordecidingwhattodotoday,giventhatwemayfaceanother
decisiontomorrow.
Inthischapter,weaddressthecomputationalissuesinvolvedinmakingdecisionsinastochas-
ticenvironment. WhereasChapter15wasconcernedwithone-shotorepisodicdecisionprob-
lems, in which the utility of each action’s outcome was well known, we are concerned here
Sequentialdecision w...

### 16.1 Sequential Decision Problems

Supposethatanagentissituatedinthe4×3environmentshowninFigure16.1(a). Beginning
inthestartstate,itmustchooseanactionateachtimestep. Theinteractionwiththeenviron-
ment terminates when the agent reaches one of the goal states, marked +1 or –1. Just as for
search problems, the actions available to the agent in each state are given by ACTIONS(s),
sometimes abbreviated to A(s); in the 4×3 environment, t...

### 16.1.1 Utilities over time

IntheMDPexampleinFigure16.1,theperformanceoftheagentwasmeasuredbyasumof
rewardsforthetransitionsexperienced. Thischoiceofperformancemeasureisnotarbitrary,
but it is not the only possibility for the utility function2 on environment histories, which we
writeasU ([s ,a ,s ,a ...,s ]).
h 0 0 1 1 n
2 InthischapterweuseU fortheutilityfunction(tobeconsistentwiththerestofthebook),butmanyworks
aboutMDPsuse...

### 16.1.2 Optimal policies and the utilities of states

Having decided that the utility of a given history is the sum of discounted rewards, we can
compare policies by comparing the expected utilities obtained when executing them. We
assumetheagentisinsomeinitialstatesanddefineS (arandomvariable)tobethestatethe
t
agentreachesattimet whenexecutingaparticularpolicyπ. (Obviously,S =s,thestatethe
0
agent is in now.) The probability distribution over state ...

### 16.1.3 Reward scales

Chapter15notedthatthescaleofutilitiesisarbitrary: anaffinetransformationleavestheop-
timaldecisionunchanged. WecanreplaceU(s)byU(cid:48)(s)=mU(s)+bwheremandbareany
constantssuchthatm>0. Itiseasytosee,fromthedefinitionofutilitiesasdiscountedsums
ofrewards, thatasimilartransformationofrewardswillleavetheoptimalpolicyunchanged
inanMDP:
R(cid:48)(s,a,s(cid:48))=mR(s,a,s(cid:48))+b.
Itturnsout,however,...

### 16.1.4 Representing MDPs

The simplest way to represent P(s(cid:48)|s,a) and R(s,a,s(cid:48)) is with big, three-dimensional tables
of size |S|2|A|. This is fine for small problems such as the 4×3 world, for which the tables
have112×4=484entrieseach. Insomecases, thetablesaresparse—mostentriesarezero
because each state s can transition to only a bounded number of states s(cid:48)—which means the
tablesareofsizeO(|S(cid:107...

### 16.2 Algorithms for MDPs

Inthissection,wepresentfourdifferentalgorithmsforsolvingMDPs. Thefirstthree,value
iteration, policy iteration, and linear programming, generate exact solutions offline. The
MonteCarlo fourthisafamilyofonlineapproximatealgorithmsthatincludesMonteCarloplanning.
planning...

### 16.2.1 Value Iteration

Valueiteration TheBellmanequation(Equation(16.5))isthebasisofthevalueiterationalgorithmforsolv-
ing MDPs. If there are n possible states, then there are n Bellman equations, one for each...

### 16.2.2 Policy iteration

In the previous section, we observed that it is possible to get an optimal policy even when
the utility function estimate is inaccurate. If one action is clearly better than all others, then
the exact magnitude of the utilities on the states involved need not be precise. This insight
Policyiteration suggestsanalternativewaytofindoptimalpolicies. Thepolicyiterationalgorithmalternates
thefollowing t...

### 16.2.3 Linear programming

Linear programming or LP, which was mentioned briefly in Chapter 4 (page 139), is a
general approach for formulating constrained optimization problems, and there are many
industrial-strength LP solvers available. Given that the Bellman equations involve a lot of
sumsandmaxes, itisperhapsnotsurprisingthatsolvinganMDPcanbereducedtosolving
asuitablyformulatedlinearprogram.
Thebasicideaoftheformulatio...

### 16.2.4 Online algorithms for MDPs

Valueiterationandpolicyiterationareofflinealgorithms: liketheA∗ algorithminChapter3,
they generate an optimal solution for the problem, which can then be executed by a simple
agent. For sufficiently large MDPs, such as the Tetris MDP with 1062 states, exact offline
solution,evenbyapolynomial-timealgorithm,isnotpossible. Severaltechniqueshavebeen
developedforapproximateofflinesolutionofMDPs;thesear...

### 16.3 Bandit Problems

In Las Vegas, a one-armed bandit is a slot machine. A gambler can insert a coin, pull the
lever, and collect the winnings (if any). An n-armed bandit has n levers. Behind each N-armedbandit
leverisafixedbutunknownprobabilitydistributionofwinnings;eachpullsamplesfromthat
unknowndistribution.
Thegamblermustchoosewhichlevertoplayoneachsuccessivecoin—theonethathas
paidoffbest,ormaybeonethathasnotbeent...

### 16.3.1 Calculating the Gittins index

To get more of a feel for the index, let’s calculate the value of the numerator, denominator,
andratioinEquation(16.15)fordifferentpossiblestoppingtimesonthedeterministicreward
sequence0,2,0,7.2,0,0,0,...:
T 1 2 3 4 5 6
R 0 2 0 7.2 0 0
t
∑γtR
t
0.0 1.0 1.0 1.9 1.9 1.9
∑γt 1.0 1.5 1.75 1.875 1.9375 1.9687
ratio 0.0 0.6667 0.5714 1.0133 0.9806 0.9651
Clearly, the ratio will decrease from here on, be...

### 16.3.2 The Bernoulli bandit

Bernoullibandit Perhaps the simplest and best-known instance of a bandit problem is the Bernoulli bandit,
where each arm M produces a reward of 0 or 1 with a fixed but unknown probability µ.
i i
The state of arm M is defined by s and f, the counts of successes (1s) and failures (0s) so
i i i
farforthatarm; thetransitionprobabilitypredictsthenextoutcometobe1withprobability
(s)/(s + f) and 0 with pr...

### 16.3.3 Approximately optimal bandit policies

CalculatingGittinsindicesformorerealisticproblemsisrarelyeasy. Fortunately,thegeneral
properties observed in the preceding section—namely, the desirability of some combination
of estimated value and uncertainty—lend themselves to the creation of simple policies that
turnouttobe“nearlyasgood”asoptimalpolicies.
ThefirstclassofmethodsusestheupperconfidenceboundorUCBheuristic,previously Upperconfidenc...

### 16.3.4 Non-indexable variants

Bandit problems were motivated in part by the task of testing new medical treatments on
seriouslyillpatients. Forthistask,thegoalofmaximizingthetotalnumberofsuccessesover
timeclearlymakessense: eachsuccessfultestmeansalifesaved,eachfailurealifelost.
If we change the assumptions slightly, however, a different problem emerges. Suppose
that, instead of determining the best medical treatment for each ...

### 16.4 Partially Observable MDPs

ThedescriptionofMarkovdecisionprocessesinSection16.1assumedthattheenvironment
was fully observable. With this assumption, the agent always knows which state it is in.
This,combinedwiththeMarkovassumptionforthetransitionmodel,meansthattheoptimal
policydependsonlyonthecurrentstate.
Whentheenvironmentisonlypartiallyobservable,thesituationis,onemightsay,much
less clear. The agent does not necessarily ...

### 16.4.1 Definition of POMDPs

To get a handle on POMDPs, we must first define them properly. A POMDP has the same
elements as an MDP—the transition model P(s(cid:48)|s,a), actions A(s), and reward function
R(s,a,s(cid:48))—but, like the partially observable search problems of Section 4.4, it also has a
sensor model P(e|s). Here, as in Chapter 14, the sensor model specifies the probability of
perceivingevidenceeinstates.5 Forex...

### 16.5 Algorithms for Solving POMDPs

We have shown how to reduce POMDPs to MDPs, but the MDPs we obtain have a contin-
uous (and usually high-dimensional) state space. This means we will have to redesign the
dynamic programming algorithms from Sections 16.2.1 and 16.2.2, which assumed a finite
state space and a finite number of actions. Here we describe a value iteration algorithm de-
signedspecificallyforPOMDPs,followedbyanonlinedec...

### 16.5.1 Value iteration for POMDPs

Section16.2.1describedavalueiterationalgorithmthatcomputedoneutilityvalueforeach
state. With infinitely many belief states, we need to be more creative. Consider an optimal
policyπ∗ anditsapplicationinaspecificbeliefstateb: thepolicygeneratesanaction, then,
foreachsubsequentpercept,thebeliefstateisupdatedandanewactionisgenerated,andso
on. Forthisspecificb,therefore,thepolicyisexactlyequivalenttoac...

### 16.5.2 Online algorithms for POMDPs

The basic design for an online POMDP agent is straightforward: it starts with some prior
belief state; it chooses an action based on some deliberation process centered on its current
beliefstate;afteracting,itreceivesanobservationandupdatesitsbeliefstateusingafiltering
algorithm;andtheprocessrepeats.
One obvious choice for the deliberation process is the expectimax algorithm from Sec-
tion 16.2.4,...

## Key Entities Mentioned

- Richard Bellman

## Algorithms & Concepts

- [[Online algorithm]]
- [[Monte Carlo]]
- [[X
algorithm]]
- [[Theresulting
Modifiedpolicy algorithm]]
- [[Witness algorithm]]
- [[T algorithm]]
- [[P algorithm]]
- [[X algorithm]]
- [[Value Iteration]]

## Cross-References

- Previous: [[Chapter 15 - Making Simple Decisions]]
- Next: [[Chapter 17 - Multiagent Decision Making]]
- Part: Part IV: Uncertain Knowledge and Reasoning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 16. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
