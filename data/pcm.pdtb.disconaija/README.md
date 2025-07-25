# pcm.pdtb.disconaija

### DiscoNaija: a discourse-annotated Nigerian Pidgin corpus

To cite this corpus, please refer to the following article:

Scholman, M. C., Marchal, M., Brown, A., & Demberg, V. (2025). [DiscoNaija: a discourse-annotated parallel Nigerian Pidgin-English corpus. Language Resources and Evaluation, 1-37.](https://link.springer.com/article/10.1007/s10579-025-09850-3).

```bibtex
@article{scholman2025disconaija,
  title={DiscoNaija: a discourse-annotated parallel Nigerian Pidgin-English corpus},
  author={Scholman, Merel CJ and Marchal, Marian and Brown, AriaRay and Demberg, Vera},
  journal={Language Resources and Evaluation},
  pages={1--37},
  year={2025},
  publisher={Springer}
}
```

## Introduction

DiscoNaija is a parallel English-Nigerian Pidgin corpus of PDTB 3.0-style discourse relation annotations.
It includes annotations of explicit and inter-sentential implicit discourse relations in the PDTB3 framework (Webber et al., 2019). 
Specifically, the corpus contains 11,344 discourse relation annotations over a total of 140,859 words, and 4,952 connectives, over 78 types. The annotations are available for both the English texts and the Nigerian Pidgin texts.

Despite Nigerian Pidgin being the most widely spoken pidgin/creole language in the world (Faraclas, 2021), linguistic resources on Nigerian Pidgin are limited. As part of a larger project studying the syntactic and prosodic structure of Nigerian Pidgin, Caron et al. (2019) created a corpus of transcribed spoken data. The Naija Treebank contains Pidgin utterances, as well as their English translations.  DiscoNaija is an expansion of this Naija Treebank corpus with a discourse annotation layer. The annotation was done on the English texts and then projected to the Nigerian Pidgin texts.

The corpus is freely available at: https://osf.io/8m5vk/

## DISRPT 2025 Shared Task Information

For the DISRPT 2025 shared task on discourse connective identification and discourse relation classification, we only release the annotations for Nigerian Pidgin. 
We follow the established `train`, `dev`, and `test` partitions proposed by the authors.

A few examples were removed from the relation instances, because of some span errors in the original corpus, resulting in the following distribution:

* Split set: train
    * implicit: 4488
    * explicit: 3201
    * altlex: 62
    * hypophora: 83
* Split set: dev
    * implicit: 676
    * explicit: 363
    * altlex: 12
    * hypophora: 1
* Split set: test
    * implicit: 627
    * altlex: 6
    * explicit: 379
    * hypophora: 5

POS tags and syntactic parses are manually annotated gold data. 

### Note on connective identification 

The base units are utterances in dialogues.
The UD tokens contain many symbols representing either some form of punctuation or phenomena related to speech.
These symbols are kept in the conllu and tok files, 

Note that, in a few cases, the connective can appear in an utterance that is not part of arg1 or arg2, but the connective is always attached to arg2 (except for multi tokens connectives, such as even..if where each part possibly belongs to a different utterance).


### Notes on Relation Classification

The symbols are kept in the unit1_text and unit2_text, and the unit1_sent	and unit2_sent in rels files.
The raw versions, u1_raw and u2_raw, in rels files correspond to the raw text distributed with the corpus, and do not contain all these symbols but a classic punctuation.

Original discoNaija contain 35 fine-grained relation labels, following the PDTB3 relation set.
A few examples are annotated with a label 'narration-answer': they correspond to Temporal.Asynchronous.Precedence relations.
The corpus includes: implicit, explicit, altlex and hypophora types of relation.
All labels have been mapped using the mapping_disrpt25.json file that can be found in utils/.