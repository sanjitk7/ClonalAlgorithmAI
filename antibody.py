from util import create_uuid

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

class Antibody:
    def __init__(self,data = []):
        self.__id = create_uuid()
        self.__t_id = data[0]
        self.__indiscriminate_purchase = data[1]
        self.__purchase_total_realative_score = data[2]
        self.__expensive_items_score = data[3]
        self.__card_present_status = data[4]
        self.__is_swipe_or_chip = data[5]
        self.__is_sign_or_pin = data[6]
        self.__freq_recent_purchase_score = data[7]
        self.__easy_resale_items_score = data[8]
        self.__geodist_deviation_factor = data[9]
        self.__known_ip = data[10]
        self.__known_mac = data[11]
        self.__time_abnormality_score = data[12]
        self.__geodist_ship_deviation = data[13]
        self.__known_browser = data[14]

    def get_t_id(self):
        return self.__t_id

    def get_indiscriminate_purchase(self):
        return self.__indiscriminate_purchase

    def get_purchase_total_realative_score(self):
        return self.__purchase_total_realative_score

    def get_expensive_items_score(self):
        return self.__expensive_items_score

    def get_card_present_status(self):
        return self.__card_present_status
    
    def get_is_swipe_or_chip(self):
        return self.__is_swipe_or_chip
    
    def get_is_sign_or_pin(self):
        return self.__is_sign_or_pin
    
    def get_freq_recent_purchase_score(self):
        return self.__freq_recent_purchase_score

    def get_easy_resale_items_score(self):
        return self.__easy_resale_items_score

    def get_geodist_deviation_factor(self):
        return self.__geodist_deviation_factor

    def get_known_ip(self):
        return self.__known_ip

    def get_known_mac(self):
        return self.__known_mac

    def get_time_abnormality_score(self):
        return self.__time_abnormality_score

    def get_geodist_ship_deviation(self):
        return self.__geodist_ship_deviation

    def get_known_browser(self):
        return self.__known_browser

    def get_properties_as_list(self):
        ls = []
        ls.append(self.__t_id)
        ls.append(self.__indiscriminate_purchase)
        ls.append(self.__purchase_total_realative_score)
        ls.append(self.__expensive_items_score)
        ls.append(self.__card_present_status)
        ls.append(self.__is_swipe_or_chip)
        ls.append(self.__is_sign_or_pin)
        ls.append(self.__freq_recent_purchase_score)
        ls.append(self.__easy_resale_items_score)
        ls.append(self.__geodist_deviation_factor)
        ls.append(self.__known_ip)
        ls.append(self.__known_mac)
        ls.append(self.__time_abnormality_score)
        ls.append(self.__geodist_ship_deviation)
        ls.append(self.__known_browser)
        return ls




