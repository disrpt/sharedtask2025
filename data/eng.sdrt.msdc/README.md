# eng.sdrt.msdc

## Description

The Minecraft Structured Dialogue Corpus (MSDC) is a discourse annotated version of the Minecraft Dialogue Corpus (MDC; Narayan-Chen et al., 2019), with complete, situated discourse structures in the style of SDRT (Asher and Lascarides, 2003). 
The annotated structures feature both linguistic discourse moves and nonlinguistic actions.

This dataset consists of 410 games in the train+dev set and 137 games in the test set, in total 547 annotated games/dialogues.

The dialogues in the MSDC range in length from 10 to over 200 turns, in which the speaker turns are annotated with Elementary Discourse Units (EDUs, linguistic clauses) and Elementary Event Units (EEUs, the Builder actions) using the Glozz tool.  

### Download

You may download the entire corpus from the MDSC github: https://github.com/linagora-labs/MinecraftStucturedDialogueCorpus


### License and Attribution Information

The MSDC corpus is made available under the
Creative Commons license Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
https://creativecommons.org/licenses/by-nc-sa/4.0/

If you use this corpus in a scientific publication, we would appreciate citations to the following paper:

```bibtex
@inproceedings{thompson-etal-2024-discourse,
    title = "Discourse Structure for the {M}inecraft Corpus",
    author = "Thompson, Kate  and
      Hunter, Julie  and
      Asher, Nicholas",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.444/",
    pages = "4957--4967",
}
```

### Contact information

Kate Thompson
E-mail: cthompson@linagora.com


## DISRPT 2025 Shared Task Information

- In DISRPT, we treat **action turns (EEUs) as linguistic utterances**. As a result, EEUs such as "place purple 4 1 1, place purple 4 1 -1" are also parsed and included in the .conll, .tok, and .rel files. This decision is motivated by the fact that EEUs represent a significant portion of the MSDC corpus and often carry discourse relations. Excluding them would lead to the loss of roughly one-third of the annotated discourse relations and would render much of what would remain of the dialogues difficult to comprehend.
  
- Note that a sequence of actions like "place purple 4 1 1 , place purple 4 1 - 1" is considered as ONE segment, so there is no need to split them, as shown in the .tok files.

- Sentences may contain multiple discourse units. The .rels files contain no split EDUs, i.e. unit1 and unit2 are always uninterrupted sequences of tokens.

- The train, dev, and test splits follow those used in the original paper.


