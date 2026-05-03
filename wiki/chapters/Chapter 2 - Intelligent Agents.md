---
type: chapter
tags: [aima, chapter, intelligent-agents]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 2
---

# Chapter 2 - Intelligent Agents

## Summary

Chapter 2 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **intelligent agents**. This chapter is part of Part I: Artificial Intelligence. The chapter contains approximately 7,630 words and covers foundational concepts, algorithms, and frameworks central to understanding intelligent agents in the context of artificial intelligence.

## Key Points

- **Introduction**: 2
CHAPTER
INTELLIGENT AGENTS
Inwhichwediscussthenatureofagents,perfectorotherwise,thediversityofenvironments,
andtheresultingmenagerieofagenttypes.
Chapter 1 identified the concept of rational agents as central to our approach to artificial
intelligence. Inthischapter,wemakethisnotionmoreconcrete. W...
- **2.1 Agents and Environments**: Environment Anagentisanythingthatcanbeviewedasperceivingitsenvironmentthroughsensorsand
Sensor actinguponthatenvironmentthroughactuators. ThissimpleideaisillustratedinFigure2.1.
Actuator A human agent has eyes, ears, and other organs for sensors and hands, legs, vocal tract,
and so on for actuators....
- **2.2 Good Behavior: The Concept of Rationality**: A rational agent is one that does the right thing. Obviously, doing the right thing is better Rationalagent
thandoingthewrongthing,butwhatdoesitmeantodotherightthing?...
- **2.2.1 Performance measures**: Moral philosophy has developed several different notions of the “right thing,” but AI has
generallystucktoonenotioncalledconsequentialism: weevaluateanagent’sbehaviorbyits Consequentialism
consequences. Whenanagentisplunkeddowninanenvironment,itgeneratesasequenceof
actionsaccordingtotheperceptsitrec...
- **2.2.2 Rationality**: Whatisrationalatanygiventimedependsonfourthings:
• Theperformancemeasurethatdefinesthecriterionofsuccess.
• Theagent’spriorknowledgeoftheenvironment.
• Theactionsthattheagentcanperform.
• Theagent’sperceptsequencetodate.
Definitionofa (cid:73) Thisleadstoadefinitionofarationalagent:
rationalagent
Fo...

## Sections Overview

### Introduction

2
CHAPTER
INTELLIGENT AGENTS
Inwhichwediscussthenatureofagents,perfectorotherwise,thediversityofenvironments,
andtheresultingmenagerieofagenttypes.
Chapter 1 identified the concept of rational agents as central to our approach to artificial
intelligence. Inthischapter,wemakethisnotionmoreconcrete. Wewillseethattheconcept
ofrationalitycanbeappliedtoawidevarietyofagentsoperatinginanyimaginableenviro...

### 2.1 Agents and Environments

Environment Anagentisanythingthatcanbeviewedasperceivingitsenvironmentthroughsensorsand
Sensor actinguponthatenvironmentthroughactuators. ThissimpleideaisillustratedinFigure2.1.
Actuator A human agent has eyes, ears, and other organs for sensors and hands, legs, vocal tract,
and so on for actuators. A robotic agent might have cameras and infrared range finders for
sensors and various motors for ac...

### 2.2 Good Behavior: The Concept of Rationality

A rational agent is one that does the right thing. Obviously, doing the right thing is better Rationalagent
thandoingthewrongthing,butwhatdoesitmeantodotherightthing?...

### 2.2.1 Performance measures

Moral philosophy has developed several different notions of the “right thing,” but AI has
generallystucktoonenotioncalledconsequentialism: weevaluateanagent’sbehaviorbyits Consequentialism
consequences. Whenanagentisplunkeddowninanenvironment,itgeneratesasequenceof
actionsaccordingtotheperceptsitreceives. Thissequenceofactionscausestheenvironment
togothroughasequenceofstates. Ifthesequenceisdesira...

### 2.2.2 Rationality

Whatisrationalatanygiventimedependsonfourthings:
• Theperformancemeasurethatdefinesthecriterionofsuccess.
• Theagent’spriorknowledgeoftheenvironment.
• Theactionsthattheagentcanperform.
• Theagent’sperceptsequencetodate.
Definitionofa (cid:73) Thisleadstoadefinitionofarationalagent:
rationalagent
For each possible percept sequence, a rational agent should select an action that is ex-
pectedtomaxim...

### 2.2.3 Omniscience, learning, and autonomy

Omniscience We need to be careful to distinguish between rationality and omniscience. An omniscient
agent knows the actual outcome of its actions and can act accordingly; but omniscience is
impossible in reality. Consider the following example: I am walking along the Champs
Elyse´es one day and I see an old friend across the street. There is no traffic nearby and I’m...

### 2.3 The Nature of Environments

