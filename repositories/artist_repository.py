from db.run_sql import run_sql
from models.artist import Artist
  
def select_all():  
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

# def select(id):
#     user = None
#     sql = "SELECT * FROM users WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     if results:
#         result = results[0]
#         user = User(result['first_name'], result['last_name'], result['id'])
#     return user