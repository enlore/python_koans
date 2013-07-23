#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    score = 0
    if len(dice) is 0:
        return score

    if len(dice) is 1:
        if dice[0] is 5:
            score = 50
        if dice[0] is 1:
            score = 100
        return score
   
    occurance_count = {}
    if len(dice) is not 0:
        for die in dice:
            if occurance_count.has_key(die):
                occurance_count[die] += 1
            else:
                occurance_count[die] = 1

        # iter over occ counts for each digit
        # for one and five, if count is less than three, score accordingly
        # for everything else, diminish count by threes, incrementing score
        # per chunk accordingly
        for key, val in occurance_count.items():
            if key is 1: 
                count = val / 3
                rem = val % 3
                score += 1000 * count
                score += 100 * rem 

            elif key is 5:
                count = val / 3
                rem = val % 3
                score += 500 * count
                score += 50 * rem 

            else: 
                if val % 3 is 0:
                    count = val / 3
                    score += (100 * key) * count

        return score

class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))
    
    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))
    
    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))
    
    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1, 5, 5, 1]))
    
    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2, 3, 4, 6]))
    
    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1, 1, 1]))
    
    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2, 2, 2]))
        self.assertEqual(300, score([3, 3, 3]))
        self.assertEqual(400, score([4, 4, 4]))
        self.assertEqual(500, score([5, 5, 5]))
        self.assertEqual(600, score([6, 6, 6]))
        self.assertEqual(600, score([3,3,3,3,3,3]))
        self.assertEqual(1200, score([4,4,4,4,4,4,4,4,4]))
        
    
    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2, 5, 2, 2, 3]))
        self.assertEqual(550, score([5, 5, 5, 5]))
        self.assertEqual(1150, score([1, 1, 1, 5, 1]))
        
    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1, 2, 2, 2]))
        self.assertEqual(350, score([1, 5, 2, 2, 2]))
