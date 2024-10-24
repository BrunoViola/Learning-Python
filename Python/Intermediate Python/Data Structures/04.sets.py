# Sets

my_favorite_fruits = {'Apple', 'Grape', 'Watermelon'}
friend_favorite_fruits = {'Strawberry', 'Apple', 'Blueberry'}

union_result = my_favorite_fruits.union(friend_favorite_fruits)
intersection_result = my_favorite_fruits.intersection(friend_favorite_fruits)
difference_my_and_friend = my_favorite_fruits.difference(friend_favorite_fruits)
difference_friend_and_my = friend_favorite_fruits.difference(my_favorite_fruits)

print(f"Union Result: {union_result}")
print(f"Intersection Result: {intersection_result}")
print(f"Difference my-friend: {difference_my_and_friend}")
print(f"Difference friend-my: {difference_friend_and_my}")

my_favorite_fruits.add('Pineapple')
print(f"Added Pineapple: {my_favorite_fruits}")
my_favorite_fruits.remove('Pineapple')
print(f"Removed Pineapple: {my_favorite_fruits}")

print(f"Is Apple in my list of favorite fruits? {'Apple' in my_favorite_fruits}")