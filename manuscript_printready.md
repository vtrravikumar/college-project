---
# ------------------------------------------------------------------
# Book Identity
# ------------------------------------------------------------------

title: ANALYSIS OF ARTIFICIAL NEURAL NETWORK
subtitle: USING BACK PROPAGATION & GENETIC ALGORITHM
author:
  - KUMARESAN U
  - RAGUPATHI KUMAR D.
  - RAVI KUMAR V.T.R.

# ------------------------------------------------------------------
# Publication
# ------------------------------------------------------------------

edition: Reading Draft
version: v1.0
copyright_year: 2026
# ------------------------------------------------------------------
# Layout
# ------------------------------------------------------------------

type: technical-document
language: en
---
# ANALYSIS OF ARTIFICIAL NEURAL NETWORK

## VIVA VOCE EXAMINATION



The Viva Voce Examination of the Project work done by RAVI KUMAR V.I.R. E 451640 (Reg. No) in partial fulfillment of the requirements for the B.E degree in COMPUTER SCIENCE & ENGINEERING was held on 13 OCTOBER'98 


INTERNAL EXAMINER                                   EXTERNAL EXAMINER

## CERTIFICATE



This is to certify that the project titled "Analysis of Artificial Neural Network" is a bonofide work done be by RAVI KUMAR V.T.R. Reg.No E451640 in partial fulfillment of the requirement for the award of the degree of Bachelor of Engineering in Computer Science and Engineering during 1994-1998. 




PROJECT GUIDE                                       HEAD OF THE DEPARTMENT 

## Acknowledgement

We are thankful to our Director Dr. V. Shanmuganathan for giving excellent opportunity for taking up the course and providing a conducive environment to finish our project successfully.

We extend our sincere thanks to Prof.S. Ramakrishnan.(System Manager & Head Of CSE Dept.) for his guidance and suggestions towards the improvement of our project. 

We have immense pleasure in thanking our guide Miss.Shameem Fathima and our guide Mr. R.Balasubramanian under whose guidance the project has been shaped in a very successful manner. 

Last but not the least we would like to thank the Technical support group of our Brainland Computer Centre for providing all that we needed and staying late in the night for us. 

Above all, I express my gratitude to my beloved parents for shaping me as an Engineer.

## Abstract

The aim of the project is to implement a system based on Genetic algorithm with enhanced encoding. The system is used to evolve forward Artificial Neural Network which has been applied to problem areas of boolean functions. 

Evolving Neural Network means that optimizing of the connection and connectivity of the Neural Network. Although many techniques like Back Propagation learning exists, a new approach using Genetic Algorithm has been tried in this work

Genetic Algorithm is randomized search technique that is domain free, robust and has a fast rate of convergence. Genetic Algorithm search methods are rooted in the mechanism of evolution and natural genetics. They combine survival of the fittest among string randomized information exchange to form search algorithm with some of the innovative flairs of human search.

In this project we compare the efficiency of Genetic Algorithm and Back Propagation Algorithm and observe that Genetic Algorithm are efficient and robust optimization tools which outperform their counterpart.

## INTRODUCTION

### GENERAL

Artificial Neural Net models have been studied for many years on the hope of achieving human-like performance in various fields to find number of real world applications. These models are composed of many non - linear computational elements operating in parallel and arranged in patterns reminiscent of biological neural nets. Computational elements or nodes are connected by weights that are typically adapted during use to improve performance. There has been a recent resurgence in the field of Artificial Neural Networks caused by new net topologies, algorithms and analog VLSI implementation techniques. 

Standard techniques exist for training Neural Networks. But there is still a need for better and efficient techniques to train Neural Networks. In the proposed project, this problem has been modelled as an optimization problem and novell approach called *GENETIC ALGORITHM* has been adopted to solve it.

### STATE OF THE ART

Currently there are various classical optimization techniques. 

Calculus based methods use a set of necessary and sufficient conditions to be satisfied by the solution of an optimization problem. This method can be further divided into Direct and Indirect methods. These techniques can be used only in a restricted set of well. behaved problem. 

Enumerated techniques search every point related to an objective function's domain space one point at a time. They are simple to implement but may required significant computation. 

Guided random search techniques are based on enumeration techniques but use additional information to guide the search They can solve very complete problems. The major sub classes are Simulated Annealing and Evolutionary Algorithms. Both are evolutionary processes. But Simulated Annealing on the other hand are based on natural selection principles. This form of search evolves throughout generations, improving the features of potential solutions by means of biologically inspired operations . This in turn subdivided into Evolutionary Strategies and Genetic Algorithms.

