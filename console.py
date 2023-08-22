import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

# album_1=Album('Marshall Mathers LP', 'Eminem', 'Hip-hop')
# album_2=Album('Five', 'Five', 'Pop')

albums = album_repository.select_all()
print(albums)

# user_repository.delete_all()
# task_repository.delete_all()

# user_1 = User("Cobra", "Commander")
# user_repository.save(user_1)
# user_2 = User("Simon", "Cowell")
# user_repository.save(user_2)

# users = user_repository.select_all()

# task_1 = Task("Destroy Mainstream Music", 50, user_2)
# task_repository.save(task_1)

# task_2 = Task("Botox", 50, user_2)
# task_repository.save(task_2)

# results = task_repository.tasks_for_user(user_2)
# print(results)

# # task_1 = Task("Take over the world", "Ming the Merciless", 10)
# # task_repository.save(task_1)

# # found_task = task_repository.select(1)
# # found_task.mark_complete()
# # task_repository.update(found_task)

# # found_task = task_repository.select(1)
# # print(found_task.completed)


# # task_repository.delete_all()

# # task_repository.delete(1)

# # result = task_repository.select_all()
# # for task in result:
# #     print(task.__dict__)

pdb.set_trace()