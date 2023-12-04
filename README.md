# QPong - Quantum Computing Integrated Pong Game

<img width="1000" alt="Aykun Baba" src="https://github.com/ruzgarimren/YHP/assets/135638786/21f27f27-911c-4a80-b86c-4e4d8a45642c">

## Introduction
In this innovative project, a passionate developer has crafted an immersive gaming experience that seamlessly integrates the intricate realms of quantum computing and electrical circuits. Focused on algorithmic design components, the game incorporates an integrated quantum circuit, enabling direct influence over the paddle's behaviors based on the established circuit infrastructure, meticulously created by Ruzgar Imren.

---


## A Unique Fusion of Traditional Gaming and Quantum Principles

"Qpong" presents a unique fusion of traditional gaming with quantum computing principles. In this innovative simulation resembling a classic ball-and-paddle game, one player manages a paddle employing conventional computer-based strategies. Meanwhile, the other player's paddle, controlled by the client, operates through a quantum circuit situated at the bottom of the screen. The quantum circuit, replete with a diverse array of quantum gates, including Toffoli, Controlled X gate, Pauli X gate, S gate, and T dagger gate, empowers the client to intricately manipulate their paddle's behavior within the game. This integration of quantum principles not only elevates the gameplay's challenge but also offers an immersive experience, enabling players to engage with quantum concepts while relishing the thrill of the game.


<img width="1000" alt="Code Block" src="https://github.com/ruzgarimren/YHP/assets/135638786/9dc9513d-4980-4602-8d1e-a1164abb3ba5">

---


## Quantum Circuit Integration for Paddle Control

- **Quantum Paddle Control**: The core gameplay revolves around a quantum circuit that empowers players to control their paddles using quantum gates.
- **Toffoli, Controlled X, Pauli X, S, T Dagger Gates**: Qpong incorporates these quantum gates within the circuit, offering diverse strategies for paddle manipulation.

<img width="1000" alt="Quantum Circuit" src="https://github.com/ruzgarimren/YHP/assets/135638786/9f8295ce-48f1-42f9-bd5e-af33caf2ef7b">

---


## NumPy for Quantum Operations

- **Quantum Circuit Operations**: Qpong utilizes NumPy extensively for efficient representation and manipulation of quantum states, gates, and circuits.
- **Optimized Quantum Logic**: NumPy's array-based operations optimize quantum gate implementations, enhancing the computational efficiency of the quantum simulation.

<img width="1000" alt="Numpy Operations" src="https://github.com/ruzgarimren/YHP/assets/135638786/af67f3a1-63dd-42e6-8d84-0eeac413eb66">

---


## Pygame for an Immersive Gaming Experience

