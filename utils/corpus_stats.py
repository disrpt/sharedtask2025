import locale
import io, sys, re, os
from glob import glob
from collections import defaultdict, OrderedDict

script_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = script_dir + os.sep + ".." + os.sep + "data"
corpora = [o for o in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir,o))]
stats = defaultdict(lambda : defaultdict(int))
gold_syn = ["eng.erst.gum","eng.erst.gentle","eng.pdtb.gum","eng.pdtb.gentle","eng.rst.rstdt","eng.pdtb.pdtb"]
expected_underscored = ["eng.erst.gum","eng.pdtb.gum","eng.pdtb.pdtb","eng.rst.rstdt","zho.pdtb.cdtb","tur.pdtb.tdb"]
test = True

for corpus in corpora:
	sys.stderr.write(" o Processing " + corpus + "\n")
	d = stats[corpus]
	d["corpus"] = corpus
	d["lang"], d["framework"] = corpus.split(".")[:-1]
	files = glob(".." + os.sep + "data" + os.sep + corpus + os.sep + "*.rels")
	for file_ in sorted(files):  # Train will be last
		text = io.open(file_, encoding="utf8").read()
		rel_rows = [l.split("\t")[-1] for i,l in enumerate(text.split("\n")) if "\t" in l and i>0]
		rels = set(rel_rows)
		d["rel_types"] = len(rels)  # We assume the last file (usually train) has examples of all relations
		d["discont"] = "yes" if "<*>" in text else "no"  # Last file (usually train) should have example of <*>
		d["underscored"] = "yes" if "____" in text else "no"
		d["rels"] += len(rel_rows)

	files = glob(".." + os.sep + "data" + os.sep + corpus + os.sep + "*.conllu")
	# sort files
	train_f = [f for f in files if "train." in f]
	dev_f = [f for f in files if "dev." in f]
	test_f = [f for f in files if "test." in f]
	files = train_f + dev_f + test_f

	all_toks = 0
	all_sents = 0
	all_docs = 0
	all_segs = 0
	for file_ in files:
		text = io.open(file_,encoding="utf8").read()
		docs = text.count("# newdoc")
		if docs == 0:
			sys.stderr.write("No documents found in " + file_)
			sys.exit(0)
		sents = text.count("\n1\t")
		segs = text.count("B-seg") + text.count("B-conn")
		just_toks = text.strip()
		just_toks = re.sub(r"\n+",r'\n',just_toks) # Remove blank lines
		just_toks = re.sub(r"^[0-9]+-[^\n]+\n",r'\n',just_toks,flags=re.MULTILINE)  # Remove multi-toks if present
		just_toks = re.sub(r"^#[^\n]+\n",r'',just_toks,flags=re.MULTILINE)  # Remove comment lines
		toks = just_toks.count("\n") + 1
		if "_train" in file_:
			part = "train"
		elif "_dev" in file_:
			part = "dev"
		else:
			part = "test"
		d[part+"_toks"] = toks
		d[part+"_sents"] = sents
		d[part+"_docs"] = docs
		d[part+"_segs"] = segs
		all_toks += toks
		all_sents += sents
		all_docs += docs
		all_segs += segs
	if test:
		d["test_tok%"] = 100*d["test_toks"]/float(all_toks)
	if "dev_toks" in d:
		d["dev_tok%"] = 100*d["dev_toks"]/float(all_toks)
	else:
		d["dev_tok%"] = d["dev_toks"] = 0
	if "train_toks" in d:
		d["train_tok%"] = 100*d["train_toks"]/float(all_toks)
	else:
		d["train_tok%"] = d["train_toks"] = 0
	if "dev_docs" in d:
		d["dev_doc%"] = 100*d["dev_docs"]/float(all_docs)
	else:
		d["dev_doc%"] = d["dev_docs"] = 0
	if test:
		d["test_doc%"] = 100*d["test_docs"]/float(all_docs)
	if "train_docs" in d:
		d["train_doc%"] = 100*d["train_docs"]/float(all_docs)
	else:
		d["train_doc%"] = d["train_docs"] = 0
	d["total_sents"] = all_sents
	d["total_toks"] = all_toks
	d["total_docs"] = all_docs
	d["total_segs"] = all_segs
	d["seg_style"] = "Conn" if "pdtb" in corpus else "EDU"
	if ".gum" in corpus:
		d["underscored"] = "part"
	#if "SpaceAfter" in text:
	#	d["SpaceAfter"] = "yes"
	#else:
	#	d["SpaceAfter"] = "no"
	if text.count("\tcase\t") > 50:
		if text.count("\tdobj\t") > 1:
			d["syntax"] = "UD (V1)"
		else:
			d["syntax"] = "UD"
	else:
		d["syntax"] = "other"
	if corpus in gold_syn:
		d["syntax"] += " (gold)"
	if re.search(r'^[0-9]+-',text,flags=re.MULTILINE) is not None:
		d["MWTs"] = "yes"
	else:
		d["MWTs"] = "no"
	if re.search(r'^[0-9]+\.',text,flags=re.MULTILINE) is not None:
		d["ellip"] = "yes"
	else:
		d["ellip"] = "no"