GAs came into existence as a result of doctoral dissertation of Dr.John Holland of university of Michigan, Ann Arbor. Ever since it gained immense popularity and prominence and have been applied to a number of areas .A lot of research work have been carried out throughout the world .David E. Goldberg, prof, General Engineering, University of Illinois at Urbana-campaign, has been a forerunner of research in GA and has produced one of the widely referenced text on GA .Dr. Kenneth De jong of george Mason University has proposed a test suite that attempts to formalize the concepts behind the working of GA.

### MOTIVATION OF THE PROJECT

The field of Genetic Algorithm is new and evolving. It has a wide variety of application. 

One of the major problem in constructing any Neural Network is fixing the inter neuron weight in real - time .Genetic algorithm to be a useful integration, when not a viable alternative to more common algorithm such as Back propagation .So these stood as a cause of motivation to pursue this project.

### SCOPE OF THE PROJECT

Artificial Neural Network have a spectrum of practical application in various fields. The work of this project can be applied for determining the optimal network for any such application.

## PROBLEM DEFINITION AND METHODOLOGY

### PROBLEM DEFINITION

The aim of the project is to implement a system based on Genetic algorithm with enhanced encoding. The system is used to evolve feed forward. Artificial Neural Network which has been applied to problem areas of boolean function learning and Robot arm movement.

### METHODOLOGY

A Generic algorithm emulates biological evolutionary theories to solve optimization problems .A GA consist of set individual elements ( the population) and a set of biologically inspired operators defined over the population itself. According to evolutionary theories, only the most suited elements in a population are likely to survive and generates offspring , thus transmitting their biological heredity to new generations. In computing terms, a GA maps a problem onto a set of (typically binary)strings, each string representing a potential solution. The GA that manipulates the most promising strings in its search for improved solution. Thus this concept is applied to a Neural Network design it as an optimization problem. First an initial set of individuals are generated, each representing a concatenated string of weights of the links of a neural network. Tine each string is evaluated for a fitness solution using the objective function of calculating the mean squared error by feed forwarding on the network.

As per the GA the fitter string i.e., one with aless error will be eligible for survival and the strings of lesser fitness are omitted from going to next generation. The GA operations like reproduction, crossover, mutation etc. are applied in every generation and this process is repeated for a fixed number of generation or until a fittest solution is evaluated. The string with optimal fitness value will be taken as final concatenated weight of the links

## EVOLUTIONARY DESIGN CONCEPTS

### INTRODUCTION

Technology periodically steals a leaf from nature's book Evolutionary design paradigm is one such example. This paradigm is focused on Genetic Algorithm to explore its advantage over conventional algorithms while learning neural networks.

### GENETIC ALGORITHM

Genetic Algorithm are essentially robust search algorithm based on the mechanics of natural selection and natural genetics. They are best suited for problems having comparatively larger solution spaces. They use randomized information exchange between solutions to obtain an optimal solution. Genetic Algorithms start with a finite set of solution strings called the initial population and then apply the operators, Reproduction, Crossover & Mutation These operators are applied repeatedly thereby guiding the search towards better and better solutions. The power of GA stands in its ability to exploit historical information to improve future performance. Moreover the algorithm conducts a parallel search by sampling various parts of the hyperplane of solution at the same time.

#### ALGORITHM INTERNALS

I.GO GAs work by maintaining a population of candidate solutions to a given problem.. Each solution is stored as an artificial chromosome, represented by a string of bits,integers or characters(usually represented by bits). An initial population of solution is created randomly. Only a fixed number of candidate solutions are transferred from one generation to the next. Those solutions that are less fit tend to die off( this is done by selection operation to be discussed later). Successively new solutions are created by building on the better solution previously encountered( this is done using crossover and mutation operators explained later) thereby inducing the search to become successively concentrated in areas of current optima.

#### TERMINOLOGIES USED

Many biological terms are used in the Genetic Algorithm literature. The pool of solutions is often called the "population", individual strings in the pool are "chromosome", individual features are "genes" and the value of the feature in a particular solution is "allele". Example don In a particular problem, a variable x to be optimized is evolved using 4-bit encoded string. The illustration of strings during some intermediate step is shown in the table X3 X4 X2

### THE ALGORITHM

#### PSEUDOCODE

The Genetic Algorithm pseudo code is given as, Initialise population POPIO]. Evaluate population POPIOI. Generation =1. While termination criterion not reached Select solutions for POPIGeneration] from POPIGeneration-1]. Perform Crossover on POP[Generation]. Perform Mutation on POP[Generation]. Evaluate POPIGeneration]. Generation = Generation + 1

#### OVERVIEW

