
# Minecraft Structured Dialogue Corpus 

The Minecraft Structured Dialogue Corpus (MSDC) is a discourse-annotated version of the Minecraft Dialogue Corpus (MDC), created by Julia Hockenmaier's lab in 2019. 

**Original MDC:** https://juliahmr.cs.illinois.edu/Minecraft/ACL2019.html

The MSDC features complete, situated discourse structures in the style of Situated Discourse Representation Theory (Asher and Lascarides, 2003). 

The data are available at: https://github.com/linagora-labs/MinecraftStucturedDialogueCorpus

**Paper:** https://aclanthology.org/2024.lrec-main.444/
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
    abstract = "We provide a new linguistic resource: The Minecraft Structured Dialogue Corpus (MSDC), a discourse annotated version of the Minecraft Dialogue Corpus (MDC; Narayan-Chen et al., 2019), with complete, situated discourse structures in the style of SDRT (Asher and Lascarides, 2003). Our structures feature both linguistic discourse moves and nonlinguistic actions. To show computational tractability, we train a discourse parser with a novel ``2 pass architecture'' on MSDC that gives excellent results on attachment prediction and relation labeling tasks especially long distance attachments."
}
```

The MSDC can also be found on Hugging Face: 
https://huggingface.co/datasets/linagora/MinecraftStructuredDialogueCorpus

# Data
### Corpus Stats

|                  | Train+Val | Test | Total |
|----------------|-------|--------|------|
|No. Dialogues | 407| 133| 540|
|No. EDUs | 12913 | 4137 | 17050 |
|No. EEUs (squished) |8909|2738|11647| 
|No. Relation instances |26279|8250|34529|
|No. Multi-parent DUs |4789|1476|6265|

*NB: the EDU/EEU counts are a correction of those included in the LREC paper.

#### Breakdown by relation type and endpoint type*. 
*'Lin' is EDU and 'NL' is nonlinguistic DU, or EEU.
#### Forward Relations                                                
                                     
|                       | Lin-Lin  |Lin-NL |NL-Lin  |NL-NL  |Total|
|-----------------------|----------|-------|--------|-------|-----|
|Elaboration            |    4076  |     0 |      0 |     0 | 4076|
|Acknowledgement        |    1814  |     0 |    2736|      0| 4550|
|Continuation           |    2029  |     0 |       0|      0| 2029|
|Contrast               |    398   |     0 |       0|      0|  398|
|Correction             |    230   |     0 |    964 |    968| 2162|
|Result                 |    1944  |  6015 |    2369|      0|10418|
|Comment                |    1512  |     0 |    164 |      0| 1676|
|Question-answer_pair   |    1933  |     0 |      0 |      0| 1933|
|Narration              |     4455 |     0 |    0   |      0|4455 |
|Clarification_question |    960   |     0 |    0   |      0| 960 |
|Confirmation_question  |    43    |     0 |     956|      0|  999|
|Q-Elab                 |    229   |     0 |    0   |      0|  229|
|Explanation            |    108   |     0 |    0   |      0|  108|
|Alternation            |    173   |     0 |    0   |      0|  173|
|Conditional            |    67    |     0 |    0   |      0|   67|
|Sequence               |    0     |     38|    0   |      0|   38|

#### Backwards Relations 
|                       | Lin-Lin  |Lin-NL |NL-Lin  |NL-NL  |Total|
|-----------------------|----------|-------|--------|-------|-----| 
|Comment                |    242   |     0 |    0   |      0| 242 |
|Conditional            |    16    |     0 |    0   |      0| 16  |

#### Builder Action Formats 
For the BertLine parser, each Builder action move is compressed to a single code representing place/pick, color and xyz coordinates. 
The corpus data has with the natural language representation for each move is provided in the `data/reformat` directory. These files can also be generated from the BertLine data using the `action_format.py` script also provided in the data directory. This script can be modified if a different linguistic representation of builder moves is desired. 
*Alternatively, the formatted data can be found in the Hugging Face repository https://huggingface.co/datasets/linagora/MinecraftStructuredDialogueCorpus. 

# Parser 

We use the BertLine parser as originally described in [Bennis et al, 2023](https://aclanthology.org/2023.eacl-main.247.pdf). 

#### To reproduce our results, run the notebooks in this order:
 1.  bert_finetune.ipynb
 2.  bert_linear.ipynb
 3.  bert_multitaks.ipynb
 4.  bert_multitask_test.ipynb
 