first = True
all_keys = list(stats["eng.erst.gum"].keys())
all_keys.append("corpus")
for corpus in sorted(stats.keys()):
	d = stats[corpus]
	if first:
		print("| " + " | ".join([k for k in all_keys if "%" not in k]) + " |")
		print("| " + " | ".join(["---" for k in all_keys if "%" not in k]) + " |")
	first = False
	vals = []
	for key in all_keys:
		if "%" not in key:
			if isinstance(d[key],str):
				vals.append(str(d[key]))
			else:
				#vals.append(locale.format("%d", key, grouping=True))
				vals.append(f'{d[key]:,}')
	print("| "+" | ".join(vals) + " |")

for c in corpora:
	if c in expected_underscored:
		if stats[c]["underscored"] == "no":
			sys.stderr.write(f"Warning: {c} should have underscored tokens, but it does not.\n")

stats_total = defaultdict(lambda : "---")
stats_total["corpus"] = "Total"
stats_total["lang"] = len(set([d["lang"] for d in stats.values()]))
stats_total["framework"] = len(set([d["framework"] for d in stats.values()]))
stats_total["rel_types"] = 17
stats_total["underscored"] = len(set([d["underscored"] for d in stats.values() if d["underscored"] != "no"]))
stats_total["discont"] = len([d["discont"] for d in stats.values() if d["discont"] != "no"])
stats_total["MWTs"] = len([d["MWTs"] for d in stats.values() if d["MWTs"] != "no"])
stats_total["ellip"] = len([d["ellip"] for d in stats.values() if d["ellip"] != "no"])
stats_total["rels"] = sum([int(d["rels"]) for d in stats.values()])
stats_total["total_toks"] = sum([int(d["total_toks"]) for d in stats.values()])
stats_total["total_sents"] = sum([int(d["total_sents"]) for d in stats.values()])
stats_total["total_docs"] = sum([int(d["total_docs"]) for d in stats.values()])
stats_total["train_toks"] = sum([int(d["train_toks"]) for d in stats.values()])
stats_total["train_sents"] = sum([int(d["train_sents"]) for d in stats.values()])
stats_total["train_docs"] = sum([int(d["train_docs"]) for d in stats.values()])
stats_total["train_segs"] = sum([int(d["train_segs"]) for d in stats.values()])
stats_total["dev_toks"] = sum([int(d["dev_toks"]) for d in stats.values()])
stats_total["dev_sents"] = sum([int(d["dev_sents"]) for d in stats.values()])
stats_total["dev_docs"] = sum([int(d["dev_docs"]) for d in stats.values()])
stats_total["dev_segs"] = sum([int(d["train_segs"]) for d in stats.values()])
stats_total["test_toks"] = sum([int(d["test_toks"]) for d in stats.values()])
stats_total["test_sents"] = sum([int(d["test_sents"]) for d in stats.values()])
stats_total["test_docs"] = sum([int(d["test_docs"]) for d in stats.values()])
stats_total["test_segs"] = sum([int(d["train_segs"]) for d in stats.values()])
stats_total["total_segs"] = sum([int(d["total_segs"]) for d in stats.values()])

print("| " + " | ".join(["---" for k in all_keys if "%" not in k]) + " |")
keys = [k for k in all_keys if "%" not in k]
for k in keys:
	if isinstance(stats_total[k],int):
		stats_total[k] = f'{stats_total[k]:,}'
row = ["**"+str(stats_total[k])+"**" for k in keys]
row[-1] = "**---**"
print("| " + " | ".join(row) + " |")
#print("| " + " | ".join(["---" for k in all_keys if "%" not in k]) + " |")
print("| " + " | ".join(["**"+k+"**" for k in all_keys if "%" not in k]) + " |")
