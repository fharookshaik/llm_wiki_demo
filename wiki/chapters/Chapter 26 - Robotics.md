---
type: chapter
tags: [aima, chapter, robotics]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 26
---

# Chapter 26 - Robotics

## Summary

Chapter 26 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **robotics**. This chapter is part of Part VI: Communicating, Perceiving, and Acting. The chapter contains approximately 14,602 words and covers foundational concepts, algorithms, and frameworks central to understanding robotics in the context of artificial intelligence.

## Key Points

- **Introduction**: 26
CHAPTER
ROBOTICS
Inwhichagentsareendowedwithsensorsandphysicaleffectorswithwhichtomoveabout
andmakemischiefintherealworld....
- **26.1 Robots**: Robot Robots are physical agents that perform tasks by manipulating the physical world. To do
Effector so, they are equipped with effectors such as legs, wheels, joints, and grippers. Effectors are
designed to assert physical forces on the environment. When they do this, a few things may
happen: the...
- **26.2 Robot Hardware**: Sofarinthisbook,wehavetakentheagentarchitecture—sensors,effectors,andprocessors—
asgiven,andhaveconcentratedontheagentprogram. Butthesuccessofrealrobotsdepends
atleastasmuchonthedesignofsensorsandeffectorsthatareappropriateforthetask....
- **26.2.1 Types of robots from the hardware perspective**: Whenyouthinkofarobot,youmightimaginesomethingwithaheadandtwoarms,moving
around on legs or wheels. Such anthropomorphic robots have been popularized in fiction Anthropomorphic
robot
suchasthemovieTheTerminatorandthecartoonTheJetsons. Butrealrobotscomeinmany
shapesandsizes.
Manipulatorsarejustrobotarm...
- **26.2.2 Sensing the world**: Passivesensor Sensors are the perceptual interface between robot and environment. Passive sensors, such
as cameras, are true observers of the environment: they capture signals that are generated
Activesensor by other sources in the environment. Active sensors, such as sonar, send energy into the
env...

## Sections Overview

### Introduction

26
CHAPTER
ROBOTICS
Inwhichagentsareendowedwithsensorsandphysicaleffectorswithwhichtomoveabout
andmakemischiefintherealworld....

### 26.1 Robots

Robot Robots are physical agents that perform tasks by manipulating the physical world. To do
Effector so, they are equipped with effectors such as legs, wheels, joints, and grippers. Effectors are
designed to assert physical forces on the environment. When they do this, a few things may
happen: therobot’sstatemightchange(e.g.,acarspinsitswheelsandmakesprogressonthe
roadasaresult),thestateoftheenv...

### 26.2 Robot Hardware

Sofarinthisbook,wehavetakentheagentarchitecture—sensors,effectors,andprocessors—
asgiven,andhaveconcentratedontheagentprogram. Butthesuccessofrealrobotsdepends
atleastasmuchonthedesignofsensorsandeffectorsthatareappropriateforthetask....

### 26.2.1 Types of robots from the hardware perspective

Whenyouthinkofarobot,youmightimaginesomethingwithaheadandtwoarms,moving
around on legs or wheels. Such anthropomorphic robots have been popularized in fiction Anthropomorphic
robot
suchasthemovieTheTerminatorandthecartoonTheJetsons. Butrealrobotscomeinmany
shapesandsizes.
Manipulatorsarejustrobotarms. Theydonotnecessarilyhavetobeattachedtoarobot Manipulator
body;theymightsimplybeboltedontoatableor...

### 26.2.2 Sensing the world

Passivesensor Sensors are the perceptual interface between robot and environment. Passive sensors, such
as cameras, are true observers of the environment: they capture signals that are generated
Activesensor by other sources in the environment. Active sensors, such as sonar, send energy into the
environment. They rely on the fact that this energy is reflected back to the sensor. Active
sensorstend...

### 26.2.3 Producing motion

