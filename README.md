# DISRPT/sharedtask2025

Repository for DISRPT2025 Shared Task on Discourse Unit Segmentation, Connective Detection, and Discourse Relation Classification.  


**Please check our [FAQ](https://sites.google.com/view/disrpt2025/faq?authuser=0) page on our main [website](https://sites.google.com/view/disrpt2025/home) for more information about the Shared Task, Participation, and Evaluation etc.!**  

**Update (16/05/2025)**: Sample data has been released! 

Additional datasets will be release in June 2025.
Test data as well as surprise datasets will be released in July 2025! 

**Shared task participants are encouraged to follow this repository in case bugs are found and need to be fixed.** 


## Introduction

The [DISRPT 2025](https://sites.google.com/view/disrpt2025/home) shared task, to be held in conjunction with [CODI 2025](https://sites.google.com/view/codi-crac2025/) and [EMNLP 2025](https://2025.emnlp.org/), introduces the fourth iteration of a cross-formalism shared task on **discourse unit segmentation** and **connective detection**, as well as the second iteration of a cross-formalism **discourse relation classification** task.

We *will* provide training, development, and test datasets from all available languages and treebanks in the **RST**, **ERST**, **SDRT**, **PDTB**, **dependency** and **ISO** formalisms, using a uniform format. 
Because different corpora, languages and frameworks use different guidelines, the shared task is meant to promote design of flexible methods for dealing with various guidelines, and help to push forward the discussion of standards for computational approaches to discourse relations. We include data for evaluation with and without gold syntax, or otherwise using provided automatic parses for comparison to gold syntax data.

This year, we provide a unified set of labels for the discourse relation prediction task, to make evaluation across datasets easier. This labelset only contains **17 different labels**, while we counted **353 different labels** in the original data.


## Types of Data
The tasks are oriented towards finding the locus and type of discourse relations in texts, rather than predicting complete trees or graphs. For frameworks that segment text into non-overlapping spans covering each entire documents (RST and SDRT), the segmentation task corresponds to finding the **starting point of each discourse unit**. For PDTB-style datasets, the unit-identification task is to identify the **spans of discourse connectives** that explicitly identify the existence of a discourse relation. These tasks use the files ending in `.tok` and `.conllu` for the **plain** text and **parsed** scenarios respectively.  

For relation classification, two discourse unit spans are given in text order together with the direction of the relation and context, using both plain text data and stand-off token index pointers to the treebanked files. Information is included for each corpus in the `.rels` file, with token indices pointing to the `.tok` file, though parse information may also be used for the task. The column to be predicted is the final label column; the penultimate `orig_label` column gives the original label from the source corpus, which may be different, for reference purposes only. This column may not be used. The relation direction column may be used for prediction and does not need to be predicted by systems (essentially, systems are labeling a kind of ready, unlabeled but directed dependency graph).  

Note that some datasets contain **discontinuous** discourse units, which sometimes nest the second unit in a discourse relation. In such cases, the unit beginning first in the text is considered `unit1` and gaps in the discourse unit are given as `<*>` in the inline text representation. Token index spans point to the exact coverage of the unit either way, which in case of discontinuous units will contain multiple token spans.  


### Notes on Discourse Relations

Compared to the data of the 2023 shared task, we provide a unified set of **17 labels** across all datasets. Note that some datasets will not include all the 17 labels (e.g. Attribution is only annotated in RST datasets). 

The full mapping is given as a json file in utils/mapping_disrpt25.json.



<!---
*Note about MWE*..............
--->


## Rules
External resources are allowed, including NLP tools, word embeddings/pre-trained language models, and **other** gold datasets for MTL etc. However, no further gold annotations of the datasets included in the task may be used (example: you may not use OntoNotes coref to pretrain a system that will be tested on WSJ data from RST-DT or PDTB, since this could contaminate the evaluation; exception: you may do this if you exclude WSJ data from OntoNotes during training).

**Training with dev is not allowed.** One could do so (e.g. as an experiment) and report the resulting scores in their paper, but such results will not be considered / reported as the official scores of the system in the overall ranking. 

We propose a new constraint and two tracks this year: **only one multilingual model should be submitted per task**, with a limited number of parameters for the Closed-track:
* Closed track: **Parameter-count limited**, openly reproducible models will be evaluated by the DISRPT team and ranked
* Open track: We also welcome descriptions of systems based on large / closed models, but these will not participate in the final rankings as we cannot evaluate them.


Please also make sure to use seeds to keep performance as reproducible as possible!


## Evaluation

Evaluation scripts are provided for all tasks under [`utils`](https://github.com/disrpt/sharedtask2025/tree/main/utils).
In general, final results of each dataset will be reported on the corresponding`test` partition. 

**For datasets without a corresponding training set** (e.g. `eng.dep.covdtb`, `tur.pdtb.tedm`):  

- The scores will be reported as any other regular datasets on the `test` partition 
using the relation inventory of each respective dataset
  - one can collapse relations in any way one would like to during training, but the final results will be reported on each dataset's own relation labels, as indicated in the last column (i.e. `label`) in the corresponding test `.rels` file. 
- Systems can be trained on either a corpus with the same language or any other combination of the datasets available in DISRPT 2025. 
- For better interpretation of the results, we kindly ask you to 
  - document the composition of the training data in your README.md file as well as the paper describing the system. 
  - also report model performance on `dev` sets (wherever applicable) in the paper describing the system (this can go into the appendix of the paper)



## Directories

The shared task repository currently comprises the following directories:

  * `data` - individual corpora from various languages and frameworks. 
    * Folders are given names in the scheme `LANG.FRAMEWORK.CORPUS`, e.g. `eng.rst.gum` is the directory for the GUM corpus, which is in English and annotated in the framework of Rhetorical Structure Theory (RST).
    * Note that some corpora (eng.rst.rstdt, eng.pdtb.pdtb, tur.pdtb.tdb, zho.pdtb.cdtb) **do not contain text** or have some documents without text (eng.rst.gum) and text therefore needs to be reconstructed using `utils/process_underscores.py`.
  * `utils` - scripts for validating, evaluating and generating data formats. The official scorer for segmentation and connective detection is `seg_eval.py`, and the official scorer for relation classification is `rel_eval.py`.

See the README files in individual data directories for more details on each dataset.


## Surprise Language(s)
To be announced in July!


## Submitting a System

Systems should be accompanied by a regular workshop paper in the EMNLP format, as described on [the CODI workshop website](https://sites.google.com/view/codi-crac2025/home?authuser=0). During submission, you will be asked to supply a URL from which your system can be downloaded. If your system does not download necessary resources by itself (e.g. word embeddings), these resources should be included at the download URL. The system download should include a README file describing exactly how paper results can be reproduced. Please do not supply pre-trained models, but rather instructions on how to train the system using the downloaded resources and **make sure to seed your model** to rule out random variation in results. For any questions regarding system submissions, please contact the organizers.

## Important Dates
- **May 16th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sample` release**
- June 16th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`train/dev` release
- July 14th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`test` release
- August 1st, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System release
- September 19th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Camera ready
- November 8 or 9th, 2025  &nbsp; &nbsp; &nbsp; &nbsp; CODI CRAC Workshop, EMNLP, China.


## Statistics

