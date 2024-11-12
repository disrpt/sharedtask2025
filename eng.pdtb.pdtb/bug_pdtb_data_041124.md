# After bug correction

Total number of senses, incl 2nd sense (as part of one label): 130


Distrib type is the same in both data:
explicit 24240
implicit 21827
altlex 1498
altlexc 140
hypophora 146

The same as in the updated annotation manual:

- Explicit
>>> 16908+7332
24240

- Implicit
>>> 6234+15593
21827


Secondary senses DISRPT: {'explicit': 1167, 'implicit': 1075, 'altlex': 33}

Secondary senses PDTB: {'explicit': 1167, 'implicit': 1075, 'altlex': 33}



# Bug correction

## Total number per type: 

### in DISRPT

explicit 24197
implicit 21809
altlex 1496
altlexc 139
hypophora 146

### in original PDTB

explicit 24240
implicit 21827
altlex 1498
altlexc 140
hypophora 146
entrel 5538
norel 287




## Errors: missing instances (all in DEV)

bug probably from the script adding types (missing files are not in the list)

explicit -43
implicit -18
altlex -2
altlexc -1

= 64

### Number of instances missing per file 

File in PDTB not in DISRPT: 2218 MISSING 8
File in PDTB not in DISRPT: 2245 MISSING 1
File in PDTB not in DISRPT: 2246 MISSING 6
File in PDTB not in DISRPT: 2216 MISSING 3
File in PDTB not in DISRPT: 2233 MISSING 6
File in PDTB not in DISRPT: 2219 MISSING 17
File in PDTB not in DISRPT: 2244 MISSING 1
File in PDTB not in DISRPT: 2217 MISSING 1
File in PDTB not in DISRPT: 2215 MISSING 5
File in PDTB not in DISRPT: 2254 MISSING 3
File in PDTB not in DISRPT: 2252 MISSING 3
File in PDTB not in DISRPT: 2208 MISSING 8
File in PDTB not in DISRPT: 2251 MISSING 2
TOTAL MISSING 64

## Manual correction

2208 - ok
2215 - ok 
2216 - ok
2217 - ok
2218 - ok
2219 - ok
2233 - ok
2244 - ok
2245 - ok
2246 - ok
2251 - ok
2252 - ok
2254 - ok

- Add lines from disrpt 23 rel files to the 2024 dev rel file (version with tokens)
- Can't recompute the raw text here, so we remove that info for now (with debug_pdtb_lrec24.py) + add unknown as type for new lines
- Need to add the rel type manually


## Errors: switching explicit / implicit

Count numbers of explicit : implicit in DISRPT data vs orginial PDTB data

0155 explicit 32 33
0155 implicit 31 30
0210 implicit 18 17
0210 explicit 10 11
0296 explicit 37 38
0296 implicit 48 47
0553 implicit 37 36
0553 explicit 47 48
0655 explicit 20 21
0655 implicit 13 12
0799 explicit 19 20
0799 implicit 23 22
0819 implicit 26 25
0819 explicit 33 34
0961 implicit 8 9
0961 explicit 27 26
1457 explicit 26 27
1457 implicit 38 37
1549 implicit 28 27
1549 explicit 23 24
2059 explicit 45 46
2059 implicit 36 35
2125 implicit 17 15
2125 explicit 13 15

### Manual Correction

### 0799
change l.15255, implicit --> explicit expansion.conjunction

--------------------------------------------
	 explicit 19 20
		 comparison.contrast 1
		 temporal.synchronous;contingency.cause.reason 1
		 expansion.disjunction 1
		 comparison.concession.arg2-as-denier 3
		 temporal.asynchronous.succession 1
		 comparison.concession.arg1-as-denier 1
		 temporal.asynchronous.succession;contingency.cause.reason 1
		 contingency.condition.arg2-as-cond 2
		 expansion.conjunction 8 <--

		 comparison.contrast 1
		 temporal.synchronous 1
		 expansion.disjunction 1
		 comparison.concession.arg2-as-denier 3
		 temporal.asynchronous.succession 2
		 comparison.concession.arg1-as-denier 1
		 contingency.condition.arg2-as-cond 2
		 expansion.conjunction 9 <--
