---
type: chapter
tags: [aima, chapter, introduction]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 1
---

# Chapter 1 - Introduction

## Summary

Chapter 1 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **introduction**. This chapter is part of Part I: Artificial Intelligence. The chapter contains approximately 10,677 words and covers foundational concepts, algorithms, and frameworks central to understanding introduction in the context of artificial intelligence.

## Key Points

- **Introduction**: 1
CHAPTER
INTRODUCTION
In which we try to explain why we consider artificial intelligence to be a subject most
worthyofstudy,andinwhichwetrytodecidewhatexactlyitis,thisbeingagoodthingto
decidebeforeembarking.
We call ourselves Homo sapiens—man the wise—because our intelligence is so important Intell...
- **1.1.1 Acting humanly: The Turing test approach**: Turingtest TheTuringtest,proposedbyAlanTuring(1950),wasdesignedasathoughtexperimentthat
wouldsidestepthephilosophicalvaguenessofthequestion“Canamachinethink?” Acom-
puterpassesthetestifahumaninterrogator,afterposingsomewrittenquestions,cannottell
whetherthewrittenresponsescomefromapersonorfromacompu...
- **1.1.2 Thinking humanly: The cognitive modeling approach**: To say that a program thinks like a human, we must know how humans think. We can learn
abouthumanthoughtinthreeways:
Introspection • introspection—tryingtocatchourownthoughtsastheygoby;
Psychological • psychologicalexperiments—observingapersoninaction;
experiment
Brainimaging • brainimaging—observin...
- **1.1.4 Acting rationally: The rational agent approach**: An agent is just something that acts (agent comes from the Latin agere, to do). Of course, Agent
allcomputerprogramsdosomething, butcomputeragentsareexpectedtodomore: operate
autonomously, perceive their environment, persist over a prolonged time period, adapt to...
- **1.1.5 Beneficial machines**: The standard model has been a useful guide for AI research since its inception, but it is
probablynottherightmodelinthelongrun. Thereasonisthatthestandardmodelassumes
thatwewillsupplyafullyspecifiedobjectivetothemachine.
Foranartificiallydefinedtasksuchaschessorshortest-pathcomputation,thetaskcomes
...

## Sections Overview

### Introduction

1
CHAPTER
INTRODUCTION
In which we try to explain why we consider artificial intelligence to be a subject most
worthyofstudy,andinwhichwetrytodecidewhatexactlyitis,thisbeingagoodthingto
decidebeforeembarking.
We call ourselves Homo sapiens—man the wise—because our intelligence is so important Intelligence
to us. For thousands of years, we have tried to understand how we think and act—that is,
howo...

### 1.1.1 Acting humanly: The Turing test approach

Turingtest TheTuringtest,proposedbyAlanTuring(1950),wasdesignedasathoughtexperimentthat
wouldsidestepthephilosophicalvaguenessofthequestion“Canamachinethink?” Acom-
puterpassesthetestifahumaninterrogator,afterposingsomewrittenquestions,cannottell
whetherthewrittenresponsescomefromapersonorfromacomputer. Chapter28discusses
the details of the test and whether a computer would really be intelligent i...

### 1.1.2 Thinking humanly: The cognitive modeling approach

To say that a program thinks like a human, we must know how humans think. We can learn
abouthumanthoughtinthreeways:
Introspection • introspection—tryingtocatchourownthoughtsastheygoby;
Psychological • psychologicalexperiments—observingapersoninaction;
experiment
Brainimaging • brainimaging—observingthebraininaction.
Once we have a sufficiently precise theory of the mind, it becomes possible to ex...

### 1.1.4 Acting rationally: The rational agent approach

An agent is just something that acts (agent comes from the Latin agere, to do). Of course, Agent
allcomputerprogramsdosomething, butcomputeragentsareexpectedtodomore: operate
autonomously, perceive their environment, persist over a prolonged time period, adapt to...

### 1.1.5 Beneficial machines

The standard model has been a useful guide for AI research since its inception, but it is
probablynottherightmodelinthelongrun. Thereasonisthatthestandardmodelassumes
thatwewillsupplyafullyspecifiedobjectivetothemachine.
Foranartificiallydefinedtasksuchaschessorshortest-pathcomputation,thetaskcomes
with an objective built in—so the standard model is applicable. As we move into the real
world, howe...

### 1.2 The Foundations of Artificial Intelligence

Inthissection,weprovideabriefhistoryofthedisciplinesthatcontributedideas,viewpoints,
and techniques to AI. Like any history, this one concentrates on a small number of people,
events,andideasandignoresothersthatalsowereimportant. Weorganizethehistoryaround
aseriesofquestions. Wecertainlywouldnotwishtogivetheimpressionthatthesequestions
aretheonlyonesthedisciplinesaddressorthatthedisciplineshaveall...

### 1.2.1 Philosophy

