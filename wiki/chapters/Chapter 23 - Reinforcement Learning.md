---
type: chapter
tags: [aima, chapter, reinforcement-learning]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 23
---

# Chapter 23 - Reinforcement Learning

## Summary

Chapter 23 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **reinforcement learning**. This chapter is part of Part V: Learning. The chapter contains approximately 10,938 words and covers foundational concepts, algorithms, and frameworks central to understanding reinforcement learning in the context of artificial intelligence.

## Key Points

- **Introduction**: 23
CHAPTER
REINFORCEMENT LEARNING
In which we see how experiencing rewards and punishments can teach an agent how to
maximizerewardsinthefuture.
Withsupervisedlearning,anagentlearnsbypassivelyobservingexampleinput/output
pairsprovidedbya“teacher.” Inthischapter,wewillseehowagentscanactivelylearnfrom...
- **23.1 Learning from Rewards**: Consider the problem of learning to play chess. Let’s imagine treating this as a supervised
learning problem using the methods of Chapters 19, 21, and 22. The chess-playing agent
functiontakesasinputaboardpositionandreturnsamove,sowetrainthisfunctionbysup-
plying examples of chess positions, each la...
- **23.2 Passive Reinforcement Learning**: We start with the simple case of a fully observable environment with a small number of
actionsandstates,inwhichanagentalreadyhasafixedpolicyπ(s)thatdeterminesitsactions.
TheagentistryingtolearntheutilityfunctionUπ(s)—theexpectedtotaldiscountedreward
Passivelearning ifpolicyπ isexecutedbeginninginsta...
- **23.2.1 Direct utility estimation**: The idea of direct utility estimation is that the utility of a state is defined as the expected Directutility
estimation
total reward from that state onward (called the expected reward-to-go), and that each trial Reward-to-go
provides a sample of this quantity for each state visited. For example, th...
- **23.2.2 Adaptive dynamic programming**: Adaptivedynamic An adaptive dynamic programming (or ADP) agent takes advantage of the constraints
programming
among the utilities of states by learning the transition model that connects them and solv-
ing the corresponding Markov decision process using dynamic programming. For a passive
learning ag...

## Sections Overview

### Introduction

23
CHAPTER
REINFORCEMENT LEARNING
In which we see how experiencing rewards and punishments can teach an agent how to
maximizerewardsinthefuture.
Withsupervisedlearning,anagentlearnsbypassivelyobservingexampleinput/output
pairsprovidedbya“teacher.” Inthischapter,wewillseehowagentscanactivelylearnfrom
theirownexperience,withoutateacher,byconsideringtheirownultimatesuccessorfailure....

### 23.1 Learning from Rewards

Consider the problem of learning to play chess. Let’s imagine treating this as a supervised
learning problem using the methods of Chapters 19, 21, and 22. The chess-playing agent
functiontakesasinputaboardpositionandreturnsamove,sowetrainthisfunctionbysup-
plying examples of chess positions, each labeled with the correct move. Now, it so happens
that we have available databases of several million ...

### 23.2 Passive Reinforcement Learning

We start with the simple case of a fully observable environment with a small number of
actionsandstates,inwhichanagentalreadyhasafixedpolicyπ(s)thatdeterminesitsactions.
TheagentistryingtolearntheutilityfunctionUπ(s)—theexpectedtotaldiscountedreward
Passivelearning ifpolicyπ isexecutedbeginninginstates. Wecallthisapassivelearningagent.
agent
Thepassivelearningtaskissimilartothepolicyevaluationtask...

### 23.2.1 Direct utility estimation

The idea of direct utility estimation is that the utility of a state is defined as the expected Directutility
estimation
total reward from that state onward (called the expected reward-to-go), and that each trial Reward-to-go
provides a sample of this quantity for each state visited. For example, the first of the three
trialsshownearlierprovidesasampletotalrewardof0.76forstate(1,1),twosamplesof0.8...

### 23.2.2 Adaptive dynamic programming

