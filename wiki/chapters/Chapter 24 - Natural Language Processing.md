---
type: chapter
tags: [aima, chapter, natural-language-processing]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 24
---

# Chapter 24 - Natural Language Processing

## Summary

Chapter 24 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **natural language processing**. This chapter is part of Part VI: Communicating, Perceiving, and Acting. The chapter contains approximately 9,466 words and covers foundational concepts, algorithms, and frameworks central to understanding natural language processing in the context of artificial intelligence.

## Key Points

- **Introduction**: 24
CHAPTER
NATURAL LANGUAGE PROCESSING
In which we see how a computer can use natural language to communicate with humans
andlearnfromwhattheyhavewritten.
About 100,000 years ago, humans learned how to speak, and about 5,000 years ago they
learned to write. The complexity and diversity of human lang...
- **24.1 Language Models**: Formallanguages,suchasfirst-orderlogic,arepreciselydefined,aswesawinChapter8. A
grammardefinesthesyntaxoflegalsentencesandsemanticrulesdefinethemeaning.
Naturallanguages,suchasEnglishorChinese,cannotbesoneatlycharacterized:
• Languagejudgmentsvaryfrompersontopersonandtimetotime. Everyoneagreesthat
“...
- **24.1.1 The bag-of-words model**: Section 12.6.1 explained how a naive Bayes model based on the presence of specific words
could reliably classify sentences into categories; for example sentence (1) below is catego-
rizedasbusiness,and(2)asweather.
1. Stocks rallied on Monday, with major indexes gaining 1% as optimism persisted over...
- **24.1.2 N-gram word models**: The bag-of-words model has limitations. For example, the word “quarter” is common in
both the business and sports categories. But the four-word sequence “first quarter earnings
report” is common only inbusinessand “fourth quarter touchdown passes” is common only
in sports. We’d like our model to mak...
- **24.1.3 Other n-gram models**: Analternativetoann-gramwordmodelisacharacter-levelmodelinwhichtheprobability Character-level
model
of each character is determined by the n−1 previous characters. This approach is helpful
fordealingwithunknownwords,andforlanguagesthattendtorunwordstogether,asinthe
Danishword“Speciallægepraksisplanlæ...

## Sections Overview

### Introduction

24
CHAPTER
NATURAL LANGUAGE PROCESSING
In which we see how a computer can use natural language to communicate with humans
andlearnfromwhattheyhavewritten.
About 100,000 years ago, humans learned how to speak, and about 5,000 years ago they
learned to write. The complexity and diversity of human language sets Homo sapiens apart
fromallotherspecies. Ofcoursethereareotherattributesthatareuniquelyhuma...

### 24.1 Language Models

Formallanguages,suchasfirst-orderlogic,arepreciselydefined,aswesawinChapter8. A
grammardefinesthesyntaxoflegalsentencesandsemanticrulesdefinethemeaning.
Naturallanguages,suchasEnglishorChinese,cannotbesoneatlycharacterized:
• Languagejudgmentsvaryfrompersontopersonandtimetotime. Everyoneagreesthat
“Nottobeinvitedissad”isagrammaticalsentenceofEnglish,butpeopledisagreeon
thegrammaticalityof“Tobenoti...

### 24.1.1 The bag-of-words model

Section 12.6.1 explained how a naive Bayes model based on the presence of specific words
could reliably classify sentences into categories; for example sentence (1) below is catego-
rizedasbusiness,and(2)asweather.
1. Stocks rallied on Monday, with major indexes gaining 1% as optimism persisted over
thefirstquarterearningsseason.
2. HeavyraincontinuedtopoundmuchoftheeastcoastonMonday,withfloodwarn...

### 24.1.2 N-gram word models

The bag-of-words model has limitations. For example, the word “quarter” is common in
both the business and sports categories. But the four-word sequence “first quarter earnings
report” is common only inbusinessand “fourth quarter touchdown passes” is common only
in sports. We’d like our model to make that distinction. We could tweak the bag-of-words
model by treating special phrases like “first-qu...

### 24.1.3 Other n-gram models

Analternativetoann-gramwordmodelisacharacter-levelmodelinwhichtheprobability Character-level
model
of each character is determined by the n−1 previous characters. This approach is helpful
fordealingwithunknownwords,andforlanguagesthattendtorunwordstogether,asinthe
Danishword“Speciallægepraksisplanlægningsstabiliseringsperiode.”
Character-level models are well suited for the task of language identi...

### 24.1.4 Smoothing n-gram models

High-frequencyn-gramslike“ofthe”havehighcountsinthetrainingcorpus,sotheirproba-
bilityestimateislikelytobeaccurate: withadifferenttrainingcorpuswewouldgetasimilar
estimate. Low-frequency n-grams have low counts that are subject to random noise—they
havehighvariance. Ourmodelswillperformbetterifwecansmoothoutthatvariance.
Furthermore,thereisalwaysachancethatwewillbeaskedtoevaluateatextcontaining
Ou...

### 24.1.5 Word representations

N-grams can give us a model that accurately predicts the probability of word sequences,
telling us that, for example, “a black cat” is a more likely English phrase than “cat black a”
because“ablackcat”appearsinabout0.000014%ofthetrigramsinatrainingcorpus,while
“catblacka”doesnotappearatall. Everythingthatthen-gramwordmodelknows,itlearned
fromcountsofspecificwordsequences.
ButanativespeakerofEnglis...

