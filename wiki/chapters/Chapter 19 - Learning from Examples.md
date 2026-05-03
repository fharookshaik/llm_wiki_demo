---
type: chapter
tags: [aima, chapter, learning-from-examples]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 19
---

# Chapter 19 - Learning from Examples

## Summary

Chapter 19 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **learning from examples**. This chapter is part of Part V: Learning. The chapter contains approximately 21,374 words and covers foundational concepts, algorithms, and frameworks central to understanding learning from examples in the context of artificial intelligence.

## Key Points

- **Introduction**: 19
CHAPTER
LEARNING FROM EXAMPLES
Inwhichwedescribeagentsthatcanimprovetheirbehaviorthroughdiligentstudyofpast
experiencesandpredictionsaboutthefuture.
Anagentislearningifitimprovesitsperformanceaftermakingobservationsabouttheworld.
Learningcanrangefromthetrivial,suchasjottingdownashoppinglist,tothe...
- **19.1 Forms of Learning**: Any component of an agent program can be improved by machine learning. The improve-
ments,andthetechniquesusedtomakethem,dependonthesefactors:
• Whichcomponentistobeimproved.
• Whatpriorknowledgetheagenthas,whichinfluencesthemodelitbuilds.
• Whatdataandfeedbackonthatdataisavailable.
Chapter2describe...
- **19.2 Supervised Learning**: Moreformally,thetaskofsupervisedlearningisthis:
GivenatrainingsetofN exampleinput–outputpairs Trainingset
(x ,y ),(x ,y ),...(x ,y ),
1 1 2 2 N N
whereeachpairwasgeneratedbyanunknownfunctiony= f(x),
discoverafunctionhthatapproximatesthetruefunction f.
The function h is called a hypothesis about the ...
- **19.2.1 Example problem: Restaurant waiting**: We will describe a sample supervised learning problem in detail: the problem of deciding
whethertowaitforatableatarestaurant. Thisproblemwillbeusedthroughoutthechapter
todemonstratedifferentmodelclasses. Forthisproblemtheoutput, y, isaBooleanvariable
thatwewillcallWillWait; itistrueforexampleswherew...
- **19.3 Learning Decision Trees**: A decision tree is a representation of a function that maps a vector of attribute values to Decisiontree
a single output value—a “decision.” A decision tree reaches its decision by performing a
sequence of tests, starting at the root and following the appropriate branch until a leaf is
reached. Each...

## Sections Overview

### Introduction

19
CHAPTER
LEARNING FROM EXAMPLES
Inwhichwedescribeagentsthatcanimprovetheirbehaviorthroughdiligentstudyofpast
experiencesandpredictionsaboutthefuture.
Anagentislearningifitimprovesitsperformanceaftermakingobservationsabouttheworld.
Learningcanrangefromthetrivial,suchasjottingdownashoppinglist,totheprofound,as
when Albert Einstein inferred a new theory of the universe. When the agent is a computer...

### 19.1 Forms of Learning

Any component of an agent program can be improved by machine learning. The improve-
ments,andthetechniquesusedtomakethem,dependonthesefactors:
• Whichcomponentistobeimproved.
• Whatpriorknowledgetheagenthas,whichinfluencesthemodelitbuilds.
• Whatdataandfeedbackonthatdataisavailable.
Chapter2describedseveralagentdesigns. Thecomponentsoftheseagentsinclude:
1. Adirectmappingfromconditionsonthecurrent...

### 19.2 Supervised Learning

Moreformally,thetaskofsupervisedlearningisthis:
GivenatrainingsetofN exampleinput–outputpairs Trainingset
(x ,y ),(x ,y ),...(x ,y ),
1 1 2 2 N N
whereeachpairwasgeneratedbyanunknownfunctiony= f(x),
discoverafunctionhthatapproximatesthetruefunction f.
The function h is called a hypothesis about the world. It is drawn from a hypothesis space Hypothesisspace
H of possible functions. For example, the...

### 19.2.1 Example problem: Restaurant waiting

We will describe a sample supervised learning problem in detail: the problem of deciding
whethertowaitforatableatarestaurant. Thisproblemwillbeusedthroughoutthechapter
todemonstratedifferentmodelclasses. Forthisproblemtheoutput, y, isaBooleanvariable
thatwewillcallWillWait; itistrueforexampleswherewedowaitforatable. Theinput, x,
isavectoroftenattributevalues,eachofwhichhasdiscretevalues:
1. Altern...