--------------------------------------------
	 implicit 23 22
		 contingency.cause.result 3
		 temporal.asynchronous.precedence 3
		 contingency.cause.reason 3
		 expansion.level-of-detail.arg2-as-detail 3
		 expansion.instantiation.arg2-as-instance 2
		 temporal.synchronous;comparison.contrast 2
		 expansion.conjunction 3 <--
		 comparison.concession.arg2-as-denier 2
		 expansion.level-of-detail.arg1-as-detail 1
		 expansion.manner.arg1-as-manner 1

		 contingency.cause.result 3
		 temporal.asynchronous.precedence 3
		 contingency.cause.reason 3
		 expansion.level-of-detail.arg2-as-detail 3
		 expansion.instantiation.arg2-as-instance 2
		 temporal.synchronous 2
		 expansion.conjunction 2 <--
		 comparison.concession.arg2-as-denier 2
		 expansion.manner.arg1-as-manner 1
		 expansion.level-of-detail.arg1-as-detail 1
--------------------------------------------
	 altlex 2 2
		 expansion.substitution.arg1-as-subst 1
		 contingency.cause.reason 1

		 expansion.substitution.arg1-as-subst 1
		 contingency.cause.reason 1
--------------------------------------------
	 altlexc 1 1
		 comparison.similarity 1

		 comparison.similarity 1

### 0819

l. 15656 implicit --> explicit expansion.conjunction

--------------------------------------------
	 implicit 26 25
		 expansion.level-of-detail.arg2-as-detail 5
		 comparison.contrast 1
		 expansion.conjunction 7
		 contingency.cause.result 2
		 contingency.purpose.arg2-as-goal 4
		 temporal.asynchronous.precedence 2
		 temporal.synchronous 3
		 contingency.condition.arg2-as-cond 1
		 comparison.concession.arg2-as-denier 1

		 expansion.level-of-detail.arg2-as-detail 5
		 comparison.contrast 1
		 expansion.conjunction 6
		 contingency.cause.result 2
		 contingency.purpose.arg2-as-goal 4
		 temporal.asynchronous.precedence 2
		 temporal.synchronous 3
		 contingency.condition.arg2-as-cond 1
		 comparison.concession.arg2-as-denier 1
--------------------------------------------
	 explicit 33 34
		 contingency.cause.reason 1
		 expansion.conjunction 7
		 temporal.asynchronous.succession;contingency.cause.reason 1
		 comparison.concession.arg2-as-denier 4
		 temporal.asynchronous.precedence 2
		 temporal.synchronous 9
		 comparison.contrast 2
		 comparison.concession+speechact.arg2-as-denier+speechact 1
		 expansion.substitution.arg2-as-subst 1
		 contingency.condition.arg2-as-cond 2
		 contingency.purpose.arg1-as-goal;expansion.manner.arg2-as-manner 1
		 temporal.asynchronous.succession 1
		 expansion.instantiation.arg2-as-instance 1

		 contingency.cause.reason 1
		 expansion.conjunction 8
		 temporal.asynchronous.succession 2
		 temporal.asynchronous.precedence 2
		 comparison.concession.arg2-as-denier 4
		 temporal.synchronous 9
		 comparison.contrast 2
		 contingency.condition.arg2-as-cond 2
		 expansion.substitution.arg2-as-subst 1
		 comparison.concession+speechact.arg2-as-denier+speechact 1
		 contingency.purpose.arg1-as-goal 1
		 expansion.instantiation.arg2-as-instance 1
--------------------------------------------
	 altlex 3 3
		 expansion.conjunction 1
		 contingency.cause.result 1
		 comparison.contrast 1

		 expansion.conjunction 1
		 contingency.cause.result 1
		 comparison.contrast 1
--------------------------------------------
	 altlexc 1 1
		 comparison.similarity 1

		 comparison.similarity 1

### 0155

l. 3250 implicit --> explicit (2 parts connective) comparison.concession.arg2-as-denier

