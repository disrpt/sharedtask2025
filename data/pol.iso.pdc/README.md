# pol.iso.pdc

### Polish Discourse Corpus

This dataset contains the reannotation of a subset of the Polish Coreference Corpus (PCC) [1] with ISO 24617-8 discourse relations [2, 3].

This work is part of the ongoing Universal Discourse project at the Institute of Computer Science of the Polish Academy of Sciences, funded by the National Science Center (NCN). The dataset is still under development and will be expanded in the future.


**License:** CC BY-NC 4.0


If you find this work useful in your research, please cite: [https://aclanthology.org/2024.lrec-main.1123/](https://aclanthology.org/2024.lrec-main.1123/).

```bibtex
@inproceedings{
    ogr:etal:24,
    author = "Ogrodniczuk, Maciej and Tomaszewska, Aleksandra and Ziembicki, Daniel and Żurowski, Sebastian and Tuora, Ryszard and Zwierzchowska, Aleksandra",
    url = "https://aclanthology.org/2024.lrec-main.1123/",
    pdf = "https://aclanthology.org/2024.lrec-main.1123.pdf",
    title = "{P}olish {D}iscourse {C}orpus ({PDC}): Corpus Design, {ISO}-Compliant Annotation, Data Highlights, and Parser Development",
    pages = "12829--12835",
    crossref = "lrec:coling:24"
}
@proceedings{
    lrec:coling:24,
    editor = "Calzolari, Nicoletta and Kan, Min-Yen and Hoste, Veronique and Lenci, Alessandro and Sakti, Sakriani and Xue, Nianwen",
    publisher = "ELRA and ICCL",
    title = "Proceedings of the {2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)}",
    url = "https://aclanthology.org/events/coling-2024/",
    booktitle = "Proceedings of the {2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)}",
    year = "2024",
    address = "Torino, Italy"
}
```

Other relevant works on the ISO 24617-8 discourse taxonomy:

1. Ogrodniczuk, M., Glowinska, K., Kopec, M., Savary, A., & Zawisławska, M. (2013). Polish Coreference Corpus. Language and Technology Conference.

2. Tomaszewska, A., Silvano, P., Leal, A., & Amorim, E. (2024). ISO 24617-8 Applied: Insights from Multilingual Discourse Relations Annotation in English, Polish, and Portuguese. International Symposium on Algorithms.

3. Zurowski, S., Ziembicki, D., Tomaszewska, A., Ogrodniczuk, M., & Drozd, A. (2023). Adopting ISO 24617-8 for Discourse Relations Annotation in Polish: Challenges and Future Directions. International Conference on Language, Data, and Knowledge.



## DISRPT 2025 Shared Task Information

POS tags, morphology, and syntactic parses were added using Stanza's `default_accurate` model for Polish (`pl`) while preserving tokenization and sentence splits from the Polish Coreference Corpus.
```Python
    nlp = stanza.Pipeline(
        'pl',
        pretokenized=True,
        tokenize_pretokenized=True,
        package='default_accurate',
    )
```


### Notes on Segmentation

This dataset contains annotation for discontinuous discourse units and connectives. Explicit relation connectives are not included in the argument spans for the .rels data.