Now that we have a definition of rationality, we are almost ready to think about building
Taskenvironment rational agents. First, however, we must think about task environments, which are essen-
tiallythe“problems”towhichrationalagentsarethe“solutions.” Webeginbyshowinghow
to specify a task environment, illustrating the process with a number of examples. We then
showthattaskenvironmentscomeinavari...

### 2.3.1 Specifying the task environment

In our discussion of the rationality of the simple vacuum-cleaner agent, we had to specify
theperformancemeasure,theenvironment,andtheagent’sactuatorsandsensors. Wegroup
alltheseundertheheadingofthetaskenvironment. Fortheacronymicallyminded,wecall
PEAS thisthePEAS(Performance,Environment,Actuators,Sensors)description. Indesigningan
agent,thefirststepmustalwaysbetospecifythetaskenvironmentasfullyas...

### 2.3.2 Properties of task environments

The range of task environments that might arise in AI is obviously vast. We can, however,
identify a fairly small number of dimensions along which task environments can be catego-
rized. These dimensions determine, to a large extent, the appropriate agent design and the
applicability of each of the principal families of techniques for agent implementation. First
welistthedimensions,thenweanalyzese...

### 2.4 The Structure of Agents

Sofarwehavetalkedaboutagentsbydescribingbehavior—theactionthatisperformedafter
anygivensequenceofpercepts. Nowwemustbitethebulletandtalkabouthowtheinsides
work. The job of AI is to design an agent program that implements the agent function— Agentprogram
the mapping from percepts to actions. We assume this program will run on some sort of
computingdevicewithphysicalsensorsandactuators—wecallthisthe...

### 2.4.1 Agent programs

The agent programs that we design in this book all have the same skeleton: they take the
current percept as input from the sensors and return an action to the actuators.5 Notice the
differencebetweentheagentprogram,whichtakesthecurrentperceptasinput,andtheagent
function, whichmaydependontheentirepercepthistory. Theagentprogramhasnochoice
buttotakejustthecurrentperceptasinputbecausenothingmoreisava...

### 2.4.2 Simple reflex agents

Thesimplestkindofagentisthesimplereflexagent. Theseagentsselectactionsonthebasis Simplereflexagent
ofthecurrentpercept,ignoringtherestofthepercepthistory. Forexample,thevacuumagent
whoseagent functionistabulatedin Figure2.3isa simplereflexagent, becauseitsdecision
is based only on the current location and on whether that location contains dirt. An agent
programforthisagentisshowninFigure2.8.
Notic...

### 2.4.3 Model-based reflex agents

The most effective way to handle partial observability is for the agent to keep track of the
part of the world it can’t see now. That is, the agent should maintain some sort of internal
statethatdependsonthepercepthistoryandtherebyreflectsatleastsomeoftheunobserved Internalstate
aspectsofthecurrentstate. Forthebrakingproblem,theinternalstateisnottooextensive—
justthe previousframe fromthe camera, ...

### 2.4.4 Goal-based agents

Knowingsomethingaboutthecurrentstateoftheenvironmentisnotalwaysenoughtodecide
what to do. For example, at a road junction, the taxi can turn left, turn right, or go straight
on. The correct decision depends on where the taxi is trying to get to. In other words,
as well as a current state description, the agent needs some sort of goal information that Goal
describes situations that are desirable—fo...

### 2.4.5 Utility-based agents

Goals alone are not enough to generate high-quality behavior in most environments. For
example, many action sequences will get the taxi to its destination (thereby achieving the
goal),butsomearequicker,safer,morereliable,orcheaperthanothers. Goalsjustprovidea
crudebinarydistinctionbetween“happy”and“unhappy”states. Amoregeneralperformance
measureshouldallowacomparisonofdifferentworldstatesaccording...

### 2.4.6 Learning agents

We have described agent programs with various methods for selecting actions. We have
not, so far, explained how the agent programs come into being. In his famous early paper,
Turing (1950) considers the idea of actually programming his intelligent machines by hand.
Heestimateshowmuchworkthismighttakeandconcludes,“Somemoreexpeditiousmethod
seems desirable.” The method he proposes is to build learni...

### 2.4.7 How the components of agent programs work

Wehavedescribedagentprograms(inveryhigh-levelterms)asconsistingofvariouscompo-
nents,whosefunctionitistoanswerquestionssuchas: “Whatistheworldlikenow?” “What
action should I do now?” “What do my actions do?” The next question for a student of AI
is, “How on Earth do these components work?” It takes about a thousand pages to begin to
answerthatquestionproperly, butherewewanttodrawthereader’sattenti...

## Key Entities Mentioned

- Aristotle
- Norbert Wiener

## Algorithms & Concepts

- To be identified on detailed review

## Cross-References

- Previous: [[Chapter 1 - Introduction]]
- Next: [[Chapter 3 - Solving Problems by Searching]]
- Part: Part I: Artificial Intelligence

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 2. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