--------------------------------------------
	 explicit 32 33
		 expansion.conjunction 15
		 comparison.concession.arg1-as-denier 2
		 comparison.contrast 3
		 contingency.purpose.arg2-as-goal 1
		 comparison.concession.arg2-as-denier 2
		 contingency.condition.arg2-as-cond 1
		 contingency.cause.result 1
		 contingency.cause+belief.reason+belief 1
		 expansion.disjunction 1
		 temporal.synchronous 1
		 expansion.level-of-detail.arg2-as-detail 1
		 contingency.cause.reason 1
		 expansion.substitution.arg2-as-subst 1
		 temporal.asynchronous.precedence 1

		 expansion.conjunction 15
		 comparison.concession.arg1-as-denier 2
		 comparison.contrast 3
		 contingency.purpose.arg2-as-goal 1
		 comparison.concession.arg2-as-denier 3
		 contingency.condition.arg2-as-cond 1
		 contingency.cause.result 1
		 contingency.cause+belief.reason+belief 1
		 expansion.disjunction 1
		 temporal.synchronous 1
		 expansion.level-of-detail.arg2-as-detail 1
		 contingency.cause.reason 1
		 expansion.substitution.arg2-as-subst 1
		 temporal.asynchronous.precedence 1
--------------------------------------------
	 implicit 31 30
		 temporal.synchronous;comparison.contrast 3
		 contingency.cause.result 3
		 temporal.synchronous 1
		 contingency.cause.reason 3
		 expansion.instantiation.arg2-as-instance 7
		 expansion.level-of-detail.arg2-as-detail 4
		 comparison.concession.arg2-as-denier 2
		 contingency.purpose.arg2-as-goal 2
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 2
		 expansion.conjunction 3
		 expansion.substitution.arg2-as-subst 1

		 temporal.synchronous 4
		 contingency.cause.result 3
		 contingency.cause.reason 3
		 expansion.instantiation.arg2-as-instance 7
		 expansion.level-of-detail.arg2-as-detail 4
		 comparison.concession.arg2-as-denier 1
		 contingency.purpose.arg2-as-goal 4
		 expansion.conjunction 3
		 expansion.substitution.arg2-as-subst 1
--------------------------------------------
	 altlex 1 1
		 contingency.cause.reason 1

		 contingency.cause.reason 1

### 2059

l. 40417 implicit --> explicit (conn not only but) expansion.conjunction

--------------------------------------------
	 explicit 45 46
		 comparison.concession.arg2-as-denier 7
		 expansion.conjunction 10
		 comparison.concession.arg1-as-denier 4
		 expansion.level-of-detail.arg2-as-detail 1
		 expansion.instantiation.arg2-as-instance 2
		 contingency.purpose.arg2-as-goal 1
		 expansion.disjunction 1
		 temporal.asynchronous.precedence 4
		 contingency.condition.arg2-as-cond 6
		 temporal.asynchronous.succession 1
		 contingency.cause.reason 2
		 comparison.contrast 1
		 contingency.cause.result 2
		 temporal.synchronous 1
		 contingency.purpose.arg1-as-goal;expansion.manner.arg2-as-manner 1
		 contingency.cause.reason;expansion.manner.arg2-as-manner 1

		 expansion.conjunction 11
		 comparison.concession.arg2-as-denier 7
		 comparison.concession.arg1-as-denier 4
		 expansion.level-of-detail.arg2-as-detail 1
		 expansion.instantiation.arg2-as-instance 2
		 contingency.purpose.arg2-as-goal 1
		 expansion.disjunction 1
		 temporal.asynchronous.precedence 4
		 contingency.condition.arg2-as-cond 6
		 temporal.asynchronous.succession 1
		 contingency.cause.reason 3
		 comparison.contrast 1
		 contingency.cause.result 2
		 temporal.synchronous 1
		 contingency.purpose.arg1-as-goal 1
--------------------------------------------
	 implicit 36 35
		 expansion.instantiation.arg2-as-instance 2
		 comparison.concession.arg2-as-denier 1
		 contingency.purpose.arg2-as-goal 4
		 temporal.asynchronous.precedence 5
		 contingency.cause.result 6
		 temporal.asynchronous.succession 1
		 expansion.conjunction 3
		 contingency.cause.result;temporal.asynchronous.precedence 1
		 expansion.level-of-detail.arg2-as-detail 7
		 contingency.cause.reason 2
		 expansion.equivalence 2
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 1
		 comparison.contrast 1

		 expansion.instantiation.arg2-as-instance 2
		 comparison.concession.arg2-as-denier 1
		 contingency.purpose.arg2-as-goal 5
		 temporal.asynchronous.precedence 5
		 temporal.asynchronous.succession 1
		 contingency.cause.result 7
		 expansion.conjunction 2
		 expansion.level-of-detail.arg2-as-detail 7
		 contingency.cause.reason 2
		 expansion.equivalence 2
		 comparison.contrast 1
