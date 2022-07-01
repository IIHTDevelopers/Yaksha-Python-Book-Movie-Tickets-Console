import unittest
from inventory import MovieInventory
from movie import Movie
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=Movie("KGF",80,400)
        cls.msg=MovieInventory.add_movie(cls.m)

    def test_add_movie(self):
        test_obj = TestUtils()
        if len(MovieInventory.all_movies)!=0:
            test_obj.yakshaAssert("TestAddMovie", True, "functional")
            print("TestAddMovie = Passed")
        else:
            test_obj.yakshaAssert("TestAddMovie", False, "functional")
            print("TestAddMovie = Failed")

    def test_add_movie_message(self):
        test_obj = TestUtils()
        if self.msg=="Movie Added":
            test_obj.yakshaAssert("TestAddMovieMessage", True, "functional")
            print("TestAddMovieMessage = Passed")
        else:
            test_obj.yakshaAssert("TestAddMovieMessage", False, "functional")
            print("TestAddMovieMessage = Failed")

    def test_movie_inventory(self):
        test_obj = TestUtils()
        result=MovieInventory.show_movie_inventory()
        if type(result)==type([]):
            test_obj.yakshaAssert("TestMovieInventory", True, "functional")
            print("TestMovieInventory = Passed")
        else:
            test_obj.yakshaAssert("TestMovieInventory", False, "functional")
            print("TestMovieInventory = Failed")

    def test_find_movie_return_type(self):
        test_obj = TestUtils()
        movie_details=MovieInventory.find_movie("Pushpa",lambda x: x["movie_name"])
        if type(movie_details)==type([]):
            test_obj.yakshaAssert("TestFindMovieReturnType", True, "functional")
            print("TestFindMovieReturnType = Passed")
        else:
            test_obj.yakshaAssert("TestFindMovieReturnType", False, "functional")
            print("TestFindMovieReturnType = Failed")

    def test_find_movie(self):
        test_obj = TestUtils()
        movie_details=MovieInventory.find_movie("KGF",lambda x: x["movie_name"])
        if movie_details!=None:
            if movie_details[0]['movie_name']=='KGF':
                test_obj.yakshaAssert("TestFindMovie", True, "functional")
                print("TestFindMovie = Passed")
            else:
                test_obj.yakshaAssert("TestFindMovie", False, "functional")
                print("TestFindMovie = Failed")
        else:
            test_obj.yakshaAssert("TestFindMovie", False, "functional")
            print("TestFindMovie = Failed")

    def test_book_movie_tickets(self):
        test_obj = TestUtils()
        result=MovieInventory.book_movie_tickets("KGF",2)
        if result==800:
            test_obj.yakshaAssert("TestBookMovieTickets", True, "functional")
            print("TestBookMovieTickets = Passed")
        else:
            test_obj.yakshaAssert("TestBookMovieTickets", False, "functional")
            print("TestBookMovieTickets = Failed")