The initial population is usually created randomly. Individual members of the population i.e., chromosomes are selected for the next generation in proportion of their fitness, the measure of how near the particular solution is form the optimal solution. Two parent chromosomes are altered using generic operator to produce two children. The resultant children are each evaluated and assigned a fitness value. Next, the strings of old population is replaced by the new fittest string and the process is repeated. The stopping criterion can be maximum number of iteration, convergence or reaching an acceptable fitness level.

DIAGRAMATIC ILLUSTRATION: The working of GA can be illustrated diagramatically as in figure Offsprings Decoded strings Population (Chromosomes) New Generation Evaluation (Fitness) Genetic Operators Parents Selection Reproduction Manipulation Mates Thus a GA has the following components, a population of binary strings control parameters. a fitness function. genetic operators. a selection mechanism & a mechanism to encode the solution as binary strings.

#### OPERATORS DESCRIPTION

SELECTION OPERATOR Selection models nature's "survival of the fitness" mechanism. Fitter solution survive while weaker one perish. It can be done using a ranking method, roulette wheel selector or by tournament selection. In roulette-wheel selection, each chromosome is assigned a pie-shaped slice on a roulette-wheel where the size is proportional to the fitness of the individual chromosome. The spin is simulated by gencrating and the total of individual fitness. The winning chromosome is the one in whose slice the roulette spinner ends up. In rank based selection, two individuals are chosen using roulette wheel and the member with higher fitness is selected. In tournament selection, a set of individuals are sequentially chosen, and the member with the highest fitness is added to the mating pool. CROSSOVER OPERATOR The purpose of cross over is to create children whose genetic material resembles their parent's genes in some fashion. Thus is done with a hope that a child will have better features of both of its parents. A simple, one-point crossover between two individuals proceed in two steps. First, a cross site along the string length is chosen uniformly at random. Then the position values are exchanged between the two strings following the cross site

For example, if two selected strings are, A1111 B= 00000000 If the random choice of cross site turns out to be three, the two new strings got are, C=11100000 D=00011111 following the crossover operation. There are other two types of crossover namely multipoint crossover, partially matched crossover useful for particular application. MUTATION OPERATOR It is the occasional alteration of a chromosome like flipping a bit which has a low probability. Mutation is used to rejuvenate the search, extending the search into previously unexplored areas. It also helps in restoring lost genetic material. For example, if all the strings in a population have converged to zero at a given position and the optimal solution has a one at that position. Then crossover cannot generate a one there, while mutation could.

#### PROBLEM DEPENDENT ISSUES

The remaining components apart from the operators are grouped under problem dependent issues as they can be decided upon the given problem.

They are, Encoding mechanism - Representation of the problem as a string of digits Fitness - A means of evaluating individual potential solutions. Control parameters - The specification of problem parameters. ENCODING MECHANISM Fundamental to GA structure is the encoding mechanism for representing the optimization variables. The encoding mechanism depends upon the number of variables and the range of values taken by the variables. The length of the binary string is determined for each variables depending on its range. The bit strings for all the variables are usually concatenated and used. Sometimes, if they are real valued continuous variables, it linearly mapped and it is encoded using fixed number of bits FITNESS FUNCTION: In Generic Algorithm, the fitness value of each chromosome has to be evaluated. For this, a fitness function is needed. This function should return a value that is indicative of how good the solution string is. The fitness returned is high for fitter strings and low for worse ones. Obviously, it should return the highest value for an optimal string. Thus fitness function is problem dependent. For example, in a LPP with a maximising objective function, the objective function can be used as fitness function.

FIXUP OF CONTROL PARAMETERS The parameters of GA like probabilities of crossover and mutation, number of generations, population size and the length of strings are decided based on problem domain

### COMPARISION WITH OTHER TECHNIQUES

In order for GA to surpass their more traditional cousins in the quest for robustness, GA must differ in some very fundamental ways. Genetic algorithms are different from more normal optimization search procedures in the following ways. Advantages: GAs works with a coding of the parameter set, rather than the parameter themselves. * GAs search from a population of points, rather than from a single point. * GAs use payoff(objective function) information and not derivatives or other auxiliary knowledge. * GAs make use of probabilistic rather than deterministic transition rules.

Disadvantages: * The lack of an accurate measure of their convergence to the optimum and their intuitive nature as opposed to other proven and well established methods. * The loss of accuracy while approximating the solution string for the sake of representability in digital computers.

### Conclusion

GAs are efficient and robust optimization tools which outperform their counterparts. They are applied in search, optimization and machine learning. They have their own drawbacks owing to the limited nature of digital computers in terms of computational power, storage and the lack of formal proof of the facts behind their working

## DESIGN OF ANN EVOLUTION USING GA

### INTRODUCTION