--------------------------------------------
	 hypophora 1 1
		 hypophora 1

		  1
--------------------------------------------
	 altlex 3 3
		 expansion.level-of-detail.arg2-as-detail 1
		 contingency.condition.arg1-as-cond 1
		 contingency.cause.result 1

		 expansion.level-of-detail.arg2-as-detail 1
		 contingency.condition.arg1-as-cond 1
		 contingency.cause.result 1
--------------------------------------------
	 altlexc 1 1
		 contingency.condition.arg2-as-cond 1

		 contingency.condition.arg2-as-cond 1

### 1457

l. 27799 implicit --> explicit (on the one hand on the other) comparison.contrast

--------------------------------------------
	 explicit 26 27
		 temporal.synchronous 2
		 contingency.cause.reason 2
		 comparison.concession.arg2-as-denier 9
		 expansion.conjunction 9
		 contingency.purpose.arg2-as-goal 1
		 temporal.asynchronous.succession 2
		 temporal.asynchronous.precedence 1

		 temporal.synchronous 2
		 contingency.cause.reason 2
		 comparison.concession.arg2-as-denier 9
		 expansion.conjunction 9
		 contingency.purpose.arg2-as-goal 1
		 comparison.contrast 1
		 temporal.asynchronous.succession 2
		 temporal.asynchronous.precedence 1
--------------------------------------------
	 altlexc 1 1
		 contingency.condition.arg2-as-cond 1

		 contingency.condition.arg2-as-cond 1
--------------------------------------------
	 implicit 38 37
		 contingency.cause.result 5
		 comparison.contrast 2
		 contingency.cause+belief.result+belief 1
		 comparison.concession.arg2-as-denier 4
		 contingency.cause.reason 2
		 expansion.equivalence 2
		 contingency.condition.arg2-as-cond 1
		 contingency.purpose.arg2-as-goal 1
		 expansion.instantiation.arg2-as-instance 2
		 expansion.conjunction 6
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 2
		 expansion.level-of-detail.arg2-as-detail 5
		 temporal.asynchronous.precedence 2
		 temporal.asynchronous.succession 1
		 temporal.synchronous 1
		 contingency.cause+belief.reason+belief 1

		 contingency.cause.result 5
		 comparison.contrast 1
		 contingency.cause+belief.result+belief 1
		 comparison.concession.arg2-as-denier 4
		 expansion.equivalence 2
		 contingency.cause.reason 2
		 contingency.condition.arg2-as-cond 1
		 contingency.purpose.arg2-as-goal 3
		 expansion.instantiation.arg2-as-instance 2
		 expansion.conjunction 6
		 expansion.level-of-detail.arg2-as-detail 5
		 temporal.asynchronous.precedence 2
		 temporal.asynchronous.succession 1
		 temporal.synchronous 1
		 contingency.cause+belief.reason+belief 1
--------------------------------------------
	 hypophora 1 1
		 hypophora 1

		  1

### 2125

l. 41615 implicit -> explicit expansion.conjunction (not only but)
l. 41627 implicit -> explicit expansion.disjunction (either or)

--------------------------------------------
	 implicit 17 15
		 expansion.instantiation.arg2-as-instance 1
		 contingency.cause+belief.result+belief 2
		 contingency.cause.reason 5
		 comparison.concession.arg2-as-denier 2
		 contingency.cause.result 2
		 expansion.conjunction 1
		 expansion.level-of-detail.arg1-as-detail 1
		 temporal.asynchronous.precedence 1
		 expansion.equivalence 1
		 expansion.disjunction 1

		 expansion.instantiation.arg2-as-instance 1
		 contingency.cause+belief.result+belief 2
		 contingency.cause.reason 5
		 comparison.concession.arg2-as-denier 2
		 contingency.cause.result 2
		 expansion.level-of-detail.arg1-as-detail 1
		 temporal.asynchronous.precedence 1
		 expansion.equivalence 1
--------------------------------------------
	 explicit 13 15
		 comparison.concession.arg2-as-denier 5
		 contingency.cause.reason 1
		 expansion.conjunction 5
		 temporal.synchronous 1
		 contingency.condition.arg2-as-cond 1

		 comparison.concession.arg2-as-denier 5
		 contingency.cause.reason 1
		 expansion.conjunction 6
		 temporal.synchronous 1
		 contingency.condition.arg2-as-cond 1
		 expansion.disjunction 1

