# eng.erst.gum

### The Georgetown University Multilayer (GUM) Corpus

To cite this corpus, please refer to the following article:

Amir Zeldes, Tatsuya Aoyama, Yang Janet Liu, Siyao Peng, Debopam Das, and Luke Gessler. 2025. [eRST: A Signaled Graph Theory of Discourse Relations and Organization. Computational Linguistics](https://aclanthology.org/2025.cl-1.3/), 51(1):23–72.

```bibtex
@article{zeldes-etal-2025-erst,
    title = "e{RST}: A Signaled Graph Theory of Discourse Relations and Organization",
    author = "Zeldes, Amir  and
      Aoyama, Tatsuya  and
      Liu, Yang Janet  and
      Peng, Siyao  and
      Das, Debopam  and
      Gessler, Luke",
    journal = "Computational Linguistics",
    volume = "51",
    number = "1",
    month = mar,
    year = "2025",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/2025.cl-1.3/",
    doi = "10.1162/coli_a_00538",
    pages = "23--72",
}
```

## Introduction

GUM is a growing corpus of English texts currently covering 16 text types, each coded using a code within document names:

- academic - Academic writing from Creative Commons sources
- bio - Biographies from Wikipedia
- conversation - Face-to-face conversations from the Santa Barbara Corpus
- court - Courtroom oral transcripts
- essay - Argumentative essays
- fiction - Fiction from Creative Commons sources
- interview - Interviews from Wikimedia
- letter - Private letters and other forms of paper-written (non-e-mail) correspondence
- news - News from Wikinews
- podcast - Podcast recording transcripts
- reddit - Online forum discussions from Reddit
- speech - Political speeches
- textbook - OpenStax open access textbooks
- vlog - YouTube Creative Commons vlogs
- voyage - Travel guides from Wikivoyage
- whow - How-to guides from wikiHow

The corpus is created as part of the course LING-4427 (Computational Corpus Linguistics) at Georgetown University. Data is annotated in the enhanced RST (eRST) formalism, described in 
[this paper](https://aclanthology.org/2025.cl-1.3/). In additional to normal RST relations, the original data contains additional, tree-breaking relations, as well as multiple relations between the same
nodes. The eRST formalism also provides information on the signals for each relation, using a taxonomy of 45 subtypes arranged into 8 categories. This data is the basis for the distinction between
the encoding of the explicit and implicit relation types in the DISRPT .rels data (where explicit means signaling by an explicit discourse marker such as "also" or "on the other hand").

For more details see: https://gucorpling.org/gum

## DISRPT 2023 Shared Task Information

For the DISRPT 2023 shared task on elementary discourse unit segmentation, 
only 11 open text genres were included with plain text, while the remaining twelfth genre, 
containing Reddit forum discussions, **must be reconstructed** using the script 
in `utils/process_underscore_2024.py` (see main repository README).  
Following the 2023 shared task, four more genres were added (court, essay, letter and 
podcast were not included in 2023).

The data follows the established `train`, `dev`, and `test` partitions used for other tasks 
(e.g. for the conll shared task on UD parsing), which can be found [here](https://github.com/amir-zeldes/gum/blob/master/splits.md). 

POS tags and syntactic parses are manually annotated gold data. 

### Notes on Segmentation

GUM eRST guidelines follow the RST-DT segmentation guidelines for English, 
according to which most clauses, 
including adnominal and nested clauses are discourse units. 
This dataset contains discontinuous discourse units (split 'same-unit'). 
Note that the `.conllu` data contains some reconstructed ellipsis tokens with 
decimal IDs (e.g. 12.1); these do not appear in the other formats and are ignored in token 
index spans.


### Notes on Relation Classification

Original GUM data contains 32 fine-grained relation labels including the `same-unit` pseudo-relation, and 15 coarse-grained relation classes, separated via a hyphen (e.g. `adversative-antithesis`, `adversative-concession`, `adversative-contrast`). Relations were converted from eRST annotations using the **chain** dependency algorithm, which attaches each child of a multinuclear node to its preceding sibling with the multinuclear relation, and then attaches the left most child to the parent of the multinuclear node using its outgoing relation. Explicit and implicit relations are distinguished based on eRST signaling annotations indicating the presence of an explicit discourse marker.

A full list of the relation inventory and definitions of individual relations 
can be found [here](https://wiki.gucorpling.org/gum/rst). 