• Canformalrulesbeusedtodrawvalidconclusions?
• Howdoesthemindarisefromaphysicalbrain?
• Wheredoesknowledgecomefrom?
• Howdoesknowledgeleadtoaction?
Aristotle(384–322BCE)wasthefirsttoformulateaprecisesetoflawsgoverningtherational
partofthemind. Hedevelopedaninformalsystemofsyllogismsforproperreasoning,which
inprincipleallowedonetogenerateconclusionsmechanically,giveninitialpremises.
Ramon Llull (c...

### 1.2.2 Mathematics

• Whataretheformalrulestodrawvalidconclusions?
• Whatcanbecomputed?
• Howdowereasonwithuncertaininformation?
PhilosophersstakedoutsomeofthefundamentalideasofAI,buttheleaptoaformalscience
required the mathematization of logic and probability and the introduction of a new branch
ofmathematics: computation.
Formallogic TheideaofformallogiccanbetracedbacktothephilosophersofancientGreece,India,
and Chi...

### 1.2.3 Economics

• Howshouldwemakedecisionsinaccordancewithourpreferences?
• Howshouldwedothiswhenothersmaynotgoalong?
• Howshouldwedothiswhenthepayoffmaybefarinthefuture?...

### 1.2.4 Neuroscience

• Howdobrainsprocessinformation?
Neuroscience is the study of the nervous system, particularly the brain. Although the exact Neuroscience
wayinwhichthebrainenablesthoughtisoneofthegreatmysteriesofscience,thefactthatit
doesenablethoughthasbeenappreciatedforthousandsofyearsbecauseoftheevidencethat
strongblowstotheheadcanleadtomentalincapacitation. Ithasalsolongbeenknownthat
humanbrainsaresomehowdiff...

### 1.2.5 Psychology

• Howdohumansandanimalsthinkandact?
The origins of scientific psychology are usually traced to the work of the German physi-
cist Hermann von Helmholtz (1821–1894) and his student Wilhelm Wundt (1832–1920).
Helmholtz applied the scientific method to the study of human vision, and his Handbook of
PhysiologicalOpticshasbeendescribedas“thesinglemostimportanttreatiseonthephysics
andphysiologyofhumanvi...

### 1.2.6 Computer engineering

• Howcanwebuildanefficientcomputer?
The modern digital electronic computer was invented independently and almost simultane-
ously by scientists in three countries embattled in World War II. The first operational com-
puter was the electromechanical Heath Robinson,9 built in 1943 by Alan Turing’s team for
a single purpose: deciphering German messages. In 1943, the same group developed the
Colossus,...

### 1.2.7 Control theory and cybernetics

• Howcanartifactsoperateundertheirowncontrol?
Ktesibios of Alexandria (c. 250 BCE) built the first self-controlling machine: a water clock
with a regulator that maintained a constant flow rate. This invention changed the definition
of what an artifact could do. Previously, only living things could modify their behavior in
response tochanges in the environment. Otherexamples of self-regulatingfeedb...

### 1.2.8 Linguistics

• Howdoeslanguagerelatetothought?
In 1957, B. F. Skinner published Verbal Behavior. This was a comprehensive, detailed ac-
count of the behaviorist approach to language learning, written by the foremost expert in
the field. But curiously, a review of the book became as well known as the book itself, and
served to almost kill off interest in behaviorism. The author of the review was the linguist
No...

### 1.3 The History of Artificial Intelligence

OnequickwaytosummarizethemilestonesinAIhistoryistolisttheTuringAwardwinners:
Marvin Minsky (1969) and John McCarthy (1971) for defining the foundations of the field
basedonrepresentationandreasoning;AllenNewellandHerbertSimon(1975)forsymbolic
modelsofproblemsolvingandhumancognition;EdFeigenbaumandRajReddy(1994)for
developingexpertsystemsthatencodehumanknowledgetosolvereal-worldproblems;Judea
Pearl...

### 1.4 The State of the Art

StanfordUniversity’sOneHundredYearStudyonAI(alsoknownasAI100)convenespanels
of experts to provide reports on the state of the art in AI. Their 2016 report (Stone et al.,
2016; Grosz and Stone, 2018) concludes that “Substantial increases in the future uses of AI
applications,includingmoreself-drivingcars,healthcarediagnosticsandtargetedtreatment,
and physical assistance for elder care can be expect...

### 1.5 Risks and Benefits of AI

FrancisBacon, aphilosophercreditedwithcreatingthescientificmethod, notedinTheWis-
dom of the Ancients (1609) that the “mechanical arts are of ambiguous use, serving as well
for hurt as for remedy.” As AI plays an increasingly important role in the economic, so-
cial, scientific, medical, financial, and military spheres, we would do well to consider the
hurtsandremedies—inmodernparlance,therisksand...

## Key Entities Mentioned

- Ada Lovelace
- Alan Turing
- Allen Newell
- Aristotle
- Bertrand Russell
- Charles Babbage
- Donald Hebb
- Geoffrey Hinton
- George Boole
- Herbert Simon
- Immanuel Kant
- John McCarthy
- John von Neumann
- Marvin Minsky
- Norbert Wiener
- Patrick Winston
- Richard Bellman
- Walter Pitts
- Warren McCulloch
- Yann LeCun
- Yoshua Bengio

## Algorithms & Concepts

- [[The Algorithm]]
- [[The algorithm]]

## Cross-References

- Next: [[Chapter 2 - Intelligent Agents]]
- Part: Part I: Artificial Intelligence

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 1. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
