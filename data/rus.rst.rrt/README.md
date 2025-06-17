# rus.rst.rrt

### Russian RST Treebank

## Introduction

[Russian RST Treebank](https://rstreebank.ru/eng/) is a Russian RST corpus annotated manually using [rstWeb](https://gucorpling.org/rstweb/info/). 

As of version 2.1 (August 2022), the treebank contains annotations for 233 documents: **129 news articles** from five sources and **104 blog posts** from various sources, covering a wide range of topics including travel, life stories, IT, cosmetics, health, politics, psychology, and the environment.

## Preprocessing

The .rs3 files contained "##### " as placeholders for paragraph breaks. To revert to the original texts, we replaced "##### " with \n.


## Feedback

For further questions or inquires regarding this dataset, please contact:

Dina Pisarevskaya dinabpr@gmail.com
Maria Kobozeva marya.kobozeva@gmail.com
Svetlana Toldova toldova@yandex.ru


## Citation Info

If you use this dataset, please cite the following publication:

Pisarevskaya D. et al. (2017). [Towards building a discourse-annotated corpus of Russian](https://www.dialogue-conf.org/media/3938/pisarevskayadetal.pdf). Computational Linguistics and Intellectual Technologies: Proceedings of the International Conference "Dialogue", Vol. 1, pp. 194–204.

```bibtex
@inproceedings{PisarevskayaEtAl2017,
author = {Pisarevskaya, Dina and Ananyeva, Margarita and Kobozeva, Maria and Nasedkin, A. and Nikiforova, S. and Pavlova, I. and Shelepov, A.},
title = {Towards building a Discourse-annotated corpus of Russian},
year = {2017},
month = {06},
volum = {1}, 
pages = {194--204},
booktitle = {Computational Linguistics and Intellectual Technologies: Proceedings of the International Conference "Dialogue"},
}
```

## License

Russian RST Treebank 2.1 is publicly available under the Creative Commons - Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.


## DISRPT 2025 Shared Task Information

Since the Russian RST Treebank does not contain gold tokenization and sentence splitting, data was automatically tokenized and parsed using Stanza's Syntagrus model. As a result sentence splits in conll files are not always correct. 

~~Additionally, some scientific texts contain portions in other languages, such as bibliographical references in English, brief summaries or keywords not in Russian.~~

~~Note also that some regions of text in the Russian RST Treebank are not internally segmented despite containing multiple sentences, such as bibliographies.~~ 

This dataset contains discontinuous discourse units (split 'same-unit').
