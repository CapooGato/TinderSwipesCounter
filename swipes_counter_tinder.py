import json


with open('data.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

swipes_likes = 0
swipes_passes = 0
swipes_total = 0

for likes in data['Usage']['swipes_likes'].values():
    swipes_likes += likes

for passes in data['Usage']['swipes_passes'].values():
    swipes_passes += passes

swipes_total = swipes_likes + swipes_passes
print(f'\nSwipes count: {swipes_total}\nLikes: {swipes_likes}\nPasses: {swipes_passes}')

swipes_likes_ratio = round((swipes_likes / swipes_total) * 100, 3)  
swipes_passes_ratio = round((swipes_passes / swipes_total)* 100, 3) 

print(f'\n\nPercentages:\nLikes: {swipes_likes_ratio}%\nPasses: {swipes_passes_ratio}%')