"""
Script to evaluate segmentation f-score and perfect discourse unit segmentation proportion from two files. Two input formats are permitted:

  * One token per line, with ten columns, no sentence breaks (default *.tok format) - segmentation indicated in column 10
  * The same, but with blank lines between sentences (*.conll format)

Token columns follow the CoNLL-U format, with token IDs in the first column and pipe separated key=value pairs in the last column. 
Document boundaries are indicated by a comment: # newdoc_id = ...
The evaluation uses micro-averaged F-Scores per corpus (not document macro average).

Example:

# newdoc_id = GUM_bio_byron
1	Education	_	_	_	_	_	_	_	Seg=B-seg
2	and	_	_	_	_	_	_	_	_
3	early	_	_	_	_	_	_	_	_
4	loves	_	_	_	_	_	_	_	_
5	Byron	_	_	_	_	_	_	_	Seg=B-seg
6	received	_	_	_	_	_	_	_	_

Or:

# newdoc_id = GUM_bio_byron
# sent_id = GUM_bio_byron-1
# text = Education and early loves
1	Education	education	NOUN	NN	Number=Sing	0	root	_	Seg=B-seg
2	and	and	CCONJ	CC	_	4	cc	_	_
3	early	early	ADJ	JJ	Degree=Pos	4	amod	_	_
4	loves	love	NOUN	NNS	Number=Plur	1	conj	_	_

# sent_id = GUM_bio_byron-2
# text = Byron received his early formal education at Aberdeen Grammar School, and in August 1799 entered the school of Dr. William Glennie, in Dulwich. [17]
1	Byron	Byron	PROPN	NNP	Number=Sing	2	nsubj	_	Seg=B-seg
2	received	receive	VERB	VBD	Mood=Ind|Tense=Past|VerbForm=Fin	0	root	_	_

For PDTB-style corpora, we calculate exact span-wise f-scores for BIO encoding, without partial credit. In other words, 
predicting an incorrect span with partial overlap is the same as missing a gold span and predicting an incorrect span
somewhere else in the corpus. Note also that spans must begin with B-Conn - predicted spans beginning with I-Conn are ignored.
The file format for PDTB style corpora is similar, but with different labels:

1	Fidelity	Fidelity	PROPN	NNP	_	6	nsubj	_	_
2	,	,	PUNCT	,	_	6	punct	_	_
3	for	for	ADP	IN	_	4	case	_	Seg=B-Conn
4	example	example	NOUN	NN	_	6	obl	_	Conn=I-conn
5	,	,	PUNCT	,	_	6	punct	_	_
6	prepared	prepare	VERB	VBN	_	0	root	_	_
7	ads	ad	NOUN	NNS	_	6	obj	_	_

Arguments:
 * goldfile: shared task gold test data
 * predfile: same format, with predicted segments positions in column 10 - note **number of tokens must match**  
 * string_input: if specified, files are replaced by strings with file contents instead of file names
 * no_boundaries: specify to eval only intra-sentence EDUs
"""

""" TODO
- OK labels : en argument, pas en dur
- OK option sans ls débuts de phrases : cf script "BIO no B'
- OK imprimer les résultats + propre : sans le "o" bizarre
- OK faire 2 classes edu et connectives (conn: futur exp for eval connective extended vs head of connective)
- solution + propre pour la colonne des labels ?
- faire une classe Eval et transformer les 2 en Eval en sous-classes
"""

__author__ = "Amir Zeldes, Janet Liu, Laura Rivière"
__license__ = "Apache 2.0"
__version__ = "2.0.0"

import io, os, sys, argparse
import json
from sklearn.metrics import accuracy_score, classification_report

# MWE and ellips : no lab or "_"
# TODO :
# print scores *100: 0.6825 => 68.25
# documentation (automatic generation ?)
# testunitaire