### 19.3 Learning Decision Trees

A decision tree is a representation of a function that maps a vector of attribute values to Decisiontree
a single output value—a “decision.” A decision tree reaches its decision by performing a
sequence of tests, starting at the root and following the appropriate branch until a leaf is
reached. Each internal node in the tree corresponds to a test of the value of one of the input
attributes, the br...

### 19.3.1 Expressiveness of decision trees

ABooleandecisiontreeisequivalenttoalogicalstatementoftheform:
Output ⇔ (Path ∨Path ∨···),
1 2
where each Path is a conjunction of the form (A = v ∧A = v ∧···) of attribute-value
i m x n y
tests corresponding to a path from the root to a true leaf. Thus, the whole expression is
in disjunctive normal form, which means that any function in propositional logic can be
expressedasadecisiontree.
Formanyp...

### 19.3.2 Learning decision trees from examples

We want to find a tree that is consistent with the examples in Figure 19.2 and is as small as
possible. Unfortunately, it is intractable to find a guaranteed smallest consistent tree. But
with some simple heuristics, we can efficiently find one that is close to the smallest. The
LEARN-DECISION-TREE algorithm adopts a greedy divide-and-conquer strategy: always
testthemostimportantattributefirst,the...

### 19.3.3 Choosing attribute tests

ThedecisiontreelearningalgorithmchoosestheattributewiththehighestIMPORTANCE. We
willnowshowhowtomeasureimportance,usingthenotionofinformationgain,whichisde-
finedintermsofentropy,whichisthefundamentalquantityininformationtheory(Shannon Entropy
andWeaver,1949).
Entropy is a measure of the uncertainty of a random variable; the more information, the
less entropy. A random variable with only one possi...

### 19.3.4 Generalization and overfitting

We want our learning algorithms to find a hypothesis that fits the training data, but more
importantly,wewantittogeneralizewellforpreviouslyunseendata. InFigure19.1wesaw
thatahigh-degreepolynomialcanfitallthedata,buthaswildswingsthatarenotwarranted
bythedata: itfitsbutcanoverfit. Overfittingbecomesmorelikelyasthenumberofattributes
grows, and less likely as we increase the number of training exampl...

### 19.3.5 Broadening the applicability of decision trees

Decisiontreescanbemademorewidelyusefulbyhandlingthefollowingcomplications:
• Missing data: In many domains, not all the attribute values will be known for every
example. The values might have gone unrecorded, or they might be too expensive to
obtain. This gives rise to two problems: First, given a complete decision tree, how
should one classify an example that is missing one of the test attributes...

### 19.4 Model Selection and Optimization

Ourgoalinmachinelearningistoselectahypothesisthatwilloptimallyfitfutureexamples.
Tomakethatpreciseweneedtodefine“futureexample”and“optimalfit.”
Firstwewillmaketheassumptionthatthefutureexampleswillbelikethepast. Wecall
thisthestationarityassumption;withoutit,allbetsareoff. WeassumethateachexampleE j Stationarity
hasthesamepriorprobabilitydistribution:
P(E )=P(E )=P(E )=···,
j j+1 j+2
andisindepend...

### 19.4.1 Model selection

Figure19.8describesasimple MODEL-SELECTION algorithm. Ittakesasargumentalearn-
ing algorithm, Learner (for example, it could be LEARN-DECISION-TREE). Learner takes
one hyperparameter, which is named size in the figure. For decision trees it could be the
number of nodes in the tree; for polynomials size would be Degree. MODEL-SELECTION
starts with the smallest value of size, yielding a simple model...

### 19.4.2 From error rates to loss

Sofar,wehavebeentryingtominimizeerrorrate. Thisisclearlybetterthanmaximizingerror
rate, butitisnotthefullstory. Considertheproblemofclassifyingemailmessagesasspam
ornon-spam. Itisworsetoclassifynon-spamasspam(andthuspotentiallymissanimportant
message) than to classify spam as non-spam (and thus suffer a few seconds of annoyance).
Soaclassifierwitha1%errorrate,wherealmostalltheerrorswereclassifying...

### 19.4.3 Regularization

In Section 19.4.1, we saw how to do model selection with cross-validation. An alternative
approachistosearchforahypothesisthatdirectlyminimizestheweightedsumofempirical
lossandthecomplexityofthehypothesis,whichwewillcallthetotalcost:
Cost(h) = EmpLoss(h)+λComplexity(h)
hˆ∗ = argminCost(h).
h∈H
Here λ is a hyperparameter, a positive number that serves as a conversion rate between loss
and hypothesi...

