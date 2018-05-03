import unittest

from src.main import _validate_score_input,gre2gmat,rough_gre2gmat,rougher_gre2gmat
from src.constants import MAX_GRE, MIN_GRE, BAD_INPUT_RETURN, MIN_GMAT, MAX_GMAT

class TestScoreCalculation(unittest.TestCase):

	def setUp(self):
		pass

	def test_sanity_check_gre2gmat(self):
		ranges = range(MIN_GRE,MAX_GRE)
		for v in ranges:
			for q in ranges:
				gmat = gre2gmat(gre_verbal=v,gre_quant=q)

				self.assertTrue(gmat >= MIN_GMAT and gmat <= MAX_GMAT,
					"GMAT Score: {} from verbal: {} and quant: {}\nnot between {} and {}".format(
						gmat,v,q,MIN_GMAT,MAX_GMAT))


	def test_sanity_check_rough_gre2gmat(self):
		ranges = range(MIN_GRE,MAX_GRE)
		for v in ranges:
			for q in ranges:
				gmat = rough_gre2gmat(gre_verbal=v,gre_quant=q)

				self.assertTrue(gmat >= MIN_GMAT and gmat <= MAX_GMAT,
					"GMAT Score: {} not between {} and {}".format(
						gmat,MIN_GMAT,MAX_GMAT))


	def test_sanity_check_rougher_gre2gmat(self):
		ranges = range(MIN_GRE,MAX_GRE)
		for v in ranges:
			for q in ranges:
				gmat = rougher_gre2gmat(gre_verbal=v,gre_quant=q)

				self.assertTrue(gmat >= MIN_GMAT and gmat <= MAX_GMAT,
					"GMAT Score: {} not between {} and {}".format(
						gmat,MIN_GMAT,MAX_GMAT))

	def test_validate_quant_score_too_high(self):
		_,q = _validate_score_input(v=MAX_GRE-1,q=MAX_GRE+1)
		self.assertEquals(q,BAD_INPUT_RETURN)

	def test_validate_quant_score_too_low(self):
		_,q = _validate_score_input(v=MAX_GRE-1,q=MIN_GRE-1)
		self.assertEquals(q,BAD_INPUT_RETURN)

	def test_validate_verbal_score_too_high(self):
		v,_ = _validate_score_input(v=MAX_GRE+1,q=MAX_GRE-1)
		self.assertEquals(v,BAD_INPUT_RETURN)

	def test_validate_verbal_score_too_low(self):
		v,_ = _validate_score_input(v=MIN_GRE-1,q=MAX_GRE-1)
		self.assertEquals(v,BAD_INPUT_RETURN)

	def test_non_parseable_verbal(self):
		v,_ = _validate_score_input(v='Kellogg',q=MAX_GRE-1)
		self.assertEquals(v,BAD_INPUT_RETURN)

	def test_non_parseable_quant(self):
		_,q = _validate_score_input(v=MAX_GRE-1,q='Ross')
		self.assertEquals(q,BAD_INPUT_RETURN)




if __name__ == '__main__':
    unittest.main()