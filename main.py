from pythonProject.Repository_9.hillel_lessons.mongo_db.collection import Collection

db_instance = Collection()
print('first movie id: ', db_instance.insert_movie_1_id())
print('next movies ids: ', db_instance.insert_several_movies_ids())
print('all movies: ', db_instance.find_all_movies())
print('casablanca: ', db_instance.find_casablanca())
print('all movies in db are deleted', db_instance.delete_all_movies())