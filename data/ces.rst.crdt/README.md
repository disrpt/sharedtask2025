# ces.rst.crdt

## Czech RST Discourse Treebank 1.0 (CzRST-DT 1.0)

### Introduction

The Czech RST Discourse Treebank 1.0 (CzRST-DT 1.0, Poláková et al., 2023)
is a dataset of 54 Czech journalistic texts manually annotated using
the Rhetorical Structure Theory (RST; Mann and Thompson, 1988).
Each text document in the treebank is represented as a single tree-like
structure, the nodes (discourse units) are interconnected through
hierarchical rhetorical relations.

The dataset also contains concurrent annotations of five double-annotated
documents.

The original texts are a part of the data annotated in the Prague Dependency
Treebank (Hajič et al., 2020), although the two projects are independent.

Please visit https://ufal.mff.cuni.cz/czrst-dt1.0 for detailed and
updated information about the corpus.

The original data can be downloaded from the LINDAT/CLARIAH-CZ
repository: http://hdl.handle.net/11234/1-5174,
see the licence below.

The original data can be opened using the rstWeb annotation
tool (Gessler et al., 2019):
https://gucorpling.org/rstweb/info/


### Authors

  * Lucie Poláková (Charles University, Faculty of Mathematics and Physics),
  * Šárka Zikánová (Charles University, Faculty of Mathematics and Physics),
  * Jiří Mírovský (Charles University, Faculty of Mathematics and Physics)
  * Eva Hajičová (Charles University, Faculty of Mathematics and Physics),


### Citation

Please cite CzRST-DT 1.0 when using the corpus for your research:

Lucie Poláková, Šárka Zikánová, Jiří Mírovský, Eva Hajičová:
Czech RST Discourse Treebank 1.0. Data/software, ÚFAL MFF UK, Prague,
Czech Republic, LINDAT/CLARIAH-CZ: http://hdl.handle.net/11234/1-5174,
June 2023.


### Licence

CzRST-DT 1.0 is distributed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0) licence.

For more information and updates, see
https://ufal.mff.cuni.cz/czrst-dt1.0


### Acknowledgement


The work on version 1.0 of the corpus was financially supported by
project no. 20-09853S of the Czech Science Foundation: "Global
Coherence of Czech Texts in the Corpus-based Perspective".


### References

  * Luke Gessler, Yang Liu and Amir Zeldes: A Discourse Signal Annotation System for RST Trees. In: Proceedings of Discourse Relation Treebanking and Parsing (DISRPT 2019). Minneapolis, MN, pp. 56-61, 2019.

  * Jan Hajič, Eduard Bejček, Alevtina Bémová, Eva Buráňová, Eva Fučíková, Eva Hajičová, Jiří Havelka, Jaroslava Hlaváčová, Petr Homola, Pavel Ircing, Jiří Kárník, Václava Kettnerová, Natalia Klyueva, Veronika Kolářová, Lucie Kučová, Markéta Lopatková, David Mareček, Marie Mikulová, Jiří Mírovský, Anna Nedoluzhko, Michal Novák, Petr Pajas, Jarmila Panevová, Nino Peterek, Lucie Poláková, Martin Popel, Jan Popelka, Jan Romportl, Magdaléna Rysová, Jiří Semecký, Petr Sgall, Johanka Spoustová, Milan Straka, Pavel Straňák, Pavlína Synková, Magda Ševčíková, Jana Šindlerová, Jan Štěpánek, Barbora Štěpánková, Josef Toman, Zdeňka Urešová, Barbora Vidová Hladká, Daniel Zeman, Šárka Zikánová, Zdeněk Žabokrtský: Prague Dependency Treebank - Consolidated 1.0 (PDT-C 1.0). Data/software, LINDAT-CLARIAH, URL: http://hdl.handle.net/11234/1-3185, 2020.

  * William C. Mann and Sandra A. Thompson: Rhetorical Structure Theory: Toward a functional theory of text organization. Text-interdisciplinary Journal for the Study of Discourse 8 (3), pp. 243-281, 1988.
  
## DISRPT 2025 Shared Task Information

For the DISRPT Shared Task the data was divided into `train`, `dev` and `test` partitions, with 48, 3 and 3 documents respectively. The original data contained 8 multinuclear and 29 satellite-nucleus relation labels, including same-unit. The converted data has the final label harmonized with the reduced shared task label set. This dataset contains discontinuous discourse units (split 'same-unit'). 
