We provide elementary discourse segmentation for the SUMM-RE corpus (Hunter et al., 2024). This corpus consists of sessions made of 3 x 20’ meeting, with 2 to 4 participants, focused on event planning. Each session is associated with a different task: (i) discussing ideas for organizing an event (more presentation- and monologue-oriented), (ii) deciding what to do at the event (dialogic discussions involving divergent opinions), and (iii) planning the practical organization of the event (including task delegation). Most sessions were recorded face-to-face using head-mounted microphones, with a few additional sessions conducted via Zoom.

Four naive annotators were recruited to manually segment the dev and test portions of the corpus.  Semi-naive coder reached mean kappa-scores within the 0.85-0.89 range (See Details in Prévot et al, 2025).

The specificities of this corpus are the following:

No punctuation had been added to the transcript. Only pauses presence are signalled by a comma.
Spontaneous Speech transcripts implies high rate of disfluencies, including filled pauses and truncations.
JSON files include time stamps at the EDU level

The only modification to the original multilogue transcript consisted in removing the most obvious backchannels since they were difficult to linearize within one token sequence. For all cases that were going beyond a mere weak lexical items produced in overlap, we kept the transcript but located it after the end of the overlapping main discourse unit.

[Segmenting a French Meeting Corpus into Elementary Discourse Units](https://2025.sigdial.org/list-of-accepted-papers/) Prévot, L., Hunter, J., & Bertrand, R. (2025). Proceedings of the 26th Meeting of the Special Interest Group on Discourse and Dialogue.

[SUMM-RE: A corpus of French meeting-style conversations] (https://inria.hal.science/hal-04623038/)** Hunter, J., Yamasaki, H., Granier, O., Louradour, J., Bertrand, R., Thompson, K., & Prévot, L. (2024).  In Actes de JEP-TALN-RECITAL 2024. 31ème Conférence sur le Traitement Automatique des Langues Naturelles. ATALA & AFPC.