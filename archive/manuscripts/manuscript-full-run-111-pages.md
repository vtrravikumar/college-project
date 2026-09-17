---
title: "ANALYSIS OF ARTIFICIAL NEURAL NETWORK"
subtitle: ""
author: "RAGUPATHI KUMAR D.; RAVI KUMAR V.T.R."
type: "technical-document"
edition: ""
version: ""
copyright_year: ""
language: "en"
---

<!-- source-document: College-project-01.pdf; profile: prose -->
<!-- source: College-project-01.pdf; page: 1 -->
<!-- source-image: pages/01-College-project-01-page-1.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: layout-visual-verification -->
<!-- review-marker: figure-visual-verification -->

PROJECT REPORT
ON
ANALYSIS OF ARTIFICIAL NEURAL NETWORK
(USING BACK PROPAGATION & GENETIC' ALGOBITUM
Submitted by
KUMARESAN
U
RAGUPATHI KUMAR D.
RAVI KUMAR V.T.R.
ENGINE
SCOLLEGEO
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
J. J. COLLEGE OF ENGINEERING AND TECHNOLOGY
(Affiliated to the Bharathidasan University)
TIRUCHIRAPPALLI - 620 009
NOVEMBER 1998

---

<!-- source: College-project-01.pdf; page: 2 -->
<!-- source-image: pages/01-College-project-01-page-2.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-002/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-002/figure-candidate.png)
<!-- review-marker: layout-visual-verification -->
<!-- review-marker: figure-visual-verification -->

PROJECT REPORT
ON
ANALYSIS OF ARTIFICIAL NEURAL NETWORK
(USING BACK PROPAGATION S GENETIC ALGOBITUM)
Submitted by
U.
KUMARESAN
RAGUPATHI KUMAR D.
V.T.R
RAVI KUMAR
S.COLLEGE DA
COTONHOSE
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
J. J. COLLEGE OF ENGINEERING AND TECHNOLOGY
(Affiliated to the Bharathidasan University)
TIRUCHIRAPPALLI - 620 009
NOVEMBER 1998

---

<!-- source: College-project-01.pdf; page: 3 -->
<!-- source-image: pages/01-College-project-01-page-3.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- review-marker: layout-visual-verification -->

ANALYSIS OF ARTIFICIAL NEURAL NETWORK
(USING BACK PROPAGATION & GENETIC ALGORITHM)
Submitted
KUMARESAN.U
RAGHUPATHI KUMAR.D
RAVI KUMAR.V.T.R
in partial fulfillment of the requirements
for the award of the Degree of
BACHELOR OF ENGINEERING
In
COMPUTER SCIENCE AND ENGINEERING
of the Bharathidasan University.
Department of Computer Science and Engineering
J.J COLLEGE OF ENGINEERING & TECHNOLOGY
(Affiliated to Bharathidasan University)
TIRUCHIRAPALLI - 620 009
NOVEMBER - 1998

---

<!-- source: College-project-01.pdf; page: 4 -->
<!-- source-image: pages/01-College-project-01-page-4.png -->
<!-- structure: prose; confidence: 0.50 -->

VIVA VOCE EXAMINATION
The Viva Voce Examination of the Project work done by RAVIKUMAR V.I.R.
E 451640 (Reg. No) in partial fulfillment of the requirements for the B.E degree in
COMPUTER SCIENCE & ENGINEERING was held on 13 OCTOBER'98
b110198
2210198
INTERNAL EXAMINER
EXTERNAL EXAMINER

---

<!-- source: College-project-01.pdf; page: 5 -->
<!-- source-image: pages/01-College-project-01-page-5.png -->
<!-- structure: prose; confidence: 0.50 -->

CERTIFICATE
This is to certify that the project titled "Analysis of Artificial Neural Network"
is a bonofide work done be by RAVIKUMAR V.T.R. Reg.No E451640 in partial
fulfillment of the requirement for the award of the degree of Bachelor of Engineering
in Computer Science and Engineering during 1994-1998.
Thule
70198
HEAD OF THE DEPARTMENT
PROJECT GUIDE ONE IS

---

<!-- source: College-project-01.pdf; page: 6 -->
<!-- source-image: pages/01-College-project-01-page-6.png -->
<!-- structure: prose; confidence: 0.50 -->

# Acknowledgement
We are thankful to our Director Dr. V. Shanmuganathan
excellent opportunity for taking up the course and providing a
conducive environment to finish our project successfully
We extend our sincere thanks to Prof.S. Ramakrishnan.(System
Manager & Head Of CSE Dept.) for his guidance and suggestions
towards the improvement of our project.
We have immense pleasure in thanking our guide
Miss.Shameem Fathima and our guide Mr. R.Balasubramanian
under whose guidance the project has been shaped in a very
successful manner.
Last but not the least we would like to thank the Technical
support group of our Brainland Computer Centre for providing all
that we needed and staying late in the night for us.
Above all, I express my gratitude to my beloved parents for
shaping me as an Engineer.

---

<!-- source: College-project-01.pdf; page: 7 -->
<!-- source-image: pages/01-College-project-01-page-7.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-007/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-007/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

# Abstract
The aim of the project is to implement a system based on Genetic
algorithm with enhanced encoding. The system is used to evolve
forward Artificial Neural Network which has been applied to problem
areas of boolean functions.
Evolving Neural Network means that optimising of the connection
and connectivity of the Neural Network. Although many techniques like
Back Propagation learning exists, a new approach using Genetic
Algorithm has been tried in this work
Genetic Algorithm is randomised search technique that is domain
free, robust and has a fast rate of convergence. Genetic Algorithm search
methods are rooted in the mechanism of evolution and natural genetics.
They combine survival of the fittest among string randomised information
exchange to form search algorithm with some of the innovative flairs of
human search.
In this project we compare the efficiency of Genetic Algorithm and
Back Propagation Algorithm and observe that Genetic Algorithm are
efficient and robust optimization tools which outperform their counterpart.

---

<!-- source: College-project-01.pdf; page: 8 -->
<!-- source-image: pages/01-College-project-01-page-8.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-008/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-008/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

# INTRODUCTION
## GENERAL
Artificial Neural Net models have been studied for many years on
the hope of achieving human-like performance in various fields to find
number of real world applications. These models are composed of many
non - linear computational elements operating in parallel and arranged
inpatterns reminiscent of biological neural nets. Computational elements
or nodes are connected by weights that are typically adapted during use to
improve performance. There has been a recent resurgence in the field of
Artificial Neural Networks caused by new net topologies, algorithms and
analog VLSI implementation techniques.
Standard techniques exist for training Neural Networks. But
there is still a need for better and efficient techniques to train Neural
Networks.
In the proposed project, this problem has been modelled as
an optimization problem and novell approach called GENETIC
ALGORITHM has been adopted to solve it.

---

<!-- source: College-project-01.pdf; page: 9 -->
<!-- source-image: pages/01-College-project-01-page-9.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-009/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-009/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

## STATE OF THE ART
Currently there are various classical optimization
techniques.
Calculus based methods use a set of necessary and
sufficient conditions to be satisried by the solution of an optimization
problem. This method can be further divided into Direct and Indirect
methods. These techniques can be used only in a restricted set of well.
behaved problem.
Enumerated techniques search every point related to
an objective function's domain space one point at a time. They are simple to
implement but may required significant computation.
Guided random search techniques are based on
enumeration techniques but use additional information to guide the search
They can solve very complete problems. The major sub classes are
Simulated Annealing and Evolutionary Algorithms. Both are evolutionary
processes. But Simulated Annealing on the other hand are based on natural
selection principles. This form of search evolves throughout generations,
improving the features of potential solutions by means of biologically
inspired operations . This in turn subdivided into Evolutionary Strategies
and Genetic Algorithms.

---

<!-- source: College-project-01.pdf; page: 10 -->
<!-- source-image: pages/01-College-project-01-page-10.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-010/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-010/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

GAs came into existence as a result of doctoral dissertion of
Dr.John Holland of university of Michigan, Ann Arbor. Ever since it
gained immense popularity and prominence and have been applied to a
number of areas .A lot of research work have been carried out throughout
the world .David E. Goldberg, prof, General Engineering, University of
Illinois at Urbana-campaign, has been a forerunner of research in GA and
has produced one of the widely referenced text on GA .Dr. Kenneth
Dejong of george Mason University has proposed a test suite that attempts
to formalise the concepts behind the working of GA.
## MOTIVATION OF THE PROJECT
The field of Genetic Algorithm is new and evolving.
It has a wide variety of application.
One of the major problem in constructing any Neural
Network is fixing the inter neuron weight in real - time .Genetic algorithm
to be a useful integration, when not a viable alternative to more common
algorithm such as Backpropagation .So these stood as a cause of motivation
to pursue this project.
## SCOPE OF THE PROJECT
Artificial Neural Network have a spectrum of
practical application in various fields. The work of this project can be
applied for determining the optimal network for any such application.

---

<!-- source: College-project-01.pdf; page: 11 -->
<!-- source-image: pages/01-College-project-01-page-11.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

# PROBLEM DEFINITION AND METHODIOGY
## PROBLEM DEFINITION
The aim of the project is to implement a system based
on Genetic algorithm with enhanced encoding. The system is used to
evolve feed forward. Artificial Neural Network which has been applied to
problem areas of boolean function learning and Robot arm movement.
## METHODOLOGY
A Generic algorithm emulates biological evolutionary
theories to solve optimization problems .A GA consist of set individual
elements ( the population) and a set of biologically inspired operators
defined over the population itself. According to evolutionary theories,
only the most suited elements in a population are likely to survive and
generates offspring , thus transmitting their biological heredity to new
generations. In computing terms, a GA maps a problem onto a set of
(typically binary)strings, each string representing a potential solution. The
GA that manipulates the most promising strings in its search for improved
solution. Thus this concept is applied to a Neural Network design it as an
optimization problem.
First an initial set of individuals are generated, each
representing a concatenated string of weights of the links of a neural
network. Tine each string is evaluated for a fitness solution using the
objective function of calculating the mean squared error by feed forwarding
on the network.

---

<!-- source: College-project-01.pdf; page: 12 -->
<!-- source-image: pages/01-College-project-01-page-12.png -->
<!-- structure: prose; confidence: 0.50 -->

As per the GA the fitter string i.e., one with aless
error will be eligible for survival and the strings of lesser fitness are
omitted from going to next generation. The GA operations like
reproduction, crossover, mutation etc. are applied in every generation and
this process is repeated for a fixed number of generation or until a fittest
solution is evaluated. The string with optimal fitness value will be taken as
final concatenated weight of the links

---

<!-- source: College-project-01.pdf; page: 13 -->
<!-- source-image: pages/01-College-project-01-page-13.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

# EVOLUTIONARY DESIGN CONCEPTS
## INTRODUCTION
Technology periodically steals a leaf from nature's book
Evolutionary design paradigm is one such example. This paradigm is
focused on Genetic Algorithm to explore its advantage over conventional
algorithms while learning neural networks.
## GENETIC ALGORITHM
Genetic Algorithm are essentially robust search algorithm
based on the mechanics of natural selection and natural genetics. They are
best suited for problems having comparatively larger solution spaces. They
use randomized information exchange between solutions to obtain an
optimal solution.
Genetic Algorithms start with a finite set of solution strings
called the initial population and then apply the operators,
Reproduction,
Crossover &
Mutation
These operators are applied repeatedly thereby guiding the
search towards better and better solutions. The power of GA stands in its
ability to exploit historical information to improve future performance.
Moreover the algorithm conducts a parallel search by sampling various
parts of the hyperplane of solution at the same time.

---

<!-- source: College-project-01.pdf; page: 14 -->
<!-- source-image: pages/01-College-project-01-page-14.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

### ALGORITHM INTERNALS
I.GO GAs work by maintaining a population of candidate solutions
to a given problem.. Each solution is stored as an artificial chromosome,
represented by a string of bits,integers or characters(usually represented by
bits). An initial population of solution is created randomly. Only a fixed
number of candidate solutions are transferred from one generation to the
next. Those solutions that are less fit tend to die off( this is done by
selection operation to be discussed later). Successively new solutions are
created by building on the better solution previously encountered( this is
done using crossover and mutation operators explained later) thereby
inducing the search to become successively concentrated in areas of
current optima.
### TERMINOLOGIES USED
Many biological terms are used in the Genetic Algorithm
# literature. The pool of solutions is often called the "population", individual
strings in the pool are "chromosome", individual features are "genes" and
the value of the feature in a particular solution is "allele".
Example don In a particular problem, a variable x to be optimized is
evolved using 4-bit encoded string. The illustration of strings during some
intermediate step is shown in the table
X3
X4
# X2

---

<!-- source: College-project-01.pdf; page: 15 -->
<!-- source-image: pages/01-College-project-01-page-15.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

### THE ALGORITHM
#### PSEUDOCODE
The Genetic Algorithm pseudo code is given as,
Initialise population POPIO].
Evaluate population POPIOI.
Generation =1.
While termination criterion not reached
Select solutions for POPIGeneration]
from POPIGeneration-1].
Perform Crossover on POP[Generation].
Perform Mutation on POP[Generation].
Evaluate POPIGeneration].
Generation = Generation + 1
#### OVERVIEW
The initial population is usually created randomly.
Individual members of the population i.e., chromosomes are selected for
the next generation in proportion of their fitness, the measure of how near
the particular solution is form the optimal solution. Two parent
chromosomes are altered using generic operator to produce two children.
The resultant children are each evaluated and assigned a fitness value.
Next, the strings of old population is replaced by the new fittest string and
the process is repeated. The stopping criterion can be maximum number of
iteration, convergence or reaching an acceptable fitness level.

---

<!-- source: College-project-01.pdf; page: 16 -->
<!-- source-image: pages/01-College-project-01-page-16.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- review-marker: layout-visual-verification -->

DIAGRAMATIC ILLUSTRATION:
The working of GA can be illustrated diagramatically as in
figure
Offsprings
Decoded strings
Population
(Chromosomes)
New
Generation
Evaluation (Fitness)
Genetic Operators
Parents
Selection
Reproduction
Manipulation Mates
Thus a GA has the following components,
a population of binary strings
control parameters.
a fitness function.
genetic operators.
a selection mechanism &
a mechanism to encode the solution as binary
strings.

