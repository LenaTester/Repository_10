from pymongo import MongoClient
import urllib.parse

class BaseDB:
    def __init__(self):
        username = urllib.parse.quote_plus("lenatester")
        password = urllib.parse.quote_plus("Oliasc1@")
        url = "mongodb+srv://{}:{}@cluster0.llrpg.mongodb.net/movies?retryWrites=true&w=majority".format(username,
                                                                                                         password)
        self.my_client = MongoClient(url)

        self.mydb = self.my_client["movies"]
        self.my_collection = self.mydb["movies"]

    def insert_one_movie(self, movie):
        return self.my_collection.insert_one(movie)

    def insert_three_movies(self, movies):
        return self.my_collection.insert_many(movies)

    def find_all(self):
        all_movies = self.my_collection.find()
        for movie in all_movies:
            print(movie)

    def find_casablanca(self):
        casablanca = self.my_collection.find_one({'title': 'Casablanca'})
        print(casablanca)

    def delete_all(self):
        return self.my_collection.delete_many({})


#self.my_client.close()