### 19.4.4 Hyperparameter tuning

In Section 19.4.1 we showed how to select the best value of the hyperparameter size by
applyingcross-validationtoeachpossiblevalueuntilthevalidationerrorrateincreases. That
is a good approach when there is a single hyperparameter with a small number of possible
values. But when there are multiple hyperparameters, or when they have continuous values,
itismoredifficulttochoosegoodvalues.
Thesimplest...

### 19.5 The Theory of Learning

How can we be sure that our learned hypothesis will predict well for previously unseen in-
puts? That is, how do we know that the hypothesis h is close to the target function f if
we don’t know what f is? These questions have been pondered for centuries, by Ockham,
Hume,andothers. Inrecentdecades,otherquestionshaveemerged: howmanyexamplesdo
we need to get a good h? What hypothesis space should we ...

### 19.5.1 PAC learning example: Learning decision lists

Decisionlists We now show how to apply PAC learning to a new hypothesis space: decision lists. A
decision list consists of a series of tests, each of which is a conjunction of literals. If a
test succeeds when applied to an example description, the decision list specifies the value
to be returned. If the test fails, processing continues with the next test in the list. Decision
lists resemble decis...

### 19.6 Linear Regression and Classification

Now it is time to move on from decision trees and lists to a different hypothesis space, one
Linearfunction thathasbeenusedforhundredsofyears: theclassoflinearfunctionsofcontinuous-valued
inputs. We’ll start with the simplest case: regression with a univariate linear function, oth-
erwise known as “fitting a straight line.” Section 19.6.3 covers the multivariable case. Sec-
tions19.6.4and19.6.5sho...

### 19.6.1 Univariate linear regression

Aunivariatelinearfunction(astraightline)withinputxandoutputyhastheformy=w x+
1
w , where w and w are real-valued coefficients to be learned. We use the letter w because
0 0 1
Weight we think of the coefficients as weights; the value of y is changed by changing the relative
weightofonetermoranother. We’lldefinewtobethevector(cid:104)w ,w (cid:105),anddefinethelinear
0 1
functionwiththoseweightsas
h...

### 19.6.2 Gradient descent

The univariate linear model has the nice property that it is easy to find an optimal solution
wherethepartialderivativesarezero. Butthatwon’talwaysbethecase,soweintroducehere
amethodforminimizinglossthatdoesnotdependonsolvingtofindzeroesofthederivatives,
andcanbeappliedtoanylossfunction,nomatterhowcomplex.
AsdiscussedinSection4.2(page137)wecansearchthroughacontinuousweightspace
byincrementallymodi...

### 19.6.3 Multivariable linear regression

We can easily extend to multivariable linear regression problems, in which each example Multivariablelinear
regression
x isann-elementvector.8 Ourhypothesisspaceisthesetoffunctionsoftheform
j
h (x )=w +w x +···+w x =w +∑wx .
w j 0 1 j,1 n j,n 0 i j,i
i
8 ThereadermaywishtoconsultAppendixAforabriefsummaryoflinearalgebra. Also,notethatweusethe
term“multivariableregression”tomeanthattheinputisavector...

### 19.6.4 Linear classifiers with a hard threshold

Linear functions can be used to do classification as well as regression. For example, Fig-
ure19.15(a)showsdatapointsoftwoclasses: earthquakes(whichareofinteresttoseismolo-
gists)andundergroundexplosions(whichareofinteresttoarmscontrolexperts). Eachpoint
is defined by two input values, x and x , that refer to body and surface wave magnitudes
1 2
computed from the seismic signal. Given these traini...

### 19.6.5 Linear classification with logistic regression

We have seen that passing the output of a linear function through the threshold function
createsalinearclassifier;yetthehardnatureofthethresholdcausessomeproblems: thehy-
pothesish (x)isnotdifferentiableandisinfactadiscontinuousfunctionofitsinputsandits
w
weights. This makes learning with the perceptron rule a very unpredictable adventure. Fur-
thermore, thelinearclassifieralwaysannouncesacomplete...

### 19.7 Nonparametric Models

Linearregressionusesthetrainingdatatoestimateafixedsetofparametersw. Thatdefines
our hypothesis h (x), and at that point we can throw away the training data, because they
w
areallsummarizedbyw. Alearningmodelthatsummarizesdatawithasetofparametersof
Parametricmodel fixedsize(independentofthenumberoftrainingexamples)iscalledaparametricmodel.
When data sets are small, it makes sense to have a strong ...

