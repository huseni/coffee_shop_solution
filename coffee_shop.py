__author__ = 'kathiria'

# Inputs #
# y = 47.6,
# x = -122.4
# coffee_shop_file = 'C:\Users\kathiria\PycharmProjects\pydev\CoffeeShops.csv'

from math import sqrt
from math import pow
import csv
import os
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
    if not (x1 or y1 or x2 or y2):
        raise ValueError("missing value for all the coordinates. please provide the correct value")
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def get_distance_list_details(coffee_shop_file=None):
    """
    To read the coffee shop details csv file and return the list of shops.
    :param coffee_shop_file:
    :return:
    """
    coffee_shop_list = list()
    if not coffee_shop_file:
        raise ValueError("Missing the coffee shop %s file. Please provide the required file." % coffee_shop_file)
    with open(coffee_shop_file) as fh:
        csv_read = csv.reader(fh)
        for rows in csv_read:
            coffee_shop_list.append(rows)
        return coffee_shop_list


def get_coffee_shops(x1, y1, coffee_shop_list):
    """
    To read the list, compute the distance b/w points for the users and return the dictionary of it.
    :param coffeeshop_file:
    :return:
    """
    if isinstance(y1, int) or isinstance(y1, float):
        print("Valid user_y_coordinate value : %r entered!" % y1)
    else:
        if not y1.isdigit():
            raise TypeError("User's Y-coordinate value can be integer-digit or float-digit")

    if isinstance(x1, int) or isinstance(x1, float):
        print("Valid user_x_coordinate value : %r entered!" % x1)
    else:
        if not x1.isdigit():
            raise TypeError("User's X-coordinate value can be integer-digit or float-digit")

    if not coffee_shop_list:
        raise ValueError("Missing the value for %s. Please check and enter" % coffee_shop_list)
    else:
        if not isinstance(coffee_shop_list, list):
            raise TypeError("The value enter for %s is not a list type. Please check and enter" % coffee_shop_list )

    distance_dict = dict()
    for l in coffee_shop_list:
        x2 = float(l[1])
        y2 = float(l[2])
        location = str(l[0])
        if not(x2 or y2 or location):
            raise ValueError("Not all the required values for %s, %s and %s present in the coffee shop list file" % (x2, y2, location))
        distance_dict[location] = compute_distance(x1, y1, x2, y2)
    return distance_dict


def gather_and_validate_input(_user_y_coordinate, _user_x_coordinate, _shop_file_path):
    """
    To validate the input parameters.
    :return:
    """
    if isinstance(_user_y_coordinate, int) or isinstance(_user_y_coordinate, float):
        print("Valid user_y_coordinate value : %r entered!" % _user_y_coordinate)
    else:
        if not _user_y_coordinate.isdigit():
            raise TypeError("User's Y-coordinate value can be integer-digit or float-digit")

    if isinstance(_user_x_coordinate, int) or isinstance(_user_x_coordinate, float):
        print("Valid user_x_coordinate value : %r entered!" % _user_x_coordinate)
    else:
        if not _user_x_coordinate.isdigit():
            raise TypeError("User's X-coordinate value can be integer-digit or float-digit")

    if not os.path.exists(_shop_file_path):
        raise OSError("Path %s does not exist. Please provide the correct directory path" % os.path.dirname(_shop_file_path))
    elif not os.path.isfile(_shop_file_path):
        raise IOError("%s is not a file. Please provide the correct file name" % os.path.basename(_shop_file_path))
    else:
        print("Valid coffee_shop_file_path value : %r entered!" % _shop_file_path)


def nearest_coffee_shops(_user_y_coordinate, _user_x_coordinate, _shop_file_path):
    """
    To return the list of nearest coffee shop.
    :return:
    """
    gather_and_validate_input(_user_y_coordinate, _user_x_coordinate, _shop_file_path)
    user_y_coordinate = float(_user_y_coordinate)
    user_x_coordinate = float(_user_x_coordinate)

    distance_dict = (get_coffee_shops(user_y_coordinate, user_x_coordinate, get_distance_list_details(shop_file_path)))

    print("------------------------------------------------------------------------")
    print("######### Nearest Coffee Shops #########")
    print("------------------------------------------------------------------------")
    list_of_shops = sorted(distance_dict.items(), key=lambda x: x[1])
    for i in range(3):
        print (list_of_shops[i])


if __name__ == '__main__':

    user_y_coordinate = input("Enter the value of user's Y-coordinate : ")
    user_x_coordinate = input("Enter the value of user's X-coordinate : ")
    shop_file_path = input("Enter the value of coffee shop file fullpath : ")
    start_time  = datetime.datetime.now()
    try:
        nearest_coffee_shops(user_y_coordinate, user_x_coordinate, shop_file_path)
    except StandardError, e:
        raise
    end_time = datetime.datetime.now()
    time_for_execution = end_time - start_time
    print (" ******* Time complexity ******")
    print ("execution_start_time : %s " % start_time)
    print ("Execution_end_time : %s " % end_time)
    print ("Execution Time : %s" % time_for_execution.microseconds)

# SAMPLE TEST INPUT & OUTPUT #
# --------------------------------------- #
# C:\Python27\python.exe C:/Users/kathiria/PycharmProjects/pydev/coffee_shop.py
# Enter the value of user's Y-coordinate : 47.6
# Enter the value of user's X-coordinate : -122.4
# Enter the value of coffee shop file fullpath : 'C:\Users\kathiria\PycharmProjects\pydev\CoffeeShops.csv'
# Valid user_y_coordinate value : 47.6 entered!
# Valid user_x_coordinate value : -122.4 entered!
# Valid coffee_shop_file_path value : 'C:\\Users\\kathiria\\PycharmProjects\\pydev\\CoffeeShops.csv' entered!
# Valid user_y_coordinate value : -122.4 entered!
# Valid user_x_coordinate value : 47.6 entered!
# ------------------------------------------------------------------------
# ######### Nearest Coffee Shops #########
# ------------------------------------------------------------------------
# ('Starbucks Seattle2', 0.06454339625400246)
# ('Starbucks Seattle', 0.0861441234211632)
# ('Starbucks SF', 10.079316088406003)
