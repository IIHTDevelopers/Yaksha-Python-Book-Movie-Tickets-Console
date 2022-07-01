import unittest
from myexception import MovieAlreadyAvailableError,MovieNotAvailableError,TicketsNotAvailableError
from inventory import MovieInventory
from movie import Movie
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        m=Movie("Avathar",10,400)
        MovieInventory.add_movie(m)

    def test_exception_at_add_movie(self):
        test_obj = TestUtils()
        try:
            m=Movie("Avathar",50,500)
            MovieInventory.add_movie(m)
            print(MovieInventory.all_movies)
            test_obj.yakshaAssert("TestExceptionAtAddMovie", False, "exception")
            print("TestExceptionAtAddMovie = Failed")
        except MovieAlreadyAvailableError:
            test_obj.yakshaAssert("TestExceptionAtAddMovie", True, "exception")
            print("TestExceptionAtAddMovie = Passed")

    def test_exception_ticket_not_available(self):
        test_obj = TestUtils()
        try:
            MovieInventory.book_movie_tickets("Avathar",20)
            test_obj.yakshaAssert("TestExceptionTicketNotAvailable", False, "exception")
            print("TestExceptionTicketNotAvailable = Failed")
        except TicketsNotAvailableError:
            test_obj.yakshaAssert("TestExceptionTicketNotAvailable", True, "exception")
            print("TestExceptionTicketNotAvailable = Passed")

    def test_exception_movie_not_available(self):
        test_obj = TestUtils()
        try:
            MovieInventory.book_movie_tickets("Pushpa",2)
            test_obj.yakshaAssert("TestExceptionMovieNotAvailable", False, "exception")
            print("TestExceptionMovieNotAvailable = Failed")
        except MovieNotAvailableError:
            test_obj.yakshaAssert("TestExceptionMovieNotAvailable", True, "exception")
            print("TestExceptionMovieNotAvailable = Passed")
