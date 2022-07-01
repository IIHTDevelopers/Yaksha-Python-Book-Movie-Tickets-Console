from movie import Movie
from inventory import MovieInventory
class MainClass:
    def read_movie_details():
        print("--- Add Movies and Tickets ---")
        n=int(input("Enter number of movies"))
        for i in range(n):
            movie_name=input("Enter movie name")
            aval_tickets=int(input("Enter number of tickets"))
            ticket_price=int(input("Enter ticket price"))
            m=Movie(movie_name,aval_tickets,ticket_price)
            message=MovieInventory.add_movie(m)
            print(message)

    def show_inventory():
        print("------------MOVIE INVENTORY-----------------")
        lst=MovieInventory.show_movie_inventory()
        for d in lst:
            for k,v in d.items():
                print(k,v)

    def search_movie():
        print("------------SEARCH MOVIE-----------------")
        category = input("Your are searching movie by ? (Must enter input as 'movie_name') ")
        movie_name = input("Enter movie name? ")
        movie_details=MovieInventory.find_movie(movie_name,lambda x: x[category])
        print(movie_details or 'No movies found')

    def book_tickets():
        print("---Book Movie Tickets---")
        movie_name=input("Enter movie name")
        tickets=int(input("Enter number of tickets"))
        total_cost=MovieInventory.book_movie_tickets(movie_name,tickets)
        print("Movie Tickets booked and total cost  RS:",total_cost)

if __name__=="__main__":
    MainClass.read_movie_details()
    MainClass.show_inventory()
    MainClass.search_movie()
    MainClass.book_tickets()
