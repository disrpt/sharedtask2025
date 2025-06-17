"""
Script to validate contents of each dataset under ../data/<dataset>/*.(tok|conllu|rels) files.

"""

from glob import glob
from collections import defaultdict
from argparse import ArgumentParser
import os, re

valid_rels =  {'alternation', 'attribution', 'causal', 'comment', 'concession', 'condition', 'conjunction', 'contrast',
               'elaboration', 'explanation', 'frame', 'label', 'mode', 'organization', 'purpose', 'query',
               'reformulation', 'temporal'}
all_rel_types = {"explicit", "implicit", "unknown", "altlex", "altlexc", "entrel", "hypophora"}
deprels = {"nsubj", "obj", "iobj", "obl", "nmod", "root", "advcl", "ccomp", "acl", "amod", "det", "case",
           "cc", "conj", "punct", "mark", "aux", "cop", "expl", "fixed", "flat", "list", "nummod",
           "parataxis", "appos", "discourse", "dep", "goeswith", "vocative", "orphan", "reparandum",
           "advmod", "xcomp", "compound", "csubj", "dislocated", "clf"}
upos = {"ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART",
        "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X"}


def test_rels(filename):
    """
    Tests:
        - Check that all rels files have a header, 15 columns, no empty lines, no duplicate lines
        - No column is empty
        - Check that all relations have a valid label in last column
        - Check that relation type column (fields[-3]) is either always "unknown" or always one of "implicit"/"explicit"

    :param filename:
    :return: stats, docs, errors
    """

    stats = defaultdict(int)
    docs = defaultdict(int)
    seen_errs = set()
    errors = []

    lines = open(filename, "r", encoding="utf-8").read().strip().split("\n")
    filename = os.path.basename(filename)
    if not lines:
        errors.append(f"{filename} is empty")
    else:
        header = lines[0]
        if not header.startswith("doc\t"):
            errors.append(f"{filename} does not have a valid header: {header}")

        seen = set()
        reltypes = set()
        for l, line in enumerate(lines[1:]):
            fields = line.split("\t")
            docs[fields[0]] += 1
            stats["relations"] += 1
            if not line.strip():
                errors.append(f"{filename} line {l+2} is empty")
                continue
            if line in seen:
                errors.append(f"{filename} line {l+2} is a duplicate: {line}")
                continue
            seen.add(line)
            if len(fields) != 15:
                errors.append(f"{filename} line {l+2} has {len(fields)} fields, expected 15")
                continue
            if any(not f.strip() for f in fields):
                errors.append(f"{filename} line {l+2} has empty fields: {fields}")
                continue
            if fields[-1] not in valid_rels:
                errors.append(f"{filename} line {l+2} has invalid relation label: {fields[-1]}")
                continue
            u1_first = int(re.search(r'^[0-9]+',fields[1]).group(0))
            u2_first = int(re.search(r'^[0-9]+',fields[2]).group(0))
            if u1_first >= u2_first:
                if fields[1]== fields[2]:
                    errors.append(f"{filename} line {l+2} has invalid units, u1 and u2 are the same: {fields[1]} and {fields[2]}")
                else:
                    errors.append(f"{filename} line {l+2} has invalid unit order, u1 begins with token {u1_first} and u2 begins with token {u2_first}")
                continue
            reltypes.add(fields[-3])

    stats["relation_types"] = "invalid"
    if len(reltypes) == 1:
        if "unknown" not in reltypes and "explicit" not in reltypes:
            errors.append("" + filename + " has only one relation type: " + str(reltypes) + ", expected ['unknown'] or ['explicit']")
        else:
            stats["relation_types"] = "unknown"
    elif len(reltypes) == 2:
        if sorted(list(reltypes)) != ["explicit", "implicit"]:
            errors.append(f"{filename} has invalid relation types: {sorted(list(reltypes))}, expected ['explicit', 'implicit']")
        else:
            stats["relation_types"] = "explicit/implicit"
    elif len(reltypes) > 2:
        if any([r not in all_rel_types for r in reltypes]):
            errors.append(f"{filename} has invalid relation types: {sorted(list(reltypes))}, expected {sorted(all_rel_types)} or ['unknown']")
    else:
        errors.append(f"{filename} has unknown relation type inventory: {sorted(list(reltypes))}, expected {sorted(all_rel_types)} or ['explicit', 'implicit'] or ['unknown']")

    return stats, docs, errors


