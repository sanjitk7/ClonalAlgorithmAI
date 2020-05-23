import unittest
from clonalScript import affinity,instantiate_population
from antibody import Antibody

# t_id
# indiscriminate_purchase
# purchase_total_realative_score
# expensive_items_score
# card_present_status
# is_swipe_or_chip
# is_sign_or_pin
# freq_recent_purchase_score
# easy_resale_items_score
# geodist_deviation_factor
# known_ip
# known_mac
# time_abnormality_score
# geodist_ship_deviation
# known_browser

class TestClonalAlgorithm(unittest.TestCase):
    def test_affinity(self):
        self.assertEqual(affinity([1,1],[1,1],1),0)
    def test_antibody(self):
        ab1 = Antibody([11,20,30,15,1,1,1,60,50,1,1,1,10,1,1])
        self.assertEqual(ab1.get_t_id(),11)
        self.assertEqual(ab1.get_indiscriminate_purchase(),20)
        self.assertEqual(ab1.get_purchase_total_realative_score(),30)
        self.assertEqual(ab1.get_expensive_items_score(),15)
        self.assertEqual(ab1.get_card_present_status(),1)
        self.assertEqual(ab1.get_is_swipe_or_chip(),1)
        self.assertEqual(ab1.get_is_sign_or_pin(),1)
        self.assertEqual(ab1.get_freq_recent_purchase_score(),60)
        self.assertEqual(ab1.get_easy_resale_items_score(),50)
        self.assertEqual(ab1.get_geodist_deviation_factor(),1)
        self.assertEqual(ab1.get_known_ip(),1)
        self.assertEqual(ab1.get_known_mac(),1)
        self.assertEqual(ab1.get_time_abnormality_score(),10)
        self.assertEqual(ab1.get_geodist_ship_deviation(),1)
        self.assertEqual(ab1.get_known_browser(),1)
    def test_instantiate(self):
        populationPool = [[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0]]
        objList = instantiate_population(populationPool)
        for i in range(len(populationPool)):
            self.assertEqual(objList[i].get_properties_as_list(),populationPool[i])
        # self.assertEqual(instantiate_antibody_population([[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0]]))

if (__name__=="__main__"):
    unittest.main()