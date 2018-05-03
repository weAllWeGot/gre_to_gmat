import unittest

from src.main import validate_score_input,gre2gmat
from src.constants import MAX_GRE, MIN_GRE, BAD_INPUT_RETURN, MIN_GMAT, MAX_GMAT

class TestScoreCalculation(unittest.TestCase):

	def setUp(self):
		pass

	def test_sanity_check(self):
		ranges = range(MIN_GRE,MAX_GRE,2)
		for v in ranges:
			for q in ranges:
				gmat = gre2gmat(gre_verbal=v,gre_quant=q)

				self.assertTrue(gmat >= MIN_GMAT and gmat <= MAX_GMAT,"GMAT Score: {} not between {} and {}".format(gmat,MIN_GMAT,MAX_GMAT))


if __name__ == '__main__':
    unittest.main()