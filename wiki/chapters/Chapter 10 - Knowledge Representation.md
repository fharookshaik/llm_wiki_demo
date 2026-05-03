---
type: chapter
tags: [aima, chapter, knowledge-representation]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 10
---

# Chapter 10 - Knowledge Representation

## Summary

Chapter 10 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **knowledge representation**. This chapter is part of Part III: Knowledge, Reasoning, and Planning. The chapter contains approximately 8,717 words and covers foundational concepts, algorithms, and frameworks central to understanding knowledge representation in the context of artificial intelligence.

## Key Points

- **Introduction**: 10
CHAPTER
KNOWLEDGE REPRESENTATION
Inwhichweshowhowtorepresentdiversefactsabouttherealworldinaformthatcanbe
usedtoreasonandsolveproblems.
The previous chapters showed how an agent with a knowledge base can make inferences
that enable it to act appropriately. In this chapter we address the question ...
- **10.1 Ontological Engineering**: In“toy”domains,thechoiceofrepresentationisnotthatimportant;manychoiceswillwork.
Complex domains such as shopping on the Internet or driving a car in traffic require more
generalandflexiblerepresentations. Thischaptershowshowtocreatetheserepresentations,
concentrating on general concepts—such as Even...
- **10.2 Categories and Objects**: The organization of objects into categories is a vital part of knowledge representation. Al- C(cid:74)ategory
thoughinteractionwiththeworldtakesplaceatthelevelofindividualobjects,muchreason-
ing takes place at the level of categories. For example, a shopper would normally have the
goalofbuyinga bask...
- **10.2.1 Physical composition**: The idea that one object can be part of another is a familiar one. One’s nose is part of one’s
head, Romania is part of Europe, and this chapter is part of this book. We use the general
PartOf relation to say that one thing is part of another. Objects can be grouped into PartOf
hierarchies,reminisce...
- **10.2.2 Measurements**: In both scientific and commonsense theories of the world, objects have height, mass, cost,
and so on. The values that we assign for these properties are called measures. Ordi- Measure
nary quantitative measures are quite easy to represent. We imagine that the universe in-
cludes abstract “measure ob...

## Sections Overview

### Introduction

10
CHAPTER
KNOWLEDGE REPRESENTATION
Inwhichweshowhowtorepresentdiversefactsabouttherealworldinaformthatcanbe
usedtoreasonandsolveproblems.
The previous chapters showed how an agent with a knowledge base can make inferences
that enable it to act appropriately. In this chapter we address the question of what content
to put into such an agent’s knowledge base—how to represent facts about the world. W...

### 10.1 Ontological Engineering

In“toy”domains,thechoiceofrepresentationisnotthatimportant;manychoiceswillwork.
Complex domains such as shopping on the Internet or driving a car in traffic require more
generalandflexiblerepresentations. Thischaptershowshowtocreatetheserepresentations,
concentrating on general concepts—such as Events, Time, Physical Objects, and Beliefs—
that occur in many different domains. Representing these ab...

### 10.2 Categories and Objects

The organization of objects into categories is a vital part of knowledge representation. Al- C(cid:74)ategory
thoughinteractionwiththeworldtakesplaceatthelevelofindividualobjects,muchreason-
ing takes place at the level of categories. For example, a shopper would normally have the
goalofbuyinga basketball, ratherthanaparticularbasketballsuchasBB . Categories also
9
serve to make predictions about ...

### 10.2.1 Physical composition

