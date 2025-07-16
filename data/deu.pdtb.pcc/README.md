# deu.pdtb.pcc

## Potsdam Commentary Corpus 2.2 - PDTB annotations


The Potsdam Commentary Corpus 2.2 (PCC 2.2) is a revised and extended version
of the Potsdam Commentary Corpus (Stede 2004), a collection of 176 German
newspaper commentaries (op-ed pieces) that has been annotated with syntax trees
and three layers of discourse-level information: nominal coreference,
connectives and their arguments (similar to the PDTB, Prasad et al. 2008), and
trees reflecting discourse structure according to Rhetorical Structure Theory
(Mann/Thompson 1988).

Connectives have been annotated with the help of a semi-automatic tool, Connanno
(Stede/Heintze 2004), which identifies most connectives and suggests arguments
based on their syntactic category. The other layers have been created manually
with dedicated annotation tools.


### License

The Potsdam Commentary Corpus 2.2 is released under a Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License. You can find a
human-readable summary of the licence agreement here:

http://creativecommons.org/licenses/by-nc-sa/4.0/

If you are using our corpus for research purposes, please cite the following
paper:

  * Bourgonje, P and Stede, M (2020). The Potsdam Commentary Corpus 2.2: Extending Annotations for Shallow Discourse Parsing. Proc. of the Language Resources and Evaluation Conference (LREC), Marseille.

```bibtex
@inproceedings{bourgonje-stede-lrec2020,
    author = "Bourgonje, Peter and Stede, Manfred",
    title = "The Potsdam Commentary Corpus 2.2: Extending Annotations for Shallow Discourse Parsing",
    booktitle = "Proceedings of the 12th International Conference on Language Resources and Evaluation (LREC 2020) (to appear)",
    year = "2020",
    date = "11-16",
    month = "May",
    location = "Marseille, France",
    publisher = "European Language Resources Association (ELRA)",
    address = "Paris, France",
    keywords = ""
}
```

## DISRPT 2025 Shared Task Information

For the DISRPT shared tasks, the data is divided into `train`, `dev`, and`test` partitions, comprising 142, 17 and 17 documents, respectively.  This dataset contains discontinuous discourse units (split 'same-unit'). 

The original labels are retained in .rels files under `orig_label`; for the shared task, the final `label` column should be predicted.

Syntactic (automatic) dependency parses are made available using Stanza, but xpos tags are taken from the original PCC corpus STTS tags, 
and are therefore not harmonized with the universal upos tags column. Due to the original tokenization of the corpus, fused tokens such as 'im', 'ins' etc. are retained in the data without CoNLL-U MWTs.


## References

  * Stede, M. (2004). The Potsdam Commentary Corpus. In Proceedings of the ACL Workshop on Discourse Annotation, pages 96–102. Association for Computational Linguistics.

  * Stede, M. and Heintze, S. (2004). Machine-assisted rhetorical structure annotation. In Proc. of the 20th International Conference on Computational Linguistics, pages 425–431, Geneva.

  * Stede, M. and Neumann, A. (2014). Potsdam Commentary Corpus 2.0: Annotation for Discourse Research. Proc. of the Language Resources and Evaluation Conference (LREC), Reykjavik. 