class Evaluation:
	"""
	Generic class for evaluation between 2 files.
	:load data, basic check, basic metrics, print results.
	"""
	def __init__(self, name: str) -> None:
		self.output = dict()
		self.name = name
		self.report = ""
		self.fill_output('doc_name', self.name)

	def get_data(self, infile: str, str_i=False) -> str:
		"""
		Stock data from file or stream.
		"""
		if str_i == False:
			data = io.open(infile, encoding="utf-8").read().strip().replace("\r", "")
		else:
			data = infile.strip()
		return data

	def fill_output(self, key: str, value) -> None:
		"""
		Fill results dict that will be printed.
		"""
		self.output[key] = value

	def check_tokens_number(self, g: list, p: list) -> None:
		"""
		Check same number of tokens/labels in both compared files.
		"""
		if len(g) != len(p):
			self.report += "\nFATAL: different number of tokens detected in gold and pred:\n"
			self.report += ">>>  In " + self.name + ": " + str(len(g)) + " gold tokens but " + str(len(p)) + " predicted tokens\n\n"
			sys.stderr.write(self.report)
			sys.exit(0)

	def check_identical_tokens(self, g: list, p: list) -> None:
		"""
		Check tokens/features are identical.
		"""
		for i, tok in enumerate(g):
			if tok != p[i]:
				self.report += "\nWARN: token strings do not match in gold and pred:\n"
				self.report += ">>> First instance in " + self.name + " token " + str(i) + "\n"
				self.report += "Gold: " + tok + " but Pred: " + p[i] + "\n\n"
				sys.stderr.write(self.report)
				break

	def compute_PRF_metrics(self, tp: int, fp: int, fn: int) -> None:
		"""
		Compute Precision, Recall, F-score from True Positive, False Positive and False Negative counts.
		Save result in dict.
		"""
		try:
			precision = tp / (float(tp) + fp)
		except Exception as e:
			precision = 0

		try:
			recall = tp / (float(tp) + fn)
		except Exception as e:
			recall = 0

		try:
			f_score = 2 * (precision * recall) / (precision + recall)
		except:
			f_score = 0

		self.fill_output("gold_count", tp + fn )
		self.fill_output("pred_count", tp + fp )
		self.fill_output("precision", precision)
		self.fill_output("recall", recall)
		self.fill_output("f_score", f_score)

	def compute_accuracy(self, g: list, p: list, k: str) -> None:
		"""
		Compute accuracy of predictions list of items, against gold list of items.
		:g: gold list
		:p: predicted list
		:k: name detail of accuracy
		"""
		self.fill_output(f"{k}_accuracy", accuracy_score(g, p) )
		self.fill_output(f"{k}_gold_count", len(g) )
		self.fill_output(f"{k}_pred_count", len(p) )

	def classif_report(self, g: list, p: list, key: str) -> None:
		"""
		Compute Precision, Recall and f-score for each instances of gold list.
		"""
		stats_dict = classification_report(g, p, labels=sorted(set(g)), zero_division=0.0, output_dict=True)
		self.fill_output(f'{key}_classification_report', stats_dict)

	def print_results(self) -> None:
		"""
		Print dict of saved results.
		"""
		# for k in self.output.keys():
		# print(f">> {k} : {self.output[k]}")

		print(json.dumps(self.output, indent=4))


