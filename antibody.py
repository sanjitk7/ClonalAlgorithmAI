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
        self.__purchase_total_relative_score = data[2]
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

    def get_id(self):
        return self.__id

    def get_t_id(self):
        return self.__t_id

    def get_indiscriminate_purchase(self):
        return self.__indiscriminate_purchase

    def get_purchase_total_relative_score(self):
        return self.__purchase_total_relative_score

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
        ls.append(self.__purchase_total_relative_score)
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

    def set_id(self,value):
        self.__id = value
    id  = property(get_id, set_id)

    def set_indiscriminate_purchase(self,value):
        self.__indiscriminate_purchase = value
    indiscriminate_purchase  = property(get_indiscriminate_purchase, set_indiscriminate_purchase)

    def set_purchase_total_relative_score(self,value):
        self.__purchase_total_relative_score = value
    purchase_total_relative_score  = property(get_purchase_total_relative_score, set_purchase_total_relative_score)

    def set_expensive_items_score(self,value):
        self.__expensive_items_score = value
    expensive_items_score  = property(get_expensive_items_score, set_expensive_items_score)

    def set_card_present_status(self,value):
        self.__card_present_status = value
    card_present_status  = property(get_card_present_status, set_card_present_status)

    def set_is_swipe_or_chip(self,value):
        self.__is_swipe_or_chip = value
    is_swipe_or_chip  = property(get_is_swipe_or_chip, set_is_swipe_or_chip)

    def set_is_sign_or_pin(self,value):
        self.__is_sign_or_pin = value
    is_sign_or_pin  = property(get_is_sign_or_pin, set_is_sign_or_pin)

    def set_freq_recent_purchase_score(self,value):
        self.__freq_recent_purchase_score = value
    freq_recent_purchase_score  = property(get_freq_recent_purchase_score, set_freq_recent_purchase_score)

    def set_easy_resale_items_score(self,value):
        self.__easy_resale_items_score = value
    easy_resale_items_score  = property(get_easy_resale_items_score, set_easy_resale_items_score)

    def set_geodist_deviation_factor(self,value):
        self.__geodist_deviation_factor = value
    geodist_deviation_factor  = property(get_geodist_deviation_factor, set_geodist_deviation_factor)

    def set_known_ip(self,value):
        self.__known_ip = value
    known_ip  = property(get_known_ip, set_known_ip)

    def set_known_mac(self,value):
        self.__known_mac = value
    known_mac  = property(get_known_mac, set_known_mac)

    def set_time_abnormality_score(self,value):
        self.__time_abnormality_score = value
    time_abnormality_score  = property(get_time_abnormality_score, set_time_abnormality_score)

    def set_geodist_ship_deviation(self,value):
        self.__geodist_ship_deviation = value
    geodist_ship_deviation  = property(get_geodist_ship_deviation, set_geodist_ship_deviation)

    def set_known_browser(self,value):
        self.__known_browser = value
    known_browser  = property(get_known_browser, set_known_browser)

    def hash(self):
        pass

    def toString(self):
        return (str(self.__id) + ":" + "tid:" + str(self.__t_id) + ":[ INDP:" + str(self.__indiscriminate_purchase) + ',PTRS:' + 
        str(self.__purchase_total_relative_score) + ',EIS:' + str(self.__expensive_items_score) + ',CPS:' + 
            str(self.__card_present_status) + ',ISOC:'+ str(self.__is_swipe_or_chip) + ',ISOP:' + str(self.__is_sign_or_pin) +
            ',FRPS:' + str(self.__freq_recent_purchase_score) + ',ERIS:' + str(self.__easy_resale_items_score) + 
            ',GDF:' + str(self.__geodist_deviation_factor) + ',KIP:' + str(self.__known_ip) + ',KMAC:' + str(self.__known_mac) +
            ',TAS:' + str(self.__time_abnormality_score) + ',GSD:' + str(self.__geodist_ship_deviation) + ',KBR:' + str(self.__known_browser) + ']')
        
    def get_all_numeric(self):
        return [self.__indiscriminate_purchase, self.__purchase_total_relative_score,self.__expensive_items_score,
        self.__freq_recent_purchase_score,self.__easy_resale_items_score,self.__geodist_deviation_factor,self.__time_abnormality_score,self.__geodist_ship_deviation]

    def get_all_boolean(self):
        return [self.__card_present_status,self.__is_swipe_or_chip,self.__is_sign_or_pin,self.__known_ip,self.__known_mac,self.__known_browser]

    def set_all_numeric(self, lst):
        self.__indiscriminate_purchase = lst[0]
        self.__purchase_total_relative_score = lst[1]
        self.__expensive_items_score = lst[2]
        self.__freq_recent_purchase_score = lst[3]
        self.__easy_resale_items_score = lst[4]
        self.__geodist_deviation_factor = lst[5]
        self.__time_abnormality_score = lst[6]
        self.__geodist_ship_deviation = lst[7]

    def set_all_boolean(self,lst):
        self.__card_present_status = lst[0]
        self.__is_swipe_or_chip = lst[1]
        self.__is_sign_or_pin = lst[2]
        self.__known_ip = lst[3]
        self.__known_mac = lst[4]
        self.__known_browser = lst[5]