### 0553

l. 10090 implict --> explicit (not only but also) expansion.conjunction

--------------------------------------------
	 implicit 37 36
		 contingency.cause.reason 5
		 expansion.instantiation.arg2-as-instance 1
		 contingency.cause.result 7
		 expansion.level-of-detail.arg2-as-detail 3
		 expansion.conjunction 8
		 contingency.cause+belief.reason+belief 2
		 comparison.contrast 1
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 2
		 contingency.purpose.arg2-as-goal 1
		 expansion.manner.arg1-as-manner 1
		 temporal.synchronous 1
		 contingency.cause+belief.result+belief 1
		 expansion.disjunction 1
		 expansion.equivalence 1
		 expansion.substitution.arg2-as-subst 1
		 comparison.concession.arg2-as-denier 1

		 contingency.cause.reason 5
		 expansion.instantiation.arg2-as-instance 1
		 contingency.cause.result 7
		 expansion.level-of-detail.arg2-as-detail 3
		 expansion.conjunction 7
		 contingency.cause+belief.reason+belief 2
		 comparison.contrast 1
		 contingency.purpose.arg2-as-goal 3
		 expansion.manner.arg1-as-manner 1
		 temporal.synchronous 1
		 contingency.cause+belief.result+belief 1
		 expansion.disjunction 1
		 expansion.equivalence 1
		 expansion.substitution.arg2-as-subst 1
		 comparison.concession.arg2-as-denier 1
--------------------------------------------
	 explicit 47 48
		 comparison.concession.arg2-as-denier 6
		 comparison.contrast 2
		 expansion.conjunction 19
		 expansion.instantiation.arg2-as-instance 2
		 contingency.condition.arg2-as-cond;expansion.level-of-detail.arg2-as-detail 1
		 expansion.manner.arg2-as-manner 1
		 contingency.purpose.arg1-as-goal;expansion.manner.arg2-as-manner 3
		 comparison.concession.arg1-as-denier 2
		 expansion.disjunction 1
		 contingency.cause.result 2
		 temporal.asynchronous.precedence 1
		 temporal.synchronous 1
		 contingency.condition.arg2-as-cond 1
		 expansion.equivalence 1
		 contingency.cause.reason 1
		 expansion.level-of-detail.arg2-as-detail 2
		 expansion.substitution.arg1-as-subst 1

		 expansion.instantiation.arg2-as-instance 2
		 expansion.conjunction 20
		 comparison.contrast 2
		 comparison.concession.arg2-as-denier 6
		 contingency.condition.arg2-as-cond 2
		 expansion.manner.arg2-as-manner 1
		 contingency.purpose.arg1-as-goal 3
		 comparison.concession.arg1-as-denier 2
		 expansion.disjunction 1
		 contingency.cause.result 2
		 temporal.asynchronous.precedence 1
		 temporal.synchronous 1
		 expansion.equivalence 1
		 contingency.cause.reason 1
		 expansion.substitution.arg1-as-subst 1
		 expansion.level-of-detail.arg2-as-detail 2
--------------------------------------------
	 altlex 8 8
		 contingency.cause.result 5
		 expansion.instantiation.arg2-as-instance 1
		 expansion.substitution.arg1-as-subst 1
		 expansion.level-of-detail.arg2-as-detail 1

		 contingency.cause.result 5
		 expansion.instantiation.arg2-as-instance 1
		 expansion.substitution.arg1-as-subst 1
		 expansion.level-of-detail.arg2-as-detail 1

### 0210

l.3884 implicit --> explicit (not only) expansion.conjunction 

--------------------------------------------
	 implicit 18 17
		 expansion.level-of-detail.arg2-as-detail 5
		 expansion.conjunction 1
		 comparison.concession.arg2-as-denier 2
		 contingency.cause.reason 4
		 contingency.purpose.arg2-as-goal 1
		 contingency.cause.result 4
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 1

		 expansion.level-of-detail.arg2-as-detail 5
		 contingency.cause.reason 4
		 comparison.concession.arg2-as-denier 2
		 contingency.purpose.arg2-as-goal 2
		 contingency.cause.result 4
--------------------------------------------
	 altlex 3 3
		 contingency.cause.result 3

		 contingency.cause.result 3
