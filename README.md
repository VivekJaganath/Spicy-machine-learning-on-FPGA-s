Extension and Evaluation of a Python-based High-level Synthesis Tool Flow

**Supervisors:** Prof. Marco Platzner and Lennart Clausing

**Student:** Vivek Jaganath

**What is this thesis about?**

This thesis is based of Hot & spicy [1], Python-based high-level synthesis tool. The main functionalities of Hot & Spicy tools are:
1. translate Python functions to HLS-suitable C functions,
2.  generate Python C wrapper bindings,
3.  automate the FPGA EDA tool flow, and
4.  retarget Python source code to use accelerated libraries

though the tool comes packed with intersting features, the tool is still naive and supports only basic Python applications.

The goal of this thesis is to extend the Hot&Spicy tool to be able to support python data structures, syntax and semantics suitable for meachine learning and data science.


**How is the goal achieved?**

The foucs is the translation of annotated python functions to HLS-suitable c functions. For this Python AST trees are used to decipher python code and convert it to revelent c code.
we extend this convertion process to support python dictionaries, tuples, sets, string and some functions like standard deviation, mean and variance.
	
**Which device is used for Implementation?**

Xilinx Zynq 7020 System-on-Chip on a Xilinx PYNQ board is used.
	
Folder Structure:

* [ ] `  /Documents/Description     `  Description of the project

* [ ] `  /Documents/Presentations   `  Slides of the initial and final presentations

* [ ] `  /Documents/Thesis          `  Thesis file identical to the printed version

* [ ] `  /Documents/Thesis/src      `  TeX source files

* [ ] `  /Code                      `  The developed work including additional documentation

* [ ] `  /Templates		    `  Templates for Thesis, Presentations and the Declaration required in the Thesis

**Refrences:**

1. https://www.isi.edu/projects/spicy/hot_spicy_improving_productivity_python_and_hls_fpgas