---

<!-- source: College-project-01.pdf; page: 17 -->
<!-- source-image: pages/01-College-project-01-page-17.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-017/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-017/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

#### OPERATORS DESCRIPTION
SELECTION OPERATOR
Selection models nature's "survival of the fitness"
mechanism. Fitter solution survive while weaker one perish. It can be done
using a ranking method, roulette wheel selector or by tournament selection.
In roulette-wheel selection, each chromosome is assigned a
pie-shaped slice on a roulette-wheel where the size is proportional to the
fitness of the individual chromosome. The spin is simulated by gencrating
and the total of individual fitness. The winning chromosome is the one in
whose slice the roulette spinner ends up.
In rank based selection, two individuals are chosen using
roulette wheel and the member with higher fitness is selected.
In tournament selection, a set of individuals are sequentially
chosen, and the member with the highest fitness is added to the mating
pool.
CROSSOVER OPERATOR
The purpose of cross over is to create children whose genetic
material resembles their parent's genes in some fashion. Thus is done with
a hope that a child will have better features of both of its parents.
A simple, one-point crossover between two individuals
proceed in two steps. First, a cross site along the string length is chosen
uniformly at random. Then the position values are exchanged between the
two strings following the cross site

---

<!-- source: College-project-01.pdf; page: 18 -->
<!-- source-image: pages/01-College-project-01-page-18.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-018/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-018/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

For example, if two selected strings are,
A1111
B= 00000000
If the random choice of cross site turns out to be three, the two new
strings got are,
C=11100000
D=00011111
following the crossover operation.
There are other two types of crossover namely multipoint
crossover, partially matched crossover useful for particular application.
MUTATION OPERATOR
It is the occasional alteration of a chromosome like flipping a
bit which has a low probability. Mutation is used to rejuvenate the search,
extending the search into previously unexplored areas. It also helps in
restoring lost genetic material.
For example, if all the strings in a population have converged
to zero at a given position and the optimal solution has a one at that
position. Then crossover cannot generate a one there, while mutation
could.
#### PROBLEM DEPENDENT ISSUES
The remaining components apart from the operators are
grouped under problem dependent issues as they can be decided upon the
given problem.

---

<!-- source: College-project-01.pdf; page: 19 -->
<!-- source-image: pages/01-College-project-01-page-19.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-019/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-019/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

They are,
Encoding mechanism - Representation of the problem as a string of digits
Fitness
- A means of evaluating individual potential
solutions.
Control parameters - The specification of problem parameters.
ENCODING MECHANISM
Fundamental to GA structure is the encoding mechanism for
representing the optimization variables. The encoding mechanism depends
upon the number of variables and the range of values taken by the
variables. The length of the binary string is determined for each variables
depending on its range. The bit strings for all the variables are usually
concatenated and used. Sometimes, if they are real valued continuous
variables, it linearly mapped and it is encoded using fixed number of bits
FITNESS FUNCTION:
In Generic Algorithm, the fitness value of each chromosome
has to be evaluated. For this, a fitness function is needed. This function
should return a value that is indicative of how good the solution string is.
The fitness returned is high for fitter strings and low for worse ones.
Obviously, it should return the highest value for an optimal string. Thus
fitness function is problem dependent. For example, in a LPP with a
maximising objective function, the objective function can be used as fitness
function.

---

<!-- source: College-project-01.pdf; page: 20 -->
<!-- source-image: pages/01-College-project-01-page-20.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-020/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-020/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

FIXUP OF CONTROL PARAMETERS
The parameters of GA like probabilities of crossover and
mutation, number of generations, population size and the length of strings
are decided based on problem domain
## COMPARISION WITH OTHER TECHNIQUES
In order for GA to surpass their more traditional
cousins in the quest for robustness, GA must differ in some very
fundamental ways.
Genetic algorithms are different from more normal
optimization search procedures in the following ways.
Advantages:
GAs works with a coding of the parameter set, rather than the
parameter themselves.
* GAs search from a population of points, rather than from a
single point.
* GAs use payoff(objective function) information and not
derivatives or other auxiliary knowledge.
* GAs make use of probabilistic rather than deterministic
transition rules.

---

<!-- source: College-project-01.pdf; page: 21 -->
<!-- source-image: pages/01-College-project-01-page-21.png -->
<!-- structure: prose; confidence: 0.50 -->

Disadvantages:
* The lack of an accurate measure of their convergence to the
optimum and their intuitive nature as opposed to other proven and well
established methods.
* The loss of accuracy while approximating the solution string for
the sake of representability in digital computers.
# Conclusion
GAs are efficient and robust optimization tools which
outperform their counterparts. They are applied in search, optimization
and machine learning. They have their own drawbacks owing to the
limited nature of digital computers in terms of computational power,
storage and the lack of formal proof of the facts behind their working

---

<!-- source: College-project-01.pdf; page: 22 -->
<!-- source-image: pages/01-College-project-01-page-22.png -->
<!-- structure: prose; confidence: 0.50 -->

# DESIGN OF ANN EVOLUTION USING GA
## INTRODUCTION
Artificial neural systems are characterised by a set of nodes
and interconnecting links. Given an application, a Neural Network has to
be trained to learn to correlate a given input to an output. In this chapter, it
has been shown how GA can be applied to designing and training a neural
Networks.
Evolutionary learning for ANNs has been introduced to
perform a global exploration of the search space, thus avoiding the
problem of stagnation that is characteristic of local search procedures.
## NEURAL NETWORK DESIGN PROBLEM
The problem is to determine an optimal network structure
and optimal set of weights of connection of the structure for a given
application. More clearly the problem involves two sub problems.

---

<!-- source: College-project-01.pdf; page: 23 -->
<!-- source-image: pages/01-College-project-01-page-23.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

### DETERMINING THE NEURAL NETWORK
ARCHITECTURE
A fully connected Neural Network may contain some links
which will not affect its performance. These redundant links can be
pruned.
Thus an optimal Neural Network in terms of number of links
has to be obtained. Such a network will be cost-effective and will work ]
better.
### DETERMINING THE SET OF WEIGHTS
In a Neural Network, knowledge is stored in the weights of
its links. Finding an optimal set of weights for the links of a Neural
Network that produces the least deviance of the actual output from the
desired output completes the Neural Networks design.
## APPLICATION OF EVOLUTIONARY DESIGN PRINCIPLES
TO NN DESIGN PROBLEM
As said earlier, the NN design problem cosists of optimizing
connections and weights of the network. Since, evolutionary design
procedures are essentially optimizing tools, it is high time now to get into
the details of how they can be applied to solve the NN design problem.
The two major design issues, as elucidated in last chapter are
addressed for the problem at hand as follows:-

---

<!-- source: College-project-01.pdf; page: 24 -->
<!-- source-image: pages/01-College-project-01-page-24.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/01-College-project-01/page-024/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/01-College-project-01/page-024/figure-candidate.png)
<!-- review-marker: figure-visual-verification -->

### STRING REPRESENTATION OF SOLUTIONS
The string representation for the two optimization problems
i.e. weights and connections are separately discussed below:
#### WEIGHT OPTIMIZATION
The objective of the problem is to determine an optimal set of
weights for the network links. Since there are as many weights as the
number of links in a network, to put in optimization jargon, there are that
many decision variables to optimize. Thus a single solution string must be
able to represent all the weights of the network so that GA can optimize
them at a stroke. To make this possible, a string is chosen which is a
concatenation of encoded weights of all the links of the network.
In the process of encoding the weights, the following,
problem specific details are considered.
DISCRENTIZATION
Typically, NN weights are real numbers. To encode them
into binary strings, the procedure of discretiozation in which these
weights are scaled by proper factor (power often) is adopted, so as to
convert them into integers. These integers are then converted into binary
numbers. The following example illustrates the procedure.

---

<!-- source-document: College-project-02.pdf; profile: prose -->
<!-- source: College-project-02.pdf; page: 1 -->
<!-- source-image: pages/02-College-project-02-page-1.png -->
<!-- structure: prose; confidence: 0.50 -->

Let the weight be 2.63.
Assuming a scaling factor of 100 i.e. 10 the scaled weights
will be 263. The binary equivalent of it is 11111101.
EXCESS NOTATION
Ingeneral, NNweights can take both positive and negative
values. In order to accommodate for this an "excess notation" for
representing the weights is used. In this notation number that fall in the
range -x to +x are mapped on to the range 0 to 2x.
E For example if the weight falls within the range of -4.5 to
+4.5, it will be linearly mapped onto a value in the range O to +9
FIXING THE RANGE
The first question that stems in one's mind while encoding
the weights is on the decision on the number of bits to be used for the
representation. The possible range of values that the weights take is the
sole factor that determines this.

---

<!-- source: College-project-02.pdf; page: 2 -->
<!-- source-image: pages/02-College-project-02-page-2.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

#### CONNECTIVITY OPTIMIZATION
For optimising the number of links, the presence or absence
ofthe links are encoded into the string. The string length will be equal to
the number of links in the network. Link presence is indicated by a 1 and
the absence by a 0 in the corresponding bit in the string.
### FITNESS FUNCTION ONE
The goodness of the solution the NN design problem is
determined by the deviance of the actual performance from the desired
performance of the network. In general, the fitness function measures their
goodness
#### WEIGHT OPTIMIZATION
For the weight optimization problem, each member of the set
of weights that is represented by a solution string, is assigned to a
corresponding link in the network. Then, the network is run in a feed
forward fashion with training data. For each input output pair of the
training data, the net error of the network is calculated by summing up the
squared errors of the output nodes of the network. The resultant error is
the sum of the squared net errors of the samples. The objective is to
minimise this resultant error. Here GA minimises the fitness function and
the fitness function is devised as,
F(C) = ERR(C)
F(C) = Fitness of the individual chromosome.
ERR(C) = Error of the individual chromosome.

---

<!-- source: College-project-02.pdf; page: 3 -->
<!-- source-image: pages/02-College-project-02-page-3.png -->
<!-- structure: prose; confidence: 0.50 -->

#### CONNECTIVITY OPTIMIZATION
In the connectivity optimization problem, the fitness of a
given set of links is determined by the quickness with which the weights of
the links that are present in the network are optimised. To put this in
precise terms, consider a population of network architecture with different
sets of links. Each of these network is run for a fixed number of
generations. The minimised error at the end of this process in each case is
noted. Fitter architecture is the one having less error.
APPLICATION
& RESULTS

---

<!-- source: College-project-02.pdf; page: 4 -->
<!-- source-image: pages/02-College-project-02-page-4.png -->
<!-- structure: prose; confidence: 0.50 -->

# APPLICATIONS AND RESULTS
## BENCH-MARKING APPLICATION
### BOOLEAN FUNCTION LEARNING
The problem dealt here are toy applications which are often used for testing and
bench marking a network. Typically the training set contains all possible input
patterns, so there is no question of generalisation.
The result obtained when training using Back propagation Algorithm and that using
Genetic Algorithm are given in this sub-division.
### RESULTS OF BP AND GA EVOLUTION
EXCLUSIVE OR
Problem Definition :
The problem is to produce the output which is the XOR function of the given
input value.
Parameters Of WIN :
The initial configuration is, two nodes in the input layer two nodes in the first
hidden layer, two nodes in the second hidden layer, and single node in the output layer.
The network is fully connected

---

<!-- source: College-project-02.pdf; page: 5 -->
<!-- source-image: pages/02-College-project-02-page-5.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- review-marker: layout-visual-verification -->

Optimal set ofweights
Links
weights
2.081
5.732
.1.013
5.564
.4.215
# 836
# 337
-5. 538
-5.689
4.210
OUTE
Neural Network For Exclusive OR
All weight of the links contribute to the network

---

<!-- source: College-project-02.pdf; page: 6 -->
<!-- source-image: pages/02-College-project-02-page-6.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- review-marker: layout-visual-verification -->

Parameter of GA :-
100
Chromosome length
25
Population size
1400
No. of generation
0.9
Probability of cross over
Probability of mutation
0.04
-5.58,5,8
Range of weights
Training Data :-
OUTPUT
INPUT
0
two node
Optimal set of weights & links :-
Optimal set oflink

---

<!-- source: College-project-02.pdf; page: 7 -->
<!-- source-image: pages/02-College-project-02-page-7.png -->
<!-- structure: prose; confidence: 0.50 -->

