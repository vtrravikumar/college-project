# Project Explanation

## Analysis of Artificial Neural Network
### Using Back Propagation & Genetic Algorithm

This document explains the original college project in two levels: first in simple language, and then in Computer Science and Engineering terms. It is intended as a project-orientation document for the reconstruction work, not as a replacement for the original report.

## 1. The project in simple language

Imagine a machine that has many small adjustable knobs.

Each knob controls how strongly one part of the machine influences another part. If the machine gives the wrong answer, we need to adjust those knobs until it gives better answers.

An Artificial Neural Network (ANN) is a mathematical model that works somewhat like this. Its connections have numerical **weights**, and those weights determine how signals flow through the network.

The 1998 project asks a simple but interesting question:

> Instead of adjusting the neural-network weights only by the usual learning method, can we use the idea of evolution to find good weights?

The project compares two approaches:

- **Back Propagation (BP):** gradually adjusts the network's weights using the errors produced by the network.
- **Genetic Algorithm (GA):** creates many possible solutions, tests them, keeps better solutions, combines parts of them, introduces small random changes, and repeats this process over generations.

A simple way to imagine the GA approach is:

1. Create many candidate neural networks.
2. Let each candidate try to solve the problem.
3. Measure how much error each candidate makes.
4. Keep the better candidates.
5. Combine candidates to create new candidates.
6. Randomly change some parts.
7. Repeat for many generations.

The hope is that, just as useful characteristics can emerge through evolution, useful neural-network configurations can be discovered through an evolutionary search.

## 2. The project in Computer Science terms

The project is fundamentally about **using a Genetic Algorithm as an optimisation/search mechanism for a feed-forward Artificial Neural Network**.

The neural network performs the actual computation. The Genetic Algorithm searches for a set of network parameters that produces good results.

Conceptually, the process is:

```
Candidate solution
      |
      v
Neural Network
      |
      v
Output for test data
      |
      v
Error / Fitness
      |
      v
Genetic Algorithm
      |
      +--> Selection
      +--> Crossover
      +--> Mutation
      |
      v
New candidate solutions
      |
      +---- repeat ----+
```

A candidate solution can be represented as a chromosome. The project describes encoding neural-network connection information/weights into strings so that the Genetic Algorithm can operate on candidate solutions.

For each candidate:

1. Decode the candidate representation into neural-network parameters.
2. Feed the input through the network.
3. Compare the network output with the desired output.
4. Calculate an error measure, described in the report using Mean Squared Error (MSE).
5. Use the resulting fitness/error to determine which candidates are retained and reproduced.

The report also discusses **enhanced encoding** and optimisation of network connectivity. The exact historical encoding convention and the precise extent to which connectivity itself was evolved still require verification against the surviving source material.

## 3. What problems did the project investigate?

The report describes experiments involving:

- **XOR**
- **3-bit parity**
- **Decoder**
- **Robot inverse kinematics / robot arm movement**
- **Neural-network connectivity optimisation / pruning**

These examples move from relatively small Boolean problems toward a more application-oriented problem involving robot-arm movement.

The project therefore was not simply an exercise in implementing a neural network. Its central theme was to investigate whether an evolutionary optimisation approach could be used to obtain useful neural-network configurations across different classes of problems.

## 4. Back Propagation versus Genetic Algorithm

The distinction can be understood as the difference between two search strategies.

### Back Propagation

Back Propagation uses the error produced by the network to calculate how the weights should be changed. The weights are adjusted progressively so that the network's output becomes closer to the desired output.

In simplified terms:

```
Network makes an error
        |
        v
Calculate how the error relates to weights
        |
        v
Adjust weights
        |
        v
Try again
```

### Genetic Algorithm

The Genetic Algorithm treats a possible neural-network configuration as an individual in a population.

```
Population of candidate solutions
        |
        v
Evaluate fitness
        |
        v
Select better candidates
        |
        v
Crossover
        |
        v
Mutation
        |
        v
Next generation
```

The important point is that the GA is not itself the neural network. It is the optimisation mechanism used to search for a suitable neural-network configuration.

## 5. What makes the 1998 project interesting today?

The original work belongs to a very different computing environment from today's machine-learning landscape.

The important historical question is therefore not:

> How would we implement this project using today's frameworks?

It is:

> What exactly did the three students build in 1998, what did they claim it demonstrated, and how faithfully can we reproduce that work today?

That distinction is central to the reconstruction.

The 2026 work has two separate stories:

### The 1998 story

Three students built and evaluated a system based on Artificial Neural Networks, Back Propagation and Genetic Algorithms, using the computing tools and techniques available to them at the time.

### The 2026 reconstruction

The surviving report, scans and source material are being recovered and reconstructed so that the original work can be understood, reproduced where evidence permits, and preserved in a modern, reproducible form.

The reconstruction must not silently turn the 1998 work into a modern implementation. Where the historical evidence is incomplete, the uncertainty should be recorded.

## 6. Evidence and reconstruction principles

The project follows this evidence hierarchy:

1. **Original project report / master scan** — primary specification.
2. **Surviving 1998 Watcom C source** — implementation evidence, but subject to extraction/transcription errors.
3. **Modern Python reconstruction** — reproducible reconstruction, not the original implementation.

Therefore:

- The original report remains the source of truth for what the project says it did.
- OCR is treated as a first-pass digitisation aid.
- Surviving source code is treated as evidence and must be visually verified against the original source where semantics matter.
- Missing parameters must not be invented.
- Modern terminology should not be retroactively substituted for historical terminology without evidence.
- Modern experimental results must be clearly distinguished from historical reported results.

## 7. What the current reconstruction is doing

The reconstruction starts with a small, reproducible validation implementation.

The current Phase 1 validation work includes:

- a feed-forward neural network;
- Mean Squared Error;
- a Back Propagation baseline;
- Genetic Algorithm weight optimisation;
- binary weight encoding/decoding utilities;
- the XOR experiment;
- repeated seeded GA runs;
- machine-readable JSON results and a Markdown summary.

The current GA implementation intentionally uses a real-valued chromosome as a stable reconstruction baseline. The historical binary/enhanced encoding convention has not yet been treated as fully verified.

The purpose of this first implementation is therefore **not to claim byte-for-byte reproduction of the 1998 Watcom C program**. It is to establish a controlled modern experiment against which the historical design can be compared.

## 8. The long-term reconstruction path

The intended sequence is:

1. Establish the reconstruction methodology.
2. Inspect and verify the surviving source.
3. Complete the historical reconstruction matrix.
4. Reconstruct the first Boolean experiment.
5. Compare historical and modern results.
6. Measure the modern implementation's runtime separately from historical claims.
7. Add the remaining Boolean experiments.
8. Reconstruct the robot-arm experiment if the surviving evidence is sufficient.
9. Complete the GA versus Back Propagation comparison.
10. Freeze the verified implementation and results.
11. Integrate the findings into the book/manuscript.
12. Preserve the reproducible implementation and supporting evidence in this repository.

## 9. One-sentence explanation

**The 1998 project investigated whether a Genetic Algorithm could evolve useful configurations of a feed-forward Artificial Neural Network, and compared that approach with Back Propagation across Boolean problems and a robot-arm application.**

## 10. Important historical caveat

This document is an explanatory guide. It intentionally separates what is clearly supported by the project material from details that still require verification.

It should therefore be read together with:

- `README.md`
- `docs/reconstruction.md`
- the original report scans under `source/report/`
- the surviving source-code evidence under `archive/original-code/`
- the validation material under `validation/`

As reconstruction progresses, this explanation may be refined when stronger historical evidence is established.