Adaptivedynamic An adaptive dynamic programming (or ADP) agent takes advantage of the constraints
programming
among the utilities of states by learning the transition model that connects them and solv-
ing the corresponding Markov decision process using dynamic programming. For a passive
learning agent, this means plugging the learned transition model P(s(cid:48)|s,π(s)) and the ob-
served rewards...

### 23.2.3 Temporal-difference learning

Solving the underlying MDP as in the preceding section is not the only way to bring the
Bellman equations to bear on the learning problem. Another way is to use the observed
transitions to adjust the utilities of the observed states so that they agree with the constraint
equations. Consider, for example, the transition from (1,3) to (2,3) in the second trial on
page 843. Suppose that as a result o...

### 23.3 Active Reinforcement Learning

A passive learning agent has a fixed policy that determines its behavior. An active learning
agent gets to decide what actions to take. Let us begin with the adaptive dynamic program-
ming(ADP)agentandconsiderhowitcanbemodifiedtotakeadvantageofthisnewfreedom.
First,theagentwillneedtolearnacompletetransitionmodelwithoutcomeprobabilities
forallactions, rather thanjust the modelfor the fixedpolicy. T...

### 23.3.1 Exploration

Figure 23.6 shows the results of one sequence of trials for an ADP agent that follows the
recommendationoftheoptimalpolicyforthelearnedmodelateachstep. Theagentdoesnot
learnthetrueutilitiesorthetrueoptimalpolicy! Whathappensinsteadisthatinthethirdtrial,
it finds a policy that reaches the +1 reward along the lower route via (2,1), (3,1), (3,2), and
(3,3). (SeeFigure23.6(b).) Afterexperimentingwithm...

### 23.3.2 Safe exploration

Sofarwehaveassumedthatanagentisfreetoexploreasitwishes—thatanynegativerewards
serve only to improve its model of the world. That is, if we play a game of chess and lose,
we suffer no damage (except perhaps to our pride), and whatever we learned will make us
a better player in the next game. Similarly, in a simulation environment for a self-driving
car, we could explore the limits of the car’s perf...

### 23.3.3 Temporal-difference Q-learning

NowthatwehaveanactiveADPagent,letusconsiderhowtoconstructanactivetemporal-
difference(TD)learningagent. Themostobviouschangeisthattheagentwillhavetolearn
atransitionmodelsothatitcanchooseanactionbasedonU(s)viaone-steplook-ahead. The
model acquisition problem for the TD agent is identical to that for the ADP agent, and the...

### 23.4 Generalization in Reinforcement Learning

Sofar,wehaveassumedthatutilityfunctionsandQ-functionsarerepresentedintabularform
withoneoutputvalueforeachstate. Thisworksforstatespaceswithuptoabout106 states,
whichismorethanenoughforourtoytwo-dimensionalgridenvironments. Butinreal-world
environmentswithmanymorestates,convergencewillbetooslow. Backgammonissimpler
thanmostreal-worldapplications,yetithasabout1020states. Wecannoteasilyvisitthemall
...

### 23.4.1 Approximating direct utility estimation

Themethodofdirectutilityestimation(Section23.2)generatestrajectoriesinthestatespace
andextracts,foreachstate,thesumofrewardsreceivedfromthatstateonwarduntiltermina-
tion. Thestateandthesumofrewardsreceivedconstituteatrainingexampleforasupervised
learningalgorithm. Forexample,supposewerepresenttheutilitiesforthe4×3worldusing
a simple linear function, where the features of the squares are just their...

### 23.4.2 Approximating temporal-difference learning