Time comparison of GA & BP! -
# secs
[Time taken for training using BP
# secs
Time taken for training using GA
THREE BIT PARITY
Problens denition
The problem is to produce an output of 1 if there is an odd number of Is in
the input pattern. O otherwise
Darameters Of NIN
The initial configuration is, three nodes in the input layer, two nodes in the first hidden
layer, two nodes in the second hidden layer and a single node in the output layer. The
network is not fully connected
Parameters of GA
132
Chromosome length
30
Population S1ze
1000
No. of generation
Probability of cross over 0.
0.09
Probability of mutation
-12, 12
Range of weights

---

<!-- source: College-project-02.pdf; page: 8 -->
<!-- source-image: pages/02-College-project-02-page-8.png -->
<!-- structure: layout; confidence: 0.80 -->
<!-- review-marker: layout-visual-verification -->

Training data :-
INPUT
OUTPUT
Optimal set of weights & links
Optimal set of link
111011110111
Optimal set of weights
weights
Links
-3187
7.34
-6.41
0.00
6.21
-4.63
155
-5.03
0.00
-0.07
5.09
-1.85
12

---

<!-- source: College-project-02.pdf; page: 9 -->
<!-- source-image: pages/02-College-project-02-page-9.png -->
<!-- structure: prose; confidence: 0.50 -->

Neural Network For Exclusive OR
Weights of links 4,9, are zero & others are non zero. So the link with zero weights are
pruned from the network.
Time comparison of GA & BP: -
Ting secs
Time taken for training using BP
# secs
Time taken for training using GA

---

<!-- source: College-project-02.pdf; page: 10 -->
<!-- source-image: pages/02-College-project-02-page-10.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: diagram-visual-verification -->

DECODER
Problem Definition:-
The problem involves, producing the output which is the decoded values
of the given input.
Parameters of NN:-
The initial configuration is, three nodes in the input layer, two nodes in the
first hidden layer, two nodes in the second hidden layer and three node in
the output layer. The network is not fully connected.
Parameters of GA: -
chromosome length
170
Population size
25
No. of generation
1900
Probability of cross over
0.5
Probabilit of mutation
0.01
RanGe of weights
-12,12
Training Data :-
INPUT
OUTPUT
0
0

---

<!-- source: College-project-02.pdf; page: 11 -->
<!-- source-image: pages/02-College-project-02-page-11.png -->
<!-- structure: prose; confidence: 0.50 -->

Optimal set of weights & links :-
Optimal set of link
Optimal set ofweights
links
weights
.7.27
0.00
.5 02
-11.55
3.45
0.00
2.92
8.18
.9.61
0.00
-2.38
8.28
-6.5
2.57
-2.05
5.09
Neural Network For Exclusive Decoder problem
Weights of link 2,6,10 are zero others are all non zero

---

<!-- source: College-project-02.pdf; page: 12 -->
<!-- source-image: pages/02-College-project-02-page-12.png -->
<!-- structure: prose; confidence: 0.50 -->

Time Comparison of GA & BP !-
# secs
Time taken for training using BP
# secs
Time taken for training using GA
# Conclusion
Thus the results of both, training using a Back propagation Algorithm and
that with a genetic Algorithm infers that the GA has a faster rate of convergence
than a conventional training algorithm.
## REAL-WORLD APPLICATOIN
5,2.1 ROBOT INVERSE KINEMATIC PROBLEM
#### INTRODUCTION
Although Neural Networks applicable to the solution of robotics control
problem are in fect, neuro controllers, their function is specialised mainly to provide
solution to robot arm movement problems. Robot kinematics involves the study of
the geometry of manipulator linkages, kinematics if fundamental importance for
robot design and control

---

<!-- source: College-project-02.pdf; page: 13 -->
<!-- source-image: pages/02-College-project-02-page-13.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

#### PROBLEM DEFINITION
OVERVIEW
Trajectory control of robotics manipulator traditionally consists of following a
pre-programmed sequence of end effector movements Robot control usually requires
control signals applied at the joints of the robot while the desired trajectory, or the
sequence of arm end positions, is specified for the end effector. The geometry of an
idealised planar robot manipulator with 2 degrees of freedom below.
82
01, 02 - Joint Angles
81
The Robot arms operate in a plane. To make the arm move, desired coordinates
of the end effector point (x,y) are fed to the robot controller so that it generates the joint
angle (01,02) for the motors that move the arms. To perform end effector position control
of a robotics manipulator Inverse kinematics problem need to be solved.
THE PROBLEM
Given the Cartesian coordinates of the end effector, the problem is to map
this coordinate to the angle by which the links of the robot manipulator have to be moved
to reach that point. There are mathematical formulae for this mapping in terms of inverse
trigonometric function. The real time computation of these formulae is time consuming
Instead of using them, a NN is designed which was trained using sufficient number of
training patterns for a given path manipulator

---

<!-- source: College-project-02.pdf; page: 14 -->
<!-- source-image: pages/02-College-project-02-page-14.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

#### PROBLEM DOMAIN-DEPENDENT DETAILS
The robot is assumed to have 2 degree of freedom and hence two link s. It is
a polar configuration robot (R-R Configuration). Now the problem is to map a Cartesian co-
ordinated (x,y,) to the (01,02). of the two links. So inputs is (x,y) and the output is (01,02).
#### WEIGHT OPTIMATION
#### FIXING THE GA PARAMETERS
To decide about the exact number of nodes, the range of weights of links
between the nodes and the various parameters, initially experiments have been done
with a 3-layered fully not connected network. While training the network, that is
optimizing its weights with the weight optimization module, many variation have
been tried out and promising experimental results are found. The are discussed below:-
ADAPTIVE MUTATION
When sufficient diversity is not in the current population, mutation
probability will be increased so as to diversify the population.
BI CROSSOVER
Two sets of population are maintained and for crossover, the two parents are
chosen one from each of the 2 sets. GA tries to evolve children that have good features
of the 2 sets.
FIXING THE RANGE OF WEIGHTS
When a fully connected three layered network is subjected to weight
optimization the decision about the range of weights influences the convergence of
the training of the network. For the robot inverse kinematics problem many experiments
have been conducted with various range and the best has been found.

---

<!-- source: College-project-02.pdf; page: 15 -->
<!-- source-image: pages/02-College-project-02-page-15.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.65; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

FIXING THE POPULATION SIZE
Population size is an important GA parameter that influences the parallelism
ofGA search. Experiments with various population size have been done for
choosing the best size.
#### CONNECTIVITY OPTIMIZATION
Having fixed the parameters of the network and the weight optimization module,
one can now embark on the task at hand. Here a two step connectivity optimization
is adopted.
In the first step, a population of network architecture is evolved. The criterion is that,
cach architecture should have different set of connection
While evaluating each of the architecture, the weights optimization module is called
and the quickness with which the architecture settles to an optimal set of weights is
measured. Actually, The weight optimization module is run for a fixed number of
generations for each of the architecture. More fitness is assigned to the architecture
that settles to less error.
Finally the weights of the network with optimal connections are optimized
by applying the weight optimization module for sufficient number of generation.
Parameter of NN
The initial configuration is, eight nodes in the input layer, two nodes in
the first hidden layer, two nodes in the second hidden layer and one node in the output
The network is not fully connected.
layer.

---

<!-- source: College-project-02.pdf; page: 16 -->
<!-- source-image: pages/02-College-project-02-page-16.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: diagram-visual-verification -->

Parameters of GA !-
128
Chromosome length
30
Population size
500
No. of generation
0.4
Probability of cross over
0.01
Probability of mutation
1.5.1.5
Range of weights
Training Data :
Ipput
Output
02
y
81
0.290889
2.9386
0.174533
8.40739
0.32725
0.19635
8.25326
3.28037
0.374
8.0309
0.2244
3.70669
0.436333
7.69392
4.24922
0.2618
0.5236
0.31416
7.14987
4.9518
0.6545
5.86087
0.3927
6.19551
0.872667
6.92405
0.5236
4.33232
optimal set of weights & links :-
Optimal set of link
111011101111110

---

<!-- source: College-project-02.pdf; page: 17 -->
<!-- source-image: pages/02-College-project-02-page-17.png -->
<!-- structure: prose; confidence: 0.50 -->

Optimal set ofweights
links
weichts
-1.11
0.39
-0.37
nAn
-0.73
0.6
nAn
053
063
-15
- 1.42
0.03
0.95
-0.78
16
0.00
Neural Networks for Robot kinematics problem
Weights of link 4,8, 11, 16 are zero & others are non-zero. So that the link with zero
weights can be pruned from the network.
Summed Error: 0.000208

---

<!-- source: College-project-02.pdf; page: 18 -->
<!-- source-image: pages/02-College-project-02-page-18.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- review-marker: layout-visual-verification -->

## CONCLUSION
Evolutionary design concepts have been successfully applied to
design and to train Neural Network. The results that are obtained confirm the fact
that Genetic Algorithm is better tool to train a Neural Network than conventional
training tools.
# Conclusion

---

<!-- source: College-project-02.pdf; page: 19 -->
<!-- source-image: pages/02-College-project-02-page-19.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

# CONCLUSION
## INTRODUCTION
GAs have shown to be good optimizers for solving problems
of NNs. In this chapter future enhancements are given and concluding
remarks are done.
## HIGHLIGHTS OF THE WORK
A system based on Evolutionary design concepts to train
Neural Networks has been successfully developed, and promising results
have been obtained. In this process the following observations are done:-
GAs converge quicker to the optimal solution if there is
diversity is not guaranteed for all generation and to boost the diversity,
adaptiveness was used. This was done by reinitialising the population and
increasing the rate of mutation.
Parameter tuning is one of the most critical issue relating to
both NN training to both NN training and GAs. The effect of varying,
certain important parameters has been thoroughly studied and results have
been shown in the form of tables and results.
The performance of the GA as an optimization tool for
training and designing NNs is very good and is comparable to that of the
available standard techniques.

---

<!-- source: College-project-02.pdf; page: 20 -->
<!-- source-image: pages/02-College-project-02-page-20.png -->
<!-- structure: prose; confidence: 0.50 -->

It can be concluded that GAs can be applied to solve any
optimization problem equally well. Application of Evolutionary concepts
to Neural architecture is one such example. It is sure that there are lot more
vistas to be explored.
## FUTURE ENHANCEMENT
There are many parameters in GA that can be manipulated
and for each and every combination of the parameters, there will be some
marked improvement in performance. More study can be made on the
impact of these parameters on the GAs performance and the result can be
used suitably.
Parallelism can be increased by using distributed GAs. Here
multiple copies of GAs are run in parallel and from time to time, best
solution are exchanged.

---

<!-- source: College-project-02.pdf; page: 21 -->
<!-- source-image: pages/02-College-project-02-page-21.png -->
<!-- structure: prose; confidence: 0.50 -->

# References
D.E.Golberg, "Genetic Algorithm in Search Optimization and Machine
learning", Addison Wesley, 1989.
[21
Jacek M. Zarada," Introduction to Artificial Neural Systems" ,Jaico
publishing India, 1991
[3]
James A. Freeman & David M.Skapura,"Neural Network Algorithm,
Applications and Programming techniques". Addison Wesley. 1991.
[4]
Darrel Whitely, Timothy Starkweather & Chris Bogart," Genetic
Algorithms and Neural Networks : Optimising Connections anc
Connectivity", Parallel Computing, 14(1990) pp 347-361.
[5]
Daniel Graupe, "Principles of Artificial Neural Network", World Scientific
Publication Co. Pte. Ltd.
[6]
Chin-Teng Lin & C.S George Lee, "Neural Fuzzy System".
[71
LiMin Fu, "Neural Networks in Computer Intelligence",McGraw Hill
International.
APPENDI

---

<!-- source: College-project-02.pdf; page: 22 -->
<!-- source-image: pages/02-College-project-02-page-22.png -->
<!-- structure: prose; confidence: 0.50 -->

# Appendix

---

<!-- source: College-project-02.pdf; page: 23 -->
<!-- source-image: pages/02-College-project-02-page-23.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.65; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

COUNTER PROPAGATION NETWORKS
INTRODUCTION:
The Counterpropagation network developed by Robert
Hecht Nielsen goes beyond the representational limits of single - layer
networks. As compared to Backpropagation, it can reduce training time by
hundredfold Counter propagation is a combination of two well-known
algorithms; the self - organizing map of Kohonen and the Grossberg The
Counter propagation network functions as a look-up table capable of
generalization. The training process associates input vectors with
corresponding output vectors. These vectors may be binary consisting of
ones and zeros, or continuous. Once the network is trained application of
an input vector produces the desired output vector. The generalization
capability of the network allows it to produce a correct output even when
it is given an input vector that is partially incorrect. This makes the
network useful for pattern -recognition, pattern - completion, and signal -
enhancement applications.

---

<!-- source: College-project-02.pdf; page: 24 -->
<!-- source-image: pages/02-College-project-02-page-24.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

NETWORK STRUCTURE:
The neuron in layer O serve only as fan - out points and
perform no computation. Each layer O neuron connects to every neuron in
layer 1 (called the KOHONEN LAYER) through a separate weight Wmin
these will be collectively reffered to as the weight matrix W. Each neuron
in layer 1 is connected to every neuron in layer2 (called the GROSSBERG
LAYER) by a weight Vnp ;these comprise the weight matrix V.
Input
Kohenen
Grossherg
Laver
layer
LaveL
- Y1
- 72 6
Desired output
# Kn
‡ Ga
- In e
Kohenen
Grossnera
Neurons
Feedfortrard Counterpropagation Network
Counter propagation functions in two modes; the
NORMAL MODE, in which it accepts an input vector X and produces an
output vector Y, and the TRAINING MODE in which an input vector is
applied and the weights are adjusted to yield the desired output vector

---

<!-- source-document: College-project-03.pdf; profile: prose -->
<!-- source: College-project-03.pdf; page: 1 -->
<!-- source-image: pages/03-College-project-03-page-1.png -->
<!-- structure: prose; confidence: 0.50 -->

NORMAL OPERATION:
The Kohonen laver :
The Kohonen layer functions in a 'winner- take -all fashion';
that is, for given input vector, one and only one Kohonen neuron outputs a
logical one; all other outputs are zero. Associated with each Kohonen
neuron it to each input Kohonen neuron K1 has weights
wIl,w21,.. wm1, comprising a weight vector WI.These connect by
way of the input layer to input signals x1,×2,.....xm,comprising the input
vector X. As with neurons in most networks, the NET output of each
Kohonen neuron is simply the summation inputs . This may be expressed as
follows:
.............tWmiXm
NET j = wljx1+w2ix2+
where NET i is the NET output of kohonen neuron j
NET j = xiwij
or in vector notation
N= XW
where N is the vector of Kohonen layer NET ouputs.
The Kohonen neuron with the largest NET value is the 'winner'. Its
output is set to one; all others are set to zero.

---

<!-- source: College-project-03.pdf; page: 2 -->
<!-- source-image: pages/03-College-project-03-page-2.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

Grossberg Laver:
The Grossberg layer functions in a familiar manner. Its
NET output is the weighted sum of the Kohonen layer outputs
k1.k2.k3.
..kn, forming the vector K. The connecting weight vector
designated V consists of the weights v11, v21, .....p. The NET output
of each Grossberg neuron is then
NET i = kiwii
where NET j is the output of the Grossberg neuron j, or in vector form
Y=KV
where Y= the Grossberg - layer output vector
K=the Kohonen - layer output vector
V= the Grossberg layer weight matrix
If the Kohonen layer is operated such that one neuron's
NET is at one and all others are at zero, only ane element of the K vector
is nonzero, and the calculation is simple. The only action of
each neuron in the Grossberg layer is to output the value of the weight that
connects it to the single nonzero Kohonen neuron.
TRAINING THE KOHONEN LAYER:
Kohonen training is aself - organizing algorithm that
operates in the supervised mode. For this reason, it is difficult to predict
which specific Kohonen neuron will be activated for a given input vector.
It is only necessary to ensure that training separates input vectors.

---

<!-- source: College-project-03.pdf; page: 3 -->
<!-- source-image: pages/03-College-project-03-page-3.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

Preprocessing the Input Vectors :
It is highly to normalize all input vector before applyingthem
to the network. This is done by dividing each component of an input vector
by that vector's length. This length is found by taking the square root of the
sum of the squares of all of the vector's components . In symbols
Xi'= Xi /(X1^2+X2^2 + hmmm+ Xn^2)^1/2
This converts an input vector into a unit vector pointing in
the same direction ;that is, a vector of unit length in n-dimensional space.
ring To train the Kohonen layer, an input vector is applied and
its dot product is calculated with the weight vector associated with each
Kohonen neuron. The neuron with the highest dot product is declared the
"winner " and its weighta are adjusted Because the dot product operation
used to calculate the NET values is a measure of similarity between the inut
and weight vectors the training process actually consists of selecting the
Kohonen neuron whose weight is most similar to the input vector, and it
still more similar. The network self - organizes so that a given Kohonen
neuron has maximum output for a given input vector: The training
equation that follows is used
Wnew = Wold + (x - Wold )
where
Wnew = the new value of a weight connecting an input
component x to the winning neuron
Wnew = the previous value of this weight

---

<!-- source: College-project-03.pdf; page: 4 -->
<!-- source-image: pages/03-College-project-03-page-4.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

= a training rate coefficient that may vary during the training
process
Each weight associated with the winning Kohonen neuron is
changed by an amount proportional to the difference between its value and
the value of the input to which it connects The direction of the change
minimizes the difference between the weight its input. The variable is a
training rate coefficient that usually starts out at 0.7 and may be gradually
reduced during training. This allows large intial steps for rapid, coarse
training and smaller steps as the final value approached .
If only one input vector were to be associated with each
Kohonen neuron, the Kohonen layer could be trained with a single
calculation per weight. The weights of a winning neuron would be made
equal to the components of the training vector (=1_ Usually the training
set includes many input vectors that are similar and the network should be
trained to activate the same Kohonen neuron for each of them. In this
case, the weights of that neuron should be the average of the input vectors
that will activate it. Setting to a low value will reduce the effect of each
training step, making the final value an average of the input vectors to
which it was trained. In this way, the weights associated with a neuron will
assume a value near the "center" of the input vectors for which that neuron
is the "winner".

---

<!-- source: College-project-03.pdf; page: 5 -->
<!-- source-image: pages/03-College-project-03-page-5.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

Interpolative Mode:
In the interpolative mode, a group of the Kohonen neurons
having the highest outputs is allowed to persent its outputs to the
Grossberg layer. The number of neurons in this group must be chosen for
the application, and ther is no conclusive evidence regarding an optimum
size Once the group is determined , its set of NET outputs is treated as a
vector and normalized to until length by dividing each each NET value by
the squareroot of the sum of the squares of the NET values in the group.
All neurons not in the group have their outputs set to zero.
TRAINING THE GROSSBERG LAYER
An input vector is applied, the Kohonen outputs are
established, and the grossberg outputs are calculated as in normal
operation. Next, each weight is adjusted only if it connects to a Kohonen
neuron having a nonzero output. The amount of the weight adjustment is
proportional to the difference between the weight and desired output of the
Grossberg neuron to which it connects. In symbols
Vij=Vij old + (Yj -Vij ) Ki
Ki = the output of Kohonen neuron i (only one Kohonen neuron
where
is nonzero )
Yj = component j of the vector of desired outputs
Initially is set approximately 0.1 and is gradually reduced
as training progresses.

---

<!-- source: College-project-03.pdf; page: 6 -->
<!-- source-image: pages/03-College-project-03-page-6.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

The weights of the grossberg layer will converge to the
average values of the desired out whereas the weights of the Kohonen
layer are trained to the average values of the inputs. Grossberrg training is
supervised; the algorithm has a desired output to which it trains. The
unsupervised, self - organising operation of the Kohonen layer produces
outputs at indeterminate positions;these mapped to the desired output of
the Grossberg layer.
APPLICATION:
In addition to the usual vector - mapping functions ,counter
propagation is useful in Data Compression. Acounter propagation network
can be used to compress data prior to transmission, there by reducing the
number of bits that must be sent Suppose an image to transmitted. It can
be divided into subimages S Each subimage is further sudivided into
pixels (picture elements ). Each subimage is then a vector, the elements of
which are the pixels of which are the pixels of which the subimage is
composed. For simplicity, assume that each pixel is either one (light) or
zero (dark) If there are n pixels in asubimage If there are n pixels in
asubimage, then n bits will be required to transmit it. If some distortion
can be tolerated, substantially fewer bits are actually required to transmit
typical images, thereby allowing an image to be transmitted rapidly. This
is possible because of the statistical distribution of sub image vectors. Some
occur frequently while others occur so seldom that they can be

---

<!-- source: College-project-03.pdf; page: 7 -->
<!-- source-image: pages/03-College-project-03-page-7.png -->
<!-- structure: prose; confidence: 0.50 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: figure-visual-verification -->

approximated roughly. The method of vector quantisation finds these
shorter bit strings that best represent subimages
A Counter propagation network can be used to perform
vector quantisation. The set of subimage vectors is used as input to train
the kohonen layer in the accertive mode in which only a single neuron is
allowed to be 1. The Grossberg weights are trained to produce the binary
code of the index of the Kohonen neuron that is 1. For example, if
Kohonen neuron 7 is 1 (and the others are all 0), the Grossberg layer will
be trained to output 00...
..000111 (the binary code for 7 ). It is this
shorter bit string is transmitted.
At the receiving end, an identically trained
counterpropagation network accepts the binary code and produces the
inverse function, an approximation of the original subimage.
This method has been applied both to speech and images,
yielding dat compression ratios of 10:1 to 100:1. The quality has been
acceptable, however some distortion of the data at the receiving end is
inevitable.
ROE CODE LISTINI
SOT

---

<!-- source-document: Code-01.pdf; profile: code -->
<!-- source: Code-01.pdf; page: 1 -->
<!-- source-image: pages/04-Code-01-page-1.png -->
<!-- structure: prose; confidence: 0.50 -->

PROGRAM TO TRAIN AND TEST NEURAL NETWORK USING
GENETIC ALGORITHM
, INCLUDING OF HEADER FILES
#include Sstdio.h>
#include <math.h>
#include «stdlib.h>
#include <string.h>
#include <alloc.h>
#include <dos.h>
#include <time.h>
#include «floath>
#include <conio.h>
include <graphics.h>
"I DEFINITION OF GA PARAMETERS
#define MAXPOP 50
#define MAXSTR 100
#define CHROMLEN 10
#define MAX 10
#define NODEO 2
#define NODE1 2
#define NODE2 2
#define NODE3 1
#define NCLS 4
#define CONCN 10
#define MERR .20
#define thres 0.2

---

<!-- source: Code-01.pdf; page: 2 -->
<!-- source-image: pages/04-Code-01-page-2.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
" DEFINITION FOR TIMING CALCULATION
al=t1.ti hour;!
#define starttime
a2=t1.ti min: I
a3=t1.ti sec:
#define stoptime b1=12.ti_hour; I
b2=12.ti min; I
b3=t2.ti sec; \
c1=(b1-al);\
c2=(b2-a2); 1
c3=(b3-a3); 1
c = (((c1*60)+c2)*60+3); 1
timetaken = c;
" INITIALISE REGISTER
union REGS i,o;
/ DEFINE THE STRUCTURES
typedef struct {
int allele;
} gene;
typedef gene chromosome[MAXSTR];
typedef struct {
chromosome chrom;
long double x;
double fitness;
int parent 1, parent2, site;
int count;
}individual;
typedef individual population[MAXPOP];
// VARIABLES DECLARATION
population oldpop,newpop;
int popsize,Ichrom, gen,maxgen;
````

---

<!-- source: Code-01.pdf; page: 3 -->
<!-- source-image: pages/04-Code-01-page-3.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
double poross, pmutation;
double sumfitness;
int mutation, ncross;
double fmax, avg, fmin;
int no_of_sol,MIN;
double oldrand[551:
int jrand, y,store;
float se, hwgt1 (MAXI|MAX],hwgt2[MAX||MAX);
float layer2[MAX][MAXI;
float owgu[MAX][MAX],layerI[MAX][MAX],0u([MAX](MAX;
int [MAX][MAX], desire[MAX][MAX];
double finar[201:
float pas[CONCNI;
float ee[CONCN];
int gbit[CONCNI;
float Irange, urange;
int bb, range;
int al, a2,a3,a4,b1,b2,63,64, c 1, 62, c3, c4;
int c, timetaken;
struct time t1, t2;
population top;
char infile[]="in. dat";
char outfile[I="out. dat".
char wtfile[1="wt. dat".
FILE *ptin;
FILE *ptout;
FILE *ptfwt;
FILE *ptfwti;
FILE *ptgbit;
FILE *ptres;
FILE *ptpop;
FILE *ptval;
char buffer[100];
FUNCTIONS DECLARATION
double
garandom(;
randomise;
garand(int,int);
warmup_rand(double);
adv _rand();
````

---

<!-- source: Code-01.pdf; page: 4 -->
<!-- source-image: pages/04-Code-01-page-4.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/04-Code-01/page-059/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/04-Code-01/page-059/figure-candidate.png)
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
flip(double probability);
gene
initialise;
initreport();
initpop0;
initdata();
objectfn(chromosome);
double
long double decode(chromosome chrom,int (bits);
success;
getpheno(int *x, chromosome chrom, int chrome);
writechrom(chromosome, int);
search(long double,int);
form_cur_pop0;
report(int);
encode(int, int);
void
void
pause(void);
generation);
crossover(chromosome, chromosome, chromosome,
chromosome, int*,int*, int*, int*, double*, double*y
select(int, double, population);
mutation(gene, double, int*);
gene
statistics(int, double*, double*, double*, double*, individual*);
forward(int);
void
void
ftest(void;
void
get iputs);
void
get _oputs;
void
finalweights(float pas[I);
void
storeweights(population);
float calcerror(int);
int menu(void);
MAIN ROUTINE
main()
int i.j;f,count=0;
int ch,mfit;
float temp;
double temp1;
````

---

<!-- source: Code-01.pdf; page: 5 -->
<!-- source-image: pages/04-Code-01-page-5.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.75; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/04-Code-01/page-060/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/04-Code-01/page-060/figure-candidate.png)
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
int gd-DETECT, gm;
population storepop;
initgraph(&gd,&gm,"y:llbolibgi");
f=0;
cleardevice():
if(ptres=fopen("*result.dat","w"))==NULL)
printf("In Cannot open xresult.dat"):
felose(ptres);
iff(ptpop=fopen("xpop.dat","w"))=-NULL)
printf("In Cannot open xpop.dat");
fclose(ptpop);
if((ptgbit=fopen("xgranbit.dat",""))==NULL)
printf(*n Cannot open xgranbit. dat");
fclose(ptgbit);
if((ptval-fopen("value.dat","r"))==NULL)
printf("In Cannot open value.dat");
fclose(ptval);
get_iputs(;
get_oputs();
cleardevice(;
pause();
i.x.ax=0;
int86(0×33,&i, &o);
i.x.ax=1;
int86(0×33,&i,&);
ü.x.ax=3;
int86(0x33,&ii, &o);
while(1)
ü.x.ax=3;
int86(0x33.&il,&o);
gotoxy(65,24);
printf("%3d,%3d",o.x.cx,o.x.dx);
tsetcolor(14);
settextstyle(1,0,2);
rectangle(70,20,550,65);
rectangle (2,2,635,470);
rectangle (3,3,634,469);
setcolor(2);
outtextxy(150,41,"GENETIC ALGORITHM IN NEURAL NETWORK ");
setcolor(3);
outtextxy(200,200." TRAIN NETWORK ");
setcolor(5);
````

---

<!-- source: Code-01.pdf; page: 6 -->
<!-- source-image: pages/04-Code-01-page-6.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- visual-candidate: assets/visuals/04-Code-01/page-061/figure-candidate.png; review: required -->
![Visual candidate](assets/visuals/04-Code-01/page-061/figure-candidate.png)
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
outtexty (200,260," TEST NETWORK ");
setcolor(4);
outtexixy(200,320," QUIT
iffo.x.bx==1)
if‹((o.x.cx>180)&&(0.x.cx<450))&&((o.x.dx>315)&&/(o.x.dx<345))
exit(0);
iffo.x.bx==1)
if(((o.x.cx>180)&&(o.x.cx<450))&&((o.x.dx>256)&&(o.x.dx<290)))
cleardevice();
gotoxy(2,2);
printf("InFINAL TESTING..... Inin");
ftest);
fprintf(ptres, "n");
for(i=0;¡<NCLS;i++)
forj=0;j<NODE3;j++)
fprintf(ptres,"out[%d][%d]=%f",ij,out(i][l);
sprintf(buffer, "TESTING OVER...");
outtextxy (200,320,buffer);
getchO;
cleardevice();
pause;
iffo.x.bx==1)
ifl((0.x.cx>180)&&(o.x.cx<450))&&((o.x.dx>190)&&(o.x.dx<230)))
cleardevice(;
initialise();
for(i=0.i<popsize;it+)
storepop[i]=oldpop[i);
for(i=0;i<popsize;it+)
for(j=0;j<Ichrom:j++-)
fprintf(ptpop,"%d",oldpop[i].chrom[j]);
rewind(ptgbit);
rewind(ptres);
int b=0;
````

---

<!-- source: Code-01.pdf; page: 7 -->
<!-- source-image: pages/04-Code-01-page-7.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
while(b<1)
b++;
gen=0;
countt+;
for(i=0;i<popsize;it-+)
oldpop[i]=storepop[il;
for(i=0;<CONCN;i++)
fscanf(ptgbit,"%d", &gbitfil):
for(i 0;i<popsize;i++)
{ oldpop[i].fitness=objectfn(oldpop[i].chrom);
}
statistics(popsize, &fmax, &avg, & fmin, &sumfitness, newpop);
printf("(ninin.");
gettime(&t1);
starttime;
do
printf(".. ");
delay(100);
gent t;
generation0);
statistics(popsize, &fmax, &avg, & fmin, &sumfitness, newpop);
for(i=0;i<MAXPOP;i++)
oldpop[i]=newpop[i];
no_of_sol-form_cur_pop);
success;
if((gen%100)==NULL)
pause;
} while((gen<maxgen));
gettime(&t2);
stoptime;
fcloseall);
storeweights(oldpop);
printf("InTIME TAKEN %d SECS ", timetaken);
printf("nTRANING IS OVER ");
getch);
pause;
break:
````

---

<!-- source: Code-01.pdf; page: 8 -->
<!-- source-image: pages/04-Code-01-page-8.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
ROUTINE TO PERFORM GI
ITION OF GA CYCLE
generation()
int ijjeross, mate 1, mate2;
population temppop;
j=0;
matel=select(popsize, sumfitness, oldpop);
mate2=select(popsize, sumfitness, oldpop);
crossover(oldpop[matel].chrom, oldpop[mate2). chrom,
newpopti).chrom, newpop[+1].chrom, &ncross, &chrom,
Enmutation, &jcross, &pcross, &pmutation);
newpopti].x=(decode(newpoptil.chrom,Ichrom));
newpopli].fitness=objectfn(newpopli].chrom);
newpop(il.parent1=matel:
newpoplil.parent2=mate2;
newpopti].xsite=jcross;
newpop[+1].x=(decode( newpopli+1].chrom, Ichrom));
newpop[j+1].fitness-objectfn(newpop[j+1].chrom);
newpop[j+1].parent1=matel;
newpopti+1].parent2=mate2;
newpop[j+1].site=jcross;
for(i=0;¡<2;it +)
temppop[i]=newpop[il;
if(temppop[0].fitness <temppop[1].fitness)
y=0;
else
y=1;
temppop(y].×=temppop[y].x/1e30;
oldpop[store]-temppoply];
for(i=0:1<popsize;it +)
newpop[i]=oldpopi];
for(i=0;i<popsize;i++);
ROUTINE TO CALL INITIALISATION ROUTINES
initialise(
initdata();
initpop(;
````

---

<!-- source: Code-01.pdf; page: 9 -->
<!-- source-image: pages/04-Code-01-page-9.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
settextstyle(1,0,2);
sprintf«(buffer," Population initialised...");
outtextxy(100,330, buffer);
getch();
cleardevice);
outtextxy(100,100,"TRAINING.
gotoxy(3, 10);
I ROUTINE TO EVALUATE OBJECTIVE FUNCTION
double objectfn(chromosome n1)
int ij,k,1,m,n, c,p, ct;
individual a[CONCN];
individual d[CONCN];
float b[20];
float in=0.0;
i=0;
k=0;
1=0;
m=0;
c=0;
p=0;
n=0;
for(j=0,m=0;j Ichrom:j++)
while(j==m)
{
for(i=m;i<j+CHROMLEN;i++)
d[n].chrom[I++]=a[k].chrom[i];
b[p]=decode(d[nJ:chrom, CHROMLEN);
m=m+CHROMLEN;
ptt;
n=0;
1=0;
````

---

<!-- source: Code-01.pdf; page: 10 -->
<!-- source-image: pages/04-Code-01-page-10.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(p=0;p<CONCN;p++)
{ ee[p]=b[p//100.00;
if(ee[p]>urange)
ee[p)=urange-ee[p);
k=0;
p=0;
1=0;
m=0;
i=0;
se=0.0;
finalweights(ee);
for(i=0;i<NCLS;i++)
forward(i);
in=calcerror(i);
se=setin;
se=se/(NODE3*NCLS);
pause);
return(se);
ROUTINE TO PERFORM DECODING OF BINARY STRING
TO AN INTEGER
long double decode(chromosome chrom, int Ibits)
intij;
long double accum=0.0,powerof2=1.0;
for(i=0;i<Ibits;it +);
for(i-Ibits-1:>=0;j--)
if(chrom[j].allele)
accum+=powerof2;
powerof2*=2.0;
return accum;
````

---

<!-- source: Code-01.pdf; page: 11 -->
<!-- source-image: pages/04-Code-01-page-11.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
# ROUTINE TO PERFORM
ISATION OF GA PARAMETERS
initdata()
char chi
int j;
float temp:
ptval =fopen("value.dat", "");
cleardevice();
outtextxy(220,30," GENETIC ALGORITHM ");
outtextxy(100, 100," GA PARAMETERS ");
outtextxy(100,110."
- "):
printf("nln");
fscanf(ptval, "%d", &popsize);
sprintf(buffer," POPSIZE = %d", popsize);
outtextxy(100,150,buffer);
Escanf(ptval, "%d", &maxgen);
sprintf(buffer," MAX GENERATION = %d", maîgen);
outtextxy(100,180,buffer);
fscanf(ptval,"%Lf",&pcross);
sprintf(buffer," CROSS OVER PROB. = %.21f",pcross);
outtextxy(100,210,buffer);
fscanf(ptval,"%lf", &pmutation);
sprintf(buffer," MUTATIOM PROB.= %.21f", pmutation);
outtextxy (100,240, buffer);
fscanf(ptval,"%f", &lrange);
sprintf(buffer," LOWER RANGE= %2f' Irange);
outtextxy(100,270, buffer);
fscanf(ptval, "%f", &urange);
sprintf(buffer," UPPER RANGE= %2f", urange);
outtextxy (100,300,buffer);
getch();
cleardevice();
gotoxy(1,2);
randomise();
nmutation=0;
ncross=0;
Ichrom=CHROMLEN*CONCN;
temp=2*urange*100;
````

---

<!-- source: Code-01.pdf; page: 12 -->
<!-- source-image: pages/04-Code-01-page-12.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
range=(int)temp;
fprintE(ptres, "Innpopsize %d,gen %d,cp %.21f,mp
fclose(ptval);
%.21f,range(%. 216,%.210)In", popsize, maxgen, pcross,pmutation,Irange, urange);
ROUTINE TO PERFORM
ALISATION OF POPULATION
initpop()
int ijjI;
int y;
long double temp=0.0;
for(=0j<popsizej++)
bb=0;
for(i=0;<CONCN;i+-+)
printf(". ");
delay(100);
y=random(range);
encode(j,y);
for(i=0;i-Ichrom;i++)
temp=(decode(oldpop[jJ.chrom,Ichrom));
oldpop[il.‹=temp/120;
oldpopli].parent1=0:
oldpopli].parent2=oldpop[i].xsite=0;
ROUTINE TO PERFORM ENCODING OF AN INTEGER TO
BINARY STRING
void encode(int index int value)
{
int ij, term;
chromosome tit;
long int y;
````

---

<!-- source: Code-01.pdf; page: 13 -->
<!-- source-image: pages/04-Code-01-page-13.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
newrand=prand-newrand;
if(newrand <0)
newrand++;
prand=oldrandril
adv _rand();
adv_rand0);
adv_rand(;
jrand=-1;
I ROUTINE TO PERFORM RANDOM NUMBER GENERATION
double garandom()
jrand++:
if(jrand>54)
jrand=0;
adv_rand0;
}
pause;
return((oldrand[jrand])/2);
/ ROUTINE TO PERFORM RANDOM NUMBER GENERATION
int garnd(int low, int high)
int i;
if(low>-high)
i=low;
else
¡ (int) (2*garandom()* (high-low+ 1)+low);
if(i> high)
i=high;
return i:
````

---

<!-- source: Code-01.pdf; page: 14 -->
<!-- source-image: pages/04-Code-01-page-14.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
VERATION
" ROUTINE TO PERFORM RAT
randomise()
double seed;
do
seed=0.45678;
while(seed<0.O|seed> 1.0);
warmup_rand(seed);
/ ROUTINE TO PERFORM FLIPPING OF A BIT
gene flip(double probability)
gene tmp;
if (probability==1.0)
tmp.allele=1;
else
tmp.allele=((2*garandom())<=probability);
return imp;
I ROUTINE TO PERFORM ROULETTE WHEEL SELECTION
int select(int popsize, double sumfitness, population pop)
double rand, partsum;
int j;
double temp;
int templ;
j=-1;
partsum=0.0;
rand=0.0;
temp=0.0;
temp=garandom);
rand=temp*sumhitness;
````

---

<!-- source: Code-01.pdf; page: 15 -->
<!-- source-image: pages/04-Code-01-page-15.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
j++;
partsum += poptil. fitness;
}while(/(partsum>=rand)I==(popsize-1)));
retum j;
/ ROUTINE TO PERFORM MUTATION OPERATOR
gene mutation(gene allval, double mutation, int *nutation)
{
gene mutate;
gene Imp;
mutate=flip(pmutation);
if(mutate.allele)
nmutation++;
tmp.allele=(Ialival. allele);
return imp;
}
return allval;
/ ROUTINE TO PERFORM CROSSOVER OPERATOR
crossover(chromosome p1, chromosome p2, chromosome c1, chromosome c2,
int "ncross, int *Ichrom, int *nmutation, int *jeross,
double *pcross, double "mutation)
int j;
if(flip(*pcross).allele)
*jcross=garnd(0,(*Ichrom)-1);
*ncross++;
else
*jeross=(*Ichrom)-1;
for(i=0;j<*jcross:j++)
{
c1 [i]=mutation(p1 C], *pmutation, nmutation);
c2[i]=mutation(p2[i], *pmutation, nmutation);
````

---

<!-- source: Code-01.pdf; page: 16 -->
<!-- source-image: pages/04-Code-01-page-16.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
if(~jcross!= *Ichrom)
for(j=*jcross:<*Ichrom;j++)
c2[] mutation(p1L], "pmutation, nmutation);
c1[l=mutation(p2[il, *pmutation, nmutation):
pause;
/ ROUTINE TO WRITE CHROMOSOME
writechrom(chromosome chrom, int Ichrom)
{
int j;
for(j=0j Ichromijt +)
/ROUTINE TO PERFORM SEARCH OF OFFSPRING
int search(long double pheno,int no of sol)
long double temp =0.0;
population curpop;
int i;
for(j=0j<no_of_solj++)
{
pause;
temp=fabs(pheno-curpop[i].x);
pause;
if(fabs(pheno-curpop[i].x)<=1e-25)
return j;
return - 1;
````

---

<!-- source: Code-01.pdf; page: 17 -->
<!-- source-image: pages/04-Code-01-page-17.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
"ROUTINE TO FORM CURRENT POPULATION
int form cur pop()
int i.place.k:
int no of sol =1;
population curpop;
for(j=0;j-Ichrom;i++)
curpop[0].chrom[j]=newpop[0].chrom[i]:
curpop[0].×=newpop[0].x;
curpop[0].fitness=newpop[0].fitness;
curpop[0].count=1;
for(j=1j<popsize:j++)
place=search(newpop[i].x,no_of_sol);
if(place 1s -1)
curpopiplace].count++;
else
for(k=0;k<Ichrom:k++)
curpop[no_of_sol].chrom[k]=newpopljl.chrom[k];
curpop[no_of _sol].x=newpopli].x;
curpop[no_of _sol].fitness newpopli]. fitness;
curpop[no_of_sol].count=1;
no_of_solt+;
}
in 3
return no_of_ sol;
/ ROUTINE TO DETERMINE THE PERCENTAGE OF SUCCESS
TO GO FOR NEXT GENERATION
int success)
int ij;
double min;
double percent;
MIN = 0;
min = oldpop[0]. fitness;
````

---

<!-- source: Code-01.pdf; page: 18 -->
<!-- source-image: pages/04-Code-01-page-18.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(i=1:ispopsize:i++)
for(i=0;j<Ichrom;i++)
tpop|il.chrom|i]=oldpop[il.chrom/j|;
if((oldpop[il. fitness < min))
min oldpop[il. fitness;
if(min<0.05)
return 1;
return 0;
ROUTINE TO CALCULATE THE GA VARIABLES
statistics(int popsize, double *max, double *avg, double *min,
double *sumfitness, individual *pop)
{
int ij;
float temp=0.0;
*sumfitness=0.0;
*avg=0.0;
#fmax=0.0;
*min=0.0;
for(i=0;i<popsize;i++)
*sumfitness += popli].fitness;
*avg= *sumfitness/popsize;
*fmax=*fmin=pop[0]. fitness;
store=0;
for(i=1;¡<popsize;i++)
if(pop[i] fitness>*fmax)
*fmax=pop[i]. fitness;
store=1:
if(popli].fitness < *fmin)
*fin=pop[i]. fitness;
````

---

<!-- source: Code-01.pdf; page: 19 -->
<!-- source-image: pages/04-Code-01-page-19.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
ROUTINE TO PERFORM FORWARD PROPAGATION
void forward(int count)
int ij;
float net1, net2, net3;
for(i=0;i<NODE1;i++)
net1=0.0;
for(j=0;j<NODEO:j++)
{
netl+= hwgt1[jli]*[count]lil;
}
layer1[count](i]=1/(1+exp(-net1));
}
for(i=0:1<NODE2:1++)
{ net2=0.0:
for(=0j<NODE1;++)
net2+= hwgt2 ]li]*layer1[count]Ul;
}
layer2[count][i]=1/1+exp(-net2));
for(i=0:i<NODE3;i+-+)
{ net3=0.0;
for(j=0;j<NODE2;j++)
{
net3+= owgt[jlli]*layer2[count]D];
}
out[count][i]=1/(1+exp(-net3));
pause);
return;
````

---

<!-- source: Code-01.pdf; page: 20 -->
<!-- source-image: pages/04-Code-01-page-20.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
ROUTINE TO CALCULATE FINAL WEIGHTS
void finalweights(float pas[CONCNI)
int ij.k.kk:
k=0;
kk=0;
for(i=0;¡<NODEO;i++)
for(j=0;j<NODE1;j++)
{ if(gbit[kk]==0)
hwgt1 i]fil=0;
else
hwgt1[i][i]=pas[k]*gbit[kk);
k++:
for(1=0;¡<NODE1;i++)
{ for(j-Oj-NODE2j++)
if(gbit[kk]==0)
hwgt2[i]fil=0;
else
hwgt2[i]Li]=pas[k]*gbit[kk];
k+t;
kk++:
for(=0;¡<NODE2:1++)
{ for(i=0:¡<NODE3:i++)
if(gbit[kk]==0)
owgti]b]=0;
else
owgti](i]=pas[k]*gbit[kk];
k++:
````

---

<!-- source: Code-01.pdf; page: 21 -->
<!-- source-image: pages/04-Code-01-page-21.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
do
j++;
partsum += poptil. fitness;
¿while(!(partsum>=rand)||(j==(popsize-1));
retum i:
/ ROUTINE TO PERFORM MUTATION OPERATOR
gene mutation(gene allval, double mutation, int *nutation)
gene mutate;
gene imp;
mutate=flip(pmutation);
if(mutate.allele)
tmp.allele=(!allval. allele);
return tmp;
return allval;
ROUTINE TO PERFORM CROSSOVER OPERATOR
crossover(chromosome p1, chromosome p2, chromosome c1, chromosome c2,
int *ncross, int *Ichrom, int *mutation, int *jcross.
double *peross, double *mutation)
int j;
if(flip (*pcross).allele)
*jcross=gard(0,(*Ichrom)-1);
*ncross++
else #jcross=(*Ichrom)-1;
for(j=0;j<*jcross:j++)
{
c1 fil=mutation(p1 [il, *pmutation, nmutation);
c2fil=mutation(p2[il, *pmutation,nmutation);
````

---

<!-- source: Code-01.pdf; page: 22 -->
<!-- source-image: pages/04-Code-01-page-22.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
pause);
return;
ROUTINE TO PERFORM STORING OF FINAL WEIGHTS
void storeweights(population pop)
int ij,k,I,m,n,c, p;
individual a[CONCN];
individual d[CONCNI;
float b[CONCN];
float e[CONCNI;
i=0;
k=0;
1=0;
m=0;
c=0;
p=0;
n=0;
ptfwt1=fopen(wgtfile, "w");
for(j=0;j<Ichrom:j++)
a[k].chrom[c++J=pop[0].chrom[jl;
for(j=0,m=0;j<Ichrom;j++)
while(j==m)
for(i=m;i<j+CHROMLEN:i++)
d[n].chrom[I++]=a[k].chrom[i];
b[p]=decode(d[n].chrom,CHROMLEN);
M=m+CHROMLEN;
p+t;
n=0;
10;
for(p=0;p<CONCN;p++)
{e[p]=b[p]/100.00;
if(e[p]>urange)
[p]-urange-e[p);
p=0;
````

---

<!-- source: Code-01.pdf; page: 23 -->
<!-- source-image: pages/04-Code-01-page-23.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(i=0;i<NODEO;i++)
{
for 0;j<NODE1:++)
{
hwgt1(ilD]=e[P++];
forintf(ptfvt1, "%fn", hwgt1 (i]lil);
}
for(i=0;<NODE1;i++)
{
for(=0j<NODE2j++)
{
higt2[JD]=eLP++];
forinti(ptfiwt1,"%fn", hwgt2(1]DD);
fori=0;¡<NODE2;¡++)
{
for(j=0j<NODE3;++)
owgti][i]=e[p++];
forintf(ptfwt1,"%fIn", owgt[i](il);
pause);
fclose(ptfwt1);
return;
// ROUTINE TO PERFORM TESTING OF PATTERNS
void fest)
int n;p,in,v,i.j,k,1;
float percent;
int s;
float store [MAX];
float array[MAX][MAX];
float finer[MAXI;
float temp;
fcloseall@;
if(ptfwtl-fopen(wgtfile,"s"))==NULL)
printf("'InCannot open weight file");
rewind(ptfwtI);
````

---

<!-- source: Code-01.pdf; page: 24 -->
<!-- source-image: pages/04-Code-01-page-24.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
print?"MFINAL WEIGHTS... In");
for(i=0;i<NODEO;i++)
'{
orG -Oj<NODEI;++)
iffscant«pttwel,"%P', Schwgulf|DiD==NULL)
printf"Error scanning the figt fileln");
for(i=0;i<NODE1;i++)
forG=0j<NODE2;+-+)
{
fscanf(ptfwt1,"%f", &hwgt2ri]fin;
3
for(i=0;i<NODE2;i++)
{
for(j=0j<NODE3;j++)
fscanf(ptfwt1, "%fln", &owgt[i]lil);
pause);
get_iputs;
for(p=0;p<NCLS;p++)
{
forward(p);
printf("in Pattern testing is over... In");
pause;
cleardevice();
printf("Enter the no. of patterns identified->");
scanf("%d", &in);
percent = (float)in/(float)NCLS*100.00;
sprintf(buffer," Percentage of success is %f "percent);
outtextxy(200,240, buffer);
pause);
fclose(ptfwtI);
return;
````

---

<!-- source-document: Code-02.pdf; profile: code -->
<!-- source: Code-02.pdf; page: 1 -->
<!-- source-image: pages/05-Code-02-page-1.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
print ("MENAL WEIGHTS...n'");
fOr(=0; NODEO;it-+)
ffscanf(ptfivt1,"%P, &hwgti(ilLI)==NULL)
print(Error scanning the figt filetn");
for(i=0;i<NODE1;i++)
for(i=0j NODEZ:j++)
{
fscanf(ptfwt1, "%f', Schwgt2[ILl);
for(i=0.¡<NODE2;i++)
{
forG=0-j<NODE3;j++)
fscanf(ptfwt1, "%fin", &owgt[i][il);
pause();
get_iputsO;
for(p=0;p<NCLS;p++)
{
forward (p);
printf(*in Pattern testing is over... In");
pause);
cleardevice();
printf("Enter the no. of patterns identified->");
scanf("%d", &in);
percent = (float)in/(float)NCLS*100.00;
sprintf (buffer." Percentage of success is %f ",percent);
outtextxy(200,240,buffer);
pause;
fclose(ptfwt1);
return;
````

---

<!-- source: Code-02.pdf; page: 2 -->
<!-- source-image: pages/05-Code-02-page-2.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
ROUTINE TO PERFORM CALCULATION OF ERRORTERM
float calcerror(int count)
int i;
float errorterm;
float merrorterm=0.0;
float ferrorterm;
for(i=1;¡<=NODE3;i++)
{
errorterm=(desire[count][i]-out[count](i]);
merTorterm += errorterm* errorterm;
}
ferrorterm = 0.5°merrorterm:
return(ferrorterm);
ROUTINE TO PERFORM READING OF INPUTS FROM INPUT FILE
void get iputs(void)
{
int i,j;
int s;
if((ptin-fopen(infile,"$"))==NULL)
printf("'Incannot open input file");
pause;
rewind(ptin);
for(i=0;<=NCLS;i++)
for(j=0:j<=NODEO:j++)
{
fscanf(ptin, "d", &s);
if(s==0)
X[i]G]=O;
else
fclose(ptin);
pause;
````

---

<!-- source: Code-02.pdf; page: 3 -->
<!-- source-image: pages/05-Code-02-page-3.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
ROUTINE TO PERFORM READING OF OUTPUTS FROM OUTPUT FILE
void get oputs(void)
{
int ij;
int s;
if((ptout-fopen(outfile,"#"))==NULL)
printf("InCannot open output file");
rewind(ptout);
for(1=0;¡<=NCLS;i++)
{ for(j=0;j<=NODE3j++)
{
fscanf(ptout,"%d", &s);
if(s==0)
desire[ilti|=0;
else desire[JUil=1;
fclose(ptout);
pause;
````

---

<!-- source: Code-02.pdf; page: 4 -->
<!-- source-image: pages/05-Code-02-page-4.png -->
<!-- structure: code; confidence: 0.80 -->
<!-- visual-structure: figure; confidence: 0.70; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
PROGRAM TO TRAIN AND TEST NEURAL NETWORK USING
BACKPROPAGATION ALGORITHM
INCLUDING OF HEADER FILES
#include <stdio.h>
#include <math.h>
#include «stdlib.h>
Hinclude «string.h
#include «alloc.h>
#include <dos.h>
#include <time.h>
#include <conio.h>
#include «graphics.h>
DEFINITION OF BACKPROPAGATION PARAMETERS
#define ncls 4
#define node0 2
#define nodel 2
#define node2 2
#define node3 1
#define thersb 0.5
#define MAX1 30
#define ALPHA 1
#define MITER 5000
DEFINITION FOR TIMING CALCULATION
#define starttime ab1=btl.ti hour; \
ab2=-bt1.ti min; I
ab3=btl.ti sec;
#define stoptime bb1=bt2.ti hour; I
bb2=bt2.ti min;
bb3=bt2.ti sec; \
bel=(bb1-ab1);\
bc2=(bb2-ab2);\
bc3=(bb3-ab3): \
be = (((bc1*60)+bc2)*60+bc3); 1
btimetaken = bc;
````

---

<!-- source: Code-02.pdf; page: 5 -->
<!-- source-image: pages/05-Code-02-page-5.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
VARIABLES DECLARATION
union REGS it,o;
int desire[MAX1][MAX11
int bx[MAXI||MAXI:
float layerb1[MAX1][MAX1]layerb2[MAX1][MAX1 Lout
float hwgtb1 [MAXI|[MAX11.hwgtb2[MAX11IMAX
MAXI
float owgtb[MAX1][MAX1] obwgt[]
float hbwgt2[MAX1]hbwgt1
float finer:
struct time btl,bt2;
char infile[|= "in.dat".
char outfile I= "out. dat".
char wgtfile[l= "wgt.dat"
int ab1,ab2,ab3,ab4,bb1,bb2,bb3,bb4, bc 1,bc2, bc3, bc4;
int be, btimetaken, choose;
FILE *ptiwt;
FILE *pttwt;
FILE *ptfwtb1;
FILE *ptinI;
FILE *poutI;
ewind FILE *ptert;
FILE *ptmse;
FILE *ptop;
FILE "ptresb;
FUNCTIONS DECLARATION
void initweights(void);
void forward1(int count);
void reverse(int count);
void tempweights(void);
void prevweights(void);
void finalweights(void);
void get_ip(void);
void get_op(void);
void test(void);
float calcerror1 (int count);
void pause1();
int menul(void);
float randomweight(unsigned init);
````

---

<!-- source: Code-02.pdf; page: 6 -->
<!-- source-image: pages/05-Code-02-page-6.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.70; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
MAIN ROUTINE
main(
int i,j,k,l,m;
int s[51;
int ch:
float sgert;
float msger;
int epoc=1;
int gd=DETECT,gm;
initgraph(&gd, &gm, "y:\bollbgi");
cleardevice);
iff((pterr = fopen("oserr.dat", "w+"))=NULL)
printf("n Cannot open oserr. dat");
if((ptop = fopen("osop.dat", "w+"))=NULL)
printf("n Cannot open osop.dat");
if((ptmse = fopen("osmse. dat","w+ "))=NULL)
printf("In Cannot open osmse. dat");
if((ptresb = fopen("result. dat","a")=NULL)
printf("In Cannot open result. dat");
rewind(pterr);
rewind(ptop);
rewind(ptmse);
rewind (pttwt);
cleardevice0;
i.x.ax=0;
int86(0x33,&i, &o);
ix.ax=1;
int86(0x33,&ii,&o);
ü.x.ax=3;
int86(0x33,&i, &o);
while(1)
i.x.ax=3;
int86(0×33,&i, &o);
gotoxy(69,25);
printf("%3d,%3d",o.x.cx,o.x.dx);
settextstyle(1,0,2);
setcolor(7);
rectangle(3,3,635,470);
rectangle(4,4,634, 469);
rectangle(70, 10,570,80);
````

---

<!-- source: Code-02.pdf; page: 7 -->
<!-- source-image: pages/05-Code-02-page-7.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
outtextxy(100,30,"BACK-PROPAGATION NEURAL NETWORK ")
setcolor (2);
outtexixy(200,200," TRAIN NETWORK ");
setcolor(4);
outtextxy(200,260," TEST NETWORK ").
setcolor(3);
outtextxy(200,320," QUIT
iffo.x.bx==1)
ift((o.x.cx>180)&&(0.x.cx<450))&&((o.x.dx>315)&&(o.x.dx<345)))
exit(0);
iffo.x.bx==1)
if(((0.X.Cx>180)&&(o.X.cx<450))&&((o.x.dx>256)&&(o.x.dx<290)))
{
cleardevice();
testO;
cleardevice();
if(o.x.bx==1)
if(((o.x.cx>180)&&(o.x.cx<450))&&((o.x.dx>190)&&(o.x.dx<230)))
cleardevice();
srand (12345);
initweights();
get_ip();
get_op();
outtextxy(10,10," TRAINING ..");
gotoxy(10, 10);
msgerr=1.0;
gettime(&bt1);
starttime;
while(MITER >= epoc)
sqerT=0.0;
epoc++;
for(i=1;¡<=ncls;it-+)
forward1(i);
````

---

<!-- source: Code-02.pdf; page: 8 -->
<!-- source-image: pages/05-Code-02-page-8.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
reverse(j);
sgerr = sgert + finerr;
msgeir = sqerr/(node'" ncis);
printf(".");
delay(30);
(epoc % 50) ? 1 : fprintf(ptmse,"In epoc = %d, sqerror = %{, msqerror =
%f",epoc,sgert,msgerr);
if((epoc % 2000) == 0)
tempweights();
gettime(&bt2);
stoptime;
finalweights0);
printf("In Final Weights stored");
fclose(pterr);
fclose(ptmse);
fclose(ptresb);
ptresb-fopen("result. dat", "w");
fprintf(ptresb,"%d",btimetaken);
printf("'n Time Taken %d Secs", btimetaken);
printf("InTraining is over.. In");
getch();
cleardevice0;
break;
ROUTINE TO PERFORM FORWARD PROPAGATION
void forward1 (int count)
{
int ij;
````

---

<!-- source: Code-02.pdf; page: 9 -->
<!-- source-image: pages/05-Code-02-page-9.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
float netl,net2.net3:
for(i=1;i<=nodel;i++)
{
net1=0.0;
for(j=1g<=node0;i++)
{
net1+=hwgtb1 lli]*bx[count]Dil;
netl+=hbwgt1 [il;
layerb1[count][i]=1/(1+exp(-net1));
}
for(i=1;i<=node2;i++)
{
net2=0.0;
for(j=1;<=nodel;i++)
{
net2+=hwgtb2(i](i]*layerb1[count]lil;
}
net2+=hbwgt2 ];
layerb2[count][i]=1/(1+exp(-net2));
for(i=1;¡<=node3;i++)
{
net3=0.0; me del
for(=1;<=node2;j++)
{
net3+=owgtb[illi]*layerb2[count]Cil;
3
net3+=obwgti];
outb[count][i]=1/(1+exp(-net3));
return;
ROUTINE TO PERFORM REVERSE PROPAGATION
void reverse(int count)
int iik;
float delta[MAX1][MAXI];
float delta1[MAXI][MAX1],delta2[MAXI][MAXI];
````

---

<!-- source: Code-02.pdf; page: 10 -->
<!-- source-image: pages/05-Code-02-page-10.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
float sum[MAX11;
float temp=0.0;
float temp1=0.0;
for(i=1, finerr=0.0;i<=node3;i++)
temp = outb[count](]*(1-outb[count][il);
temp1= (desire1[count]li]-out[count]fil);
deltalcount][i]=temp*(desire1(count]Li]-outb[count]fil);
finer+=0.5*temp1 *temp1;
}
fork=1;k<=node2;k++)
{
sum[k]=0.0;
for(i=1;i<=node3;it-+)
{
sum[k] +=owgtb[k](i]* delta[count]ii;
}
temp = layerb2|count][k]*(I-layerb2[count][kJ);
delta2[count][k]=temp*sum[kl;
fork=1;k<=nodel;k++)
sum[k]=0.0;
for(1=1;¡<=node2;1++)
{
sum[k] +=hwgtb2[k][i]*delta2[count]Li];
}
temp = layerb1 [count][k]*(1-layerb1[count][k]);
delta1[count][k]=temp*sum[k];
for(j=1;<=node3:i++)
for(i=1:¡<=node2:i++)
3
temp=delta[count][j]*layerb2[count][i];
owgtb[i]Li]=owgtb[i]D]+ALPHA * temp;
for(j=1;<=node2;j++)
for(i=1:¡<=nodel:i++)
temp-delta2[count]Li]*layerb1(count]fi);
hwgtb2(ilD)-hwgtb2/1GI+-ALPHA * temp;
````

---

<!-- source: Code-02.pdf; page: 11 -->
<!-- source-image: pages/05-Code-02-page-11.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(i=1;<=node1;++)
{
for(i=1;¡<=node0;it +)
{
temp=deltal[count]Ci]*bx[count]fil
hwgtb1 (IC]-hwgtb1 iJU|+ ALPHA * temp;
retuin;
ROUTINE TO PERFORM STORING OF TEMPORARY WEIGHTS
void tempweights(void)
int ij;
if(pttwt-fopen("ostwt.dat", "w+"))==NULL)
printf("In Cannot open ostwt. dat file");
exit(0);
rewind(pttwt);
for(i=1;¡<=nodeO;i++)
fori=1;j<=nodel;i++)
{
fprintf(pttwt, "%f",hwgtb1 [i]Gil;
for(i=1;¡<=nodel;i++)
{
fprintf(pttwt,"%f", hbwgt1[i]);
for(i=1;¡<=nodel;it +)
{ for(j=1;j<=node2;j++)
{
fprintf(pttwt,*%f*,hwgtb2[1]G));
for(i=1;¡<=node2;i+-+)
{
printf(pttwt, "%f", hbwgt2[1]);
````

---

<!-- source: Code-02.pdf; page: 12 -->
<!-- source-image: pages/05-Code-02-page-12.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
fordi=1;i<-node2;i++)
{
for(i=Ij<-node3j++)
fprintf(pttwt,"%f",owg1b|IDl);
for(i=1;i<=node3;i++)
fprint (pttwt, "%f", obwvgtti));
fclose (pttwt);
return;
void finalweights(void)
intij;
i((ptfivib1-fopen(wgtfile,"w+")=-NULL)
{
printf("nCannot open weight file");
exit(0);
rewind(ptfwtb1);
for(=1:¡<=node0:i++)
for(j=1;j<=node1;j++)
{
fprintf(ptfwtb1,"%fln",hwgtb1(i]GiI);
for(i=1;¡<=node1;i++)
fprintf(ptfwtb1,"%fn", hbwgt1[il);
for(i=1:i<=nodel:i++)
for(=1;j<=node2;j+-+)
{printf(ptfwtb1,"%fn",hwgtb2[IDl);
````

---

<!-- source: Code-02.pdf; page: 13 -->
<!-- source-image: pages/05-Code-02-page-13.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.80; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
forti=1;¡<=node2;it +)
{
fprintfptfwvib1, "%An", hbwgt2|i);
for(i=1;i<=node2;it-+)
{ for(j=1j<=node3j++)
{
fprintf(ptfwib1, "%fn",owgtblilfil;
for(i=1;<=node3;it-+)
fprintf(ptfwtb1,"%fln", obwgtil);
}
fclose(ptfwtb1);
retumn;
ROUTINE TO PERFORM INITIALISATION OF WEIGHTS
void initweights(void)
{
int ij;
if(ptiwt-fopen("osiwt. dat", "w+"))==NULL)
printf("InCannot open weight file");
for(=1:¡<=node0;i++)
for(j=1;<=nodel;++)
{
hwgtb1filli]=randomweight(0);
hwgtb1fi]fil=((1.0-(-1.0)Y/((node0+1)*32767.0)*rand(+(-1.0/(node0+1)));
Éprintf(ptiwt, '"%fln", hwgtb1(iril)
for(i=1:¡<=nodel:i++)
hbwgt1 [i]=fabs(randomweight(0));
hbwgt1fil=fabs((1.0-(-1.0))/((node0+1)*32767.0)*rand()+(-1.0/(node0+1)));
fprintf(ptiwt,"%fn", hbwgt1fil);
````

---

<!-- source: Code-02.pdf; page: 14 -->
<!-- source-image: pages/05-Code-02-page-14.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.65; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
forti=1;<=node1;i++)
for(j=1j<=node2;j++)
{
hwgtb2(i]D]=randomweight(0);
Awver62|010|=((1.0-(-1.O))«(node0+1) 32767.0)*rand0+(-1.0/(nod.0+1))
printf(ptiwt,"*An", hwgtb2(iNDil):
for(i=1;i<=node2;i+-+)
hbwgt2[i]-fabs(randomweight(0));
hbwgt2/i=-fabs((1.0-(-1.0))/(node1+1)*32767.0)*rand0)+(-1.0/(node2+1)));
fprintf(ptiwt, "%fin", hbwgt2[il);
} for(i=1;<=node2;i++)
for(j=1;<=node3;j++)
owgtb[i]U]=randomweight(0);
owgtb[1]U]=((1.0-(-1.0))/(node2+1)*32767.0)*rand0+(-1.O/(node2+1)));
fprintf(ptiwt, "%fin", owgtbrimril);
for(i=1:¡<=node3:i++)
obwgt[i]-fabs(randomweight(0));
obwgti]=fabs((1.0-(-1.0))/((node2+1)*32767.0)*rand()+(-1.0/(node2+1)));
fprintf(ptiwt, "%fin",obwgt[il);
}
fclose (ptiwt);
return;
ROUTINE TO PERFORM TESTING OF PATTERNS
void test
int n,p, in, v,i.j,k,I;
float percent;
ints;
float store[MAX1];
float array[MAXI][MAXI];
float finer[MAXI];
float large;
float temp;
````

---

<!-- source: Code-02.pdf; page: 15 -->
<!-- source-image: pages/05-Code-02-page-15.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
if (ptfwtb1=fopen(wgtfile,"r"))=NULL)
printf(*'In Cannot open twt.dat";
rewind(ptfwtb1);
gotoxy(10, 10);
printf("In Final Weights... In");
for(i=1;i<=node0;i++)
for(j=1;j<=nodel;++)
if(fscanf(ptfwtb1,"%f",&hwgtb1(i]G])==NULL)
printf("Error Scanning the fwgt filen");
for(i=1;i<=node1;i++)
fscanf(ptfwtb1,"%f", &chbwgt1 fil);
for(i=1;<=nodel;i++)
{ for(j=1;j<=node2;j++)
fscanf(ptfwtb1,"%f", &chwgtb2[i]Li|);
for(i=1:¡<=node2;i++)
fscanf(ptfwtb1,"%f", &chbwgt2[il);
for(i=1;¡<=node2;i++)
for(j=1;<=node3;++)
fscanf(ptfwtb1,"%f", &owgtb[i][l);
for(i=1;¡<=node3;i++)
fscanf(ptfwtb1,"%f", &obwgt[il);
}
get _ip();
````

---

<!-- source: Code-02.pdf; page: 16 -->
<!-- source-image: pages/05-Code-02-page-16.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(p=1;p<=ncls;p++)
forward1 (p);
}
printf("In Pattern testing is over... In");
printf"In Enter the no. of patterns identified->");
scanf("%d", &in);
percent = (float)in/(float)ncls*100.00;
printff"In Percentage of success is %fn", percent);
pause1(;
fclose(ptfwtb1);
return;
ROUTINE TO PERFORM GETCH FUNCTION
void pause1(void)
getch();
ROUTINE TO PERFORM GENERATION OF RANDOM WEIGHTS
float randomweight(unsigned init)
int num;
if(init==1)
srand((unsigned)time(NULL));
num=rand(%100;
return 2*((float)(num/100.0))-1;
ROUTINE TO PERFORM CALCULATION OF ERROR TEAM
float calcerror1 (int count)
int i;
float errorterm;
float merrorterm0.0;
float ferrorterm;
for(i=1;¡<=node3;1++)
errorterm=(desire1 [count](il-outb[count (il)
````

---

<!-- source: Code-02.pdf; page: 17 -->
<!-- source-image: pages/05-Code-02-page-17.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: diagram; confidence: 0.80; reasons: line-structure-signals -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: diagram-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
merrorterm += errorterm* errorterm;
ferrorterm = 0.5 * merrorterm;
return(ferrorterm);
ROUTINE TO PERFORM READING OF INPUTS FROM INPUT FILE
void get_ip(void)
int ii:
int s;
if«(ptin1-fopen(infile,"+"))==NULL)
printf("Incannot open input file");
rewind(ptin1);
for(i=1:1<=ncls:¡++)
for(j=1;<=node0;j++)
{
fscanf(ptin1, "%d",&s);
if(s==0)
else bxli]b]=1;
ROUTINE TO PERFORM READING OF OUTPUTS FROM OUTPUT FILE
void get _op(void)
int LJ;
int s;
if((ptoutl=fopen(outfile,"$"))==NULL)
printf("InCannot open output file");
rewind(ptoutl);
for(i=1;¡<=ncls;it-+)
for(j=1;j<=node3;jt+)
fscanf(ptout1, "%d", &s);
if(s==0)
desire 1 [1](i]=0;
````

---

<!-- source: Code-02.pdf; page: 18 -->
<!-- source-image: pages/05-Code-02-page-18.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
else
desire1|fil=1;
ROUTINE TO PERFORM INITIALISATION OF PREVIOUS WEIGHTS
void prevweights(void)
int i.j;
if((ptiwt-fopen("osiwt. dat","-"))=NULL.)
{
printf("In Cannot open weight file");
pause1(;
exit(0);
rewind(ptiwt);
for(i=1;¡<=node0;i++)
for(j=1;¡<=nodel;i++)
{
fscanf(ptiwt,"%f", &hwgtb1 lUl);
}
for(i=1;¡<=node1;it-+)
fscanf(ptiwt,"%f", &chbwgt1[il);
for(i=1;¡<=nodel;i++)
{ for(j=1;j<=node2j++)
{ fscanf(ptiwt,"%f",&chwgtb2[ilL)):
}
for(i=1:¡<=node2;i++)
{
fscanf(ptiwt,"%f", &hbwgt2[il);
````

---

<!-- source: Code-02.pdf; page: 19 -->
<!-- source-image: pages/05-Code-02-page-19.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(i=1;i<=node2;i++)
for(j=1;<=node3;++)
fscanf(ptiwt,"%f",&owgtb(iltil);
for(i=1:i<=node3;i++)
з
fscanf(ptiwt, "%f", &obwgtil);
}
close (ptiwt);
return;
````

---

<!-- source: Code-02.pdf; page: 20 -->
<!-- source-image: pages/05-Code-02-page-20.png -->
<!-- structure: code; confidence: 0.80 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
PROGRAM TO TRAIN AND TEST THE NEURAL NETWORK
USING COUNTER PROPAGATION ALGORITHM
INCLUDING THE HEADER FILES
#include «stdio.h>
#include «float.h>
#include «math.h>
#include <string.h>
#include <dos.h>
#include <process.h>
#include <conio.h>
#include <alloc.h>
#include «stdlib.h>
#include <time.h>
# include «graphics.h>
TIME CALCULATION
#define starttime
al=t1.ti_hour; I
a2=t1.ti min; I
a3=t1.ti _sec;
#define stoptime
b1=t2.ti_hour; |
b2-12.ti min;
b3=12.ti sec; I
c1 = (b1-al);
c2 = (62-a2);
c3 = (63-a3); 1
6 = (((c1*60) +62) 60+c3); 1
timetaken = c;
25
#define no inputs
10
#define kohonen nodes
3
#define grossberg nodes
3
#define no. lavers
3
#define n learn set
1
Fdefine n test set
union REGS i,o;
struct file name
char f10];
};
````

---

<!-- source: Code-02.pdf; page: 21 -->
<!-- source-image: pages/05-Code-02-page-21.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
VARIABLE DECLARATION
int actual no inputs, file _no, min, tmas, tine, file ptr, hundreds, tens, ones;
int ij, total no_trails=0,sample ptr,c;
char buffer[1001:
int al,a2,a3,b1,b2,b3, timetaken, c1, c2, c3;
struct time t1,12;
int max_n_ trails=2000;
int increment =0,leam_ptr-0;
int newline charum=5:
int no nodes;
GLOBAL DECLARATIONS FOR THE NEURAL NETWORK
float w1[kohonen_nodes][no_inputs;
float w2[grossberg_nodes][kohonen_nodes],x1 [no _inputs];
float x2[kohonen_nodes];
float x3[grossberg_nodes];
float desired[grossberg_nodes];
float learing rate =1.5;
float large =-999.0;
float train rate coef=.7, beta=.1;
float x_fln_learn_set]|no_inputs];
float normalizing_factor=1.0;
char *temp;
static char begining[]= "alpha000";
char files[201;
float alpha, largest=-999;
int win neuron, number=0;
float counter =0.0, count beta=0.0;
FUNCTION DECLARATION
test network);
read real;
vold read weights);
void save weights);
train();
initialize values);
recalculate weight matrix0:
````

---

<!-- source: Code-02.pdf; page: 22 -->
<!-- source-image: pages/05-Code-02-page-22.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.65; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
MAIN ROUTINE
main()
int learn ptr;
int option;
int gd=DETECT, gm;
initgraph(&gd, &gm, "y:Ilbollbgi");
cleardevice();
initialize _values();
option=999;
tmin-000; // numeric index to training files names
set
tmax=003; // should equal n_leam_
tinc=1;
i.x.ax=0;
int86(0x33,&ii,&o);
i.x.ax=1;
int86(0×33, &i, &o);
ii.x.ax=3;
int86(0x33,&ii,&o);
while(1)
ü.x.ax=3;
int86(0x33, &i,&);
gotoxy(69,24);
printf(¼%3d,%3d",o.x.cx, o.x.dx);
setcolor(6);
rectangle(3,3,630,470);
rectangle(4,4,629, 469);
total no trails+ r
avoium("cls");
settextstyle(1,0,2);
// setcolor(1);
rectangle(70, 10,570,80);
setcolor(9);
outtextxy(100,30,"COUNTER PROPAGATION NEURAL NETWORK "):
setcolor(7);
outtextxy(200,120." TRAIN NETWORK ");
setcolor(8);
TEST NETWORK ");
outtextxv(200.170."
setcolor(10);
````

---

<!-- source: Code-02.pdf; page: 23 -->
<!-- source-image: pages/05-Code-02-page-23.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.80; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
outtesty (200,220," READ WEIGHTS ");
setcolor(11);
outtestxy(200,270," SAVE WEIGHTS");
setcolor(12);
"):
outtexixy(200,320," QUIT
iffo.x.bx==1)
#(CO.x.cx>180)&-& (0.x.cx<450))&.&(o.x.dx>315)&&(o.x.dx<345)))
exit(0);
if(o.x.bx==1)
f4(0.x.cx>180)&.&(o.x.cx<450))&.&((o.x.dx>115)&&(o.×.dx<140))
cleardevice();
gettime(&t1);
starttime;
gotoxy (2,2);
sample_ptr=0;
for(file ptt-tmin;file ptrtmax,;file ptr-file ptr+inc)
hundreds=file _ptr/100;
tens=(file ptr-100*hundreds)/10;
ones=(file pt-100*hundreds-10*tens);
strepy(files, begining);
liles|5]=48+ hundreds; // we choose 5,6,7 char replaced in alpha000
files[6]=48+ tens;
files[7]=48+ones;
/ read in the file read _real;
sample_ptr++:
} I end for loop
printf("Inln");
train();
gettime (&12);
stoptime:
getch();
cleardevice();
outtextxy(100, 10," TRAINING IS OVER ... ");
getch();
outtextxy (100, 150," TIME TAKEN : ");
gotoxy(40,11);
sprintf(buffer, "%d Sec",timetaken);
outtextxy (350, 150, buffer);
outtextxy (300,400," PRESS ANY KEY TO CONTINUE...");
getch();
cleardevice);
}
// end option
if(o.x.bx==1)
if (o.×(x>180)&8/0.x.cx<4501)8.8440.x.dx>168)8-8(0.x.dx<198))
````

---

<!-- source: Code-02.pdf; page: 24 -->
<!-- source-image: pages/05-Code-02-page-24.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
cleardevice0;
test network();
cleardevice();
if(o.x.bx==1)
8440. x.cx>180)8&(0.x.cx<450))8&(0.x.dx>217)8-&(0.x.dx<248))
cleardevice(;
read weights);
deardevice);
if(o.x.bx==1)
iN((0.>.cx>180)&&(0.x.cx<450)) & &((0.x. d*›266)&.&(o.x.dx 301)»
{
cleardevice();
save weights);
cleardevice;
read real
FILE *fdi;
int found;
char temp2[80];
float sum;
getch();
sp fdi-fopen("alpha000","¡"); // open input file
fdi-fopen("alpha000", "r");
printf("In reading file ==>%sin", begining);
if (fdi==NULL)
printf("could not open input fileln");
printf("press any key to continueln");
fclose(fdi);
i=-999;
return 0;
printff"nin reading the data. In");
sum=0.0;
j=-1
````

---

<!-- source-document: Code-03.pdf; profile: code -->
<!-- source: Code-03.pdf; page: 1 -->
<!-- source-image: pages/06-Code-03-page-1.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
found=99;
14:
it(j%newline charum = O && j!=0)
Iscani(fdi, "m");
found fscanfffdi,"%", &x_#(sample _ptrjlil);
while(found!=BOF && je=no _inputs-1);
actual no inputs=j-l;
for(i -O;i?-actual no _ inputs;it +)
if(1%5= 0) printf«"n"):
print‹"%f",× [sample ptrIfil):
if(x f[sample _ptr]fi]==0)
× Asample ptrifil=-1:
felose(fdi);
for(i O;i<=actual no inputs;it 4)
sum+=(x_f(sample_ptr]fi]*x_f[sample ptr](il);
for(i=0;i<=actual no_inputs;it +)
x_f]sample_ptr][i]=x_f[sample_ptr][i/sqrt(sum);
calculate actual output
float sum, input;
largest=-999;
for(j=0;j<kohonen_nodes;j++){
sum=0.0;
for(i=0;i<=no inputs;it+)
sum += w10 ]*xl;
if(sum>largest)
{
largest=sum;
number =j;
}
I printf("neuron=%d,sum=%fln" j,sum);
printf(".. ");
/ delay(10);
for(j=0; j<kohonen nodes:j++)
````

---

<!-- source: Code-03.pdf; page: 2 -->
<!-- source-image: pages/06-Code-03-page-2.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
\2[i1 0.0;
X2[number]=1.0;
ford=0j kohonen_nodesj++)
if(x2[l==1)
printf?".. ");
/ delay(10);
/I printf‹"wining kohonen =%d\n" j);
for(j 0j<grossberg _nodes;++) {
sum=0.0;
for(i=0; kohonen nodes:it +)
sum += W201 ]*x2|i);
X30]=sum;
for(=0j<grossberg_nodes;jt+)
printf(".."):
I delay(10);
I printf("Ingrossberg = %d %f" j,‹3[il);
/I printf("In
In");
recalculate _weight_matrix)
float sum;
if(learn_ptr==increment +1){
counter += 0.0;
count_beta += 0.0;
else
{
counter+=0.02;
count_beta+=0.02;
train rate_coef- 0.7 * exp(-counter);
for(=0j-kohonen_nodesj++)
for(i=0;¡<no inputs;i++){
if(j==number)
WILLi]-w1DlE]+ (train_rate _coef*(×1 [i]-wIC][i]);
sum=0.0;
````

---

<!-- source: Code-03.pdf; page: 3 -->
<!-- source-image: pages/06-Code-03-page-3.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(i 0;j<no inputs:i+4)
sum += (w1[number}[i]*w1[number]fil)
ift sum > 0.0 )
for(i=0;i<no inputs;i++)
wi[number](i] w1[number||i|/sqrt(sum);
bela=. 1 *exp(-count beta);
for(j=0;j<grossberg nodesjt.+)
for(i O;iskohonen nodes;it+)
if(jaenumber){
w2L1(i]=w2GIli]+(beta*desired(i]-w2C1lil);
increment=learn pt;
initialize _values
float sum;
srand (2);
for(=0; j kohonen nodes; j++)
for(i=0; i<no_inputs; it+)
w1 IL]=(rand()/32676.0 -.5)*1.0;
srand (2);
for(j=0; j<grossberg _nodes; j++)
for(i=0; i<kohonen_nodes; it+)
w2[ill]=(rand(/32676.0 -5)*1.0;
sum = 0.0;
for(j=0; j<kohonen_ nodes; j++)
for(i=0; ¡<no inputs; it+)
sum += (w1filfil * wIGTil;
for(=0; j<kohonen_nodes; j++)
for(i=0; ¡<no _inputs; it +)
w1fi](i] = w1ßlli]/sqrt(sum);
sum = 0.0:
for(j=0; j<grossberg_ nodes; jt +)
for(i=0; i<kohonen nodes; i++)
sum += (w2(If] * w2G]lil;
for(j=0; j-grossberg _ nodes; jt +)
for(i=0; i-kohonen nodes; it+)
w2[1] = w2 Til/sqrt(sum);
````

---

<!-- source: Code-03.pdf; page: 4 -->
<!-- source-image: pages/06-Code-03-page-4.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
for(i 0; i grossberg nodes; i++)
desired|i]=0.0;
train)
int total no_trials;
while (train_rate_coef > 0.01)
for(leam_ptr=0;leam_ptr<n_leam_set;lear_ptr++)
I printf("leam _ptr=%d, training rate =%An", learn_ptr, train_rate _coef);
I printf("beta rate = %An", beta);
for(i-0;i<n_learn_set;it+)
desired[i]=0.0;
desired[learn_ptr]=1.0;
for(i=0;i<no_ inputs;i++)
X1[i]=x_flearn_ptr]lil;
calculate actual output();
recalculate _weight_matrix);
1=999;
test _network()
int test _ptr;
FILE *fdi;
int found;
float sum;
char test_file [20];
cleardevice0;
I cliscr;
for(test _ptr-0;test _ptr<n_ test set;test ptr++)
settextstvle(1.0.1):
outtextxy(100.42." PLEASE ENTER THE TEST FILE NAME: ")
I printf("PLEASE ENTER THE TEST FILE NAME =>
gotoxy(60,4);
scanf("%s", &test_file);
fdi=fopen(test_file, "r");
````

---

<!-- source: Code-03.pdf; page: 5 -->
<!-- source-image: pages/06-Code-03-page-5.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- visual-structure: figure; confidence: 0.60; reasons: non-text-visual-density -->
<!-- review-marker: code-ocr-verification -->
<!-- review-marker: figure-visual-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
fdi=fopen(test _ file,"«");
print("n Reading file ass%sin", test file):
if(fdi== NULL)
printf("could not open input filen");
printf("press any key to continue.");
fclose(fdi:
i=-999;
return(1);
)
printf("la\nReading the data....");
J=-1;
found=999;
do
j++;
if(j%newline charum==0 && jI=0)
fscanf(fdi, "In");
found=fscanf(fdi, "%f",&x f[test _ptr][jl);
while (found!=EOF && j<=no inputs-1);
actual no inputs=j-1;
for(i=0;¡<=actual no _inputs;i++)
if(i%5==0) printf("'m");
printf("%f",×_f[test_ptr]lil);
if(x_f[test_ptr](i]==0)
X_fltest_ptr]li]=-1;
}
fclose(fdi);
getch();
sum=0.0;
for(i=0;<=actual _no _inputs;it +)
sum+=(x_f(test ptr]fi] * ‹_fltest ptr]lil.
if(sum>0.0)
for(i=0;¡<=actual no inputs:i++)
X_f{test _ptr]li]=x_f|test ptr][il/sqri(sum);
for(i=0;¡<no inputs;i++)
X1 [i]=x_f[test ptr]lil;
printf("Inln");
calculate actual output();
outtextxy (300, 400," PRESS ANY KEY TO CONTINUE...");
````

---

<!-- source: Code-03.pdf; page: 6 -->
<!-- source-image: pages/06-Code-03-page-6.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
getch);
¡=999;
void read weights)
static char weightf[]= "weights.wts";
FILE *fdi;
int found = 99;
char temp2[80];
float sum;
clrscrO;
cleardevice0;
fdi=fopen(weightf,"¡");
printf("reading file==>%sIn", weightf);
getch();
if(fdi==-NULL)
{
printf("could not open input file! In");
printf("press any key to continue.");
fclose(fdi);
1=-999;
return;
printf("nin reading the weights.... nin");
getch();
for(i=0;i kohonen _nodes;it+)
for(j=0j<no inputs j++)
{
fscant(fdi,"%f", &w1[_Ll);
printf(*%ft",w1[illil);
}
printf("n");
getch);
cleardevice();
gotoxy(1,1);
for(i=0;¡<grossberg _nodes;it+)
for(j=0:j<kohonen nodes:j++) {
fscanf(fdi,"%f", &w2[ilDl);
printf("%flt",w2(1]DI);
}
printf("n");
````

---

<!-- source: Code-03.pdf; page: 7 -->
<!-- source-image: pages/06-Code-03-page-7.png -->
<!-- structure: code; confidence: 0.90 -->
<!-- review-marker: code-ocr-verification -->

<!-- review: OCR code listing requires verification against the source scan -->

````
felose(fdi);
outtexixy(300, 400," PRESS ANY KEY TO CONTINUE...");
getch);
void save weights)
{
static char weightf]]="weights.wts";
clrscr();
FILE *fdi;
int found = 99;
char temp2[80];
float sum;
cleardevice();
-fdi-fopen (weightf, "w");
sprintf(buffer, "SAVING FILE ==> %s In", weightf);
outtextxy (200, 100, buffer);
if(fdi==NULL)
printf("could not open output filelln");
printf("press any key to continue.");
fclose(fdi);
i=-999;
return;
outlextxy(200,250, "SAVING THE WEIGHTS... ");
/I printf(" ninnInSAVING THE WEIGHTS.
.");
for(i=0;i<kohonen nodes;i++)
for(j=0;j<no inputs:j++)
fprintf(fdi,"%ft",w1 [1]Ul);
printf("In");
}
for(i=0;i<grossberg_nodes;it+)
for(j=0j kohonen_nodesjt+)
fprintf(fdi, "%fl", w2[i]G]);
printf("n"):
````

---

<!-- source: Code-03.pdf; page: 8 -->
<!-- source-image: pages/06-Code-03-page-8.png -->
<!-- structure: layout; confidence: 0.75 -->
<!-- review-marker: layout-visual-verification -->

felose(fdi):
outfexixy(300, 400," PRESS ANY KEY TO CONTINUE....
getch();

---