def test_conllu(filename, tokmode=False):
    """
    Tests that a conllu file has:

    In both modes:
    - Only lines with either 10 fields (tab delim), no tabs but begin with '# anno( = val)?', or blank lines
    - End with two new lines
    - Have at least one '# newdoc id = <docname>' line
    - Col 1 is always a number (token ID), range (1-2) or ellipsis ID (1.1,1.2, etc.)
    - Col 10 must contain either Seg=B-seg/I-seg/O or Conn=B-conn/I-conn/O

    In conllu mode (tokmode=False):
    - Col 3 must be a valid UPOS tag (17 tags: ADJ, ADP, ADV, AUX, CCONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X)
    - Col 6 must be an integer
    - Col 7 must be a valid UD deprel, ignoring subtypes (e.g. nsubj:pass -> nsubj)

    :param filename:
    :return:
    """
    stats = defaultdict(int)
    docs = defaultdict(int)
    errors = []
    seen_errs = set()

    conllu = open(filename).read()
    filename = os.path.basename(filename)
    if not conllu.endswith("\n\n"):
        errors.append(f"{filename} does not end with two new lines")
    if "# newdoc id = " not in conllu:
        errors.append("" + filename + " does not have a '# newdoc id = <docname>' line")

    lines = conllu.strip().split("\n")

    for l, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("#"):
            if line.startswith("# newdoc id = "):
                docname = line.split(" = ")[-1].strip()
        if "\t" in line:
            fields = line.split("\t")
            if len(fields) != 10:
                errors.append(f"{filename} line '{l+1}' has {len(fields)} fields, expected 10")
            if not (fields[0].count("-") == 1 or fields[0].isdigit() or int(float(fields[0])) >= 0 or fields[0].count(".") > 1):
                errors.append(f"{filename} line {l+1} has invalid token ID: {fields[0]}")
            if "-" in fields[0]:
                if any([x in fields[-1] for x in {"Seg=B-seg", "Seg=I-seg", "Seg=O", "Conn=B-conn", "Conn=I-conn", "Conn=O"}]) and "BIOMWT" not in seen_errs:
                    errors.append(f"{filename} line {l+1} has BIO tags in MWT line, suppressing further errors")
                    seen_errs.add("BIOMWT")
            else:
                if not "." in fields[0] and not any([x in fields[-1] for x in {"Seg=B-seg", "Seg=I-seg", "Seg=O", "Conn=B-conn", "Conn=I-conn", "Conn=O"}]) and "BIO" not in seen_errs:
                    errors.append(f"{filename} line {l+1} has invalid segmentation/connective annotation (no BIO tag), suppressing further errors")
                    seen_errs.add("BIO")
                if fields[3] not in upos and not tokmode:
                    errors.append(f"{filename} line {l+1} has invalid UPOS tag: {fields[3]}")
                if not fields[6].isdigit() and not tokmode and not "." in fields[0]:
                    errors.append(f"{filename} line {l+1} has invalid dependency relation ID: {fields[6]}")
                deprel = fields[7].split(":")[0]
                if deprel not in deprels and not tokmode and not "." in fields[0]:
                    errors.append(f"{filename} line {l+1} has invalid dependency relation: {fields[7]}")

    return stats, docs, errors


if __name__ == "__main__":
    p = ArgumentParser(description="Validate datasets in the repository")
    p.add_argument("-c","--corpus", default=None, type=str, help="Corpus to validate (default: all corpora)")
    p.add_argument("-d","--datadir", default=None, type=str, help="Directory containing datasets to validate (default: ../data)")

    args = p.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep
    if args.datadir:
        datadir = os.path.abspath(args.datadir)
    else:
        datadir = os.path.abspath(script_dir + ".." + os.sep + "data")
    datasets = glob(datadir + os.sep + "*")

    if args.corpus is not None:
        datasets = [d for d in datasets if os.path.basename(d) == args.corpus]
        if not datasets:
            print(f"No datasets found for corpus '{args.corpus}'")
            exit(1)


    for dataset in datasets:
        if os.path.basename(dataset) in ["ita.pdtb.luna","pol.iso.pdc"]:
            continue
        print(f"o {dataset.split(os.sep)[-1]}:", end=" ")
        rels_files = glob(os.path.join(dataset, "*.rels"))
        conllu_files = glob(os.path.join(dataset, "*.conllu"))
        tok_files = glob(os.path.join(dataset, "*.tok"))
        valid_files = 0
        seen_errs = False

        for filename in rels_files:
            stats, docs, errors = test_rels(filename)
            filename = os.path.basename(filename)
            if errors:
                if not seen_errs:
                    print()
                seen_errs = True
                print(f"  ! Errors in {filename}:")
                for error in errors:
                    print("    -", error)
            else:
                valid_files += 1

        for filename in conllu_files:
            stats, docs, errors = test_conllu(filename)
            filename = os.path.basename(filename)
            if errors:
                if not seen_errs:
                    print()
                seen_errs = True
                print(f"  ! Errors in {filename}:")
                for error in errors:
                    print("    -", error)
            else:
                valid_files += 1

        for filename in tok_files:
            stats, docs, errors = test_conllu(filename, tokmode=True)
            filename = os.path.basename(filename)
            if errors:
                if not seen_errs:
                    print()
                seen_errs = True
                print(f"  ! Errors in {filename}:")
                for error in errors:
                    print("    -", error)
            else:
                valid_files += 1

        if valid_files == len(rels_files) + len(conllu_files) + len(tok_files):
            print("OK")

