# eng.erst.gentle

### Repository for the DISRPT version of the Genre Tests for Linguistic Evaluation (GENTLE) Corpus

This repository contains DISRPT format versions of the Genre Tests for Linguistic Evaluation (GENTLE) corpus, an English out-of-domain test set following the same multilayer annotations found in the [GUM corpus](https://gucorpling.org/gum/). The texts are of the following 8 genres:

  * dictionary entries
  * live esports commentary
  * legal documents
  * medical notes
  * poetry
  * mathematical proofs
  * course syllabuses
  * threat letters

The data is annotated using Enhanced Rhetorical Structure Theory (eRST), as described in [this paper](https://aclanthology.org/2025.cl-1.3/).

For more details see: https://gucorpling.org/gum/gentle.html

## Splits - test only

The entire corpus is designed to be a *test set* of challenging genres for NLP systems to be evaluated on. Although one can train a model on this corpus, or concatenate it to another training set, we present this entire corpus as a test set, and do not provide any official train / dev data.

## Citing

To cite this corpus, please refer to the following article:

  * Aoyama, Tatsuya, Shabnam Behzad, Luke Gessler, Lauren Levine, Jessica Lin, Yang Janet Liu, Siyao Peng, Yilun Zhu and Amir Zeldes (2023) "GENTLE: A Genre-Diverse Multilayer Challenge Set for English NLP and Linguistic Evaluation". In: Proceedings of the Seventeenth Linguistic Annotation Workshop (LAW-XVII 2023), 166–178. Toronto, Canada.

```bibtex
@inproceedings{aoyama-etal-2023-gentle,
    title = "{GENTLE}: A Genre-Diverse Multilayer Challenge Set for {E}nglish {NLP} and Linguistic Evaluation",
    author = "Aoyama, Tatsuya  and
      Behzad, Shabnam  and
      Gessler, Luke  and
      Levine, Lauren  and
      Lin, Jessica  and
      Liu, Yang Janet  and
      Peng, Siyao  and
      Zhu, Yilun  and
      Zeldes, Amir",
    booktitle = "Proceedings of the 17th Linguistic Annotation Workshop (LAW-XVII)",
    year = "2023",
    address = "Toronto, Canada",
    url = "https://aclanthology.org/2023.law-1.17",
    doi = "10.18653/v1/2023.law-1.17",
    pages = "166--178",
}
```

### Notes on Segmentation

GENTLE follows the RST-DT segmentation guidelines for English, 
according to which most clauses, 
including adnominal and nested clauses are discourse units. 
This dataset contains discontinuous discourse units (split 'same-unit'). 
Note that the `.conllu` data contains some reconstructed ellipsis tokens with 
decimal IDs (e.g. 12.1); these do not appear in the other formats and are ignored in token 
index spans.

### Notes on Relation Classification

Original GENTLE data contains 32 fine-grained relation labels including the `same-unit` pseudo-relation, and 15 coarse-grained relation classes, separated via a hyphen (e.g. `adversative-antithesis`, `adversative-concession`, `adversative-contrast`). Relations were converted from eRST annotations using the **chain** dependency algorithm, which attaches each child of a multinuclear node to its preceding sibling with the multinuclear relation, and then attaches the left most child to the parent of the multinuclear node using its outgoing relation. 

A full list of the relation inventory and definitions of individual relations 
can be found [here](https://wiki.gucorpling.org/gum/rst). 