--------------------------------------------
	 explicit 10 11
		 contingency.condition.arg2-as-cond 1
		 comparison.concession.arg2-as-denier 1
		 contingency.cause.reason 1
		 expansion.conjunction 6
		 temporal.synchronous 1

		 expansion.conjunction 7
		 contingency.condition.arg2-as-cond 1
		 comparison.concession.arg2-as-denier 1
		 contingency.cause.reason 1
		 temporal.synchronous 1

### 0296

l. 5592 implicit -> explicit contingency.condition.arg2-as-cond (if then)

--------------------------------------------
	 explicit 37 38
		 comparison.concession.arg2-as-denier 7
		 expansion.conjunction 14
		 contingency.cause.reason 3
		 comparison.contrast 1
		 comparison.concession.arg1-as-denier 1
		 contingency.condition.arg2-as-cond 1
		 contingency.purpose.arg2-as-goal 1
		 expansion.instantiation.arg2-as-instance 1
		 expansion.manner.arg2-as-manner 2
		 temporal.synchronous 4
		 temporal.asynchronous.precedence 2

		 comparison.concession.arg2-as-denier 7
		 expansion.conjunction 14
		 contingency.cause.reason 3
		 comparison.contrast 1
		 comparison.concession.arg1-as-denier 1
		 contingency.condition.arg2-as-cond 2
		 contingency.purpose.arg2-as-goal 1
		 expansion.instantiation.arg2-as-instance 1
		 expansion.manner.arg2-as-manner 2
		 temporal.synchronous 4
		 temporal.asynchronous.precedence 2
--------------------------------------------
	 implicit 48 47
		 expansion.substitution.arg2-as-subst 1
		 expansion.conjunction 8
		 contingency.cause.reason 8
		 comparison.contrast 4
		 contingency.cause.result 5
		 contingency.cause+belief.result+belief 1
		 expansion.instantiation.arg2-as-instance 1
		 expansion.level-of-detail.arg2-as-detail 4
		 temporal.asynchronous.succession 4
		 comparison.concession.arg2-as-denier 3
		 contingency.condition.arg2-as-cond 1
		 expansion.equivalence 6
		 expansion.disjunction 1
		 temporal.asynchronous.precedence;contingency.cause.result 1

		 expansion.substitution.arg2-as-subst 1
		 expansion.conjunction 8
		 contingency.cause.reason 8
		 comparison.contrast 4
		 contingency.cause.result 5
		 contingency.cause+belief.result+belief 1
		 expansion.instantiation.arg2-as-instance 1
		 expansion.level-of-detail.arg2-as-detail 4
		 temporal.asynchronous.succession 4
		 comparison.concession.arg2-as-denier 3
		 expansion.equivalence 6
		 expansion.disjunction 1
		 temporal.asynchronous.precedence 1
--------------------------------------------
	 altlex 2 2
		 expansion.equivalence 1
		 contingency.cause.result 1

		 expansion.equivalence 1
		 contingency.cause.result 1
--------------------------------------------
	 hypophora 2 2
		 hypophora 2

		  2

### 1549

l. 29137 implicit -> explicit expansion.conjunction (not only but also)

--------------------------------------------
	 implicit 28 27
		 contingency.cause.reason 4
		 comparison.concession.arg2-as-denier 1
		 expansion.level-of-detail.arg2-as-detail 3
		 expansion.conjunction 7
		 expansion.instantiation.arg2-as-instance 6
		 contingency.purpose.arg2-as-goal 2
		 temporal.asynchronous.precedence 2
		 expansion.substitution.arg2-as-subst 1
		 contingency.condition.arg2-as-cond 1
		 temporal.synchronous 1

		 contingency.cause.reason 4
		 comparison.concession.arg2-as-denier 1
		 expansion.level-of-detail.arg2-as-detail 3
		 expansion.conjunction 6
		 expansion.instantiation.arg2-as-instance 6
		 contingency.purpose.arg2-as-goal 2
		 temporal.asynchronous.precedence 2
		 expansion.substitution.arg2-as-subst 1
		 contingency.condition.arg2-as-cond 1
		 temporal.synchronous 1
