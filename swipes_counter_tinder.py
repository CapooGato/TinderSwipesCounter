import json


try:
    with open('data.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("[Error]: Make sure file 'data.json' is in the directory.")
except PermissionError:
    print("[Error]: Program doesn't have permision to the 'data.json' file.")
except Exception as e:
    print(f"[Error]: Unexpected error occured: {e}")


swipes_likes = 0
swipes_passes = 0
swipes_total = 0

for likes in data['Usage']['swipes_likes'].values():
    swipes_likes += likes

for passes in data['Usage']['swipes_passes'].values():
    swipes_passes += passes

swipes_total = swipes_likes + swipes_passes
print(f'\nSwipes in total: {swipes_total}\nLikes: {swipes_likes}\nPasses: {swipes_passes}')

swipes_likes_ratio = round((swipes_likes / swipes_total) * 100, 3)  
swipes_passes_ratio = round((swipes_passes / swipes_total)* 100, 3) 

print(f'\nPercentages:\nLikes: {swipes_likes_ratio}%\nPasses: {swipes_passes_ratio}%\n')