We can apply these ideas equally well to temporal-difference learners. All we need do is
adjusttheparameterstotrytoreducethetemporaldifferencebetweensuccessivestates. The
new versions of the TD and Q-learning equations (23.3 on page 846 and 23.7 on page 853)
aregivenby
∂Uˆ (s)
θ ←θ +α[R(s,a,s(cid:48))+γUˆ (s(cid:48))−Uˆ (s)] θ (23.11)
i i θ θ
∂θ
i
forutilitiesand
∂Qˆ (s,a)
θ ←θ +α[R(s,a,s(cid:48))...

### 23.4.3 Deep reinforcement learning

There are two reasons why we need to go beyond linear function approximators: first, there
may be no good linear function that comes close to approximating the utility function or
the Q-function; second, we may not be able to invent the necessary features, particularly in
new domains. If you think about it, these are really the same reason: it is always possible
to representU or Q as linear combin...

### 23.4.4 Reward shaping

As noted in the introduction to this chapter, real-world environments may have very sparse
rewards: manyprimitiveactionsarerequiredtoachieveanynonzeroreward. Forexample,a
soccer-playing robot might send a hundred thousand motor control commands to its various
jointsbeforeconcedingagoal. Nowithastoworkoutwhatitdidwrong. Thetechnicalterm
Creditassignment for this is the credit assignment problem. Ot...

### 23.4.5 Hierarchical reinforcement learning

Anotherwaytocopewithverylongactionsequencesistobreakthemupintoafewsmaller
pieces, and then break those into smaller pieces still, and so on until the action sequences
areshortenoughtomakelearningeasy. Thisapproachiscalledhierarchicalreinforcement
Hierarchical
reinforcement learning (HRL), and it has much in common with the HTN planning methods described
learning
in Chapter 11. For example, scoring...

### 23.5 Policy Search

The final approach we will consider for reinforcement learning problems is called policy
search. In some ways, policy search is the simplest of all the methods in this chapter: the Policysearch
ideaistokeeptwiddlingthepolicyaslongasitsperformanceimproves,thenstop.
Let us begin with the policies themselves. Remember that a policy π is a function that
mapsstatestoactions. Weareinterestedprimarilyinp...

### 23.6 Apprenticeship and Inverse Reinforcement Learning

Some domains are so complex that it is difficult to define a reward function for use in rein-
forcementlearning. Exactlywhatdowewantourself-drivingcartodo? Certainlyitshould
not take too long to get to the destination, but it should not drive so fast as to incur undue
risk or to get speeding tickets. It should conserve fuel/energy. It should avoid jostling or
accelerating the passengers too much, ...

### 23.7 Applications of Reinforcement Learning

We now turn to applications of reinforcement learning. These include game playing, where
thetransitionmodelisknownandthegoalistolearntheutilityfunction,androbotics,where
themodelisinitiallyunknown....

### 23.7.1 Applications in game playing

InChapter1wedescribedArthurSamuel’searlyworkonreinforcementlearningforcheck-
ers,whichbeganin1952. Afewdecadespassedbeforethechallengewastakenupagain,this
timebyGerryTesauroinhisworkonbackgammon. Tesauro’sfirstattempt(1990)wasasys-
temcalled NEUROGAMMON. Theapproachwasaninterestingvariantonimitationlearning.
Theinputwasasetof400gamesplayedbyTesauroagainsthimself. Ratherthanlearnapol-...

### 23.7.2 Application to robot control

The setup for the famous cart–pole balancing problem, also known as the inverted pendu- Cart–pole
lum, is shown in Figure 23.9(a). The problem is to keep the pole roughly upright (θ≈90◦) Invertedpendulum
byapplyingforcestomovethecartrightorleft,whilekeepingthepositionxwithinthelimits
ofthetrack. Severalthousandpapersinreinforcementlearningandcontroltheoryhavebeen
publishedonthisseeminglysimpleprob...

## Key Entities Mentioned

- Alan Turing

## Algorithms & Concepts

- [[Policy search]]
- [[Policy Search]]
- [[L algorithm]]
- [[This algorithm]]
- [[Wehavealotofpowerful
algorithm]]
- [[The algorithm]]
- [[P algorithm]]
- [[S algorithm]]

## Cross-References

- Previous: [[Chapter 22 - Deep Learning]]
- Next: [[Chapter 24 - Natural Language Processing]]
- Part: Part V: Learning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 23. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