- **Visually Engaging Graphics**: Pygame's powerful rendering capabilities bring vivid and visually appealing elements to Qpong, including paddle, ball, and background imagery.

  - [Fonts Repository](https://github.com/ruzgarimren/YHP/tree/main/sounds)
  
- **Dynamic Sound Effects**: Engaging sound effects enrich the gaming experience, offering auditory feedback on ball movement, paddle hits, and gameplay interactions.

  - [Sounds Repository](https://github.com/ruzgarimren/YHP/tree/main/sounds)

- **Vibrant Visuals**: Pygame enables the inclusion of captivating graphics, delivering visually stimulating elements such as colorful paddles, dynamic ball animations, and vibrant backgrounds.

  - [Images Repository](https://github.com/ruzgarimren/YHP/tree/main/assets/)

<img width="1000" alt="Engaging and Nostalgic Graphics" src="https://github.com/ruzgarimren/YHP/assets/135638786/ddccdb72-9256-4d52-9242-987d7cbe4b2a">

---


## Resources

- [IBM Quantum Computing Lab](https://quantum-computing.ibm.com/lab)
- [QOSF Projects](https://qosf.org/project_list/)
- [Quantum Computing Open Source Projects](https://medium.com/@mnf710104/quantum-computing-open-source-projects-f23e7ead31ec)
- [NumPy Documentation](https://numpy.org/doc/)
- [IBM Research YouTube Channel](https://www.youtube.com/@ibmresearch)
- [Qiskit YouTube Channel](https://www.youtube.com/@qiskit)
- [Pygame Documentation](https://www.pygame.org/docs/)

---

## Forks
<img width="1000" alt="Kamil Fork" src="https://github.com/ruzgarimren/YHP/assets/135638786/780e2c5a-303b-4185-963c-67cfd932cfc4">

---


# Qiskit
[![License](https://img.shields.io/github/license/Qiskit/qiskit-terra.svg?)](https://opensource.org/licenses/Apache-2.0) <!--- long-description-skip-begin -->
[![Release](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg)](https://github.com/Qiskit/qiskit-terra/releases)
[![Downloads](https://img.shields.io/pypi/dm/qiskit-terra.svg)](https://pypi.org/project/qiskit-terra/)
[![Coverage Status](https://coveralls.io/repos/github/Qiskit/qiskit-terra/badge.svg?branch=main)](https://coveralls.io/github/Qiskit/qiskit-terra?branch=main)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qiskit)
[![Minimum rustc 1.64.0](https://img.shields.io/badge/rustc-1.64.0+-blue.svg)](https://rust-lang.github.io/rfcs/2495-min-rust-version.html)
[![Downloads](https://static.pepy.tech/badge/qiskit-terra)](https://pepy.tech/project/qiskit-terra)<!--- long-description-skip-end -->
[![DOI](https://zenodo.org/badge/161550823.svg)](https://zenodo.org/badge/latestdoi/161550823)

**Qiskit**  is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.

This library is the core component of Qiskit, which contains the building blocks for creating and working with quantum circuits, quantum operators, and primitive functions (sampler and estimator).
It also contains a transpiler that supports optimizing quantum circuits and a quantum information toolbox for creating advanced quantum operators. 

For more details on how to use Qiskit, refer to the documentation located here:

<https://docs.quantum.ibm.com/>


## Installation

We encourage installing Qiskit via ``pip``:

```bash
pip install qiskit
```

Pip will handle all dependencies automatically and you will always install the latest (and well-tested) version.

To install from source, follow the instructions in the [documentation](https://qiskit.org/documentation/contributing_to_qiskit.html#install-install-from-source-label).

## Create your first quantum program in Qiskit

Now that Qiskit is installed, it's time to begin working with Qiskit. The essential parts of a quantum program are:
1. Define and build a quantum circuit that represents the quantum state
2. Define the classical output by measurements or a set of observable operators
3. Depending on the output, use the primitive function `sampler` to sample outcomes or the `estimator` to estimate values.

Create an example quantum circuit using the `QuantumCircuit` class:

```python
import numpy as np
from qiskit import QuantumCircuit

# 1. A quantum circuit for preparing the quantum state |000> + i |111>
qc_example = QuantumCircuit(3)
qc_example.h(0)          # generate superpostion
qc_example.p(np.pi/2,0)  # add quantum phase
qc_example.cx(0,1)       # 0th-qubit-Controlled-NOT gate on 1st qubit
qc_example.cx(0,2)       # 0th-qubit-Controlled-NOT gate on 2nd qubit
```

This simple example makes an entangled state known as a [GHZ state](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state) $(|000\rangle + i|111\rangle)/\sqrt{2}$. It uses the standard quantum gates: Hadamard gate (`h`), Phase gate (`p`), and CNOT gate (`cx`). 

Once you've made your first quantum circuit, choose which primitive function you will use. Starting with `sampler`,
we use `measure_all(inplace=False)` to get a copy of the circuit in which all the qubits are measured:

```python
# 2. Add the classical output in the form of measurement of all qubits
qc_measured = qc_example.measure_all(inplace=False)

# 3. Execute using the Sampler primitive
from qiskit.primitives.sampler import Sampler
sampler = Sampler()
job = sampler.run(qc_measured, shots=1000)
result = job.result()
print(f" > Quasi probability distribution: {result.quasi_dists}")
```
Running this will give an outcome similar to `{0: 0.497, 7: 0.503}` which is `000` 50% of the time and `111` 50% of the time up to statistical fluctuations.  
To illustrate the power of Estimator, we now use the quantum information toolbox to create the operator $XXY+XYX+YXX-YYY$ and pass it to the `run()` function, along with our quantum circuit. Note the Estimator requires a circuit _**without**_ measurement, so we use the `qc_example` circuit we created earlier.

```python
# 2. define the observable to be measured 
from qiskit.quantum_info import SparsePauliOp
operator = SparsePauliOp.from_list([("XXY", 1), ("XYX", 1), ("YXX", 1), ("YYY", -1)])

# 3. Execute using the Estimator primitive
from qiskit.primitives import Estimator
estimator = Estimator()
job = estimator.run(qc_example, operator, shots=1000)
result = job.result()
print(f" > Expectation values: {result.values}")
```

Running this will give the outcome `4`. For fun, try to assign a value of +/- 1 to each single-qubit operator X and Y 
and see if you can achieve this outcome. (Spoiler alert: this is not possible!)

Using the Qiskit-provided `qiskit.primitives.Sampler` and `qiskit.primitives.Estimator` will not take you very far. The power of quantum computing cannot be simulated 
on classical computers and you need to use real quantum hardware to scale to larger quantum circuits. However, running a quantum 
circuit on hardware requires rewriting them to the basis gates and connectivity of the quantum hardware.
The tool that does this is the [transpiler](https://qiskit.org/documentation/apidoc/transpiler.html) 
and Qiskit includes transpiler passes for synthesis, optimization, mapping, and scheduling. However, it also includes a
default compiler which works very well in most examples. The following code will map the example circuit to the `basis_gates = ['cz', 'sx', 'rz']` and a linear chain of qubits $0 \rightarrow 1 \rightarrow 2$ with the `coupling_map =[[0, 1], [1, 2]]`.

```python
from qiskit import transpile
qc_transpiled = transpile(qc_example, basis_gates = ['cz', 'sx', 'rz'], coupling_map =[[0, 1], [1, 2]] , optimization_level=3)
```

For further examples of using Qiskit you can look at the tutorials in the documentation here:

<https://qiskit.org/documentation/tutorials.html>

### Executing your code on real quantum hardware

Qiskit provides an abstraction layer that lets users run quantum circuits on hardware from any vendor that provides a compatible interface. 
The best way to use Qiskit is with a runtime environment that provides optimized implementations of `sampler` and `estimator` for a given hardware platform. This runtime may involve using pre- and post-processing, such as optimized transpiler passes with error suppression, error mitigation, and, eventually, error correction built in. A runtime implements `qiskit.primitives.BaseSampler` and `qiskit.primitives.BaseEstimator` interfaces. For example,
some packages that provide implementations of a runtime primitive implementation are:

* https://github.com/Qiskit/qiskit-ibm-runtime

Qiskit also provides a lower-level abstract interface for describing quantum backends. This interface, located in
``qiskit.providers``, defines an abstract `BackendV2` class that providers can implement to represent their
hardware or simulators to Qiskit. The backend class includes a common interface for executing circuits on the backends; however, in this interface each provider may perform different types of pre- and post-processing and return outcomes that are vendor-defined. Some examples of published provider packages that interface with real hardware are:

* https://github.com/Qiskit/qiskit-ibm-provider
* https://github.com/qiskit-community/qiskit-ionq
* https://github.com/qiskit-community/qiskit-aqt-provider
* https://github.com/qiskit-community/qiskit-braket-provider
* https://github.com/qiskit-community/qiskit-quantinuum-provider
* https://github.com/rigetti/qiskit-rigetti

<!-- This is not an exhaustive list, and if you maintain a provider package please feel free to open a PR to add new providers -->

You can refer to the documentation of these packages for further instructions
on how to get access and use these systems.

## Contribution Guidelines

If you'd like to contribute to Qiskit, please take a look at our
[contribution guidelines](CONTRIBUTING.md). By participating, you are expected to uphold our [code of conduct](CODE_OF_CONDUCT.md).

We use [GitHub issues](https://github.com/Qiskit/qiskit-terra/issues) for tracking requests and bugs. Please
[join the Qiskit Slack community](https://qisk.it/join-slack) for discussion, comments, and questions.
For questions related to running or using Qiskit, [Stack Overflow has a `qiskit`](https://stackoverflow.com/questions/tagged/qiskit).
For questions on quantum computing with Qiskit, use the `qiskit` tag in the [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/questions/tagged/qiskit) (please, read first the [guidelines on how to ask](https://quantumcomputing.stackexchange.com/help/how-to-ask) in that forum).


## Authors and Citation

Qiskit is the work of [many people](https://github.com/Qiskit/qiskit-terra/graphs/contributors) who contribute
to the project at different levels. If you use Qiskit, please cite as per the included [BibTeX file](CITATION.bib).

## Changelog and Release Notes

The changelog for a particular release is dynamically generated and gets
written to the release page on Github for each release. For example, you can
find the page for the `0.9.0` release here:

<https://github.com/Qiskit/qiskit-terra/releases/tag/0.9.0>

The changelog for the current release can be found in the releases tab:
[![Releases](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg?style=flat&label=)](https://github.com/Qiskit/qiskit-terra/releases)
The changelog provides a quick overview of notable changes for a given
release.

Additionally, as part of each release detailed release notes are written to
document in detail what has changed as part of a release. This includes any
documentation on potential breaking changes on upgrade and new features.
For example, you can find the release notes for the `0.9.0` release in the
Qiskit documentation here:

https://qiskit.org/documentation/release_notes.html#terra-0-9

## Acknowledgements

We acknowledge partial support for Qiskit development from the DOE Office of Science National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage (C2QA) under contract number DE-SC0012704.

## License

[Apache License 2.0](LICENSE.txt)


---
![pygame](https://raw.githubusercontent.com/pygame/pygame/main/docs/reST/_static/pygame_logo.svg)

|AppVeyorBuild| |PyPiVersion| |PyPiLicense|
|Python3| |GithubCommits| |BlackFormatBadge|

Pygame_ is a free and open-source cross-platform library
for the development of multimedia applications like video games using Python.
It uses the `Simple DirectMedia Layer library`_ and several other
popular libraries to abstract the most common functions, making writing
these programs a more intuitive task.

`We need your help`_ to make pygame the best it can be!
New contributors are welcome.

## Installation

Before installing pygame, you must check that Python is installed
on your machine. To find out, open a command prompt (if you have
Windows) or a terminal (if you have MacOS or Linux) and type this:

   python --version

If a message such as "Python 3.8.10" appears, it means that Python
is correctly installed. If an error message appears, it means that
it is not installed yet. You must then go to the [official website](https://www.pygame.org/docs/) and follow the instructions.

Once Python is installed, you have to perform a final check: you have
to see if pip is installed. Generally, pip is pre-installed with
Python but we are never sure. Same as for Python, type the following
command:

   pip --version

If a message such as "pip 20.0.2 from /usr/lib/python3/dist-packages/pip
(python 3.8)" appears, you are ready to install pygame! To install
it, enter this command:

   pip install pygame

## Help

If you are just getting started with pygame, you should be able to
get started fairly quickly.  Pygame comes with many tutorials and
introductions.  There is also full reference documentation for the
entire library. Browse the documentation on the [docs page](https://www.pygame.org/docs/). You
can also browse the documentation locally by running
`python -m pygame.docs` in your terminal. If the docs aren't found
locally, it'll launch the online website instead.

The online documentation stays up to date with the development version
of pygame on GitHub.  This may be a bit newer than the version of pygame
you are using. To upgrade to the latest full release, run 
`pip install pygame --upgrade` in your terminal.

Best of all, the examples directory has many playable small programs
which can get you started playing with the code right away.

Pygame is a powerful library for game development, offering a wide 
range of features to simplify your coding journey. Let's delve into 
what pygame has to offer:

### Features

- **Graphics:** With pygame, creating dynamic and engaging graphics has
never been easier. The library provides simple yet effective tools for
2D graphics and animation, including support for images, rectangles, 
and polygon shapes. Whether you're a seasoned game developer or just
starting out, pygame has you covered.
- **Sound:** Pygame also includes support for playing and manipulating sound
and music, making it easy to add sound effects and background music to
your games. With support for WAV, MP3, and OGG file formats, you have 
plenty of options to choose from.
- **Input:** Pygame provides intuitive functions for handling keyboard, mouse,
and joystick input, allowing you to quickly and easily implement player
controls in your games. No more struggling with complex input code, pygame
makes it simple.
- **Game Development:** Lastly, pygame provides a comprehensive suite of tools
and features specifically designed for game development. From collision 
detection to sprite management, pygame has everything you need to create
exciting and engaging games. Whether you're building a platformer, puzzle
game, or anything in between, pygame has you covered.

## Building From Source

If you want to use features that are currently in development,
or you want to contribute to pygame, you will need to build pygame
locally from its source code, rather than pip installing it.

Installing from source is fairly automated. The most work will
involve compiling and installing all the pygame dependencies.  Once
that is done, run the `setup.py` script which will attempt to
auto-configure, build, and install pygame.

Much more information about installing and compiling is available
on the [Compilation wiki page](https://www.pygame.org/wiki/Compilation).

## Contribution

- Thank you for thinking of contributing!
- To contribute to the main [project documentation](https://www.pygame.org/docs/), see `docs/README.md` or view more detailed instructions [here](https://github.com/pygame/pygame/tree/main/docs).
- New to contributing to Open Source Free Libre software? 
  - There is a draft of `"Let's write a unit test!" <http://renesd.blogspot.com/2019/11/draft-2-of-lets-write-unit-test.html>`_ which is a step by step guide on how to write your first unit test in Python for pygame, which is very similar to how you would do it for other projects.
  - Want or need to compile pygame from source? See the [compilation page](https://www.pygame.org/wiki/Compilation) for more detailed instructions.
  - For a detailed developer guide on "How to Hack Pygame", head to the [Hacking Page](https://www.pygame.org/wiki/Hacking).
  - Beginner developers looking for ways to contribute to the project can look at issues labeled `"good first issue" <https://github.com/pygame/pygame/labels/good%20first%20issue>`_ or `"Difficulty: Easy" <https://github.com/pygame/pygame/issues?q=is%3Aopen+is%3Aissue+label%3A%22Difficulty%3A+Easy%22>`_.
  - To submit patches and report bugs, visit the [Bugs & Patches](https://www.pygame.org/wiki/patchesandbugs) page for detailed instructions.
  - See the [info page](https://www.pygame.org/wiki/info) for more info and ways to get in touch with the Pygame team.

## Credits

Thanks to everyone who has helped contribute to this library.

Many thank you's for people making documentation comments, and adding to the
pygame.org wiki.

Also many thanks for people creating games and putting them on the
pygame.org website for others to learn from and enjoy.

There's many more folks out there who've submitted helpful ideas, kept
this project going, and basically made our life easier.  Thanks!

Many thank you's for people making documentation comments, and adding to the
pygame.org wiki.

Also many thanks for people creating games and putting them on the
pygame.org website for others to learn from and enjoy.

Lots of thanks to James Paige for hosting the pygame bugzilla.

Also a big thanks to Roger Dingledine and the crew at SEUL.ORG for our
excellent hosting.

Dependencies
------------

Pygame is obviously strongly dependent on SDL and Python.  It also
links to and embeds several other smaller libraries.  The font
module relies on SDL_ttf, which is dependent on freetype.  The mixer
(and mixer.music) modules depend on SDL_mixer.  The image module
depends on SDL_image, which also can use libjpeg and libpng.  The
transform module has an embedded version of SDL_rotozoom for its
own rotozoom function.  The surfarray module requires the Python
NumPy package for its multidimensional numeric arrays.
Dependency versions:

- CPython >= 3.6 (Or use PyPy3)
- SDL >= 2.0.8
- SDL_mixer >= 2.0.0
- SDL_image >= 2.0.2
- SDL_ttf >= 2.0.11
- SDL_gfx (Optional, vendored in)
- NumPy >= 1.6.2 (Optional)

## License

This library is distributed under [GNU LGPL version 2.1](https://www.gnu.org/copyleft/lesser.html).  We reserve the right to place
future versions of this library under a different license.

The programs in the `examples` subdirectory are in the public domain.

See docs/licenses for licenses of dependencies.