# eng.rst.umuc

## University of Potsdam Multilayer UNSC Corpus (UMUC)

The **University of Potsdam Multilayer UNSC Corpus (UMUC)** was assembled for the analysis of diplomatic speeches given in the UN Security Council (UNSC). The UMUC corpus contains 87 speeches taken from the [UN Security Council Debates Corpus](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KGVSYH), which contains over 25 years of digitized meeting notes.


### Preprocessing and Speeches Selection for UMUC

The preprocessing of the texts includes deleting unnecessary line breaks, removing text that is not part of the speech, and segmenting the text into Elementary Discourse Units. UMUC includes different annotation layers  such as: verbal conflicts (see related [paper](https://aclanthology.org/2024.lrec-main.716.pdf)), automatic average sentiments using Lexicoder ([Young and Soroka, 2012](https://www.tandfonline.com/doi/abs/10.1080/10584609.2012.671234)), and discourse structures using Rhetorical Structure Theory (RST) ([Mann and Thompson, 1988](https://www.degruyterbrill.com/document/doi/10.1515/text.1.1988.8.3.243/html)). To access the UMUC repository with all annotation layers, use the following link: https://github.com/discourse-lab/UMUC

The speeches in the corpus include two agenda items coverinmg the topics: The _Ukraine_ conflict in 2014 after the annexation of Crimea (and before the Minsk II agreement), and the _Women, Peace, and Security agenda_ (_WPS_)  focusing on the role of women in peace and security processes. 


### RST Guidelines

RST is a theory for analyzing the organization of texts and looks at discourse from an intention-driven perspective.
It represents the structure of a text in terms of coherence relations between text spans and captures the "plan" the author devised to influence the audience. In RST, text is segmented into Elementary Discourse Units (EDUs).

The RST layer of UMUC uses the discourse relation set of [Stede et al. 2014](https://www.sfu.ca/~mtaboada/docs/research/RST_Annotation_Guidelines.pdf), including four additional relations (all except *Topic-Comment* from [RST-DT](https://aclanthology.org/W01-1605.pdf), which is from RST layer of the [GUM Corpus](https://link.springer.com/article/10.1007/s10579-016-9343-x): 
* *Same-Unit*
* *Attribution*
* *Textual-Organization*, and 
* *Topic-Comment*. 

The EDU segmentation was done based on [RST-DT](https://aclanthology.org/W01-1605.pdf) and the [GUM Corpus' Wiki](https://wiki.gucorpling.org/gum/rst).

The RST guidelines for UMUC can be found in the following repository: 
https://github.com/linatal/rhetorical_UNSC/

### Licensing

All annotations are licensed under the Creative Commons Attribution (CC-BY) version 4.0.

### References

Please cite this paper if publishing separately about the data.

```bibtex
@inproceedings{zaczynska-stede-2024-rhetorical,
    title = "Rhetorical Strategies in the {UN} Security Council: {R}hetorical {S}tructure {T}heory and Conflicts",
    author = "Zaczynska, Karolina  and
      Stede, Manfred",
    editor = "Kawahara, Tatsuya  and
      Demberg, Vera  and
      Ultes, Stefan  and
      Inoue, Koji  and
      Mehri, Shikib  and
      Howcroft, David  and
      Komatani, Kazunori",
    booktitle = "Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue",
    month = sep,
    year = "2024",
    address = "Kyoto, Japan",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.sigdial-1.2/",
    doi = "10.18653/v1/2024.sigdial-1.2",
    pages = "15--28",
    abstract = "More and more corpora are being annotated with Rhetorical Structure Theory (RST) trees, often in a multi-layer scenario, as analyzing RST annotations in combination with other layers can lead to a deeper understanding of texts. To date, prior work on RST for the analysis of diplomatic language however, is scarce. We are interested in political speeches and investigate what rhetorical strategies diplomats use to communicate critique or deal with disputes. To this end, we present a new dataset with RST annotations of 82 diplomatic speeches aligned to existing Conflict annotations (UNSC-RST). We explore ways of using rhetorical trees to analyze an annotated multi-layer corpus, looking at both the relation distribution and the tree structure of speeches. In preliminary analyses we already see patterns that are characteristic for particular topics or countries."
}
```

## DISRPT 2025 Shared Task Information

For the DISRPT 2025 shared tasks, the data is divided into `train`, `dev`, and `test` partitions roughly balanced for size in tokens for the latter two, comprising 77, 4 and 6 documents, respectively. This dataset contains discontinuous discourse units (split 'same-unit'). 
