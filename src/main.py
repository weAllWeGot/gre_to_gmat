import warnings
from data_table import score_table
from constants import MAX_GRE, MIN_GRE, BAD_INPUT_RETURN


def validate_score_input(v,q):
	try:
		verbal = int(v)
	except:
		warnings.warn("Was not able to parse verbal score: {}\nReturning {}".format(v,BAD_INPUT_RETURN))
		return BAD_INPUT_RETURN,BAD_INPUT_RETURN
	try:
		quant = int(q)
	except:
		warnings.warn("Was not able to parse quant score: {}\nReturning {}".format(q,BAD_INPUT_RETURN))
		return BAD_INPUT_RETURN, BAD_INPUT_RETURN

	if verbal > 170 or verbal < 130:
		warnings.warn("Verbal score: {} is not between {} and {}\nReturning {}".format(verbal,MIN_SCORE,MAX_SCORE,BAD_INPUT_RETURN))
		return BAD_INPUT_RETURN, BAD_INPUT_RETURN

	if quant > 170 or quant < 130:
		warnings.warn("Quant score: {} is not between {} and {}\nReturning {}".format(quant,MIN_SCORE,MAX_SCORE,BAD_INPUT_RETURN))
		return BAD_INPUT_RETURN, BAD_INPUT_RETURN

	return verbal, quant

def gre2gmat(gre_verbal,gre_quant):
	"""
	:param gre_verbal: Numeric representation of verbal GRE score
	:type verbal: int

	:param gre_quant: Numeric representation of quantitative GRE score
	:type quant: int

	:return: Predicted GMAT score
	:rtype: int
	"""
	v,q = validate_score_input(gre_verbal,gre_quant)
	if v == BAD_INPUT_RETURN or q == BAD_INPUT_RETURN:
		return BAD_INPUT_RETURN
	else:
		return score_table.loc[q,v]


def rough_gre2gmat(v,q):
   print -2080.75 + (6.38 * v) + (10.62 * q)
  
def rougher_gre2gmat(v,q):
  print (v+q)*2.019