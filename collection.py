from pythonProject.Repository_9.hillel_lessons.mongo_db.base_db import BaseDB

class Collection(BaseDB):
    __movie_1 = {'title': 'The Dark Knight', 'year': '2008', 'genres': ['Action', 'Crime', 'Drama']}
    __movie_list = [{'title': 'Spirited Away', 'year': '2001', 'genres': ['Animation', 'Adventure', 'Family']},
                  {'title': 'Casablanca', 'year': '1942', 'genres': ['Drama', 'Romance', 'War']},
                  {'title': 'Titanic', 'year': '1997', 'genres': ['Drama', 'Romance']}]

    def insert_movie_1(self):
        self.insert_one_movie(self.__movie_1)
        return self

    def insert_movie_1_id(self):
        id = self.insert_one_movie(self.__movie_1)
        return id.inserted_id

    def insert_several_movies(self):
        self.insert_three_movies(self.__movie_list)
        return self

    def insert_several_movies_ids(self):
        ids = self.insert_three_movies(self.__movie_list)
        return ids.inserted_ids

    def find_all_movies(self):
        self.find_all()
        return self

    def find_casablanca_movie(self):
        self.find_casablanca()
        return self

    def delete_all_movies(self):
        self.delete_all()
        return self