### 19.7.1 Nearest-neighbor models

We can improveon table lookup witha slight variation: given a queryx , instead offinding
q
an example that is equal to x , find the k examples that are nearest to x . This is called k-
q q
nearest-neighborslookup. We’llusethenotationNN(k,x q )todenotethesetofkneighbors Nearestneighbors
nearesttox .
q
Todoclassification,findthesetofneighborsNN(k,x )andtakethemostcommonoutput
q
value—for example, if...

### 19.7.2 Finding nearest neighbors with k-d trees

A balanced binary tree over data with an arbitrary number of dimensions is called a k-d
K-dtree tree,fork-dimensionaltree. Theconstructionofak-dtreeissimilartotheconstructionofa
balancedbinarytree. Westartwithasetofexamplesandattherootnodewesplitthemalong
the ith dimension by testing whether x ≤m, where m is the median of the examples along
i...

### 19.7.3 Locality-sensitive hashing

Hash tables have the potential to provide even faster lookup than binary trees. But how can
wefindnearestneighborsusingahashtable,whenhashcodesrelyonanexactmatch? Hash
codes randomly distribute values among the bins, but we want to have near points grouped
togetherinthesamebin;wewantalocality-sensitivehash(LSH). Locality-sensitive
hash
We can’t use hashes to solve NN(k,x ) exactly, but with a clev...

### 19.7.4 Nonparametric regression

Now we’ll look at nonparametric approaches to regression rather than classification. Fig-
ure 19.20 shows an example of some different models. In (a), we have perhaps the simplest
method of all, known informally as “connect-the-dots,” and superciliously as “piecewise-
linearnonparametricregression.” Thismodelcreatesafunctionh(x)that,whengivenaquery
x , considers the training examples immediately t...

### 19.7.5 Support vector machines

Supportvector
In the early 2000s, the support vector machine (SVM) model class was the most popular
machine(SVM)
approach for “off-the-shelf” supervised learning, for when you don’t have any specialized
prior knowledge about a domain. That position has now been taken over by deep learning
networksandrandomforests,butSVMsretainthreeattractiveproperties:
1. SVMsconstructamaximummarginseparator—adeci...

### 19.7.6 The kernel trick

This then is the clever kernel trick: Plugging these kernels into Equation (19.10), optimal Kerneltrick
linearseparatorscanbefoundefficientlyinfeaturespaceswithbillionsof(oreveninfinitely
many) dimensions. The resulting linear separators, when mapped back to the original in-
put space, can correspond to arbitrarily wiggly, nonlinear decision boundaries between the
positiveandnegativeexamples.
In t...

### 19.8 Ensemble Learning

Sofarwehavelookedatlearningmethodsinwhichasinglehypothesisisusedtomakepre-
Ensemblelearning dictions. Theideaofensemblelearningistoselectacollection,orensemble,ofhypotheses,
h ,h ,...,h ,andcombinetheirpredictionsbyaveraging,voting,orbyanotherlevelofma-
1 2 n
Basemodel chine learning. We call the individual hypotheses base models and their combination an
Ensemblemodel ensemblemodel.
There are two ...

### 19.8.1 Bagging

In bagging,15 we generate K distinct training sets by sampling with replacement from the Bagging
original training set. That is, we randomly pick N examples from the training set, but each
of those picks might be an example we picked before. We then run our machine learning
algorithm on the N examples to get a hypothesis. We repeat this process K times, getting K
different hypotheses. Then, when a...

### 19.8.2 Random forests

Unfortunately, bagging decision trees often ends up giving us K trees that are highly corre-
lated. If there is one attribute with a very high information gain, it is likely to be the root of
mostofthetrees. Therandomforestmodelisaformofdecisiontreebagginginwhichwe Randomforest
take extra steps to make the ensemble of K trees more diverse, to reduce variance. Random
forestscanbeusedforclassificati...

### 19.8.3 Stacking

Whereasbaggingcombinesmultiplebasemodelsofthesamemodelclasstrainedondifferent
data,thetechniqueofstackedgeneralization(orstackingforshort)combinesmultiplebase Stacked
generalization
modelsfromdifferentmodelclassestrainedonthesamedata. Forexample, supposeweare
giventherestaurantdataset,thefirstrowofwhichisshownhere:
x =Yes,No,No,Yes,Some,$$$,No,Yes,French,0–10;y =Yes
1 1
We separate the data into t...