Artificial neural systems are characterised by a set of nodes and interconnecting links. Given an application, a Neural Network has to be trained to learn to correlate a given input to an output. In this chapter, it has been shown how GA can be applied to designing and training a neural Networks. Evolutionary learning for ANNs has been introduced to perform a global exploration of the search space, thus avoiding the problem of stagnation that is characteristic of local search procedures.

### NEURAL NETWORK DESIGN PROBLEM

The problem is to determine an optimal network structure and optimal set of weights of connection of the structure for a given application. More clearly the problem involves two sub problems.

#### DETERMINING THE NEURAL NETWORK

ARCHITECTURE A fully connected Neural Network may contain some links which will not affect its performance. These redundant links can be pruned. Thus an optimal Neural Network in terms of number of links has to be obtained. Such a network will be cost-effective and will work ] better.

#### DETERMINING THE SET OF WEIGHTS

In a Neural Network, knowledge is stored in the weights of its links. Finding an optimal set of weights for the links of a Neural Network that produces the least deviance of the actual output from the desired output completes the Neural Networks design.

### APPLICATION OF EVOLUTIONARY DESIGN PRINCIPLES

TO NN DESIGN PROBLEM As said earlier, the NN design problem cosists of optimizing connections and weights of the network. Since, evolutionary design procedures are essentially optimizing tools, it is high time now to get into the details of how they can be applied to solve the NN design problem. The two major design issues, as elucidated in last chapter are addressed for the problem at hand as follows:-

#### STRING REPRESENTATION OF SOLUTIONS

The string representation for the two optimization problems i.e. weights and connections are separately discussed below:

#### WEIGHT OPTIMIZATION

The objective of the problem is to determine an optimal set of weights for the network links. Since there are as many weights as the number of links in a network, to put in optimization jargon, there are that many decision variables to optimize. Thus a single solution string must be able to represent all the weights of the network so that GA can optimize them at a stroke. To make this possible, a string is chosen which is a concatenation of encoded weights of all the links of the network. In the process of encoding the weights, the following, problem specific details are considered. DISCRENTIZATION Typically, NN weights are real numbers. To encode them into binary strings, the procedure of discretiozation in which these weights are scaled by proper factor (power often) is adopted, so as to convert them into integers. These integers are then converted into binary numbers. The following example illustrates the procedure.

Let the weight be 2.63. Assuming a scaling factor of 100 i.e. 10 the scaled weights will be 263. The binary equivalent of it is 11111101. EXCESS NOTATION Ingeneral, NNweights can take both positive and negative values. In order to accommodate for this an "excess notation" for representing the weights is used. In this notation number that fall in the range -x to +x are mapped on to the range 0 to 2x. E For example if the weight falls within the range of -4.5 to +4.5, it will be linearly mapped onto a value in the range O to +9 FIXING THE RANGE The first question that stems in one's mind while encoding the weights is on the decision on the number of bits to be used for the representation. The possible range of values that the weights take is the sole factor that determines this.

#### CONNECTIVITY OPTIMIZATION

For optimising the number of links, the presence or absence ofthe links are encoded into the string. The string length will be equal to the number of links in the network. Link presence is indicated by a 1 and the absence by a 0 in the corresponding bit in the string.

### FITNESS FUNCTION ONE

The goodness of the solution the NN design problem is determined by the deviance of the actual performance from the desired performance of the network. In general, the fitness function measures their goodness

#### WEIGHT OPTIMIZATION

For the weight optimization problem, each member of the set of weights that is represented by a solution string, is assigned to a corresponding link in the network. Then, the network is run in a feed forward fashion with training data. For each input output pair of the training data, the net error of the network is calculated by summing up the squared errors of the output nodes of the network. The resultant error is the sum of the squared net errors of the samples. The objective is to minimise this resultant error. Here GA minimises the fitness function and the fitness function is devised as, F(C) = ERR(C) F(C) = Fitness of the individual chromosome. ERR(C) = Error of the individual chromosome.

#### CONNECTIVITY OPTIMIZATION

In the connectivity optimization problem, the fitness of a given set of links is determined by the quickness with which the weights of the links that are present in the network are optimised. To put this in precise terms, consider a population of network architecture with different sets of links. Each of these network is run for a fixed number of generations. The minimised error at the end of this process in each case is noted. Fitter architecture is the one having less error. APPLICATION & RESULTS

## APPLICATIONS AND RESULTS

### BENCH-MARKING APPLICATION

#### BOOLEAN FUNCTION LEARNING

The problem dealt here are toy applications which are often used for testing and bench marking a network. Typically the training set contains all possible input patterns, so there is no question of generalisation. The result obtained when training using Back propagation Algorithm and that using Genetic Algorithm are given in this sub-division.

