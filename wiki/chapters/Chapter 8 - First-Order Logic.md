---
type: chapter
tags: [aima, chapter, first-order-logic]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 8
---

# Chapter 8 - First-Order Logic

## Summary

Chapter 8 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **first-order logic**. This chapter is part of Part III: Knowledge, Reasoning, and Planning. The chapter contains approximately 7,998 words and covers foundational concepts, algorithms, and frameworks central to understanding first-order logic in the context of artificial intelligence.

## Key Points

- **Introduction**: 270 Chapter 8 First-OrderLogic
example,themeaningof“S ∧S ”isrelatedtothemeaningsof“S ”and“S .” Itwould
1,4 1,2 1,4 1,2
be very strange if “S ” meant that there is a stench in square [1,4] and “S ” meant that
1,4 1,2
there is a stench in square [1,2], but “S ∧S ” meant that France and Poland drew 1–1...
- **8.1.1 The language of thought**: Natural languages (such as English or Spanish) are very expressive indeed. We managed
to write almost this whole book in natural language, with only occasional lapses into other
languages (mainly mathematics and diagrams). There is a long tradition in linguistics and
thephilosophyoflanguagethatviews...
- **8.1.2 Combining the best of formal and natural languages**: We can adopt the foundation of propositional logic—a declarative, compositional semantics
that is context-independent and unambiguous—and build a more expressive logic on that
foundation,borrowingrepresentationalideasfromnaturallanguagewhileavoidingitsdraw-
backs. Whenwelookatthesyntaxofnaturallangu...
- **8.2 Syntax and Semantics of First-Order Logic**: We begin this section by specifying more precisely the way in which the possible worlds of
first-order logic reflect the ontological commitment to objects and relations. Then we intro-
duce the various elements of the language, explaining their semantics as we go along. The
main points are how the l...
- **8.2.1 Models for first-order logic**: Chapter 7 said that the models of a logical language are the formal structures that constitute
thepossibleworldsunderconsideration. Eachmodellinksthevocabularyofthelogicalsen-
tencestoelementsofthepossibleworld,sothatthetruthofanysentencecanbedetermined.
Thus,modelsforpropositionallogiclinkpropositi...

## Sections Overview

### Introduction

First-OrderLogic
example,themeaningof“S ∧S ”isrelatedtothemeaningsof“S ”and“S .” Itwould
1,4 1,2 1,4 1,2
be very strange if “S ” meant that there is a stench in square [1,4] and “S ” meant that
1,4 1,2
there is a stench in square [1,2], but “S ∧S ” meant that France and Poland drew 1–1 in
1,4 1,2
lastweek’sicehockeyqualifyingmatch.
However,propositionallogic,asafactoredrepresentation,lackstheexpre...

### 8.1.1 The language of thought

Natural languages (such as English or Spanish) are very expressive indeed. We managed
to write almost this whole book in natural language, with only occasional lapses into other
languages (mainly mathematics and diagrams). There is a long tradition in linguistics and
thephilosophyoflanguagethatviewsnaturallanguageasadeclarativeknowledgerepresen-
tation language. If we could uncover the rules for n...

### 8.1.2 Combining the best of formal and natural languages

We can adopt the foundation of propositional logic—a declarative, compositional semantics
that is context-independent and unambiguous—and build a more expressive logic on that
foundation,borrowingrepresentationalideasfromnaturallanguagewhileavoidingitsdraw-
backs. Whenwelookatthesyntaxofnaturallanguage,themostobviouselementsarenouns
Object andnounphrasesthatrefertoobjects(squares, pits,wumpuses)an...

### 8.2 Syntax and Semantics of First-Order Logic

We begin this section by specifying more precisely the way in which the possible worlds of
first-order logic reflect the ontological commitment to objects and relations. Then we intro-
duce the various elements of the language, explaining their semantics as we go along. The
main points are how the language facilitates concise representations and how its semantics
leadstosoundreasoningprocedures....

### 8.2.1 Models for first-order logic

Chapter 7 said that the models of a logical language are the formal structures that constitute
thepossibleworldsunderconsideration. Eachmodellinksthevocabularyofthelogicalsen-
tencestoelementsofthepossibleworld,sothatthetruthofanysentencecanbedetermined.
Thus,modelsforpropositionallogiclinkpropositionsymbolstopredefinedtruthvalues.
Modelsforfirst-orderlogicaremuchmoreinteresting. First, theyhaveob...

### 8.2.2 Symbols and interpretations

We turn now to the syntax of first-order logic. The impatient reader can obtain a complete
descriptionfromtheformalgrammarinFigure8.3.
The basic syntactic elements of first-order logic are the symbols that stand for objects,
relations, and functions. The symbols, therefore, come in three kinds: constant symbols, Constantsymbol
which stand for objects; predicate symbols, which stand for relations; ...

### 8.2.3 Terms

A term is a logical expression that refers to an object. Constant symbols are terms, but it is Term
not always convenient to have a distinct symbol to name every object. In English we might
use the expression “King John’s left leg” rather than giving a name to his leg. This is what
functionsymbolsarefor: insteadofusingaconstantsymbol,weuseLeftLeg(John).3
Inthegeneralcase,acomplextermisformedbyafun...

### 8.2.4 Atomic sentences

Now that we have terms for referring to objects and predicate symbols for referring to rela-
Atomicsentence tions,wecancombinethemtomakeatomicsentencesthatstatefacts. Anatomicsentence
Atom (oratomforshort)isformedfromapredicatesymboloptionallyfollowedbyaparenthesized
listofterms,suchas
Brother(Richard,John).
This states, under the intended interpretation given earlier, that Richard the Lionheart i...