### 24.1.7 Comparing language models

To get a feeling for what different n-gram models are like, we built unigram (i.e., bag-of-
words), bigram, trigram, and 4-gram models over the words in this book and then randomly
sampledwordsequencesfromeachofthefourmodels:
• n=1: logicalareasareconfusionamayrighttriesagentgoalthewas
• n=2: systemsareverysimilarcomputationalapproachwouldberepresented
• n=3: planningandschedulingareintegratedthes...

### 24.2 Grammar

In Chapter 7 we used Backus–Naur Form (BNF) to write down a grammar for the language
of first-order logic. A grammar is a set of rules that defines the tree structure of allowable
phrases,andalanguageisthesetofsentencesthatfollowthoserules.
Naturallanguagesdonotworkexactlyliketheformallanguageoffirst-orderlogic—they
donothaveahardboundarybetweenallowableandunallowablesentences,nordotheyhavea
singl...

### 24.2.1 The lexicon of E

0
Lexicon The lexicon, or list of allowable words, is defined in Figure 24.3. Each of the lexical cate-
gories ends in ... to indicate that there are other words in the category. For nouns, names,
verbs,adjectives,andadverbs,itisinfeasibleeveninprincipletolistallthewords. Notonly
are there tens of thousands of members in each class, but new ones—like humblebrag or
Openclass microbiome—arebeingadde...

### 24.3 Parsing

Parsing Parsingistheprocessofanalyzingastringofwordstouncoveritsphrasestructure,according
to the rules of a grammar. We can think of it as asearchfor a valid parse tree whose leaves
arethewordsofthestring. Figure24.4showsthatwecanstartwiththeSsymbolandsearch
topdown,orwecanstartwiththewordsandsearchbottomup. Puretop-downorbottom-up
parsing strategies can be inefficient, however, because they can e...

### 24.3.1 Dependency parsing

There is a widely used alternative syntactic approach called dependency grammar, which Dependency
grammar
assumesthatsyntacticstructureisformedbybinaryrelationsbetweenlexicalitems,without
aneedforsyntacticconstituents. Figure24.7showsasentencewithadependencyparseand
aphrasestructureparse.
Inonesense,dependencygrammarandphrasestructuregrammararejustnotationalvari-
ants. If the phrase structure tree...

### 24.3.2 Learning a parser from examples

Building a grammar for a significant portion of English is laborious and error prone. This
suggests that it would be better to learn the grammar rules (and probabilities) rather than
writing them down by hand. To apply supervised learning, we need input/output pairs of
sentences and their parse trees. The Penn Treebank is the best known source of such data,
with over 100 thousand sentences annotat...

### 24.4 Augmented Grammars

So far we have dealt with context-free grammars. But not every NP can appear in every
context with equal probability. The sentence “I ate a banana” is fine, but “Me ate a banana”
isungrammatical,and“Iateabandanna”isunlikely.
Theissueisthatourgrammarisfocusedonlexicalcategories,likePronoun,butwhile“I”
and “me” are both pronouns, only “I” can be the subject of a sentence. Similarly, “banana”
and “ba...

### 24.4.1 Semantic interpretation

Toshowhowtoaddsemanticstoagrammar,westartwithanexamplethatissimplerthanEn-
glish: thesemanticsofarithmeticexpressions. Figure24.10showsagrammarforarithmetic
expressions, where each rule is augmented with a single argument indicating the semantic
interpretation of the phrase. The semantics of a digit such as “3” is the digit itself. The se-
manticsoftheexpression“3+4”istheoperator“+”appliedtothesem...

### 24.4.2 Learning semantic grammars

Unfortunately,thePennTreebankdoesnotincludesemanticrepresentationsofitssentences,
justsyntactictrees. Soifwearegoingtolearnasemanticgrammar,wewillneedadifferent
sourceofexamples. ZettlemoyerandCollins(2005)describeasystemthatlearnsagrammar
for a question-answering system from examples that consist of a sentence paired with the
semanticformforthesentence:
• Sentence: WhatstatesborderTexas?
• Logica...

### 24.5 Complications of Real Natural Language

ThegrammarofrealEnglishisendlesslycomplex(andotherlanguagesareequallycomplex).
Wewillbrieflymentionsomeofthetopicsthatcontributetothiscomplexity.
Quantification Quantification: Consider the sentence “Every agent feels a breeze.” The sentence has
only one syntactic parse under E , but it is semantically ambiguous: is there one breeze
0
that is felt by all the agents, or does each agent feel a separ...

### 24.6 Natural Language Tasks

Natural language processing is a big field, deserving an entire textbook or two of its own
(Goldberg,2017;JurafskyandMartin,2020). Inthissectionwebrieflydescribesomeofthe
maintasks;youcanusethereferencestogetmoredetails.
Speechrecognition Speech recognition is the task of transforming spoken sound into text. We can then
perform further tasks (such as question answering) on the resulting text. Curr...

## Key Entities Mentioned

- None identified

## Algorithms & Concepts

- [[Rank algorithm]]
- [[Internet
search]]
- [[Web search]]
- [[Viterbi algorithm]]

## Cross-References

- Previous: [[Chapter 23 - Reinforcement Learning]]
- Next: [[Chapter 25 - Deep Learning for Natural Language Processing]]
- Part: Part VI: Communicating, Perceiving, and Acting

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 24. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