#### RESULTS OF BP AND GA EVOLUTION

EXCLUSIVE OR Problem Definition : The problem is to produce the output which is the XOR function of the given input value. Parameters Of WIN : The initial configuration is, two nodes in the input layer two nodes in the first hidden layer, two nodes in the second hidden layer, and single node in the output layer. The network is fully connected

Optimal set ofweights Links weights 2.081 5.732 .1.013 5.564 .4.215

836

337

-5. 538 -5.689 4.210 OUTE Neural Network For Exclusive OR All weight of the links contribute to the network

Parameter of GA :- 100 Chromosome length 25 Population size 1400 No. of generation 0.9 Probability of cross over Probability of mutation 0.04 -5.58,5,8 Range of weights Training Data :- OUTPUT INPUT 0 two node Optimal set of weights & links :- Optimal set oflink

Time comparison of GA & BP! -

secs

[Time taken for training using BP

secs

Time taken for training using GA THREE BIT PARITY Problens denition The problem is to produce an output of 1 if there is an odd number of Is in the input pattern. O otherwise Darameters Of NIN The initial configuration is, three nodes in the input layer, two nodes in the first hidden layer, two nodes in the second hidden layer and a single node in the output layer. The network is not fully connected Parameters of GA 132 Chromosome length 30 Population S1ze 1000 No. of generation Probability of cross over 0. 0.09 Probability of mutation -12, 12 Range of weights

Training data :- INPUT OUTPUT Optimal set of weights & links Optimal set of link 111011110111 Optimal set of weights weights Links -3187 7.34 -6.41 0.00 6.21 -4.63 155 -5.03 0.00 -0.07 5.09 -1.85 12

Neural Network For Exclusive OR Weights of links 4,9, are zero & others are non zero. So the link with zero weights are pruned from the network. Time comparison of GA & BP: - Ting secs Time taken for training using BP

secs

Time taken for training using GA

DECODER Problem Definition:- The problem involves, producing the output which is the decoded values of the given input. Parameters of NN:- The initial configuration is, three nodes in the input layer, two nodes in the first hidden layer, two nodes in the second hidden layer and three node in the output layer. The network is not fully connected. Parameters of GA: - chromosome length 170 Population size 25 No. of generation 1900 Probability of cross over 0.5 Probabilit of mutation 0.01 RanGe of weights -12,12 Training Data :- INPUT OUTPUT 0 0

Optimal set of weights & links :- Optimal set of link Optimal set ofweights links weights .7.27 0.00 .5 02 -11.55 3.45 0.00 2.92 8.18 .9.61 0.00 -2.38 8.28 -6.5 2.57 -2.05 5.09 Neural Network For Exclusive Decoder problem Weights of link 2,6,10 are zero others are all non zero

Time Comparison of GA & BP !-

secs

Time taken for training using BP

secs

Time taken for training using GA

#### Conclusion

Thus the results of both, training using a Back propagation Algorithm and that with a genetic Algorithm infers that the GA has a faster rate of convergence than a conventional training algorithm.

### REAL-WORLD APPLICATION

### ROBOT INVERSE KINEMATIC PROBLEM

#### INTRODUCTION

Although Neural Networks applicable to the solution of robotics control problem are in fect, neuro controllers, their function is specialised mainly to provide solution to robot arm movement problems. Robot kinematics involves the study of the geometry of manipulator linkages, kinematics if fundamental importance for robot design and control

#### PROBLEM DEFINITION

OVERVIEW Trajectory control of robotics manipulator traditionally consists of following a pre-programmed sequence of end effector movements Robot control usually requires control signals applied at the joints of the robot while the desired trajectory, or the sequence of arm end positions, is specified for the end effector. The geometry of an idealised planar robot manipulator with 2 degrees of freedom below. 82 01, 02 - Joint Angles 81 The Robot arms operate in a plane. To make the arm move, desired coordinates of the end effector point (x,y) are fed to the robot controller so that it generates the joint angle (01,02) for the motors that move the arms. To perform end effector position control of a robotics manipulator Inverse kinematics problem need to be solved. THE PROBLEM Given the Cartesian coordinates of the end effector, the problem is to map this coordinate to the angle by which the links of the robot manipulator have to be moved to reach that point. There are mathematical formulae for this mapping in terms of inverse trigonometric function. The real time computation of these formulae is time consuming Instead of using them, a NN is designed which was trained using sufficient number of training patterns for a given path manipulator

#### PROBLEM DOMAIN-DEPENDENT DETAILS

The robot is assumed to have 2 degree of freedom and hence two link s. It is a polar configuration robot (R-R Configuration). Now the problem is to map a Cartesian co- ordinated (x,y,) to the (01,02). of the two links. So inputs is (x,y) and the output is (01,02).

#### WEIGHT OPTIMATION

#### FIXING THE GA PARAMETERS

To decide about the exact number of nodes, the range of weights of links between the nodes and the various parameters, initially experiments have been done with a 3-layered fully not connected network. While training the network, that is optimizing its weights with the weight optimization module, many variation have been tried out and promising experimental results are found. The are discussed below:- ADAPTIVE MUTATION When sufficient diversity is not in the current population, mutation probability will be increased so as to diversify the population. BI CROSSOVER Two sets of population are maintained and for crossover, the two parents are chosen one from each of the 2 sets. GA tries to evolve children that have good features of the 2 sets. FIXING THE RANGE OF WEIGHTS When a fully connected three layered network is subjected to weight optimization the decision about the range of weights influences the convergence of the training of the network. For the robot inverse kinematics problem many experiments have been conducted with various range and the best has been found.

FIXING THE POPULATION SIZE Population size is an important GA parameter that influences the parallelism ofGA search. Experiments with various population size have been done for choosing the best size.

#### CONNECTIVITY OPTIMIZATION

Having fixed the parameters of the network and the weight optimization module, one can now embark on the task at hand. Here a two step connectivity optimization is adopted. In the first step, a population of network architecture is evolved. The criterion is that, cach architecture should have different set of connection While evaluating each of the architecture, the weights optimization module is called and the quickness with which the architecture settles to an optimal set of weights is measured. Actually, The weight optimization module is run for a fixed number of generations for each of the architecture. M$$e fitness is assigned to the architecture that settles to less error. Finally the weights of the network with optimal connections are optimized by applying the weight optimization module for sufficient number of generation. Parameter of NN The initial configuration is, eight nodes in the input layer, two nodes in the first hidden layer, two nodes in the second hidden layer and one node in the output The network is not fully connected. layer.

Parameters of GA !- 128 Chromosome length 30 Population size 500 No. of generation 0.4 Probability of cross over 0.01 Probability of mutation 1.5.1.5 Range of weights Training Data : Ipput Output 02 y 81 0.290889 2.9386 0.174533 8.40739 0.32725 0.19635 8.25326 3.28037 0.374 8.0309 0.2244 3.70669 0.436333 7.69392 4.24922 0.2618 0.5236 0.31416 7.14987 4.9518 0.6545 5.86087 0.3927 6.19551 0.872667 6.92405 0.5236 4.33232 optimal set of weights & links :- Optimal set of link 111011101111110

Optimal set ofweights links weichts -1.11 0.39 -0.37 nAn -0.73 0.6 nAn 053 063 -15 - 1.42 0.03 0.95 -0.78 16 0.00 Neural Networks for Robot kinematics problem Weights of link 4,8, 11, 16 are zero & others are non-zero. So that the link with zero weights can be pruned from the network. Summed Error: 0.000208

### CONCLUSION

Evolutionary design concepts have been successfully applied to design and to train Neural Network. The results that are obtained confirm the fact that Genetic Algorithm is better tool to train a Neural Network than conventional training tools.

## CONCLUSION

### INTRODUCTION

GAs have shown to be good optimizers for solving problems of NNs. In this chapter future enhancements are given and concluding remarks are done.

### HIGHLIGHTS OF THE WORK

A system based on Evolutionary design concepts to train Neural Networks has been successfully developed, and promising results have been obtained. In this process the following observations are done:- GAs converge quicker to the optimal solution if there is diversity is not guaranteed for all generation and to boost the diversity, adaptiveness was used. This was done by reinitialising the population and increasing the rate of mutation. Parameter tuning is one of the most critical issue relating to both NN training to both NN training and GAs. The effect of varying, certain important parameters has been thoroughly studied and results have been shown in the form of tables and results. The performance of the GA as an optimization tool for training and designing NNs is very good and is comparable to that of the available standard techniques.

It can be concluded that GAs can be applied to solve any optimization problem equally well. Application of Evolutionary concepts to Neural architecture is one such example. It is sure that there are lot more vistas to be explored.

### FUTURE ENHANCEMENT

There are many parameters in GA that can be manipulated and for each and every combination of the parameters, there will be some marked improvement in performance. More study can be made on the impact of these parameters on the GAs performance and the result can be used suitably. Parallelism can be increased by using distributed GAs. Here multiple copies of GAs are run in parallel and from time to time, best solution are exchanged.

## References

D.E.Golberg, "Genetic Algorithm in Search Optimization and Machine learning", Addison Wesley, 1989. [21 Jacek M. Zarada," Introduction to Artificial Neural Systems" ,Jaico publishing India, 1991 [3] James A. Freeman & David M.Skapura,"Neural Network Algorithm, Applications and Programming techniques". Addison Wesley. 1991. [4] Darrel Whitely, Timothy Starkweather & Chris Bogart," Genetic Algorithms and Neural Networks : Optimising Connections anc Connectivity", Parallel Computing, 14(1990) pp 347-361. [5] Daniel Graupe, "Principles of Artificial Neural Network", World Scientific Publication Co. Pte. Ltd. [6] Chin-Teng Lin & C.S George Lee, "Neural Fuzzy System". [71 LiMin Fu, "Neural Networks in Computer Intelligence",McGraw Hill International. APPENDI

## Appendix

### COUNTER PROPAGATION NETWORKS INTRODUCTION: 
The Counterpropagation network developed by Robert Hecht Nielsen goes beyond the representational limits of single - layer networks. As compared to Backpropagation, it can reduce training time by hundredfold Counter propagation is a combination of two well-known algorithms; the self - organizing map of Kohonen and the Grossberg The Counter propagation network functions as a look-up table capable of generalization. The training process associates input vectors with corresponding output vectors. These vectors may be binary consisting of ones and zeros, or continuous. Once the network is trained application of an input vector produces the desired output vector. The generalization capability of the network allows it to produce a correct output even when it is given an input vector that is partially incorrect. This makes the network useful for pattern -recognition, pattern - completion, and signal - enhancement applications.

### NETWORK STRUCTURE: 
The neuron in layer O serve only as fan - out points and perform no computation. Each layer O neuron connects to every neuron in layer 1 (called the KOHONEN LAYER) through a separate weight Wmin these will be collectively reffered to as the weight matrix W. Each neuron in layer 1 is connected to every neuron in layer2 (called the GROSSBERG LAYER) by a weight Vnp ;these comprise the weight matrix V. Input Kohenen Grossherg Laver layer LaveL - Y1 - 72 6 Desired output
Kn

‡ Ga - In e Kohenen Grossnera Neurons Feedfortrard Counterpropagation Network Counter propagation functions in two modes; the NORMAL MODE, in which it accepts an input vector X and produces an output vector Y, and the TRAINING MODE in which an input vector is applied and the weights are adjusted to yield the desired output vector

### NORMAL OPERATION: 
#### The Kohonen layer : 
The Kohonen layer functions in a 'winner- take -all fashion'; that is, for given input vector, one and only one Kohonen neuron outputs a logical one; all other outputs are zero. Associated with each Kohonen neuron it to each input Kohonen neuron K1 has weights wIl,w21,.. wm1, comprising a weight vector WI.These connect by way of the input layer to input signals x1,×2,.....xm,comprising the input vector X. As with neurons in most networks, the NET output of each Kohonen neuron is simply the summation inputs . This may be expressed as follows: .............tWmiXm NET j = wljx1+w2ix2+ where NET i is the NET output of kohonen neuron j NET j = xiwij or in vector notation N= XW where N is the vector of Kohonen layer NET ouputs. The Kohonen neuron with the largest NET value is the 'winner'. Its output is set to one; all others are set to zero.

#### Grossberg Laver: 
The Grossberg layer functions in a familiar manner. Its NET output is the weighted sum of the Kohonen layer outputs k1.k2.k3. ..kn, forming the vector K. The connecting weight vector designated V consists of the weights v11, v21, .....p. The NET output of each Grossberg neuron is then NET i = kiwii where NET j is the output of the Grossberg neuron j, or in vector form Y=KV where Y= the Grossberg - layer output vector K=the Kohonen - layer output vector V= the Grossberg layer weight matrix If the Kohonen layer is operated such that one neuron's NET is at one and all others are at zero, only ane element of the K vector is nonzero, and the calculation is simple. The only action of each neuron in the Grossberg layer is to output the value of the weight that connects it to the single nonzero Kohonen neuron. 

#### TRAINING THE KOHONEN LAYER: 
Kohonen training is aself - organizing algorithm that operates in the supervised mode. For this reason, it is difficult to predict which specific Kohonen neuron will be activated for a given input vector. It is only necessary to ensure that training separates input vectors.

#### Preprocessing the Input Vectors : 
It is highly to normalize all input vector before applyingthem to the network. This is done by dividing each component of an input vector by that vector's length. This length is found by taking the square root of the sum of the squares of all of the vector's components . In symbols Xi'= Xi /(X1^2+X2^2 + hmmm+ Xn^2)^1/2 This converts an input vector into a unit vector pointing in the same direction ;that is, a vector of unit length in n-dimensional space. ring To train the Kohonen layer, an input vector is applied and its dot product is calculated with the weight vector associated with each Kohonen neuron. The neuron with the highest dot product is declared the "winner " and its weighta are adjusted Because the dot product operation used to calculate the NET values is a measure of similarity between the inut and weight vectors the training process actually consists of selecting the Kohonen neuron whose weight is most similar to the input vector, and it still more similar. The network self - organizes so that a given Kohonen neuron has maximum output for a given input vector: The training equation that follows is used Wnew = Wold + (x - Wold ) where Wnew = the new value of a weight connecting an input component x to the winning neuron Wnew = the previous value of this weight

= a training rate coefficient that may vary during the training process Each weight associated with the winning Kohonen neuron is changed by an amount proportional to the difference between its value and the value of the input to which it connects The direction of the change minimizes the difference between the weight its input. The variable is a training rate coefficient that usually starts out at 0.7 and may be gradually reduced during training. This allows large intial steps for rapid, coarse training and smaller steps as the final value approached . If only one input vector were to be associated with each Kohonen neuron, the Kohonen layer could be trained with a single calculation per weight. The weights of a winning neuron would be made equal to the components of the training vector (=1_ Usually the training set includes many input vectors that are similar and the network should be trained to activate the same Kohonen neuron for each of them. In this case, the weights of that neuron should be the average of the input vectors that will activate it. Setting to a low value will reduce the effect of each training step, making the final value an average of the input vectors to which it was trained. In this way, the weights associated with a neuron will assume a value near the "center" of the input vectors for which that neuron is the "winner".

#### Interpolative Mode: 
In the interpolative mode, a group of the Kohonen neurons having the highest outputs is allowed to persent its outputs to the Grossberg layer. The number of neurons in this group must be chosen for the application, and ther is no conclusive evidence regarding an optimum size Once the group is determined , its set of NET outputs is treated as a vector and normalized to until length by dividing each each NET value by the squareroot of the sum of the squares of the NET values in the group. All neurons not in the group have their outputs set to zero. 

#### TRAINING THE GROSSBERG LAYER 
An input vector is applied, the Kohonen outputs are established, and the grossberg outputs are calculated as in normal operation. Next, each weight is adjusted only if it connects to a Kohonen neuron having a nonzero output. The amount of the weight adjustment is proportional to the difference between the weight and desired output of the Grossberg neuron to which it connects. In symbols Vij=Vij old + (Yj -Vij ) Ki Ki = the output of Kohonen neuron i (only one Kohonen neuron where is nonzero ) Yj = component j of the vector of desired outputs Initially is set approximately 0.1 and is gradually reduced as training progresses.

The weights of the grossberg layer will converge to the average values of the desired out whereas the weights of the Kohonen layer are trained to the average values of the inputs. Grossberrg training is supervised; the algorithm has a desired output to which it trains. The unsupervised, self - organising operation of the Kohonen layer produces outputs at indeterminate positions;these mapped to the desired output of the Grossberg layer. 

#### APPLICATION: 
In addition to the usual vector - mapping functions ,counter propagation is useful in Data Compression. Acounter propagation network can be used to compress data prior to transmission, there by reducing the number of bits that must be sent Suppose an image to transmitted. It can be divided into subimages S Each subimage is further sudivided into pixels (picture elements ). Each subimage is then a vector, the elements of which are the pixels of which are the pixels of which the subimage is composed. For simplicity, assume that each pixel is either one (light) or zero (dark) If there are n pixels in asubimage If there are n pixels in asubimage, then n bits will be required to transmit it. If some distortion can be tolerated, substantially fewer bits are actually required to transmit typical images, thereby allowing an image to be transmitted rapidly. This is possible because of the statistical distribution of sub image vectors. Some occur frequently while others occur so seldom that they can be

approximated roughly. The method of vector quantisation finds these shorter bit strings that best represent subimages A Counter propagation network can be used to perform vector quantisation. The set of subimage vectors is used as input to train the kohonen layer in the accertive mode in which only a single neuron is allowed to be 1. The Grossberg weights are trained to produce the binary code of the index of the Kohonen neuron that is 1. For example, if Kohonen neuron 7 is 1 (and the others are all 0), the Grossberg layer will be trained to output 00... ..000111 (the binary code for 7 ). It is this shorter bit string is transmitted. At the receiving end, an identically trained counterpropagation network accepts the binary code and produces the inverse function, an approximation of the original subimage. This method has been applied both to speech and images, yielding dat compression ratios of 10:1 to 100:1. The quality has been acceptable, however some distortion of the data at the receiving end is inevitable.

---