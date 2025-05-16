"""
This script aims to process licensed datasets of the DISRPT project.
There are 2 modes:
:del    characters of relevant texts are replaced with "_"
:add    "_" are replaced with corresponding characters.
"""

"""
Following the logic in process_underscore.py 2021 [A.Zeldes],
this script aims to be easy to use, to read.
"""

"""
There are 3 types of files to add/del:
- .tok : tokens + lemmas
- .conllu : tokens + lemmas
- .rels : tokens (or MWE)
"""

__author__ = "Amir Zeldes + Laura Rivière"
__license__ = "Apache 2.0"
__version__ = "3.0.0"



from argparse import ArgumentParser
from collections import defaultdict
import sys, os, io, re
from glob import glob


DATA_DIR = "data"
HEADER_rels = "doc\tunit1_toks\tunit2_toks\tunit1_txt\tunit2_txt\tu1_raw\tu2_raw\ts1_toks\ts2_toks\tunit1_sent\tunit2_sent\tdir\trel_type\torig_label\tlabel"
META_DOCID = "# newdoc id = "
META_TEXT = "# text = "
GUM_DOCS = {
	"GUM_reddit_macroeconomics": [
		{"year": "2017", "month": "09", "id": "6zm74h", "type": "post","source":"undef"},
		{"year": "2017", "month": "09", "id": "dmwwqlt", "type":"comment","source":"undef"}
	],
	"GUM_reddit_stroke": [
		{"year": "2017", "month": "08", "id": "6ws3eh", "type": "post","source":"undef"},
		{"year": "2017", "month": "08", "id": "dmaei1x", "type":"comment","source":"undef"},
		{"year": "2017", "month": "08", "id": "dmaiwsm", "type":"comment","source":"undef"},
		{"year": "2017", "month": "09", "id": "dmkx8bk", "type":"comment","source":"undef"},
		{"year": "2017", "month": "09", "id": "dmm1327", "type":"comment","source":"undef"},
		{"year": "2017", "month": "08", "id": "dmaoodn", "type":"comment","source":"undef"}
	],
	"GUM_reddit_polygraph": [
		{"year": "2014", "month": "12", "id": "2q6qnv", "type": "post","source":"undef"}
	],
	"GUM_reddit_ring": [
		{"year": "2016", "month": "09", "id": "5570x1", "type": "post","source":"undef"},
		{"year": "2016", "month": "09", "id": "d885ma0", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d8880w7", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88u7dg", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88unu3", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88v0sz", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88xaqu", "type":"comment","source":"undef"},
		{"year": "2016", "month": "10", "id": "d893mj9", "type":"comment","source":"undef"},
		{"year": "2016", "month": "09", "id": "d88s4bb", "type":"comment","source":"undef"},
		{"year": "2016", "month": "10", "id": "d88zt6x", "type":"comment","source":"undef"}
	],
	"GUM_reddit_space": [
		{"year": "2016", "month": "08", "id": "50hx5c", "type": "post","source":"undef"},
		{"year": "2016", "month": "08", "id": "d7471k5", "type":"comment","source":"undef"},
		{"year": "2016", "month": "08", "id": "d74i5ka", "type":"comment","source":"undef"},
		{"year": "2016", "month": "08", "id": "d74ppi0", "type":"comment","source":"undef"}
	],
	"GUM_reddit_superman": [
		#{"year": "2017", "month": "04", "id": "68e0u3", "type": "post", "title_only": True},  # Post title not included in this document
		{"year": "2017", "month": "05", "id": "dgys1z8", "type":"comment","source":"undef"}
	],
	"GUM_reddit_bobby": [
		{"year":"2018","month":"06","id":"8ph56q","type": "post","source":"undef"},
		{"year":"2018","month":"06","id":"e0b8zz4","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0dwqlg","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e15pcqu","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0dz1mp","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e1uuo9e","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0brc9w","type":"comment","source":"undef"},
		{"year":"2018","month":"06","id":"e0bz951","type":"comment","source":"undef"}
	],
	"GUM_reddit_escape": [
		{"year":"2017","month":"05","id":"69r98j","type": "post","source":"undef"},
		{"year":"2017","month":"05","id":"dh96n8v","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9enpe","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dht8oyn","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dhn0hoe","type":"comment","source":"undef"},
		{"year":"2017","month":"07","id":"dk9ted1","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh98kcg","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9zxej","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"di9x7j9","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"di9xsrt","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"din85zf","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dinab0w","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dinaggd","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dinbyb9","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dj65sp1","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dizdd8a","type":"comment","source":"undef"},
		{"year":"2017","month":"07","id":"dk78qw8","type":"comment","source":"undef"},
		{"year":"2017","month":"08","id":"dm0gqc7","type":"comment","source":"undef"},
		{"year":"2017","month":"10","id":"domd1r0","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9irie","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dh9iw36","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"djlcwu5","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"dlzcxpy","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dhabstb","type":"comment","source":"undef"},
		{"year":"2017","month":"05","id":"dhbr3m6","type":"comment","source":"undef"},
		{"year":"2017","month":"06","id":"diz97qy","type":"comment"}
	],
	"GUM_reddit_gender": [
		{"year":"2018","month":"09","id":"9e5urs","type":"post","source":"bigquery"},
		{"year":"2018","month":"09","id":"e5mg3s7","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5mkpok","type":"comment","source":"bigquery"},
		{"year":"2018","month":"09","id":"e5nxbmb","type":"comment","source":"bigquery"},
		{"year":"2018","month":"09","id":"e5nzg9j","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5mh94v","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5mmenp","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5ms5u3","type":"comment","source":"undef"}
	],
	"GUM_reddit_monsters":[
		{"year":"2018","month":"09","id":"9eci2u","type":"post","source":"undef"},
		{"year":"2018","month":"09","id":"e5ox2jr","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5p3gtl","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5pnfro","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5q08o4","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5pney1","type":"comment","source":"undef"},
	],
	"GUM_reddit_pandas":[
		{"year":"2018","month":"09","id":"9e3s9h","type":"post","source":"undef"},
		{"year":"2018","month":"09","id":"e5lwy6n","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m397o","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3xgb","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3z2e","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lwbbt","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m38sr","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m42cu","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lvlxm","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lvqay","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lw5t6","type":"comment","source":"undef"},  # Blowhole
		{"year":"2018","month":"09","id":"e5lwz31","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lxi0s","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lwxqq","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lzv1b","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m48ag","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m1yqe","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lx0sw","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m2n80","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m2wrh","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3blb","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5lvxoc","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m1abg","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m1w5i","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3pdi","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m3ruf","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m4yu2","type":"comment","source":"undef"},
		{"year":"2018","month":"09","id":"e5m5bcb","type":"comment","source":"undef"}
	],
	"GUM_reddit_steak": [
		{"year":"2015","month":"08","id":"3im341","type":"post","source":"undef"}
	],
	"GUM_reddit_card": [
		{"year":"2019","month":"08","id":"cmqrwo","type":"post","source":"undef"},
		{"year":"2019","month":"08","id":"ew3zrqg","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew43d2c","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew43oks","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew43ymc","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew46h1p","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew46oly","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew46wq7","type":"comment","source":"undef"},
		{"year":"2019","month":"08","id":"ew470zc","type":"comment","source":"undef"}
	],
	"GUM_reddit_callout": [
		{"year":"2019","month":"09","id":"d1eg3u","type":"post","source":"undef"},
		{"year":"2019","month":"09","id":"ezkucpg","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezkv0cc","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezkwbx9","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezlh2o6","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezlkajf","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezlnco2","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezo20yy","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezkwcvh","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezl07dm","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezmajm7","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezl1wz3","type":"comment","source":"undef"},
	],
	"GUM_reddit_conspiracy": [
		{"year":"2019","month":"02","id":"aumhwo","type":"post","source":"undef"},
		{"year":"2019","month":"02","id":"eh9rt0n","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eh9tvyw","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"ehc0l2q","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"ehclwtv","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eh9jo5x","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"ehr2665","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eha3c1q","type":"comment","source":"undef"},
		{"year":"2019","month":"02","id":"eha5jlq","type":"comment","source":"undef"},
	],
	"GUM_reddit_introverts": [
		{"year":"2019","month":"06","id":"by820m","type":"post","source":"undef","title_double": True},  # Possible title was repeated by annotator
		{"year":"2019","month":"06","id":"eqeik8m","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqfgaeu","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqfplpg","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqg6a5u","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqh6j29","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqhjtwr","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqi2jl3","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqii2kf","type":"comment","source":"undef"},
		{"year":"2019","month":"06","id":"eqhlj8j","type":"comment","source":"undef"},

	],
	"GUM_reddit_racial": [
		{"year":"2019","month":"09","id":"d1urjk","type":"post","source":"undef"},
		{"year":"2019","month":"09","id":"ezq9y6w","type":"comment","source":"bigquery"},
		{"year":"2019","month":"09","id":"ezqpqmm","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezq8xs7","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezr55wk","type":"comment","source":"undef"},
	],
	"GUM_reddit_social": [
		{"year":"2019","month":"09","id":"d1qy3g","type":"post","source":"undef"},
		{"year":"2019","month":"09","id":"ezpb3jg","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpdmy3","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpjor8","type":"comment","source":"bigquery"},
		{"year":"2019","month":"09","id":"ezpiozm","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpc1ps","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezp9fbh","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezqrumb","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpe0e6","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpf71f","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezt7qlf","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpc4jj","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpa2e4","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpfzql","type":"comment","source":"undef"},
		{"year":"2019","month":"09","id":"ezpi39v","type":"comment","source":"undef"},
	]
}

def get_proxy_data() -> dict:
	import requests
	out_posts = {}
	tab_delim = requests.get("https://gucorpling.org/gum/fetch_text_proxy.py").text
	for line in tab_delim.split("\n"):
		if "\t" in line:
			post, text = line.split("\t")
			out_posts[post] = text
	return out_posts

def get_no_space_strings(cache_dict) -> dict:
	import ast

	no_space_docs = defaultdict(str)

	for doc in GUM_DOCS:
		for post in GUM_DOCS[doc]:
			if post["id"] in cache_dict:
				json_result = cache_dict[post["id"]]
			parsed = ast.literal_eval(json_result)[0]
			if post["type"]=="post":
				plain = parsed["selftext"]
				title = parsed["title"]
				if "title_only" in post:
					if post["title_only"]:
						plain = ""
				if "title_double" in post:
					title = title + " " + title
			else:
				plain = parsed["body"]
				title = ""
			if "_space" in doc:
				plain = plain.replace("&gt;","")  # GUM_reddit_space has formatting &gt; to indicate indented block quotes
			elif "_gender" in doc:
				plain = plain.replace("- The vast","The vast")
				plain = plain.replace("- Society already accommodates","Society already accommodates")
				plain = plain.replace("- Society recognizes disabilities","Society recognizes disabilities")
				plain = plain.replace("- It’s a waste of time","It’s a waste of time")
				plain = plain.replace("PB&amp;J","PB&J")
			elif "_monsters" in doc:
				plain = plain.replace("1. He refers to","a. He refers to")
				plain = plain.replace("2. Using these","b. Using these")
				plain = plain.replace("3. And he has","c. And he has")
				plain = plain.replace("&#x200B; &#x200B;","")
				plain = re.sub(r' [0-9]+\. ',' ',plain)
			elif "_ring" in doc:
				plain = plain.replace("&gt;",">")
			elif "_escape" in doc:
				plain = plain.replace("*1 year later*","1 year later")
			elif "_racial" in doc:
				plain = plain.replace("> ","")
			elif "_callout" in doc:
				plain = plain.replace("_it","it").replace("well?_","well?").replace(">certain","certain")
			elif "_conspiracy" in doc:
				plain = plain.replace(">", "")
			elif "_stroke" in doc:
				plain = plain.replace("&amp;", "&")
			elif "_bobby" in doc:
				plain = plain.replace("&amp;", "&")
			elif "_introvert" in doc:
				plain = plain.replace("enjoy working out.","enjoy working out").replace("~~","")
			elif "_social" in doc:
				plain = plain.replace("the purpose","those purpose").replace("&#x200B;","")
			no_space = re.sub(r"\s","",plain).replace("*","")
			no_space = re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',no_space)  # Remove Wiki style links: [text](URL)
			if no_space_docs[doc] == "":
				no_space_docs[doc] += re.sub(r"\s","",title).replace("*","")
			no_space_docs[doc] += no_space

	return no_space_docs

def get_list_of_corpus_files(name: str) -> list: 
	""" Get list of datasets files from name of corpus.
	:in: name of corpus
	:out: list of datasets 
	"""
	corpus_files = glob(os.sep.join(["..",DATA_DIR, name, f"{name}*.conllu"])) + \
				   glob(os.sep.join(["..",DATA_DIR, name, f"{name}*.tok"])) + \
				   glob(os.sep.join(["..", DATA_DIR, name, f"{name}*.rels"]))

	sys.stderr.write("Found " + str(len(corpus_files)) + " files in " + os.sep.join(["..",DATA_DIR, name]) + "\n")
	
	return corpus_files

def underscore_files(files_path_li: list) -> None: # TODO Refactor ?
	""" Mask text with underscores in specific files and leave cues for reconstruction.
	:in: list of paths
	"""

	def underscore_rel_field(text: str) -> str:
		""" Replace characters by underscore in a text while keeping discontonuous markers.
		:in: text
		:out: string of unsercores/spaces and disc. markers
		"""
		blanked = []
		text = text.replace("<*>","❤")
		for c in text:
			if c!="❤" and c!=" ":
				blanked.append("_")
			else:
				blanked.append(c)
		return "".join(blanked).replace("❤","<*>")

	for f_path in files_path_li:
		skiplen = 0
		with io.open(f_path, 'r', encoding='utf8') as fin:
			lines = fin.readlines()

		with io.open(f_path, 'w', encoding='utf8', newline="\n") as fout:
			output = []
			if f_path.endswith(".rels"):
				for l, line in enumerate(lines):
					line = line.strip()
					if "\t" in line and l > 0:
						doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, u1_raw, u2_raw, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, rel_type, orig_label, label = line.split("\t")
						if "GUM" in doc and "reddit" not in doc:
							output.append(line)
							continue
						unit1_txt = underscore_rel_field(unit1_txt)
						unit2_txt = underscore_rel_field(unit2_txt)
						u1_raw = underscore_rel_field(u1_raw) 
						u2_raw = underscore_rel_field(u2_raw) 
						unit1_sent = underscore_rel_field(unit1_sent)
						unit2_sent = underscore_rel_field(unit2_sent)
						fields = doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, u1_raw, u2_raw, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, rel_type, orig_label, label	
						line = "\t".join(fields)
					output.append(line)
			else:
				doc = ""
				for line in lines:
					line = line.strip()
					if line.startswith("# newdoc id"):
						doc = line.split("=",maxsplit=1)[1].strip()
					if "GUM" in doc and "reddit" not in doc:
						output.append(line)
						continue
					if line.startswith("# text"):
						m = re.match(r'(# text ?= ?)(.+)',line)
						if m is not None:
							line = m.group(1) + re.sub(r'[^\s]','_',m.group(2))
							output.append(line)
					elif "\t" in line:
						#print(line)
						fields = line.split("\t")
						tok_col, lemma_col = fields[1:3]
						if "_reddit" in doc or "eng.erst.gum" not in f_path:
							if lemma_col == tok_col:  # Delete lemma if identical to token
								fields[2] = '_'
							elif tok_col.lower() == lemma_col:
								fields[2] = "*LOWER*"
							if skiplen < 1:
								fields[1] = len(tok_col)*'_'
							else:
								skiplen -=1
						output.append("\t".join(fields))
						if "-" in fields[0]:  # Multitoken
							start, end = fields[0].split("-")
							start = int(start)
							end = int(end)
							skiplen = end - start + 1
					else:
						output.append(line)
			fout.write('\n'.join(output) + "\n")

def harvest_text(files: list) -> dict:
	"""
	:param files: LDC files containing raw text data
	:return: Dictionary of document base names (e.g. wsj_0013) to string of non-whitespace characters in the document
	"""
	docs = {}
	for file_ in files:
		docname = os.path.basename(file_).split(".")[0]
		try:
			text = io.open(file_,encoding="utf8").read()
		except:
			text = io.open(file_,encoding="Latin1").read()  # e.g. wsj_0142

		text = text.replace(".START","")  # Remove PDTB .START codes
		text = re.sub(r'\s','', text)  # Remove all whitespace
		docs[docname] = text # = soupe de characters
		
	return docs

def restore_GUM_docs(path_to_underscores: str, text_dict: dict) -> None:
	"""
	Specific methods for GUM because it is partially underscored and has ellipsea.
	:path_to_underscores: path to corpus folder
	:text_dict: dict as Dict[docname] = allcharacterswithoutspace
	TODO : factorisation/fusion with def restore_docs.
	"""
	dep_files = glob(path_to_underscores+os.sep+"*.conllu")
	tok_files = glob(path_to_underscores+os.sep+"*.tok") 
	rel_files = glob(path_to_underscores+os.sep+"*.rels")
	
	idx_tok_dict = restore_GUM_dep_files(dep_files, text_dict)
	rebuild_GUM_tok_files_from_dep_files(tok_files)
	restore_GUM_rel_files(rel_files, idx_tok_dict)

def restore_docs(path_to_underscores: str, text_dict: dict) -> None: # text_dict: Dict[doc_id]=text no space
	""" Main method to unmasking.
	:path_to_underscores: path to corpus folder
	:text_dict: dict as Dict[docname] = allcharacterswithoutspace
	"""

	dep_files = glob(path_to_underscores+os.sep+"*.conllu")
	tok_files = glob(path_to_underscores+os.sep+"*.tok") 
	rel_files = glob(path_to_underscores+os.sep+"*.rels")
	
	idx_tok_dict = restore_dep_files(dep_files, text_dict)
	rebuild_tok_files_from_dep_files(tok_files)
	restore_rel_files(rel_files, idx_tok_dict)

def rebuild_GUM_tok_files_from_dep_files(files: list) -> None:
	""" From dep files, get token, lemmas, labels and compute ID for tok files
	:files: tok_files .toks
	:dep_files: .conllu
	"""

	for file_ in files:
		print(f"restore {file_}")
		dep_file = re.sub(".tok", ".conllu", file_)
		lines = open(f"{dep_file}", 'r', encoding='utf-8').readlines()
		output = []
		tokid = 0

		for i, line in enumerate(lines):
			line = line.strip()
			if line.startswith("#"):
				if line.startswith(META_DOCID) and i == 0:
					output.append(line)
					tokid = 0
				elif line.startswith(META_DOCID) and i > 0:
					output.append(f"\n{line}")
					tokid = 0
				else:
					continue
			elif line == "":
				continue
			else: 
				fields = line.split("\t")
				if "." in fields[0]: # ellips not display in .tok => for coherence, keep ID n.m and label = "_"
					label = get_tok_label_from_dep_label(fields[-1])
					#get m value
					m = fields[0].split(".")[1]
					newid = f"{str(tokid)}.{m}"
					#tokid += 1
					new_fields = [str(newid), fields[1], "_", "_", "_", "_", "_", "_", "_", label]
					output.append("\t".join(new_fields))
				elif "-" in fields[0]:
					label = get_tok_label_from_dep_label(fields[-1])
					mweid = get_mweid(tokid, fields[0])
					new_fields = [mweid, fields[1], "_", "_", "_", "_", "_", "_", "_", label]
					output.append("\t".join(new_fields))    ### NOT FIELDS 0 !!
				else:
					label = get_tok_label_from_dep_label(fields[-1])
					tokid += 1
					new_fields = [str(tokid), fields[1], "_", "_", "_", "_", "_", "_", "_", label]
					output.append("\t".join(new_fields))    ### NOT FIELDS 0 !!

		with open(f"{file_}", 'w', encoding='utf-8', newline="\n") as fo:
			fo.write("\n".join(output) + "\n")

def rebuild_tok_files_from_dep_files(files: list) -> None:
	""" From dep files, get token, lemmas, labels and compute ID for tok files
	:files: tok_files .toks
	:dep_files: .conllu
	"""

	for file_ in files:
		print(f">>> Processing for tok {file_}...")
		dep_file = re.sub(".tok", ".conllu", file_)
		lines = open(f"{dep_file}", 'r', encoding='utf-8').readlines()
		output = []
		tokid = 0

		for i, line in enumerate(lines):
			line = line.strip()
			if line.startswith("#"):
				if line.startswith(META_DOCID) and i == 0:
					output.append(line)
					tokid = 0
				elif line.startswith(META_DOCID) and i > 0:
					output.append(f"\n{line}")
					tokid = 0
				else:
					continue
			elif line == "":
				continue
			else: 
				fields = line.split("\t")
				if "." in fields[0]: # ellips not display in .tok TODO change that ? (only GUM now)
					continue
				elif "-" in fields[0]:
					label = get_tok_label_from_dep_label(fields[-1])
					mweid = get_mweid(tokid, fields[0])
					new_fields = [mweid, fields[1], "_", "_", "_", "_", "_", "_", "_", label]
					output.append("\t".join(new_fields))    ### NOT FIELDS 0 !!
				else:
					label = get_tok_label_from_dep_label(fields[-1])
					tokid += 1
					new_fields = [str(tokid), fields[1], "_", "_", "_", "_", "_", "_", "_", label]
					output.append("\t".join(new_fields))    ### NOT FIELDS 0 !!

		with open(f"{file_}", 'w', encoding='utf-8', newline="\n") as fo:
			fo.write("\n".join(output) + "\n")

def get_mweid(tokid: int, conllid) -> str:
	""" Define IDs of MWE (contracted form) document-based for tok from sentence-based from dep.
	:tokid: current token count, document-based.
	:conllid: current token count, sentence-based.
	:out: MWE ID shaped as n-m with n and m document-based.
	"""
	n = compute_mwe_status(conllid) # number of word in the MWE
	if n == 3:
		pass
		#print(conllid)
	mweid = f"{tokid + 1}-{tokid + 1 + n -1}"
	return mweid

def get_tok_label_from_dep_label(label:str) -> str:
	""" Get clean label for tok file from dep file where label column may have multiple unrelated labels.
	"""
	options = ["Conn=O","Conn=B-conn","Conn=I-conn","Seg=O","Seg=B-seg"] # "_" (MWE-contracted), "Conn=O" (ellips)
	newlabel = "_"

	if label == "_": # ellips ? => "_"
		newlabel = label
	
	for it in options:
		if it in label:
			newlabel = it

	return newlabel

def restore_GUM_dep_files(files, text_dict) -> dict:
	""" This function reads and writes dep files, with replacement of underscores by corresponding text.
		In the meantime, a dictionary is filled as: Dict[docname][token id document based]="token string"
		without contracted forms of MWE. Will be used to fill syntactic text in .rels.

	:files: list of dep files path
	:text_dict: dictionary of text as Dict[docname]="full doc as one string without space"
	:return Dict of (syntactical) tokens
	"""
	# specific GOESWITH patches
	patches = ['16	____	_	X	IN	_	15	goeswith	15:goeswith	CorrectForm=_|XML=</sic>|Seg=O', '6	_______	_	X	VBG	_	5	goeswith	5:goeswith	CorrectForm=_|XML=</sic>|Seg=O']
	patches.append('16	____	_	X	IN	_	15	goeswith	15:goeswith	CorrectForm=_|XML=</sic>|Conn=O')
	patches.append('6	_______	_	X	VBG	_	5	goeswith	5:goeswith	CorrectForm=_|XML=</sic>|Conn=O')

	my_dict = {}

	for file_ in files:
		print(f"restore {file_}")
		lines = open(file_, 'r', encoding='utf-8').readlines()
		output = []

		tid = 0 # token ID document-based
		cid = 0 # character ID deocument-based
		cid_delay_mwe = 0 # variable to adjust CID while MWE
		mwe_status = 0
		docname = ""

		for line in lines:
			line = line.strip()

			if line.startswith(META_DOCID): # newdoc
				docname = re.sub(META_DOCID, "", line)
				my_dict[docname] = {}
				
				tid = 0
				cid = 0
				output.append(line)

			elif "GUM" in docname and "reddit" not in docname:
				output.append(line)

			elif line.startswith(META_TEXT):
				masked = re.sub(META_TEXT, "", line)
				unmasked = fill_text_with_char(cid, text_dict[docname], masked)
				output.append(f"{META_TEXT}{unmasked}")
			elif line.startswith("#"): # other metadata
				output.append(line)
			elif line == "": # empty lines between sent or doc
				output.append(line)
			else:
				fields = line.split("\t")
				if "-" in fields[0]: # MWE contracted form
					fields[1] = fill_text_with_char(cid, text_dict[docname], fields[1])
					output.append("\t".join(fields))
					cid_delay_mwe = cid + len(fields[1])
					mwe_status = compute_mwe_status(fields[0])
					
				elif "." in fields[0]: # ellipsis in GUM ==> useless cause no case of ellipsis in reddit (2024/04/04)
					pass

				else:

					tid += 1

					# get token and lemma
					if len(re.sub("_", "", fields[1])) > 0: # if not underscored

						fields[2] = compute_lemma(fields[1], fields[2]) #--------------------------------
						output.append("\t".join(fields))

					else:
						fields[1] = fill_text_with_char(cid, text_dict[docname], fields[1])
						fields[2] = compute_lemma(fields[1], fields[2]) # -----------------------------
						fields[2] = "_" if line in patches else fields[2]
						output.append("\t".join(fields))


					# define cid depending on mwe status
					if mwe_status == 1:
						cid = cid_delay_mwe
					elif mwe_status > 1:
						cid = cid
					elif mwe_status == 0:
						cid = cid + len(fields[1])
					mwe_status = get_mwe_status(mwe_status)

					# fill dict for tokens in rels (without contracted forms) 
					my_dict[docname][int(tid)] = fields[1]


		with open(f"{file_}", 'w', encoding='utf-8', newline="\n") as fo:
			fo.write("\n".join(output) + "\n")
	return my_dict

def restore_dep_files(files: list, text_dict) -> dict:
	""" This fynction read and write dep files, with replacement of underscores by corresponding text.
		In the meantime, a dictionary is filled as: Dict[docname][token id document based]="token string" without contracted forms of MWE. Will be used to fill syntactical text in .rels.
	:files: list of dep files path
	:text_dict: dictionary of text as Dict[docname]="full doc as one string without space"
	:return Dict of (syntactical) tokens
	"""

	my_dict = {}

	for file_ in files:
		print(f">>> Processing for conllu {file_}...")
		lines = open(file_, 'r', encoding='utf-8').readlines()
		output = []

		tid = 0 # token ID document-based
		cid = 0 # character ID document-based
		cid_delay_mwe = 0 # variable to adjust CID while MWE
		mwe_status = 0

		for line in lines:
			line = line.strip()

			if line.startswith(META_DOCID): # newdoc
				docname = re.sub(META_DOCID, "", line)
				my_dict[docname] = {}
				
				tid = 0
				cid = 0
				output.append(line)

			elif line.startswith(META_TEXT):
				masked = re.sub(META_TEXT, "", line)
				unmasked = fill_text_with_char(cid, text_dict[docname], masked)
				output.append(f"{META_TEXT}{unmasked}")
			elif line.startswith("#"): # other metadata
				output.append(line)
			elif line == "": # empty lines between sent or doc
				output.append(line)
			else:
				fields = line.split("\t")
				if "-" in fields[0]: # MWE contracted form
					fields[1] = fill_text_with_char(cid, text_dict[docname], fields[1])
					output.append("\t".join(fields))
					cid_delay_mwe = cid + len(fields[1])
					mwe_status = compute_mwe_status(fields[0])
					
				elif "." in fields[0]: # ellips in GUM # TODO something more factorized and cleaner ><
					pass
				else:

					tid += 1

					# get token and lemma
					if len(re.sub("_", "", fields[1])) > 0: # if not underscored
						fields[2] = compute_lemma(fields[1], fields[2])
						output.append("\t".join(fields))
					else:
						fields[1] = fill_text_with_char(cid, text_dict[docname], fields[1])
						fields[2] = compute_lemma(fields[1], fields[2])
						output.append("\t".join(fields))

					# define cid depending on mwe status
					if mwe_status == 1:
						cid = cid_delay_mwe
					elif mwe_status > 1:
						cid = cid
					elif mwe_status == 0:
						cid = cid + len(fields[1])
					mwe_status = get_mwe_status(mwe_status)

					# fill dict for tokens in rels (without contracted forms) 
					my_dict[docname][int(tid)] = fields[1]


		with open(f"{file_}", 'w', encoding='utf-8', newline="\n") as fo:
			fo.write("\n".join(output) + "\n")
			#print(my_dict.keys())
	return my_dict

def fill_text_with_char(cid: int, text_doc: str, masked: str) -> str :
	""" This method get text string from characters span IDS. 
	:cid: first character ID 
	:text_doc: full doc text no space
	:masked: string of underscores to replace with character 
	:out: span of text
	"""
	unmasked = ""
	for c in masked:
		if c == "_":
			unmasked = unmasked + text_doc[cid:cid+1]
			cid += 1
		elif c == " ":
			unmasked = unmasked + c
	return unmasked

def compute_lemma(f1: str, f2: str) -> str:
	""" This function compute lemma from cues in masked files.
	:f1: unmasked text of token
	:f2: masked lemma
	:out: unmasked lemma
	"""
	lemma = ""
	if f2 == "_":
		lemma = f1
	elif f2 == "*LOWER*":
		lemma = f1.lower()
	else:
		lemma = f2
	return lemma

def compute_mwe_status(f0: int) -> int:
	""" This function compute if current token are inside a MWE or not.
	:f0: status in
	:status:  status out
	"""
	nbs = f0.split("-")
	status = int(nbs[1]) - int(nbs[0]) + 1 # number of extended forms
	return status

def get_mwe_status(status: int) -> int:
	""" This function compute if current token are inside a MWE or not.
	:in: status in
	:out:  status out
	"""
	if status > 0 : # current token is part of MWE
		status -= 1
	elif status == 0:
		status = 0
	return status

def restore_GUM_rel_files(files: list, idx_dict: dict) -> None:
	""" Reconstruction of text in rels files, using dicts and IDs 1-document-based.
	:files: list of rels files masked
	:idx_dict:	dict of syntactical tokens as Dict[docname][ID] = token string
	"""

	for file_ in files:
		print(f"restore {file_}")
		#store toks
		tok_path = re.sub(".rels",".tok", file_)
		tok_dict = get_tokenized_text(tok_path) # pour tout le file.tok . relevant to get 1-based id document based.

		#store rels
		lines = open(file_, 'r', encoding='utf-8').readlines()
		output = [] # List of new lines

		for line in lines:
			line = line.strip()
			if line != "" and not line.startswith(HEADER_rels)  :
				doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, u1_raw, u2_raw, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, rel_type, orig_label, label = line.split("\t")
				if "reddit" in doc:
					unit1_txt = get_span_from_idx(unit1_toks, idx_dict[doc]) # my_dict[docname][tid] = fields[1]
					unit2_txt = get_span_from_idx(unit2_toks, idx_dict[doc])
					u1_raw = get_raw_span_from_idx(unit1_toks, tok_dict[doc])
					u2_raw = get_raw_span_from_idx(unit2_toks, tok_dict[doc])
					unit1_sent = get_span_from_idx(s1_toks, idx_dict[doc])
					unit2_sent = get_span_from_idx(s2_toks, idx_dict[doc])
				output.append("\t".join([doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, u1_raw, u2_raw, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, rel_type, orig_label, label]))
			else:
				output.append(line)

		with open(f"{file_}", 'w', encoding='utf-8', newline="\n") as fo:
			fo.write("\n".join(output) + "\n")

def restore_rel_files(files: list, idx_dict: dict) -> None:
	""" Reconstruction of text in rels files, using dicts and IDs 1-document-based.
	:files: list of rels files masked
	:idx_dict:	dict of syntactical tokens as Dict[docname][ID] = token string
	"""

	for file_ in files:
		print(f">>> Processing for rels {file_}...")
		#store toks
		tok_path = re.sub(".rels",".tok", file_)
		tok_dict = get_tokenized_text(tok_path) # pour tout le file.tok

		#store rels
		lines = open(file_, 'r', encoding='utf-8').readlines()
		output = [] # List of new lines

		for line in lines:
			line = line.strip()
			if line != "" and not line.startswith(HEADER_rels):
				doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, u1_raw, u2_raw, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, rel_type, orig_label, label = line.split("\t")
				unit1_txt = get_span_from_idx(unit1_toks, idx_dict[doc]) # my_dict[docname][tid] = fields[1]
				unit2_txt = get_span_from_idx(unit2_toks, idx_dict[doc])
				u1_raw = get_raw_span_from_idx(unit1_toks, tok_dict[doc])
				u2_raw = get_raw_span_from_idx(unit2_toks, tok_dict[doc])
				unit1_sent = get_span_from_idx(s1_toks, idx_dict[doc])
				unit2_sent = get_span_from_idx(s2_toks, idx_dict[doc])
				output.append("\t".join([doc, unit1_toks, unit2_toks, unit1_txt, unit2_txt, u1_raw, u2_raw, s1_toks, s2_toks, unit1_sent, unit2_sent, direction, rel_type, orig_label, label]))
			else:
				output.append(line)

		with open(f"{file_}", 'w', encoding='utf-8', newline="\n") as fo:
			fo.write("\n".join(output) + "\n")

def get_tokenized_text(path: str) -> dict:
	""" This function harvests all tokens full lines but ellipsis of a .tok file. Relevant to get 1-based token IDs document-based.
	:in: path to the file
	:out: Dict[docname] = List of tokens lines
	"""
	
	tok_dict = {}
	with open(path, "r", encoding="utf-8") as ft:
		t_data = ft.readlines()
		k = ""
		v =[]
	for i, line in enumerate(t_data):
		line =line.strip()
		if line.startswith("# newdoc id") and i == 0:
			k = re.sub("# newdoc id = ", "", line)
		elif line.startswith("# newdoc id"): ### redondant ----------------- ??
			k = re.sub("# newdoc id = ", "", line)
		elif line == "" :
			tok_dict[k] = v
			v = []
		elif i == len(t_data)-1:
			v.append(line)
			tok_dict[k] = v
			v = []
		elif line.startswith("#"):
			continue
		elif re.match(r"^\d+\.\d", line): # no need for ellips in raw text
			continue
		else:
			v.append(line)

	return tok_dict

def get_span_from_idx(unit: str, doc_dict: dict) -> str:
	""" Rebuild text from span of tokens IDs document-based of shape "n-m, p"
    :unit: unit a span IDs
    :doc_dict: from dep_file, Dict[token IDs] = token : only syntactical IDs/tokens (no MWE contracted forms)  
	:out: corresponding text sequence, with discontinuity marker if any as "blabla <*> blablabla"
    """

	text = ""

	if re.search(",", unit): # discontinuity
		units = unit.split(",")
		texts = []
		for un in units:
			if re.search("-", un): # multi tokens span
				txt = []
				segs = un.split("-")
				a = int(segs[0])
				b = int(segs[1])
				txt.append(doc_dict[a])
				i = a + 1
				while i <= b:
					txt.append(doc_dict[i])
					i += 1
				t = " ".join(txt)
				texts.append(t)
			else:
				txt = doc_dict[int(un)]
				texts.append(txt)
			text = " <*> ".join(texts)
	else:
		if re.search("-", unit): # multi tokens span
			txt = []
			segs = unit.split("-")
			a = int(segs[0])
			b = int(segs[1])
			txt.append(doc_dict[a])
			i = a + 1
			while i <= b:
				txt.append(doc_dict[i])
				i += 1
			text = " ".join(txt)
		else:
			text = doc_dict[int(unit)]

	return text

def get_raw_span_from_idx(unit: str, doc_dict_tok: dict) -> str:
	""" Rebuild text from span of tokens IDs document-based of shape "n-m, p"
    :unit: unit a span IDs
    :doc_dict_tok: from tok_file, Dict[token IDs] = token : only raw/natural IDs/tokens (no MWTs extended forms)  
	:out: corresponding text sequence, with discontinuity marker if any as "blabla <*> blablabla"
    """
	
	idx = unit
	text = ""
	parts = idx.split(",") # marker of discontinuity
	if len(parts) == 1:
		if len(parts[0].split("-")) > 1: # interval
			s = parts[0].split("-")[0]
			e = parts[0].split("-")[1]
			segment_text = get_segment(doc_dict_tok, s, e)
			text = segment_text
		else: # unique token
			s = parts[0].split("-")[0]
			e = ""
			segment_text = get_segment(doc_dict_tok, s, e)
			text = segment_text
	elif len(parts) > 1:
		texts = []
		for it in parts:
			if len(it.split("-")) > 1:
				s = it.split("-")[0]
				e = it.split("-")[1]
				segment_text = get_segment(doc_dict_tok, s, e)
				texts.append(segment_text)
			else:
				s = it.split("-")[0]
				e = ""
				segment_text = get_segment(doc_dict_tok, s, e)
				texts.append(segment_text)
		text = " <*> ".join(texts)

	return text
	
def get_segment(doc_dict_tok: dict, s: str, e="") -> str:
	""" Get span of raw text.
	:in: interval {s,e} or uniq {s} ID(s). 
	:doc_dict_tok: Dict[ID] = token from tok file (so with contracted form of MWE)
	:out: string of tokens with spaces in between.
	"""
	
	data_doc = doc_dict_tok
	words_li = []

	if e == "": # cas of unique token
		i = 0
		while i < len(data_doc):
			id = data_doc[i].split("\t")[0]
			word = data_doc[i].split("\t")[1]
			if id.split("-")[0] == s: # start of segment ## !!! inutile ?? TODO verif
				words_li.append(word)
				break
			else:
				i += 1
	else:
		i=0
		while i < len(data_doc):	
			id = data_doc[i].split("\t")[0]
			word = data_doc[i].split("\t")[1]

			if id.split("-")[0] == s: # start of segment
				words_li.append(word)
				if "-" in id: # contracted form can be > 2 forms !!!!!
					nb = get_nb_of_words(id)
					i = i + nb + 1 # ---------------------------------------------- e-s !
				else:
					i += 1
			elif id.split("-")[0] == e: # end of segment
				words_li.append(word)
				break
			elif len(words_li) > 0: # on est dans le segment
				words_li.append(word)
				if "-" in id: # contracted form can be > 2 forms !!!!!
					nb = get_nb_of_words(id)
					i = i + nb + 1 # ---------------------------------------------- e-s !
				else:
					i += 1
			else:
				i += 1
	
	return " ".join(words_li)
	
def get_nb_of_words(id:str) -> int:
	""" Compute how many tokens are hidden in a Multi-Words Expression.
	:in: ID of MWE
	:out: number
	"""
	first_word = int(id.split("-")[0])
	last_word = int(id.split("-")[1])
	nb = last_word - first_word + 1
	return nb



if __name__ == "__main__":

	p = ArgumentParser()
	p.add_argument("-c","--corpus",action="store",choices=["eng.rst.rstdt","eng.pdtb.pdtb","zho.pdtb.cdtb","tur.pdtb.tdb","eng.erst.gum","eng.pdtb.gum","all"],default="all",help="Name of the corpus to process or 'all'")
	p.add_argument("-m","--mode",action="store",choices=["add","del"],default="add",help="Use 'add' to restore data and 'del' to replace text with underscores")
	opts = p.parse_args()


	# DEL MODE - MAKE UNDERSCORES
	if opts.mode == "del":  # Remove text from resources that need to be underscored for distribution
		files = []
		if opts.corpus == "eng.rst.rstdt" or opts.corpus == "all":
			files += get_list_of_corpus_files("eng.rst.rstdt")
		if opts.corpus == "eng.pdtb.pdtb" or opts.corpus == "all":
			files += get_list_of_corpus_files("eng.pdtb.pdtb")
		if opts.corpus == "zho.pdtb.cdtb" or opts.corpus == "all":
			files += get_list_of_corpus_files("zho.pdtb.cdtb")
		if opts.corpus == "tur.pdtb.tdb" or opts.corpus == "all":
			files += get_list_of_corpus_files("tur.pdtb.tdb")
		if opts.corpus == "eng.erst.gum" or opts.corpus == "all":
			files += get_list_of_corpus_files("eng.erst.gum")
		if opts.corpus == "eng.pdtb.gum" or opts.corpus == "all":
			files += get_list_of_corpus_files("eng.pdtb.gum")
			
		underscore_files(files)
		

	# ADD MODE - RESTORE TEXT
	elif opts.mode == "add":

		# Prompt user for corpus folders
		if opts.corpus == "eng.rst.rstdt" or opts.corpus == "all":
			rstdt_path = input("Enter path for LDC RST-DT data/ folder:\n> ")
			if not os.path.isdir(rstdt_path):
				sys.stderr.write("Can't find directory at: " + rstdt_path + "\n")
				sys.exit(0)
			files = glob(os.sep.join([rstdt_path,"RSTtrees-WSJ-main-1.0","TRAINING","*.edus"])) + glob(os.sep.join([rstdt_path,"RSTtrees-WSJ-main-1.0","TEST","*.edus"]))
			docs2text = harvest_text(files)
			restore_docs(os.sep.join(["..",DATA_DIR,"eng.rst.rstdt"]),docs2text)


		if opts.corpus == "eng.pdtb.pdtb" or opts.corpus == "all":
			pdtb_path = input("Enter path for LDC Treebank 2 raw/wsj/ folder:\n> ")
			if not os.path.isdir(pdtb_path):
				sys.stderr.write("Can't find directory at: " + pdtb_path + "\n")
				sys.exit(0)
			files = []
			for i in range(0,25):
				dir_name = str(i) if i > 9 else "0" + str(i)
				files += glob(os.sep.join([pdtb_path,dir_name,"wsj_*"]))
			docs2text = harvest_text(files)
			restore_docs(os.sep.join(["..",DATA_DIR,"eng.pdtb.pdtb"]),docs2text)


		if opts.corpus == "zho.pdtb.cdtb" or opts.corpus == "all":
			cdtb_path = input("Enter path for LDC Chinese Discourse Treebank 0.5 raw/ folder:\n> ")
			if not os.path.isdir(cdtb_path):
				sys.stderr.write("Can't find directory at: " + cdtb_path + "\n")
				sys.exit(0)
			files = glob(os.sep.join([cdtb_path,"*.raw"]))
			docs2text = harvest_text(files)
			restore_docs(os.sep.join(["..",DATA_DIR,"zho.pdtb.cdtb"]),docs2text)
		

		if opts.corpus == "tur.pdtb.tdb" or opts.corpus == "all":
			tdb_path = input("Enter path for Turkish Discourse Bank 1.0 raw/01/ folder:\n> ")
			if not os.path.isdir(tdb_path):
				sys.stderr.write("Can't find directory at: " + tdb_path + "\n")
				sys.exit(0)
			files = glob(os.sep.join([tdb_path,"*.txt"]))
			docs2text = harvest_text(files)
			restore_docs(os.sep.join(["..",DATA_DIR, "tur.pdtb.tdb"]),docs2text)


		if opts.corpus == "eng.erst.gum" or opts.corpus == "all":
			response = input("Do you want to try downloading reddit data from an available server?\n"+
							"Confirm: you are solely responsible for downloading reddit data and "+
							"may only use it for non-commercial purposes:\n[Y]es/[N]o> ")
			if response == "Y":
				print("Retrieving reddit data by proxy...")
				data = get_proxy_data()
				docs2text = get_no_space_strings(data)
			else:
				sys.stderr.write("Aborting\n")
				sys.exit(0)
			restore_GUM_docs(os.sep.join(["..",DATA_DIR,"eng.erst.gum"]),docs2text)


		if opts.corpus == "eng.pdtb.gum" or opts.corpus == "all":
			response = input("Do you want to try downloading reddit data from an available server?\n"+
							"Confirm: you are solely responsible for downloading reddit data and "+
							"may only use it for non-commercial purposes:\n[Y]es/[N]o> ")
			if response == "Y":
				print("Retrieving reddit data by proxy...")
				data = get_proxy_data()
				docs2text = get_no_space_strings(data)
			else:
				sys.stderr.write("Aborting\n")
				sys.exit(0)
			restore_GUM_docs(os.sep.join(["..",DATA_DIR,"eng.pdtb.gum"]),docs2text)