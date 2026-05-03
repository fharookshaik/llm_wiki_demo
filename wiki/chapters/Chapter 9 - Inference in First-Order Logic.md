---
type: chapter
tags: [aima, chapter, inference-in-first-order-logic]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 9
---

# Chapter 9 - Inference in First-Order Logic

## Summary

Chapter 9 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **inference in first-order logic**. This chapter is part of Part III: Knowledge, Reasoning, and Planning. The chapter contains approximately 8,539 words and covers foundational concepts, algorithms, and frameworks central to understanding inference in first-order logic in the context of artificial intelligence.

## Key Points

- **Introduction**: 300 Chapter 9 InferenceinFirst-OrderLogic
Fortunately,thereisafamoustheoremduetoJacquesHerbrand(1930)totheeffectthat
if a sentence is entailed by the original, first-order knowledge base, then there is a proof
involvingjustafinitesubsetofthepropositionalizedknowledgebase. Sinceanysuchsubset
has a ma...
- **9.2 Unification and First-Order Inference**: The sharp-eyed reader will have noticed that the propositionalization approach generates
many unnecessary instantiations of universally quantified sentences. We’d rather have an
approachthatusesjusttheonerule,reasoningthat{x/John}solvesthequeryEvil(x)asfol-
lows: given the rule that greedy kings are...
- **9.2.1 Unification**: Lifted inference rules require finding substitutions that make different logical expressions
look identical. This process is called unification and is a key component of all first-order Unification
inference algorithms. The UNIFY algorithm takes two sentences and returns a unifier for Unifier
them(a...
- **9.2.2 Storage and retrieval**: UnderlyingtheTELL,ASK,andASKVARSfunctionsusedtoinformandinterrogateaknowl-
edgebasearethemoreprimitiveSTOREandFETCHfunctions. STORE(s)storesasentences
intotheknowledgebaseand FETCH(q)returnsallunifierssuchthatthequeryqunifieswith
somesentenceintheknowledgebase. Theproblemweusedtoillustrateunificatio...
- **9.3 Forward Chaining**: InSection7.5weshowedaforward-chainingalgorithmforknowledgebasesofpropositional
definiteclauses. Hereweexpandthatideatocoverfirst-orderdefiniteclauses.
Ofcoursetherearesomelogicalsentencesthatcannotbestatedasadefiniteclause,and
thus cannot be handled by this approach. But rules of the form Antecedent...

## Sections Overview

### Introduction

InferenceinFirst-OrderLogic
Fortunately,thereisafamoustheoremduetoJacquesHerbrand(1930)totheeffectthat
if a sentence is entailed by the original, first-order knowledge base, then there is a proof
involvingjustafinitesubsetofthepropositionalizedknowledgebase. Sinceanysuchsubset
has a maximum depth of nesting among its ground terms, we can find the subset by first
generatingalltheinstantiationswithc...

### 9.2 Unification and First-Order Inference

The sharp-eyed reader will have noticed that the propositionalization approach generates
many unnecessary instantiations of universally quantified sentences. We’d rather have an
approachthatusesjusttheonerule,reasoningthat{x/John}solvesthequeryEvil(x)asfol-
lows: given the rule that greedy kings are evil, find some x such that x is a king and x is
greedy, and then infer that this x is evil. More g...

### 9.2.1 Unification

Lifted inference rules require finding substitutions that make different logical expressions
look identical. This process is called unification and is a key component of all first-order Unification
inference algorithms. The UNIFY algorithm takes two sentences and returns a unifier for Unifier
them(asubstitution)ifoneexists:
UNIFY(p,q)=θ where SUBST(θ,p)=SUBST(θ,q).
Let us look at some examples of ...

### 9.2.2 Storage and retrieval

UnderlyingtheTELL,ASK,andASKVARSfunctionsusedtoinformandinterrogateaknowl-
edgebasearethemoreprimitiveSTOREandFETCHfunctions. STORE(s)storesasentences
intotheknowledgebaseand FETCH(q)returnsallunifierssuchthatthequeryqunifieswith
somesentenceintheknowledgebase. Theproblemweusedtoillustrateunification—finding
allfactsthatunifywithKnows(John,x)—isaninstanceof FETCHing.
The simplest way to implement ...

### 9.3 Forward Chaining

InSection7.5weshowedaforward-chainingalgorithmforknowledgebasesofpropositional
definiteclauses. Hereweexpandthatideatocoverfirst-orderdefiniteclauses.
Ofcoursetherearesomelogicalsentencesthatcannotbestatedasadefiniteclause,and
thus cannot be handled by this approach. But rules of the form Antecedent ⇒ Consequent
aresufficienttocoverawidevarietyofinterestingreal-worldsystems....

### 9.3.1 First-order definite clauses

First-order definite clauses are disjunctions of literals of which exactly one is positive. That
meansadefiniteclauseiseitheratomic,orisanimplicationwhoseantecedentisaconjunction
ofpositiveliteralsandwhoseconsequentisasinglepositiveliteral. Existentialquantifiersare
notallowed,anduniversalquantifiersareleftimplicit: ifyouseeanxinadefiniteclause,that
meansthereisanimplicit∀x quantifier. Atypicalfir...

### 9.3.2 A simple forward-chaining algorithm

Figure 9.3 shows a simple forward chaining inference algorithm. Starting from the known
facts, it triggers all the rules whose premises are satisfied, adding their conclusions to the
knownfacts. Theprocessrepeatsuntilthequeryisanswered(assumingthatjustoneanswer
isrequired)ornonewfactsareadded. Noticethatafactisnot“new”ifitisjustarenaming Renaming
ofaknownfact—asentenceisarenamingofanotheriftheyare...

### 9.3.3 Efficient forward chaining

Theforward-chainingalgorithminFigure9.3isdesignedforeaseofunderstanding,noteffi-
ciency. There are three sources of inefficiency. First, the inner loop of the algorithm tries to
match every rule against every fact in the knowledge base. Second, the algorithm rechecks
every rule on every iteration, even if very few additions have been made to the knowledge
base. Third,thealgorithmcangeneratemanyfac...

### 9.4 Backward Chaining

Thesecondmajorfamilyoflogicalinferencealgorithmsusesbackwardchainingoverdef-
initeclauses. Thesealgorithmsworkbackwardfromthegoal,chainingthroughrulestofind
knownfactsthatsupporttheproof....

### 9.4.1 A backward-chaining algorithm

Figure 9.6 shows a backward-chaining algorithm for definite clauses. FOL-BC-ASK(KB,
goal)willbeprovediftheknowledgebasecontainsaruleoftheformlhs⇒goal,wherelhs
(left-hand side) is a list of conjuncts. An atomic fact like American(West) is considered as
a clause whose lhs is the empty list. Now a query that contains variables might be proved
in multiple ways. For example, the query Person(x) could b...

### 9.4.2 Logic programming

Logic programming is a technology that comes close to embodying the declarative ideal
described in Chapter 7: that systems should be constructed by expressing knowledge in a
formal language and that problems should be solved by running inference processes on that
knowledge. TheidealissummedupinRobertKowalski’sequation,
Algorithm=Logic+Control.
Prolog Prologisthemostwidelyusedlogicprogramminglangua...

### 9.4.3 Redundant inference and infinite loops

We now turn to the Achilles heel of Prolog: the mismatch between depth-first search and
searchtreesthatincluderepeatedstatesandinfinitepaths. Considerthefollowinglogicpro-
gramthatdecidesifapathexistsbetweentwopointsonadirectedgraph:...

### 9.4.4 Database semantics of Prolog

Prologusesdatabasesemantics,asdiscussedinSection8.2.8. Theuniquenamesassumption
says that every Prolog constant and every ground term refers to a distinct object, and the
closedworldassumptionsaysthattheonlysentencesthataretruearethosethatareentailed
by the knowledge base. There is no way to assert that a sentence is false in Prolog. This
makesProloglessexpressivethanfirst-orderlogic, butitisparto...

### 9.4.5 Constraint logic programming

In our discussion of forward chaining (Section 9.3), we showed how constraint satisfaction
problems (CSPs) can be encoded as definite clauses. Standard Prolog solves such problems
inexactlythesamewayasthebacktrackingalgorithmgiveninFigure5.5.
Because backtracking enumerates the domains of the variables, it works only for finite-
domainCSPs. InPrologterms, theremustbeafinitenumberofsolutionsforanyg...

### 9.5 Resolution

Thelastofourthreefamiliesoflogicalsystems,andtheonlyonethatworksforanyknowl-
edge base, not just definite clauses, is resolution. We saw on page 241 that propositional
resolution is a complete inference procedure for propositional logic; in this section, we ex-
tendittofirst-orderlogic....

### 9.5.1 Conjunctive normal form for first-order logic

Thefirststepistoconvertsentencestoconjunctivenormalform(CNF)—thatis,aconjunc-
tion of clauses, where each clause is a disjunction of literals.5 In CNF, literals can contain
variables,whichareassumedtobeuniversallyquantified. Forexample,thesentence
∀x,y,z American(x)∧Weapon(y)∧Sells(x,y,z)∧Hostile(z) ⇒ Criminal(x)
becomes,inCNF,
¬American(x)∨¬Weapon(y)∨¬Sells(x,y,z)∨¬Hostile(z)∨Criminal(x).
(cid:74...

### 9.5.2 The resolution inference rule

Theresolutionruleforfirst-orderclausesissimplyaliftedversionofthepropositionalreso-
lution rule given on page 244. Two clauses, which are assumed to be standardized apart so
that they share no variables, can be resolved if they contain complementary literals. Propo-
sitional literals are complementary if one is the negation of the other; first-order literals are
complementaryifoneunifieswiththeneg...

### 9.5.3 Example proofs

Resolution proves that KB|=α by proving that KB∧¬α unsatisfiable—that is, by deriving
the empty clause. The algorithmic approach is identical to the propositional case, described
inFigure7.13,soweneednotrepeatithere. Instead,wegivetwoexampleproofs. Thefirst
isthecrimeexamplefromSection9.3. ThesentencesinCNFare
¬American(x)∨¬Weapon(y)∨¬Sells(x,y,z)∨¬Hostile(z)∨Criminal(x)
¬Missile(x)∨¬Owns(Nono,x)∨...

### 9.5.4 Completeness of resolution

Thissectiongivesacompletenessproofofresolution. Itcanbesafelyskippedbythosewho
arewillingtotakeitonfaith.
We show that resolution is refutation-complete, which means that if a set of sentences Refutation
completeness
is unsatisfiable, then resolution will always be able to derive a contradiction. Resolution
cannot be used to generate all logical consequences of a set of sentences, but it can be us...

### 9.5.5 Equality

Noneoftheinferencemethodsdescribedsofarinthischaptercanhandleanassertionofthe
formx=ywithoutsomeadditionalwork. Threedistinctapproachescanbetaken. Thefirstis
toaxiomatizeequality—towritedownsentencesabouttheequalityrelationintheknowledge
base. We need to say that equality is reflexive, symmetric, and transitive, and we also have
tosaythatwecansubstituteequalsforequalsinanypredicateorfunction. Sowe...

### 9.5.6 Resolution strategies

We know that repeated applications of the resolution inference rule will eventually find a
proofifoneexists. Inthissubsection,weexaminestrategiesthathelpfindproofsefficiently.
Unitpreference Unitpreference: Thisstrategypreferstodoresolutionswhereoneofthesentencesisasingle
literal (also known as a unit clause). The idea behind the strategy is that we are trying to
produceanemptyclause,soitmightbeag...

## Key Entities Mentioned

- Alan Turing
- Herbert Simon

## Algorithms & Concepts

- [[Y algorithm]]
- [[An algorithm]]
- [[This
algorithm]]
- [[The algorithm]]
- [[Logic
Retealgorithm The Rete algorithm]]

## Cross-References

- Previous: [[Chapter 8 - First-Order Logic]]
- Next: [[Chapter 10 - Knowledge Representation]]
- Part: Part III: Knowledge, Reasoning, and Planning

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 9. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