The idea that one object can be part of another is a familiar one. One’s nose is part of one’s
head, Romania is part of Europe, and this chapter is part of this book. We use the general
PartOf relation to say that one thing is part of another. Objects can be grouped into PartOf
hierarchies,reminiscentoftheSubsethierarchy:
PartOf(Bucharest,Romania)
PartOf(Romania,EasternEurope)
PartOf(EasternEurope...

### 10.2.2 Measurements

In both scientific and commonsense theories of the world, objects have height, mass, cost,
and so on. The values that we assign for these properties are called measures. Ordi- Measure
nary quantitative measures are quite easy to represent. We imagine that the universe in-
cludes abstract “measure objects,” such as the length that is the length of this line seg-
ment: . Wecancallthislength1.5inches...

### 10.2.3 Objects: Things and stuff

The real world can be seen as consisting of primitive objects (e.g., atomic particles) and
composite objects built from them. By reasoning at the level of large objects such as apples
andcars,wecanovercomethecomplexityinvolvedindealingwithvastnumbersofprimitive
objectsindividually. Thereis,however,asignificantportionofrealitythatseemstodefyany
obviousindividuation—divisionintodistinctobjects. Wegi...

### 10.3 Events

InSection7.7.1wediscussedactions: thingsthathappen,suchasShoot ;andfluents: aspects
t
of the world that change, such as HaveArrow . Both were represented as propositions, and
t
we used successor-state axioms to say that a fluent will be true at timet+1 if the action at
timet causedittobetrue,orifitwasalreadytrueattimet andtheactiondidnotcauseitto
be false. That was for a world in which actions are...

### 10.3.1 Time

Eventcalculusopensusuptothepossibilityoftalkingabouttimepointsandtimeintervals.
We will consider two kinds of time intervals: moments and extended intervals. The distinc-
tionisthatonlymomentshavezeroduration:
Partition({Moments,ExtendedIntervals},Intervals)
i∈Moments ⇔ Duration(i)=Seconds(0).
Nextweinventatimescaleandassociatepointsonthatscalewithmoments,givingusabso-
lutetimes. Thetimescaleisarb...

### 10.3.2 Fluents and objects

Physical objects can be viewed as generalized events, in the sense that a physical object is
a chunk of space–time. For example, USA can be thought of as an event that began in 1776
as a union of 13 states and is still in progress today as a union of 50. We can describe the
changingpropertiesofUSAusingstatefluents,suchasPopulation(USA). ApropertyofUSA
that changes every four or eight years, barrin...

### 10.4 Mental Objects and Modal Logic

The agents we have constructed so far have beliefs and can deduce new beliefs. Yet none
of them has any knowledge about beliefs or about deduction. Knowledge about one’s own
knowledgeandreasoningprocessesisusefulforcontrollinginference. Forexample,suppose
Aliceasks“whatisthesquarerootof1764”andBobreplies“Idon’tknow.” IfAliceinsists
“think harder,” Bob should realize that with some more thought, th...

### 10.4.1 Other modal logics

Many modal logics have been proposed, for different modalities besides knowledge. One
proposalistoaddmodaloperatorsforpossibilityandnecessity: itispossiblytruethatoneof
theauthorsofthisbookissittingdownrightnow,anditisnecessarilytruethat2+2=4.
AsmentionedinSection8.1.2,somelogiciansfavormodalitiesrelatedtotime. Inlinear
Lineartemporallogic temporallogic,weaddthefollowingmodaloperators:
• XP:“Pwill...

### 10.5 Reasoning Systems for Categories

Categoriesaretheprimarybuildingblocksoflarge-scaleknowledgerepresentationschemes.
This section describes systems specially designed for organizing and reasoning with cate-
gories. Therearetwocloselyrelatedfamiliesofsystems: semanticnetworksprovidegraph- Semanticnetworks
ical aids for visualizing a knowledge base and efficient algorithms for inferring properties
of an object on the basis of its cat...

### 10.5.1 Semantic networks

In1909,CharlesS.Peirceproposedagraphicalnotationofnodesandedgescalledexistential
graphsthathecalled“thelogicofthefuture.” Thusbeganalong-runningdebatebetweenad- Existentialgraphs
vocatesof“logic”andadvocatesof“semanticnetworks.” Unfortunately,thedebateobscured
thefactthatsemanticnetworksareaformoflogic. Thenotationthatsemanticnetworkspro-
videforcertainkindsofsentencesisoftenmoreconvenient,butifwe...

### 10.5.2 Description logics

The syntax of first-order logic is designed to make it easy to say things about objects. De-
scription logics are notations that are designed to make it easier to describe definitions and Descriptionlogic
properties of categories. Description logic systems evolved from semantic networks in re-
sponse to pressure to formalize what the networks mean while retaining the emphasis on
taxonomicstructure...

### 10.6 Reasoning with Default Information

Intheprecedingsection,wesawasimpleexampleofanassertionwithdefaultstatus: people
have two legs. This default can be overridden by more specific information, such as that
LongJohnSilverhasoneleg. Wesawthattheinheritancemechanisminsemanticnetworks
implements the overriding of defaults in a simple and natural way. In this section, we study
defaults more generally, with a view toward understanding the ...

### 10.6.1 Circumscription and default logic

Wehaveseentwoexamplesofreasoningprocessesthatviolatethemonotonicitypropertyof Monotonicity
logic that was proved in Chapter 7.8 In this chapter we saw that a property inherited by all
membersofacategoryinasemanticnetworkcouldbeoverriddenbymorespecificinforma-
tionforasubcategory. InSection9.4.4,wesawthatundertheclosed-worldassumption,ifa
propositionαisnotmentionedinKBthenKB|=¬α,butKB∧α|=α.
Simplei...

### 10.6.2 Truth maintenance systems

We have seen that many of the inferences drawn by a knowledge representation system will
have only default status, rather than being absolutely certain. Inevitably, some of these in-
ferred facts will turn out to be wrong and will have to be retracted in the face of new infor-
mation. Thisprocessiscalledbeliefrevision.10 SupposethataknowledgebaseKBcontains Beliefrevision
a sentence P—perhaps a def...

## Key Entities Mentioned

- Aristotle
- Drew McDermott

## Algorithms & Concepts

- [[Google search]]

## Cross-References

- Previous: [[Chapter 9 - Inference in First-Order Logic]]
- Next: [[Chapter 11 - Automated Planning]]
- Part: Part III: Knowledge, Reasoning, and Planning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 10. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