class RelationsEvaluation(Evaluation):
	"""
	Specific evaluaion class for relations classification.
	The evaluation uses the simple accuracy score per corpus. 
	:rels disrpt-style data.
	:default eval last column "label"
	:option eval relation type (pdtb: implicit, explicit...) column "rel_type"
	"""

	HEADER = "doc\tunit1_toks\tunit2_toks\tunit1_txt\tunit2_txt\tu1_raw\tu2_raw\ts1_toks\ts2_toks\tunit1_sent\tunit2_sent\tdir\trel_type\torig_label\tlabel"
	# HEADER_23 = "doc\tunit1_toks\tunit2_toks\tunit1_txt\tunit2_txt\ts1_toks\ts2_toks\tunit1_sent\tunit2_sent\tdir\torig_label\tlabel"

	LABEL_ID = -1
	TYPE_ID = -3
	DISRPT_TYPES = ['Implicit', 'Explicit', 'AltLex', 'AltLexC', 'Hypophora']

	def __init__(self, name: str, gold_path: str, pred_path: str, str_i=False, rel_type=False) -> None:
		super().__init__(name)
		"""
		:param gold_file: Gold shared task file
		:param pred_file: File with predictions
		:param string_input: If True, files are replaced by strings with file contents (for import inside other scripts)
		:param rel_type: If True, scores are computed on types column, not label (relevant for PDTB)
		"""
		self.mode = "rel"
		self.g_path = gold_path
		self.p_path = pred_path
		self.opt_str_i = str_i
		self.opt_rel_t = rel_type
		self.key = "labels"

		self.fill_output("options", {"s": self.opt_str_i, "rt": self.opt_rel_t})

	def compute_scores(self) -> None:
		"""
		Get lists of data to compare, compute metrics.
		"""
		gold_units, gold_labels, gold_types = self.parse_rels_data(self.g_path, self.opt_str_i, self.opt_rel_t)
		pred_units, pred_labels, pred_types = self.parse_rels_data(self.p_path, self.opt_str_i, self.opt_rel_t)
		self.check_tokens_number(gold_labels, pred_labels)
		self.check_identical_tokens(gold_units, pred_units)

		self.compute_accuracy(gold_labels, pred_labels, self.key)
		self.classif_report(gold_labels, pred_labels, self.key)

		if self.opt_rel_t:
			self.get_types_scores(gold_labels, pred_labels, gold_types)

	def get_types_scores(self, g: list, p: list, tg: list) -> None:
		"""
		This function is to obtain scores of predictions against gold labels, by types of relations.
		"""

		for t in self.DISRPT_TYPES:
			gold_t = []
			pred_t = []
			for i, _ in enumerate(g):

				if tg[i] == t.lower():
					gold_t.append(g[i])
					pred_t.append(p[i])

			self.compute_accuracy(gold_t, pred_t, f"types_{t}")

	def parse_rels_data(self, path: str, str_i: bool, rel_t: bool) -> tuple[list[str], list[str]]:
		"""
		Rels format from DISRPT = header, then one relation classification instance per line. 
		:LREC_2024_header = 15 columns.
		"""
		data = self.get_data(path, str_i)
		header = data.split("\n")[0]
		assert header == self.HEADER, "Unrecognized .rels header."
		#column_ID = self.TYPE_ID if rel_t == True else self.LABEL_ID

		rels = data.split("\n")[1:]
		labels = [line.split("\t")[self.LABEL_ID] for line in rels] ######## .lower()
		units = [" ".join(line.split("\t")[:3]) for line in rels]
		types = [line.split("\t")[self.TYPE_ID] for line in rels] if rel_t == True else []



		return units, labels, types


