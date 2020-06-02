import unittest
from clonalScript import instantiate_population,makeAbSortPool
from antibody import Antibody
from affinity import affinity
from mutation import mutateOneAb

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
        ab1 = Antibody([11,20,30,15,1,1,1,60,50,1,1,1,10,1,1,1])
        self.assertEqual(affinity(ab1,ab1,"cosine"),0)
        
    def test_antibody(self):
        ab1 = Antibody([11,20,30,15,1,1,1,60,50,1,1,1,10,1,1,-1])
        self.assertEqual(ab1.get_t_id(),11)
        self.assertEqual(ab1.get_indiscriminate_purchase(),20)
        self.assertEqual(ab1.get_purchase_total_relative_score(),30)
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
        self.assertEqual(ab1.get_fraud_label(),-1)

    def test_instantiate(self):
        populationPool = [[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1,-1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0,1]]
        objList = instantiate_population(populationPool)
        for i in range(len(populationPool)):
            self.assertEqual(objList[i].get_properties_as_list_with_label(),populationPool[i])

    def test_indisctiminatePurchase(self):
        ab1 = Antibody([11,20,30,15,1,1,1,60,50,1,1,1,10,1,1,1])
        ab1.indiscriminate_purchase = 0
        self.assertEqual(ab1.indiscriminate_purchase,0)

    def test_makeAbSortPool(self):
        cellList = [Antibody([1, 10, 1, 2, 0, 0, 0, 1, 5, 30, 1, 0, 1, 10, 1,-1]),Antibody([2, 22, 5, 4, 0, 0, 0, 1, 10, 20, 0, 0, 1, 20, 0,-1]),Antibody([3, 33, 12, 1, 1, 0, 1, 90, 12, 1, 1, 1, 23, 1, 1,-1])]
        expected = [cellList[0],cellList[1],cellList[2]]
        print("expected:",expected)
        affinityList = [0.1,0.2,0.3]
        self.assertEqual(makeAbSortPool(affinityList,cellList),expected)

    def test_get_set_attr(self):
        cell = Antibody([1, 10, 1, 2, 0, 0, 0, 1, 5, 30, 1, 0, 1, 10, 1,-1])
        numAttr = cell.get_all_numeric()
        boolAttr = cell.get_all_boolean()
        self.assertEqual(numAttr,[10,1,2,1,5,30,1,10])
        self.assertEqual(boolAttr,[0,0,0,1,0,1])
        numAttrToSet = [20,2,3,4,10,40,23,95]
        cell.set_all_numeric(numAttrToSet)
        self.assertEqual(cell.get_properties_as_list_with_label(),[1, 20, 2, 3, 0, 0, 0, 4, 10, 40, 1, 0, 23, 95, 1,-1])
        boolAttrToSet = [1,1,1,1,0,1]
        cell.set_all_boolean(boolAttrToSet)
        self.assertEqual(cell.get_properties_as_list_with_label(),[1, 20, 2, 3, 1, 1, 1, 4, 10, 40, 1, 0, 23, 95, 1,-1])

if (__name__=="__main__"):
    unittest.main()