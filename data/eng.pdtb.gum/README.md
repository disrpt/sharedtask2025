# eng.pdtb.gum

### The Georgetown University Multilayer (GUM) Corpus - PDTB-style annotations

To cite this corpus, please refer to the following article:

Yang Janet Liu, Tatsuya Aoyama, Wesley Scivetti, Yilun Zhu, Shabnam Behzad, Lauren Elizabeth Levine, Jessica Lin, Devika Tiwari, and Amir Zeldes (2024). [GDTB: Genre Diverse Data for English Shallow Discourse Parsing across Modalities, Text Types, and Domains](https://aclanthology.org/2024.emnlp-main.684/). In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. Miami, Florida, 12287–12303.

```bibtex
@inproceedings{liu-etal-2024-gdtb,
    title = "{GDTB}: Genre Diverse Data for {E}nglish Shallow Discourse Parsing across Modalities, Text Types, and Domains",
    author = "Liu, Yang Janet  and
      Aoyama, Tatsuya  and
      Scivetti, Wesley  and
      Zhu, Yilun  and
      Behzad, Shabnam  and
      Levine, Lauren Elizabeth  and
      Lin, Jessica  and
      Tiwari, Devika  and
      Zeldes, Amir",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.684/",
    doi = "10.18653/v1/2024.emnlp-main.684",
    pages = "12287--12303",
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

The corpus is created as part of the course LING-4427 (Computational Corpus Linguistics) at Georgetown University. Data is annotated in the enhanced RST (eRST) formalism, described in [this paper](https://aclanthology.org/2025.cl-1.3/). While eRST annotations are contained in the folder `data/eng.erst.gum/`, this folder contains PDTB-style connective annotations for the connective detection task, as described in [this paper](https://aclanthology.org/2024.emnlp-main.684/).

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

### Notes on Connectives

GUM guidelines follow PDTB v3 guidelines for the identification of connectives and relation types (explicit, implicit, altlex, etc.), but excludes open-class lexical modifiers of connectives. As a result, the string "six months later" may be considered a connective in eng.pdtb.pdtb, but in eng.pdtb.gum only the word "later" will be annotated as a connective.

Also note that the `.conllu` data contains some reconstructed ellipsis tokens with 
decimal IDs (e.g. 12.1); these do not appear in the other formats and are ignored in token 
index spans.

More GUM guidelines can be found [here](https://wiki.gucorpling.org/gum/rst). 