--------------------------------------------
	 explicit 23 24
		 temporal.asynchronous.precedence 2
		 comparison.concession.arg2-as-denier 6
		 temporal.synchronous 1
		 expansion.conjunction 5
		 temporal.asynchronous.succession 1
		 comparison.concession.arg1-as-denier 2
		 expansion.level-of-detail.arg2-as-detail 1
		 contingency.purpose.arg2-as-goal 1
		 contingency.condition.arg2-as-cond 1
		 expansion.disjunction 1
		 contingency.cause.reason 2

		 temporal.asynchronous.precedence 2
		 temporal.synchronous 1
		 comparison.concession.arg2-as-denier 6
		 expansion.conjunction 6
		 temporal.asynchronous.succession 1
		 comparison.concession.arg1-as-denier 2
		 expansion.level-of-detail.arg2-as-detail 1
		 contingency.purpose.arg2-as-goal 1
		 contingency.condition.arg2-as-cond 1
		 expansion.disjunction 1
		 contingency.cause.reason 2
--------------------------------------------
	 altlex 1 1
		 expansion.equivalence 1

		 expansion.equivalence 1

### 0655

l. 12349 implicit -> explicit expansion.conjunction (not only)

--------------------------------------------
	 explicit 20 21
		 expansion.conjunction 6
		 comparison.concession.arg2-as-denier 2
		 contingency.condition.arg2-as-cond 3
		 temporal.synchronous 3
		 comparison.concession.arg1-as-denier 2
		 temporal.synchronous;comparison.concession.arg1-as-denier 1
		 temporal.asynchronous.succession;contingency.cause.reason 1
		 expansion.substitution.arg2-as-subst 1
		 expansion.manner.arg2-as-manner 1

		 expansion.conjunction 7
		 contingency.condition.arg2-as-cond 3
		 comparison.concession.arg2-as-denier 2
		 temporal.synchronous 4
		 comparison.concession.arg1-as-denier 2
		 temporal.asynchronous.succession 1
		 expansion.substitution.arg2-as-subst 1
		 expansion.manner.arg2-as-manner 1
--------------------------------------------
	 implicit 13 12
		 expansion.substitution.arg2-as-subst;expansion.manner.arg2-as-manner 1
		 temporal.asynchronous.precedence 2
		 expansion.conjunction 3
		 expansion.level-of-detail.arg2-as-detail 2
		 contingency.purpose.arg2-as-goal 1
		 contingency.cause.reason 1
		 expansion.instantiation.arg2-as-instance 2
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 1

		 expansion.substitution.arg2-as-subst 1
		 temporal.asynchronous.precedence 2
		 expansion.conjunction 2
		 expansion.level-of-detail.arg2-as-detail 2
		 contingency.purpose.arg2-as-goal 2
		 contingency.cause.reason 1
		 expansion.instantiation.arg2-as-instance 2
--------------------------------------------
	 altlex 1 1
		 expansion.conjunction 1

		 expansion.conjunction 1

### 0961

l. 16690 explicit -> implicit comparison.concession.arg2-as-denier ==> TODO strange overlapping of args, TO CHECK

--------------------------------------------
	 implicit 8 9
		 comparison.concession.arg2-as-denier 4
		 expansion.conjunction 1
		 contingency.purpose.arg2-as-goal;expansion.manner.arg1-as-manner 2
		 expansion.level-of-detail.arg2-as-detail 1

		 comparison.concession.arg2-as-denier 5
		 expansion.conjunction 1
		 contingency.purpose.arg2-as-goal 2
		 expansion.level-of-detail.arg2-as-detail 1
--------------------------------------------
	 explicit 27 26
		 expansion.manner.arg2-as-manner 2
		 comparison.concession.arg2-as-denier 7
		 expansion.conjunction 9
		 expansion.equivalence 1
		 temporal.asynchronous.precedence 2
		 contingency.negative-condition.arg2-as-negcond 1
		 expansion.substitution.arg2-as-subst 1
		 contingency.cause.reason 1
		 comparison.concession.arg1-as-denier 2
		 contingency.condition.arg2-as-cond 1

		 expansion.manner.arg2-as-manner 2
		 comparison.concession.arg2-as-denier 6
		 expansion.conjunction 9
		 expansion.equivalence 1
		 temporal.asynchronous.precedence 2
		 contingency.negative-condition.arg2-as-negcond 1
		 expansion.substitution.arg2-as-subst 1
		 contingency.cause.reason 1
		 comparison.concession.arg1-as-denier 2
		 contingency.condition.arg2-as-cond 1
--------------------------------------------
	 altlex 1 1
		 contingency.cause.result 1

		 contingency.cause.result 1