### 19.8.4 Boosting

The most popular ensemble method is called boosting. To understand how it works, we Boosting
need first to introduce the idea of a weighted training set, in which each example has an Weightedtraining
set
associatedweightw ≥0thatdescribeshowmuchtheexampleshouldcountduringtraining.
j
Forexample,ifoneexamplehadaweightof3andtheotherexamplesallhadaweightof1,
thatwouldbeequivalenttohaving3copiesoftheone...

### 19.8.5 Gradient boosting

For regression and classification of factored tabular data, gradient boosting, sometimes Gradientboosting
called gradient boosting machines (GBM) or gradient boosted regression trees (GBRT), has
becomeaverypopularmethod. Asthenameimplies,gradientboostingisaformofboosting
usinggradientdescent. RecallthatinADABOOST,westartwithonehypothesish
1
,andboost
it with a sequence of hypotheses that pay speci...

### 19.8.6 Online learning

Sofar,everythingwehavedoneinthischapterhasreliedontheassumptionthatthedataare
i.i.d. (independentandidenticallydistributed). Ontheonehand,thatisasensibleassumption:
ifthefuturebearsnoresemblancetothepast,thenhowcanwepredictanything? Ontheother...

### 19.9 Developing Machine Learning Systems

In this chapter we have concentrated on explaining the theory of machine learning. The
practiceofusingmachinelearningtosolvepracticalproblemsisaseparatediscipline. Over
thelast50years,thesoftwareindustryhasevolvedasoftwaredevelopmentmethodologythat
makes it more likely that a (traditional) software project will be a success. But we are still
in the early stages of defining a methodology for machin...

### 19.9.1 Problem formulation

The first step is to figure out what problem you want to solve. There are two parts to this.
Firstask,“whatproblemdoIwanttosolveformyusers?” Ananswersuchas“makeiteasier
for users to organize and access their photos” is too vague; “help a user find all photos that
matchaspecificterm,suchasParis”isbetter. Thenask,“whatpart(s)oftheproblemcanbe
solvedbymachinelearning?” perhapssettlingon“learnafunctio...

### 19.9.2 Data collection, assessment, and management

Everymachinelearningprojectneedsdata;inthecaseofourphotoidentificationprojectthere
arefreelyavailableimagedatasets,suchasImageNet,whichhasover14millionphotoswith ImageNet
about 20,000 different labels. Sometimes we may have to manufacture our own data, which
can be done by our own labor, or by crowdsourcing to paid workers or unpaid volunteers
operatingoveran Internetservice. Sometimesdata comefro...

### 19.9.3 Model selection and training

Withcleaneddatainhandandanintuitivefeelforit,itistimetobuildamodel. Thatmeans
choosing a model class (random forests? deep neural networks? an ensemble?), training
yourmodelwiththetrainingdata,tuninganyhyperparametersoftheclass(numberoftrees?
numberoflayers?) withthevalidationdata,debuggingtheprocess,andfinallyevaluatingthe
modelonthetestdata.
Thereisnoguaranteedwaytopickthebestmodelclass,butthere...

### 19.9.4 Trust, interpretability, and explainability

We have described a machine learning methodology where you develop your model with
training data, choose hyperparameters with validation data, and get a final metric with test
data. Doing well on that metric is a necessary but not sufficient condition for you to trust
your model. And it is not just you—other stakeholders including regulators, lawmakers, the
press, and your users are also intereste...

### 19.9.5 Operation, monitoring, and maintenance

Onceyouarehappywithyourmodel’sperformance,youcandeployittoyourusers. You’ll
Longtail face additional challenges. First, there is the problem of the long tail of user inputs. You
may have tested your system on a large test set, but if your system is popular, you will soon
see inputs that were never tested before. You need to know whether your model generalizes
Monitoring well for them, which means ...

## Key Entities Mentioned

- Aristotle
- John von Neumann
- Leslie Valiant

## Algorithms & Concepts

- [[Examples
algorithm]]
- [[This algorithm]]
- [[T algorithm]]
- [[E algorithm]]
- [[G algorithm]]
- [[Learning algorithm]]
- [[The
algorithm]]
- [[N algorithm]]

## Cross-References

- Previous: [[Chapter 18 - Probabilistic Programming]]
- Next: [[Chapter 20 - Knowledge in Learning]]
- Part: Part V: Learning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 19. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