class ConnectivesEvaluation(Evaluation):
	"""
	Specific evaluation class for PDTB connectives detection.
	:parse conllu-style data
	:eval upon strict connectives spans
	"""
	LAB_CONN_B = "Conn=B-conn"		# "Seg=B-Conn" 	#
	LAB_CONN_I = "Conn=I-conn"		# "Seg=I-Conn" 	#
	LAB_CONN_O = "Conn=O"			# "_"	#

	def __init__(self, name:str, gold_path:str, pred_path:str, str_i=False) -> None:
		super().__init__(name)
		"""
		:param gold_file: Gold shared task file
		:param pred_file: File with predictions
		:param string_input: If True, files are replaced by strings with file contents (for import inside other scripts)
		"""
		self.mode = "conn"
		self.seg_type = "connective spans"
		self.g_path = gold_path
		self.p_path = pred_path
		self.opt_str_i = str_i

		self.fill_output('seg_type', self.seg_type)
		self.fill_output("options", {"s": self.opt_str_i})

	def compute_scores(self) -> None:
		"""
		Get lists of data to compare, compute metrics.
		"""
		gold_tokens, gold_labels, gold_spans = self.parse_conn_data(self.g_path, self.opt_str_i)
		pred_tokens, pred_labels, pred_spans = self.parse_conn_data(self.p_path, self.opt_str_i)

		self.output['tok_count'] = len(gold_tokens)

		self.check_tokens_number(gold_tokens, pred_tokens)
		self.check_identical_tokens(gold_tokens, pred_tokens)
		tp, fp, fn = self.compare_spans(gold_spans, pred_spans)
		self.compute_PRF_metrics(tp, fp, fn)

	def compare_spans(self, gold_spans: tuple, pred_spans: tuple) -> tuple[int, int, int]:
		"""
		Compare exact spans.
		"""

		true_positive = 0
		false_positive = 0
		false_negative = 0

		for span in gold_spans: # not verified
			if span in pred_spans:
				true_positive +=1
			else:
				false_negative +=1
		for span in pred_spans:
			if span not in gold_spans:
				false_positive += 1

		return true_positive, false_positive, false_negative

	def parse_conn_data(self, path:str, str_i:bool) -> tuple[list, list, list]:
		"""
		LABEL = in last column
		"""
		data = self.get_data(path, str_i)
		tokens = []
		labels = []
		spans = []
		counter = 0
		span_start = -1
		span_end = -1
		for line in data.split("\n"):  # this loop is same than version 1
			if line.startswith("#") or line == "":
				continue
			else:
				fields = line.split("\t") # Token
				label = fields[-1]
				if "-" in fields[0] or "." in fields[0]:  # Multi-Word Expression or Ellips : No pred shall be there....
					continue
				elif self.LAB_CONN_B in label:
					if span_start > -1:  # add span
						if span_end == -1:
							span_end = span_start
						spans.append((span_start,span_end))
						span_end = -1
					label = self.LAB_CONN_B
					span_start = counter
				elif self.LAB_CONN_I in label:
					label = self.LAB_CONN_I
					span_end = counter
				else:
					label = "_"
					if span_start > -1:  # Add span
						if span_end == -1:
							span_end = span_start
						spans.append((span_start,span_end))
						span_start = -1
						span_end = -1

				tokens.append(fields[1])
				labels.append(label)
				counter += 1

		if span_start > -1 and span_end > -1:  # Add last span
			spans.append((span_start,span_end))

		if not self.LAB_CONN_B in labels:
			exit(f"Unrecognized labels. Expecting: {self.LAB_CONN_B}, {self.LAB_CONN_I}, {self.LAB_CONN_O}...")

		return tokens, labels, spans


