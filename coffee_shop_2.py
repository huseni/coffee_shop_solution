__author__ = 'kathiria'

import csv
from math import sqrt
import datetime


def compute_distance(x1, y1, x2, y2):
    """
    To compute the distance between two points in x and y axis.
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    if x1 == "" or y1 == "" or x2 == "" or y2 == "":
        raise ValueError("missing value for all the coordinates. please provide the correct value")
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


class CoffeeShop(object):
    """
    To store this structure of the object in class data structure
    """
    def __init__(self, x2, y2, shop_name):
        self.x2 = x2
        self.y2 = y2
        self.shop_name = shop_name
        self.distance = 0


def get_distance_list_details(x1,y1, coffee_shop_file=None):
    """
    To read the coffee shop details csv file and return the list of shops.
    :param coffee_shop_file:
    :return:
    """
    coffee_shop_list = list()
    with open(coffee_shop_file) as fh:
        csv_read = csv.reader(fh)
        for rows in csv_read:
            shop_name, x2, y2 = rows[0], float(rows[1]), float(rows[2])
            shop_details_object = CoffeeShop(x2, y2, shop_name)

            distance = compute_distance(x1, y1, x2, y2)
            shop_details_object.distance = distance
            inserted_flag = 0
            i = 0
            for item in coffee_shop_list:  # initially list will be empty
                if float(item.distance) >= float(shop_details_object.distance):
                    if len(coffee_shop_list) >= 3:
                        coffee_shop_list.pop() # removes the right most element from the list
                    coffee_shop_list.insert(i, shop_details_object)
                    inserted_flag = 1
                i += 1
            if inserted_flag == 0 and len(coffee_shop_list) < 3:
                coffee_shop_list.append(shop_details_object)

        for i in coffee_shop_list:
            print i.shop_name, i.distance
        return coffee_shop_list

start_time = datetime.datetime.now()
get_distance_list_details(47.6, -122.4, 'C:\Users\kathiria\PycharmProjects\pydev\CoffeeShops.csv')
end_time = datetime.datetime.now()
time_for_execution = end_time - start_time

print (" ******* Time complexity ******")
print ("execution_start_time : %s " % start_time)
print ("Execution_end_time : %s " % end_time)
print ("Execution time : %s" % time_for_execution.microseconds)
