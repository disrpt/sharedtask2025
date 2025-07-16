#tha.pdtb.tdtb

## Introduction
The Thai Discourse Treebank (TDTB) is a project at the NLP Lab at Chulalongkorn University, Bangkok, Thailand. The annotation adopts the sense inventory from PDTB 3.0. 


## Data 
The documents are sampled from the LST20 corpus (Boonkwan et al., 2020). The text consists of news articles in various genres. In the LST20 corpus, the word segmentation, sentence segmentation, and POS tags are manually annotated as part of the original LST20 corpus. 

This corpus consists 180 documents annotated with explicit discourse relations and the accompanying two argument spans. The total number of relations is 10,868 relations.

| Split | Relations |
|-------|-----------|
| train | 8279 |
| dev | 1244 |
| test | 1345 |
| *total* | 10868 | 

The dependency parser used to generate `.conllu` files is trained on the Thai Universal Dependency (Sriwirote et al., 2025). The parser achieves 87.39 UAS and 78.09 LAS without gold-standard POS tag. The parser can be found at https://github.com/nlp-chula/attaparse 

## References

```bibtex
@article{Sriwirote-etal-2024-TUD,
  title={The Thai Universal Dependency Treebank},
  author={Panyut Sriwirote and Wei Qi Leong and 
  Charin Polpanumas and Santhawat Thanyawong  and 
  William Chandra Tjhi and Wirote Aroonmanakun and 
  Attapol T. Rutherford},
  journal={Transactions of the Association for Computational Linguistics},
  year={in press},
  publisher={MIT Press Direct}
}

@article{boonkwan2020annotation,
  title={The annotation guideline of lst20 corpus},
  author={Boonkwan, Prachya and Luantangsrisuk, Vorapon and Phaholphinyo, Sitthaa and Kriengket, Kanyanat and Leenoi, Dhanon and Phrombut, Charun and Boriboon, Monthika and Kosawat, Krit and Supnithi, Thepchai},
  journal={arXiv preprint arXiv:2008.05055},
  year={2020}
}
```