class SegmentationEvaluation(Evaluation):
	"""
	Specific evaluation class for EDUs segmentation.
	:parse conllu-style data
	:eval upon first token identification
	"""
	LAB_SEG_B = "Seg=B-seg"		# "BeginSeg=Yes"
	LAB_SEG_I = "Seg=O"			# "_"

	def __init__(self, name: str, gold_path: str, pred_path: str, str_i=False, no_b=False) -> None:
		super().__init__(name)
		"""
		:param gold_file: Gold shared task file
		:param pred_file: File with predictions
		:param string_input: If True, files are replaced by strings with file contents (for import inside other scripts)
		"""
		self.mode = "edu"
		self.seg_type = "EDUs"
		self.g_path = gold_path
		self.p_path = pred_path
		self.opt_str_i = str_i
		self.no_b = True if "conllu" in gold_path.split(os.sep)[-1] and no_b == True else False  # relevant only in conllu

		self.fill_output('seg_type', self.seg_type)
		self.fill_output("options", {"s": self.opt_str_i})

	def compute_scores(self) -> None:
		"""
		Get lists of data to compare, compute metrics.
		"""
		gold_tokens, gold_labels, gold_spans = self.parse_edu_data(self.g_path, self.opt_str_i, self.no_b)
		pred_tokens, pred_labels, pred_spans = self.parse_edu_data(self.p_path, self.opt_str_i, self.no_b)

		self.output['tok_count'] = len(gold_tokens)

		self.check_tokens_number(gold_tokens, pred_tokens)
		self.check_identical_tokens(gold_tokens, pred_tokens)
		tp, fp, fn = self.compare_labels(gold_labels, pred_labels)
		self.compute_PRF_metrics(tp, fp, fn)

	def compare_labels(self, gold_labels: list, pred_labels: list) -> tuple[int, int, int]:
		"""
		
		"""
		true_positive = 0
		false_positive = 0
		false_negative = 0

		for i, gold_label in enumerate(gold_labels): # not verified
			pred_label = pred_labels[i]
			if gold_label == pred_label:
				if gold_label == "_":
					continue
				else:
					true_positive += 1
			else:
				if pred_label == "_":
					false_negative += 1
				else:
					if gold_label == "_":
						false_positive += 1
					else:  # I-Conn/B-Conn mismatch ?
						false_positive +=1

		return true_positive, false_positive, false_negative

	def parse_edu_data(self, path: str, str_i: bool, no_b: bool) -> tuple[list, list, list]:
		"""
		LABEL = in last column
		"""
		data = self.get_data(path, str_i)
		tokens = []
		labels = []
		spans = []
		counter = 0
		span_start = -1
		span_end = -1
		for line in data.split("\n"):  # this loop is same than version 1
			if line.startswith("#") or line == "":
				continue
			else:
				fields = line.split("\t")  # Token
				label = fields[-1]
				if "-" in fields[0] or "." in fields[0]:  # Multi-Word Expression or Ellipsis : No pred shall be there....
					continue
				elif no_b == True and fields[0] == "1":
					label = "_"
				elif self.LAB_SEG_B in label:
					label = self.LAB_SEG_B
				else:
					label = "_"  # 🚩
					if span_start > -1:  # Add span
						if span_end == -1:
							span_end = span_start
						spans.append((span_start, span_end))
						span_start = -1
						span_end = -1

				tokens.append(fields[1])
				labels.append(label)
				counter += 1

		if span_start > -1 and span_end > -1:  # Add last span
			spans.append((span_start, span_end))

		if not self.LAB_SEG_B in labels:
			exit(f"Unrecognized labels. Expecting: {self.LAB_SEG_B}, {self.LAB_SEG_I}...")

		return tokens, labels, spans


if __name__ == "__main__":

	p = argparse.ArgumentParser()
	p.add_argument("-g", "--goldfile", required=True, help="Shared task gold file in .tok or .conll or .rels format.")
	p.add_argument("-p", "--predfile", required=True, help="Corresponding file with system predictions.")
	p.add_argument("-t", "--task", required=True, choices=['S', 'C', 'R'], help="Choose one of the three options: S (EDUs Segmentation), C (Connectives Detection), R (Relations Classification)")
	p.add_argument("-s", "--string_input",action="store_true",help="Whether inputs are file names or strings.")
	p.add_argument("-nb", "--no_boundary_edu", default=False, action='store_true', help="Does not count EDU that starts at beginning of sentence.")
	p.add_argument("-rt", "--rel_type", default=False, action='store_true', help="Eval relations types instead of label.")

	# help(Evaluation)
	# help(SegmentationEvaluation)
	# help(ConnectivesEvaluation)
	# help(RelationsEvaluation)

	opts = p.parse_args()

	name = opts.goldfile.split(os.sep)[-1] if os.path.isfile(opts.goldfile) else f"string_input: {opts.goldfile[0:20]}..."

	if opts.task == "R":
		my_eval = RelationsEvaluation(name, opts.goldfile, opts.predfile, opts.string_input, opts.rel_type)
	elif opts.task == "C":
		my_eval = ConnectivesEvaluation(name, opts.goldfile, opts.predfile, opts.string_input)
	elif opts.task == "S":
		my_eval = SegmentationEvaluation(name, opts.goldfile, opts.predfile, opts.string_input, opts.no_boundary_edu)

	my_eval.compute_scores()
	my_eval.print_results()
