# DISRPT/sharedtask2025

Repository for DISRPT2025 Shared Task on Discourse Unit Segmentation, Connective Detection, and Discourse Relation Classification.  


**Please check our [FAQ](https://sites.google.com/view/disrpt2025/faq) page on our main [website](https://sites.google.com/view/disrpt2025/) for more information about the Shared Task, Participation, and Evaluation etc.!**  

**Update (17/06/2025)**: Full training data has been released! (Note: some surprise languages/datasets may be added during the testing phase)

**Update (29/05/2025)**: Parameter count limitation: closed track participants must ensure that the total number of parameters in their system is below 4 billion.

**Update (16/05/2025)**: Sample data has been released! 

Test data as well as surprise datasets will be released in July 2025! 

**Shared task participants are encouraged to follow this repository in case bugs are found and need to be fixed.** 


## Introduction

The [DISRPT 2025](https://sites.google.com/view/disrpt2025/) shared task, to be held in conjunction with [CODI 2025](https://sites.google.com/view/codi-crac2025/) and [EMNLP 2025](https://2025.emnlp.org/), introduces the fourth iteration of a cross-formalism shared task on **discourse unit segmentation** and **connective detection**, as well as the second iteration of a cross-formalism **discourse relation classification** task.

We *will* provide training, development, and test datasets from all available languages and treebanks in the **RST**, **eRST**, **SDRT**, **PDTB**, **dependency** and **ISO** formalisms, using a uniform format. 
Because different corpora, languages and frameworks use different guidelines, the shared task is meant to promote design of flexible methods for dealing with various guidelines, and help to push forward the discussion of standards for computational approaches to discourse relations. We include data for evaluation with and without gold syntax, or otherwise using provided automatic parses for comparison to gold syntax data.

This year, we provide a unified set of labels for the discourse relation prediction task, to make evaluation across datasets easier. This labelset only contains **17 different labels**, while we counted **353 different labels** in the original data.


## Types of Data

The tasks are oriented towards finding the locus and type of discourse relations in texts, rather than predicting complete trees or graphs. For frameworks that segment text into non-overlapping spans covering each entire documents (RST and SDRT), the segmentation task corresponds to finding the **starting point of each discourse unit**. For PDTB-style datasets, the unit-identification task is to identify the **spans of discourse connectives** that explicitly identify the existence of a discourse relation. These tasks use the files ending in `.tok` and `.conllu` for the **plain** text and **parsed** scenarios respectively.  

For relation classification, two discourse unit spans are given in text order together with the direction of the relation and context, using both plain text data and stand-off token index pointers to the treebanked files. Information is included for each corpus in the `.rels` file, with token indices pointing to the `.tok` file, though parse information may also be used for the task. The column to be predicted is the final label column; the penultimate `orig_label` column gives the original label from the source corpus, which may be different, for reference purposes only. This column may not be used. The relation direction column may be used for prediction and does not need to be predicted by systems (essentially, systems are labeling a kind of ready, unlabeled but directed dependency graph).  

Note that some datasets contain **discontinuous** discourse units, which sometimes nest the second unit in a discourse relation. In such cases, the unit beginning first in the text is considered `unit1` and gaps in the discourse unit are given as `<*>` in the inline text representation. Token index spans point to the exact coverage of the unit either way, which in case of discontinuous units will contain multiple token spans.  


### Notes on Discourse Relations

Compared to the data of the 2023 shared task, we provide a unified set of **17 labels** across all datasets. Note that some datasets will not include all the 17 labels (e.g. attribution is only annotated in RST/eRST/dependency datasets). 

The full mapping is given as a json file in utils/mapping_disrpt25.json.



<!---
*Note about MWE*..............
--->


## Rules

External resources are allowed, including NLP tools, word embeddings/pre-trained language models, and **other** gold datasets for MTL etc. However, no further gold annotations of the datasets included in the task may be used (example: you may not use OntoNotes coref to pretrain a system that will be tested on WSJ data from RST-DT or PDTB, since this could contaminate the evaluation; exception: you may do this if you exclude WSJ data from OntoNotes during training). For more details on external resources please see the FAQ on the [shared task website](https://sites.google.com/view/disrpt2025/faq).

**Training with dev is not allowed.** One could do so (e.g. as an experiment) and report the resulting scores in their paper, but such results will not be considered / reported as the official scores of the system in the overall ranking. 

We propose a new constraint and two tracks this year: **only one multilingual model should be submitted per task**, with a limited number of parameters for the Closed-track:

* Closed track: **Parameter-count limited (<=4B)**, openly reproducible models will be evaluated by the DISRPT team and ranked.
* Open track: We also welcome descriptions of systems based on large / closed models, but these will not participate in the final rankings as we cannot evaluate them.


Please also make sure to **use seeds** to keep performance as reproducible as possible!


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


## Surprise Language(s) and Dataset(s)

DISRPT25 surprise languages are Polish and Nigerian Pidgin.
DISRPT25 also includes a surpise framework with one dataset annotated within the ISO frmaework.

The surprise datasets are: 
* deu.pdtb.pcc
* eng.rst.umuc 
* pcm.pdtb.disconaija 
* pol.iso.pdc 
* zho.pdtb.ted


## Submitting a System

Systems should be accompanied by a regular workshop paper in the EMNLP format, as described on [the CODI workshop website](https://sites.google.com/view/codi-crac2025/home?authuser=0). During submission, you will be asked to supply a URL from which your system can be downloaded. If your system does not download necessary resources by itself (e.g. word embeddings), these resources should be included at the download URL. The system download should include a README file describing exactly how paper results can be reproduced. Please do not supply pre-trained models, but rather instructions on how to train the system using the downloaded resources and **make sure to seed your model** to rule out random variation in results. For any questions regarding system submissions, please contact the organizers.

## Important Dates
- May 16th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sample` release
- June 17th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`train/dev` release
- **July 16th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`test` release**
- August 4th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System submissions
- September 19th, 2025&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Camera ready
- November 8 or 9th, 2025  &nbsp; &nbsp; &nbsp; &nbsp; CODI CRAC Workshop, EMNLP, China.


## Statistics - test + surprise release

| corpus | lang | framework | rel_types | discont | underscored | rels | train_toks | train_sents | train_docs | train_segs | dev_toks | dev_sents | dev_docs | dev_segs | test_toks | test_sents | test_docs | test_segs | total_sents | total_toks | total_docs | total_segs | seg_style | syntax | MWTs | ellip | corpus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ces.rst.crdt | ces | rst | 17 | yes | no | 1,249 | 11,766 | 663 | 48 | 1,152 | 1,346 | 81 | 3 | 140 | 1,552 | 91 | 3 | 161 | 835 | 14,664 | 54 | 1,453 | EDU | UD | yes | no | ces.rst.crdt |
| deu.pdtb.pcc | deu | pdtb | 11 | yes | no | 2,109 | 26,831 | 1,773 | 142 | 934 | 3,152 | 207 | 17 | 88 | 3,239 | 213 | 17 | 94 | 2,193 | 33,222 | 176 | 1,116 | Conn | UD | no | no | deu.pdtb.pcc |
| deu.rst.pcc | deu | rst | 16 | yes | no | 2,882 | 26,517 | 1,572 | 142 | 2,534 | 3,117 | 184 | 17 | 282 | 3,202 | 188 | 17 | 295 | 1,944 | 32,836 | 176 | 3,111 | EDU | UD | no | no | deu.rst.pcc |
| eng.dep.covdtb | eng | dep | 11 | yes | no | 4,985 | 0 | 0 | 0 | 0 | 29,405 | 1,162 | 150 | 2,754 | 31,502 | 1,181 | 150 | 2,951 | 2,343 | 60,907 | 300 | 5,705 | EDU | UD | yes | no | eng.dep.covdtb |
| eng.dep.scidtb | eng | dep | 14 | yes | no | 9,903 | 62,488 | 2,570 | 492 | 6,740 | 20,299 | 815 | 154 | 2,130 | 19,747 | 817 | 152 | 2,116 | 4,202 | 102,534 | 798 | 10,986 | EDU | UD | yes | no | eng.dep.scidtb |
| eng.erst.gentle | eng | erst | 17 | yes | no | 2,552 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17,979 | 1,334 | 26 | 2,716 | 1,334 | 17,979 | 26 | 2,716 | EDU | UD (gold) | yes | no | eng.erst.gentle |
| eng.erst.gum | eng | erst | 17 | yes | part | 30,747 | 193,740 | 10,910 | 191 | 24,756 | 30,435 | 1,679 | 32 | 3,897 | 30,715 | 1,569 | 32 | 3,775 | 14,158 | 254,890 | 255 | 32,428 | EDU | UD (gold) | yes | yes | eng.erst.gum |
| eng.pdtb.gentle | eng | pdtb | 12 | yes | no | 786 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17,979 | 1,334 | 26 | 466 | 1,334 | 17,979 | 26 | 466 | Conn | UD (gold) | yes | no | eng.pdtb.gentle |
| eng.pdtb.gum | eng | pdtb | 13 | yes | part | 13,879 | 193,740 | 10,910 | 191 | 6,240 | 30,435 | 1,679 | 32 | 972 | 30,715 | 1,569 | 32 | 979 | 14,158 | 254,890 | 255 | 8,191 | Conn | UD (gold) | yes | yes | eng.pdtb.gum |
| eng.pdtb.pdtb | eng | pdtb | 13 | yes | yes | 47,792 | 975,544 | 40,395 | 1,805 | 21,484 | 97,449 | 3,983 | 177 | 2,178 | 100,386 | 4,252 | 180 | 2,386 | 48,630 | 1,173,379 | 2,162 | 26,048 | Conn | UD (gold) | yes | no | eng.pdtb.pdtb |
| eng.pdtb.tedm | eng | pdtb | 13 | yes | no | 529 | 0 | 0 | 0 | 0 | 2,616 | 143 | 2 | 110 | 5,569 | 238 | 4 | 231 | 381 | 8,185 | 6 | 341 | Conn | UD | yes | no | eng.pdtb.tedm |
| eng.rst.oll | eng | rst | 17 | no | no | 2,751 | 37,265 | 1,770 | 293 | 2,511 | 4,601 | 209 | 17 | 280 | 4,605 | 177 | 17 | 288 | 2,156 | 46,471 | 327 | 3,079 | EDU | UD | yes | no | eng.rst.oll |
| eng.rst.rstdt | eng | rst | 17 | yes | yes | 19,778 | 169,321 | 6,672 | 309 | 17,646 | 17,574 | 717 | 38 | 1,797 | 22,017 | 929 | 38 | 2,346 | 8,318 | 208,912 | 385 | 21,789 | EDU | UD (gold) | yes | no | eng.rst.rstdt |
| eng.rst.sts | eng | rst | 17 | no | no | 3,058 | 57,203 | 2,084 | 135 | 2,581 | 7,129 | 264 | 7 | 291 | 6,874 | 243 | 8 | 336 | 2,591 | 71,206 | 150 | 3,208 | EDU | UD | yes | no | eng.rst.sts |
| eng.rst.umuc | eng | rst | 15 | yes | no | 4,997 | 49,727 | 1,950 | 77 | 4,333 | 6,005 | 236 | 4 | 565 | 5,858 | 238 | 6 | 523 | 2,424 | 61,590 | 87 | 5,421 | EDU | UD | yes | no | eng.rst.umuc |
| eng.sdrt.msdc | eng | sdrt | 10 | no | no | 27,848 | 166,719 | 10,494 | 307 | 16,285 | 17,926 | 1,151 | 32 | 1,860 | 46,707 | 3,099 | 101 | 5,015 | 14,744 | 231,352 | 440 | 23,160 | EDU | UD | no | no | eng.sdrt.msdc |
| eng.sdrt.stac | eng | sdrt | 11 | no | no | 12,271 | 42,582 | 5,946 | 887 | 10,159 | 5,149 | 717 | 105 | 1,239 | 4,540 | 731 | 109 | 1,154 | 7,394 | 52,271 | 1,101 | 12,552 | EDU | UD | no | no | eng.sdrt.stac |
| eus.rst.ert | eus | rst | 16 | yes | no | 3,632 | 30,690 | 1,599 | 116 | 2,785 | 7,219 | 366 | 24 | 677 | 7,871 | 415 | 24 | 740 | 2,380 | 45,780 | 164 | 4,202 | EDU | UD | no | no | eus.rst.ert |
| fas.rst.prstc | fas | rst | 14 | yes | no | 5,191 | 52,497 | 1,713 | 120 | 4,607 | 7,033 | 202 | 15 | 576 | 7,396 | 264 | 15 | 670 | 2,179 | 66,926 | 150 | 5,853 | EDU | UD | yes | no | fas.rst.prstc |
| fra.sdrt.annodis | fra | sdrt | 12 | yes | no | 3,321 | 22,515 | 1,020 | 64 | 2,255 | 5,013 | 245 | 11 | 556 | 5,171 | 242 | 11 | 618 | 1,507 | 32,699 | 86 | 3,429 | EDU | UD | no | no | fra.sdrt.annodis |
| ita.pdtb.luna | ita | pdtb | 11 | yes | no | 1,525 | 16,209 | 2,423 | 42 | 671 | 2,983 | 453 | 6 | 139 | 6,050 | 874 | 12 | 261 | 3,750 | 25,242 | 60 | 1,071 | Conn | UD | no | no | ita.pdtb.luna |
| nld.rst.nldt | nld | rst | 16 | no | no | 2,264 | 17,562 | 1,156 | 56 | 1,662 | 3,783 | 255 | 12 | 343 | 3,553 | 240 | 12 | 338 | 1,651 | 24,898 | 80 | 2,343 | EDU | UD | no | no | nld.rst.nldt |
| pcm.pdtb.disconaija | pcm | pdtb | 13 | yes | no | 9,903 | 111,843 | 7,279 | 138 | 3,268 | 14,561 | 991 | 18 | 369 | 14,325 | 972 | 20 | 388 | 9,242 | 140,729 | 176 | 4,025 | Conn | UD (gold) | no | no | pcm.pdtb.disconaija |
| pol.iso.pdc | pol | iso | 12 | yes | no | 8,543 | 129,689 | 7,518 | 459 | 4,226 | 13,923 | 790 | 49 | 463 | 13,368 | 834 | 48 | 426 | 9,142 | 156,980 | 556 | 5,115 | EDU | UD | no | no | pol.iso.pdc |
| por.pdtb.crpc | por | pdtb | 12 | yes | no | 11,327 | 147,594 | 4,078 | 243 | 3,994 | 20,102 | 581 | 28 | 621 | 19,153 | 535 | 31 | 544 | 5,194 | 186,849 | 302 | 5,159 | Conn | UD | no | no | por.pdtb.crpc |
| por.pdtb.tedm | por | pdtb | 13 | yes | no | 554 | 0 | 0 | 0 | 0 | 2,785 | 148 | 2 | 102 | 5,405 | 246 | 4 | 203 | 394 | 8,190 | 6 | 305 | Conn | UD | no | no | por.pdtb.tedm |
| por.rst.cstn | por | rst | 15 | yes | no | 4,993 | 52,177 | 1,825 | 114 | 4,601 | 7,023 | 257 | 14 | 630 | 4,132 | 139 | 12 | 306 | 2,221 | 63,332 | 140 | 5,537 | EDU | UD | yes | no | por.rst.cstn |
| rus.rst.rrt | rus | rst | 15 | yes | no | 25,095 | 208,982 | 10,530 | 188 | 22,839 | 24,490 | 1,107 | 19 | 2,555 | 29,023 | 1,494 | 27 | 3,240 | 13,131 | 262,495 | 234 | 28,634 | EDU | UD | no | no | rus.rst.rrt |
| spa.rst.rststb | spa | rst | 16 | yes | no | 3,049 | 43,055 | 1,548 | 203 | 2,472 | 7,551 | 254 | 32 | 419 | 8,111 | 287 | 32 | 460 | 2,089 | 58,717 | 267 | 3,351 | EDU | UD | no | no | spa.rst.rststb |
| spa.rst.sctb | spa | rst | 16 | yes | no | 692 | 10,253 | 326 | 32 | 473 | 2,448 | 76 | 9 | 103 | 3,814 | 114 | 9 | 168 | 516 | 16,515 | 50 | 744 | EDU | UD | no | no | spa.rst.sctb |
| tha.pdtb.tdtb | tha | pdtb | 12 | yes | no | 10,861 | 199,135 | 5,076 | 139 | 8,277 | 27,326 | 633 | 19 | 1,243 | 30,062 | 825 | 22 | 1,344 | 6,534 | 256,523 | 180 | 10,864 | Conn | UD | no | no | tha.pdtb.tdtb |
| tur.pdtb.tdb | tur | pdtb | 13 | yes | yes | 3,176 | 398,515 | 24,960 | 159 | 7,063 | 49,952 | 2,948 | 19 | 831 | 47,891 | 3,289 | 19 | 854 | 31,197 | 496,358 | 197 | 8,748 | Conn | UD | yes | no | tur.pdtb.tdb |
| tur.pdtb.tedm | tur | pdtb | 13 | yes | no | 574 | 0 | 0 | 0 | 0 | 2,159 | 141 | 2 | 135 | 4,127 | 269 | 4 | 247 | 410 | 6,286 | 6 | 382 | Conn | UD | yes | no | tur.pdtb.tedm |
| zho.dep.scidtb | zho | dep | 14 | no | no | 1,297 | 11,288 | 308 | 69 | 871 | 3,852 | 103 | 20 | 301 | 3,621 | 89 | 20 | 235 | 500 | 18,761 | 109 | 1,407 | EDU | UD | no | no | zho.dep.scidtb |
| zho.pdtb.cdtb | zho | pdtb | 9 | yes | yes | 5,270 | 52,061 | 2,049 | 125 | 1,034 | 11,178 | 438 | 21 | 314 | 10,075 | 404 | 18 | 312 | 2,891 | 73,314 | 164 | 1,660 | Conn | UD | no | no | zho.pdtb.cdtb |
| zho.pdtb.ted | zho | pdtb | 15 | yes | no | 13,308 | 144,581 | 6,882 | 56 | 4,701 | 17,809 | 880 | 8 | 589 | 19,520 | 909 | 8 | 668 | 8,671 | 181,910 | 72 | 5,958 | Conn | UD | no | no | zho.pdtb.ted |
| zho.rst.gcdt | zho | rst | 17 | yes | no | 8,413 | 47,639 | 2,026 | 40 | 7,470 | 7,619 | 331 | 5 | 1,144 | 7,647 | 335 | 5 | 1,092 | 2,692 | 62,905 | 50 | 9,706 | EDU | UD | no | no | zho.rst.gcdt |
| zho.rst.sctb | zho | rst | 17 | yes | no | 692 | 9,655 | 361 | 32 | 473 | 2,264 | 86 | 9 | 103 | 3,577 | 133 | 9 | 168 | 580 | 15,496 | 50 | 744 | EDU | UD | no | no | zho.rst.sctb |
| **Total** | **16** | **6** | **17** | **32** | **2** | **311,796** | **3,719,383** | **180,386** | **7,414** | **201,097** | **517,711** | **24,512** | **1,129** | **201,097** | **607,078** | **31,112** | **1,280** | **201,097** | **236,010** | **4,844,172** | **9,823** | **271,007** | **---** | **---** | **17** | **2** | **Total** |
| **corpus** | **lang** | **framework** | **rel_types** | **discont** | **underscored** | **rels** | **train_toks** | **train_sents** | **train_docs** | **train_segs** | **dev_toks** | **dev_sents** | **dev_docs** | **dev_segs** | **test_toks** | **test_sents** | **test_docs** | **test_segs** | **total_sents** | **total_toks** | **total_docs** | **total_segs** | **seg_style** | **syntax** | **MWTs** | **ellip** | **corpus** |

## Statistics - train release

| corpus | lang | framework | rel_types | discont | underscored | rels | train_toks | train_sents | train_docs | train_segs | dev_toks | dev_sents | dev_docs | dev_segs | test_toks | test_docs | total_sents | total_toks | total_docs | total_segs | seg_style | syntax | MWTs | ellip | corpus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ces.rst.crdt | ces | rst | 17 | yes | no | 1,101 | 11,766 | 663 | 48 | 1,152 | 1,346 | 81 | 3 | 140 | 0 | 0 | 744 | 13,112 | 51 | 1,292 | EDU | UD | yes | no | ces.rst.crdt |
| deu.rst.pcc | deu | rst | 16 | yes | no | 2,609 | 26,517 | 1,572 | 142 | 2,534 | 3,117 | 184 | 17 | 282 | 0 | 0 | 1,756 | 29,634 | 159 | 2,816 | EDU | UD | no | no | deu.rst.pcc |
| eng.dep.covdtb | eng | dep | 11 | yes | no | 2,399 | 0 | 0 | 0 | 0 | 29,405 | 1,162 | 150 | 2,754 | 0 | 0 | 1,162 | 29,405 | 150 | 2,754 | EDU | UD | yes | no | eng.dep.covdtb |
| eng.dep.scidtb | eng | dep | 14 | yes | no | 7,993 | 62,488 | 2,570 | 492 | 6,740 | 20,299 | 815 | 154 | 2,130 | 0 | 0 | 3,385 | 82,787 | 646 | 8,870 | EDU | UD | yes | no | eng.dep.scidtb |
| eng.erst.gentle | eng | erst | 17 | yes | no | 2,552 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17,979 | 26 | 1,334 | 17,979 | 26 | 2,716 | EDU | UD (gold) | yes | no | eng.erst.gentle |
| eng.erst.gum | eng | erst | 17 | yes | part | 27,173 | 193,740 | 10,910 | 191 | 24,756 | 30,435 | 1,679 | 32 | 3,897 | 0 | 0 | 12,589 | 224,175 | 223 | 28,653 | EDU | UD (gold) | yes | yes | eng.erst.gum |
| eng.pdtb.gentle | eng | pdtb | 12 | yes | no | 786 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17,979 | 26 | 1,334 | 17,979 | 26 | 466 | Conn | UD (gold) | yes | no | eng.pdtb.gentle |
| eng.pdtb.gum | eng | pdtb | 13 | yes | part | 12,201 | 193,740 | 10,910 | 191 | 6,240 | 30,435 | 1,679 | 32 | 972 | 0 | 0 | 12,589 | 224,175 | 223 | 7,212 | Conn | UD (gold) | yes | yes | eng.pdtb.gum |
| eng.pdtb.pdtb | eng | pdtb | 13 | yes | yes | 43,497 | 975,544 | 40,395 | 1,805 | 21,484 | 97,449 | 3,983 | 177 | 2,178 | 0 | 0 | 44,378 | 1,072,993 | 1,982 | 23,662 | Conn | UD (gold) | yes | no | eng.pdtb.pdtb |
| eng.pdtb.tedm | eng | pdtb | 13 | yes | no | 178 | 0 | 0 | 0 | 0 | 2,616 | 143 | 2 | 110 | 0 | 0 | 143 | 2,616 | 2 | 110 | Conn | UD | yes | no | eng.pdtb.tedm |
| eng.rst.oll | eng | rst | 17 | no | no | 2,480 | 37,265 | 1,770 | 293 | 2,511 | 4,601 | 209 | 17 | 280 | 0 | 0 | 1,979 | 41,866 | 310 | 2,791 | EDU | UD | yes | no | eng.rst.oll |
| eng.rst.rstdt | eng | rst | 17 | yes | yes | 17,623 | 169,321 | 6,672 | 309 | 17,646 | 17,574 | 717 | 38 | 1,797 | 0 | 0 | 7,389 | 186,895 | 347 | 19,443 | EDU | UD (gold) | yes | no | eng.rst.rstdt |
| eng.rst.sts | eng | rst | 17 | no | no | 2,730 | 57,203 | 2,084 | 135 | 2,581 | 7,129 | 264 | 7 | 291 | 0 | 0 | 2,348 | 64,332 | 142 | 2,872 | EDU | UD | yes | no | eng.rst.sts |
| eng.sdrt.msdc | eng | sdrt | 10 | no | no | 21,830 | 166,719 | 10,494 | 307 | 16,285 | 17,926 | 1,151 | 32 | 1,860 | 0 | 0 | 11,645 | 184,645 | 339 | 18,145 | EDU | UD | no | no | eng.sdrt.msdc |
| eng.sdrt.stac | eng | sdrt | 11 | no | no | 11,143 | 42,582 | 5,946 | 887 | 10,159 | 5,149 | 717 | 105 | 1,239 | 0 | 0 | 6,663 | 47,731 | 992 | 11,398 | EDU | UD | no | no | eng.sdrt.stac |
| eus.rst.ert | eus | rst | 16 | yes | no | 3,147 | 30,690 | 1,599 | 116 | 2,785 | 7,219 | 366 | 24 | 677 | 0 | 0 | 1,965 | 37,909 | 140 | 3,462 | EDU | UD | no | no | eus.rst.ert |
| fas.rst.prstc | fas | rst | 14 | yes | no | 4,599 | 52,497 | 1,713 | 120 | 4,607 | 7,033 | 202 | 15 | 576 | 0 | 0 | 1,915 | 59,530 | 135 | 5,183 | EDU | UD | yes | no | fas.rst.prstc |
| fra.sdrt.annodis | fra | sdrt | 12 | yes | no | 2,700 | 22,515 | 1,020 | 64 | 2,255 | 5,013 | 245 | 11 | 556 | 0 | 0 | 1,265 | 27,528 | 75 | 2,811 | EDU | UD | no | no | fra.sdrt.annodis |
| ita.pdtb.luna | ita | pdtb | 11 | yes | no | 1,150 | 16,209 | 2,423 | 42 | 671 | 2,983 | 453 | 6 | 139 | 0 | 0 | 2,876 | 19,192 | 48 | 810 | Conn | UD | no | no | ita.pdtb.luna |
| nld.rst.nldt | nld | rst | 16 | no | no | 1,939 | 17,562 | 1,156 | 56 | 1,662 | 3,783 | 255 | 12 | 343 | 0 | 0 | 1,411 | 21,345 | 68 | 2,005 | EDU | UD | no | no | nld.rst.nldt |
| por.pdtb.crpc | por | pdtb | 12 | yes | no | 10,079 | 147,594 | 4,078 | 243 | 3,994 | 20,102 | 581 | 28 | 621 | 0 | 0 | 4,659 | 167,696 | 271 | 4,615 | Conn | UD | no | no | por.pdtb.crpc |
| por.pdtb.tedm | por | pdtb | 13 | yes | no | 190 | 0 | 0 | 0 | 0 | 2,785 | 148 | 2 | 102 | 0 | 0 | 148 | 2,785 | 2 | 102 | Conn | UD | no | no | por.pdtb.tedm |
| por.rst.cstn | por | rst | 15 | yes | no | 4,721 | 52,177 | 1,825 | 114 | 4,601 | 7,023 | 257 | 14 | 630 | 0 | 0 | 2,082 | 59,200 | 128 | 5,231 | EDU | UD | yes | no | por.rst.cstn |
| rus.rst.rrt | rus | rst | 15 | yes | no | 22,280 | 208,982 | 10,530 | 188 | 22,839 | 24,490 | 1,107 | 19 | 2,555 | 0 | 0 | 11,637 | 233,472 | 207 | 25,394 | EDU | UD | no | no | rus.rst.rrt |
| spa.rst.rststb | spa | rst | 16 | yes | no | 2,623 | 43,055 | 1,548 | 203 | 2,472 | 7,551 | 254 | 32 | 419 | 0 | 0 | 1,802 | 50,606 | 235 | 2,891 | EDU | UD | no | no | spa.rst.rststb |
| spa.rst.sctb | spa | rst | 16 | yes | no | 533 | 10,253 | 326 | 32 | 473 | 2,448 | 76 | 9 | 103 | 0 | 0 | 402 | 12,701 | 41 | 576 | EDU | UD | no | no | spa.rst.sctb |
| tha.pdtb.tdtb | tha | pdtb | 12 | yes | no | 9,517 | 199,135 | 5,076 | 139 | 8,820 | 27,326 | 633 | 19 | 1,360 | 0 | 0 | 5,709 | 226,461 | 158 | 10,180 | Conn | UD | no | no | tha.pdtb.tdtb |
| tur.pdtb.tdb | tur | pdtb | 13 | yes | yes | 2,755 | 398,515 | 24,960 | 159 | 7,063 | 49,952 | 2,948 | 19 | 831 | 0 | 0 | 27,908 | 448,467 | 178 | 7,894 | Conn | UD | yes | no | tur.pdtb.tdb |
| tur.pdtb.tedm | tur | pdtb | 13 | yes | no | 211 | 0 | 0 | 0 | 0 | 2,159 | 141 | 2 | 135 | 0 | 0 | 141 | 2,159 | 2 | 135 | Conn | UD | yes | no | tur.pdtb.tedm |
| zho.dep.scidtb | zho | dep | 14 | no | no | 1,082 | 11,288 | 308 | 69 | 871 | 3,852 | 103 | 20 | 301 | 0 | 0 | 411 | 15,140 | 89 | 1,172 | EDU | UD | no | no | zho.dep.scidtb |
| zho.pdtb.cdtb | zho | pdtb | 9 | yes | yes | 4,512 | 52,061 | 2,049 | 125 | 1,034 | 11,178 | 438 | 21 | 314 | 0 | 0 | 2,487 | 63,239 | 146 | 1,348 | Conn | UD | no | no | zho.pdtb.cdtb |
| zho.rst.gcdt | zho | rst | 17 | yes | no | 7,460 | 47,639 | 2,026 | 40 | 7,470 | 7,619 | 331 | 5 | 1,144 | 0 | 0 | 2,357 | 55,258 | 45 | 8,614 | EDU | UD | no | no | zho.rst.gcdt |
| zho.rst.sctb | zho | rst | 17 | yes | no | 533 | 9,655 | 361 | 32 | 473 | 2,264 | 86 | 9 | 103 | 0 | 0 | 447 | 11,919 | 41 | 576 | EDU | UD | no | no | zho.rst.sctb |
| **Total** | **14** | **5** | **17** | **27** | **2** | **236,326** | **3,256,712** | **154,984** | **6,542** | **184,178** | **462,261** | **21,408** | **1,033** | **184,178** | **35,958** | **52** | **179,060** | **3,754,931** | **7,627** | **216,199** | **---** | **---** | **16** | **2** | **Total** |
| **corpus** | **lang** | **framework** | **rel_types** | **discont** | **underscored** | **rels** | **train_toks** | **train_sents** | **train_docs** | **train_segs** | **dev_toks** | **dev_sents** | **dev_docs** | **dev_segs** | **test_toks** | **test_docs** | **total_sents** | **total_toks** | **total_docs** | **total_segs** | **seg_style** | **syntax** | **MWTs** | **ellip** | **corpus** |
