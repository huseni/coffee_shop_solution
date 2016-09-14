# coffee_shop_solution

1. The coffee shop problem is solved in appx. 40 minutes(refer the code file - coffee_shop.py)
2. The unittest for the code is written in 25 minutes including(refer the code file - test_coffee_shop.py)
3. The code was verified by multiple tests run manually and by unittests.
4. Didn't have enough time to consider the corner cases like un-formatted, missing column values(for the 'x-coordinates', 'y-coordinates' or the 'coffee shop' name itself), non Ascii charset, unicode type of charset, etc.
5. This code currently uses python inbuilt data structures like (dict and list) and can work fine on a file with about 5000 - 10000 records of coffee shops in it. It can be scaled to handle massive file size of GBs or TBs by using different data structure (linked list or other data structure) and also can use some concurrency features if possible.
6. Just to cover the duplicate values for the location(x2, y2), I have added the extra record (Starbucks Rio De Janeiro 2,-22.923489,-43.234418) in the file CoffeeShop.csv and verified.

Optional/alternate optimized logic(after 1 hour of time - in my free time)
1. I put a logic together to make my first solution more optimistic and memory efficient. The code file (refer the code file - coffee_shop.py).

NOTE: I have used the Python 2.7.9 for coding and testing this problem.


Things that could still be improved in the current simple solutions
---------------------------------------------------------------------
1. I could have written a decorator (validator) which can be used to validate the input parameter values (properties) at runtime instead of a general function I wrote in my solution(coffee_shop.py).
2. I could have used "class" to store the details of calculated distance and their corresponding attributes.
3. I could have written my own exception handle class (context manager) and could made more appropriate error handling.
4. I could have written some coffee_shop.csv file validator decorator.