### 8.2.5 Complex sentences

We can use logical connectives to construct more complex sentences, with the same syntax
andsemanticsasinpropositionalcalculus. Herearefoursentencesthataretrueinthemodel
ofFigure8.2underourintendedinterpretation:
¬Brother(LeftLeg(Richard),John)
Brother(Richard,John)∧Brother(John,Richard)
King(Richard)∨King(John)
¬King(Richard) ⇒ King(John)....

### 8.2.6 Quantifiers

Once we have a logic that allows objects, it is only natural to want to express properties of
Quantifier entirecollectionsofobjects, insteadofenumeratingtheobjectsbyname. Quantifiersletus
dothis. First-orderlogiccontainstwostandardquantifiers,calleduniversalandexistential.
Universal quantification (∀)
Recall the difficulty we had in Chapter 7 with the expression of general rules in proposi-
tional...

### 8.2.7 Equality

First-orderlogicincludesonemorewaytomakeatomicsentences,otherthanusingapredi-
Equalitysymbol cateandtermsasdescribedearlier. Wecanusetheequalitysymboltosignifythattwoterms
refertothesameobject. Forexample,
Father(John)=Henry
says that the object referred to by Father(John) and the object referred to by Henry are the
same. Because an interpretation fixes the referent of any term, determining the tr...

### 8.2.8 Database semantics

Continuingtheexamplefromtheprevioussection, supposethatwebelievethatRichardhas
twobrothers,JohnandGeoffrey.7 Wecouldwrite
Brother(John,Richard)∧Brother(Geoffrey,Richard), (8.3)
butthatwouldn’tcompletelycapturethestateofaffairs. First,thisassertionistrueinamodel
whereRichardhasonlyonebrother—weneedtoaddJohn(cid:54)=Geoffrey. Second,thesentence
doesn’truleoutmodelsinwhichRichardhasmanymorebrothersbe...

### 8.3 Using First-Order Logic

Nowthatwehavedefinedanexpressivelogicallanguage,let’slearnhowtouseit. Inthissec-
tion, we provide example sentences in some simple domains. In knowledge representation, Domain
adomainisjustsomepartoftheworldaboutwhichwewishtoexpresssomeknowledge.
We begin with a brief description of the TELL/ASK interface for first-order knowledge
bases. Then we look at the domains of family relationships, numbers...

### 8.3.1 Assertions and queries in first-order logic

SentencesareaddedtoaknowledgebaseusingTELL,exactlyasinpropositionallogic. Such
sentencesarecalledassertions. Forexample, wecanassertthatJohnisaking, Richardisa Assertion...

### 8.3.2 The kinship domain

Thefirstexampleweconsideristhedomainoffamilyrelationships,orkinship. Thisdomain
includes facts such as “Elizabeth is the mother of Charles” and “Charles is the father of
William”andrulessuchas“One’sgrandmotheristhemotherofone’sparent.”
Clearly,theobjectsinourdomainarepeople. UnarypredicatesincludeMaleandFemale,
amongothers. Kinshiprelations—parenthood,brotherhood,marriage,andsoon—arerepre-
sented ...

### 8.3.3 Numbers, sets, and lists

Numbers are perhaps the most vivid example of how a large theory can be built up from
Naturalnumbers a tiny kernel of axioms. We describe here the theory of natural numbers or nonnegative
integers. We need a predicate NatNum that will be true of natural numbers; we need one
Peanoaxioms constant symbol, 0; and we need one function symbol, S (successor). The Peano axioms
definenaturalnumbersandaddit...

### 8.3.4 The wumpus world

Some propositional logic axioms for the wumpus world were given in Chapter 7. The first-
orderaxiomsinthissectionaremuchmoreconcise,capturinginanaturalwayexactlywhat
wewanttosay.
Recall that the wumpus agent receives a percept vector with five elements. The corre-
spondingfirst-ordersentencestoredintheknowledgebasemustincludeboththeperceptand
thetimeatwhichitoccurred;otherwise,theagentwillgetconfu...

### 8.4 Knowledge Engineering in First-Order Logic

The preceding section illustrated the use of first-order logic to represent knowledge in three
simpledomains. Thissectiondescribesthegeneralprocessofknowledge-baseconstruction—
aprocesscalledknowledgeengineering. Aknowledgeengineerissomeonewhoinvestigates Knowledge
engineering
a particular domain, learns what concepts are important in that domain, and creates a for-
mal representation of the objec...

### 8.4.1 The knowledge engineering process

Knowledge engineering projects vary widely in content, scope, and difficulty, but all such
projectsincludethefollowingsteps:
1. Identify the questions. The knowledge engineer must delineate the range of questions
that the knowledge base will support and the kinds of facts that will be available for
eachspecificprobleminstance. Forexample,doesthewumpusknowledgebaseneedto
be able to choose actions, ...

### 8.4.2 The electronic circuits domain

Wewilldevelopanontologyandknowledgebasethatallowustoreasonaboutdigitalcircuits
ofthekindshowninFigure8.6. Wefollowtheseven-stepprocessforknowledgeengineering.
Identify the questions
There are many reasoning tasks associated with digital circuits. At the highest level, one
analyzes the circuit’s functionality. For example, does the circuit in Figure 8.6 actually add
properly? If all the inputs are ...

## Key Entities Mentioned

- Aristotle

## Algorithms & Concepts

- To be identified on detailed review

## Cross-References

- Previous: [[Chapter 7 - Logical Agents]]
- Next: [[Chapter 9 - Inference in First-Order Logic]]
- Part: Part III: Knowledge, Reasoning, and Planning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 8. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