Actuator Themechanismthatinitiatesthemotionofaneffectoriscalledanactuator;examplesinclude
transmissions,gears,cables,andlinkages. Themostcommontypeofactuatoristheelectric
actuator,whichuseselectricitytospinupamotor. Thesearepredominantlyusedinsystems
Hydraulicactuator thatneedrotationalmotion,likejointsonarobotarm. Hydraulicactuatorsusepressurized
Pneumaticactuator hydraulic fluid (like oil or wat...

### 26.4 Robotic Perception

Perceptionistheprocessbywhichrobotsmapsensormeasurementsintointernalrepresenta-
tions of the environment. Much of it uses the computer vision techniques from the previous
chapter. But perception for robotics must deal with additional sensors like lidar and tactile
sensors.
Perceptionisdifficultbecausesensorsarenoisyandtheenvironmentispartiallyobserv-
able,unpredictable,andoftendynamic. Inotherword...

### 26.4.1 Localization and mapping

Localization is the problem of finding out where things are—including the robot itself. To Localization
keepthingssimple,letusconsideramobilerobotthatmovesslowlyinaflattwo-dimensional
world. Letusalsoassumetherobotisgivenanexactmapoftheenvironment. (Anexample
of such a map appears in Figure 26.7.) The pose of such a mobile robot is defined by its
two Cartesian coordinates with values x and y and i...

### 26.4.2 Other types of perception

Not all of robot perception is about localization or mapping. Robots also perceive temper-
ature, odors, sound, and so on. Many of these quantities can be estimated using variants of
dynamicBayesnetworks. Allthatisrequiredforsuchestimatorsareconditionalprobability
distributions that characterize the evolution of state variables over time, and sensor models
thatdescribetherelationofmeasurementstost...

### 26.4.3 Supervised and unsupervised learning in robot perception

Machine learning plays an important role in robot perception. This is particularly the case
when the best internal representation is not known. One common approach is to map high-
dimensionalsensorstreamsintolower-dimensionalspacesusingunsupervisedmachinelearn-
Low-dimensional ing methods (see Chapter 19). Such an approach is called low-dimensional embedding.
embedding
Machine learning makes it po...

### 26.5 Planning and Control

The robot’s deliberations ultimately come down to deciding how to move, from the abstract
task level all the way down to the currents that are sent to its motors. In this section, we
simplifybyassumingthatperception(and,whereneeded,prediction)aregiven,sotheworld
isobservable. Wefurtherassumedeterministictransitions(dynamics)oftheworld.
Westartbyseparatingmotionfromcontrol. Wedefineapathasasequence...

### 26.5.1 Configuration space

Imagineasimplerobot,R,intheshapeofarighttriangleasshownbythelavendertrianglein
thelowerleftcornerofFigure26.11. Therobotneedstoplanapaththatavoidsarectangular
Workspace obstacle, O. The physical space that a robot moves about in is called the workspace. This
particular robot can move in any direction in the x−y plane, but cannot rotate. The figure
showsfiveotherpossiblepositionsoftherobotwithdashe...

### 26.5.2 Motion planning

Themotionplanningproblemisthatoffindingaplanthattakesarobotfromoneconfigura- Motionplanning
tiontoanotherwithoutcollidingwithanobstacle. Itisabasicbuildingblockformovement
and manipulation. In Section 26.5.4 we will discuss how to do this under complicated dy-
namics,likesteeringacarthatmaydriftoffthepathifyoutakeacurvetoofast. Fornow,we
willfocusonthesimplemotionplanningproblemoffindingageometric...

### 26.5.3 Trajectory tracking control

We have covered how to plan motions, but not how to actually move—to apply current to
motors, to produce torque, to move the robot. This is the realm of control theory, a field Controltheory
of increasing importance in AI. There are two main questions to deal with: how do we turn...

### 26.5.4 Optimal control

Ratherthanusingaplannertocreateakinematicpath,andonlyworryingaboutthedynamics
ofthesystemafterthefact,herewediscusshowwemightbeabletodoitallatonce. We’ll
take the trajectory optimization problem for kinematic paths, and turn it into true trajectory
optimizationwithdynamics: wewilloptimizedirectlyovertheactions,takingthedynamics
(ortransitions)intoaccount.
This brings us much closer to what we’ve s...

### 26.6 Planning Uncertain Movements

In robotics, uncertainty arises from partial observability of the environment and from the
stochastic (or unmodeled) effects of the robot’s actions. Errors can also arise from the use
ofapproximationalgorithmssuchasparticlefiltering,whichdoesnotgivetherobotanexact
beliefstateeveniftheenvironmentismodeledperfectly.
The majority of today’s robots use deterministic algorithms for decision making, suc...

### 26.7 Reinforcement Learning in Robotics

Thus far we have considered tasks in which the robot has access to the dynamics model of
theworld. Inmanytasks,itisverydifficulttowritedownsuchamodel,whichputsusinthe
domainofreinforcementlearning(RL).
One challenge of RL in robotics is the continuous nature of the state and action spaces,
whichwehandleeitherthroughdiscretization,or,morecommonly,throughfunctionapproxi-
mation. Policiesorvaluefunct...

### 26.7.1 Exploiting models

A natural way to avoid the need for many real-world samples is to use as much knowledge
of the world’s dynamics as possible. For instance, we might not know exactly what the
coefficient of friction or the mass of an object is, but we might have equations that describe
thedynamicsasafunctionoftheseparameters.
In such a case, model-based reinforcement learning (Chapter 23) is appealing, where
the ro...

### 26.7.2 Exploiting other information

Modelsareuseful,butthereismorewecandotofurtherreducesamplecomplexity.
Whensettingupareinforcementlearningproblem,wehavetoselectthestateandaction
spaces,therepresentationofthepolicyorvaluefunction,andtherewardfunctionwe’reusing.
Thesedecisionshavealargeimpactonhoweasyorhowhardwearemakingtheproblem.
One approach is to use higher-level motion primitives instead of low-level actions like Motionprimiti...

### 26.8 Humans and Robots

Thus far, we’ve focused on a robot planning and learning how to act in isolation. This is
useful for some robots, like the rovers we send out to explore distant planets on our behalf.
But,forthemostpart,wedonotbuildrobotstoworkinisolation. Webuildthemtohelpus,
andtoworkinhumanenvironments,aroundandwithus.
This raises two complementary challenges. First is optimizing reward when there are
people ac...

### 26.8.1 Coordination

Let’s assume for now, as we have been, that the robot has access to a clearly defined reward
function. But,insteadofneedingtooptimizeitinisolation,nowtherobotneedstooptimize
it around a human who is also acting. For example, as an autonomous car merges on the
highway,itneedstonegotiatethemaneuverwiththehumandrivercominginthetargetlane—
shoulditaccelerateandmergeinfront,orslowdownandmergebehind? La...

### 26.8.2 Learning to do what humans want

AnotherwayinteractionwithhumanscomesintoroboticsisinJ itself—therobot’scostor
R
reward function. The framework of rational agents and the associated algorithms reduce the
problem of generating good behavior to specifying a good reward function. But for robots,
asformanyotherAIagents,gettingthecostrightisstilldifficult.
Take autonomous cars: we want them to reach the destination, to be safe, to dri...

### 26.9 Alternative Robotic Frameworks

Thus far, we have taken a view of robotics based on the notion of defining or learning a
reward function, and having the robot optimize that reward function (be it via planning or
learning), sometimes in coordination or collaboration with humans. This is a deliberative Deliberative
viewofrobotics,tobecontrastedwithareactiveview. Reactive...

### 26.9.1 Reactive controllers

Insomecases,itiseasiertosetupagoodpolicyforarobotthantomodeltheworldandplan.
Then,insteadofarationalagent,wehaveareflexagent.
Forexample,picturealeggedrobotthatattemptstoliftalegoveranobstacle. Wecould
givethisrobotarulethatsaysliftthelegasmallheighthandmoveitforward,andiftheleg
encountersanobstacle,moveitbackandstartagainatahigherheight. Youcouldsaythath
ismodelinganaspectoftheworld,butwecanalsot...

### 26.9.2 Subsumption architectures

Subsumption Thesubsumptionarchitecture(Brooks,1986)isaframeworkforassemblingreactivecon-
architecture
trollers out of finite state machines. Nodes in these machines may contain tests for certain
sensor variables, in which case the execution trace of a finite state machine is conditioned
on the outcome of such a test. Arcs can be tagged with messages that will be generated
whentraversingthem,andtha...

### 26.10 Application Domains

Robotic technology is already permeating our world, and has the potential to improve our
independence,health,andproductivity. Herearesomeexampleapplications.
Home care: Robots have started to enter the home to care for older adults and people
with motor impairments, assisting them with activities of daily living and enabling them to
live more independently. These include wheelchairs and wheelchair...

## Key Entities Mentioned

- Aristotle

## Algorithms & Concepts

- [[F algorithm]]
- [[M algorithm]]
- [[L algorithm]]
- [[Monte Carlo]]
- [[The algorithm]]

## Cross-References

- Previous: [[Chapter 25 - Deep Learning for Natural Language Processing]]
- Next: [[Chapter 27 - Computer Vision]]
- Part: Part VI: Communicating, Perceiving, and Acting

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 26. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
