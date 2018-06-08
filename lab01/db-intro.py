from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to database
client = MongoClient (mongo_uri)

# 2. Get datanase
db = client.get_default_database()

# 3. Creat collection
# games = db['games']
# movies = db['movie']

# 4. Creat document

# new_movies ={
#     'Title':'50 shades of Grey',
#     'description':'Adult movie'
# }
# 5. Insert document into collection

posts.remove({'title':'Yêu em nghiêm túc'})
# # movies.insert_one(new_movies)

# all_game = games.find()

# for game in all_game:
#     print(game)