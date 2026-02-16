media = [
    'sunset_beach.png',
    'waves_crashing.mp4',
    'mountain_view.jpg',
    'forest_trail.mp4',
    'city_skyline.png',
    'street_timelapse.mp4',
    'golden_sunset.jpg',
    'river_flow.mp4',
    'snowy_mountains.png',
    'campfire_night.mp4',
    'travel_selfie.jpg',
    'friends_laughing.mp4',
    'coffee_morning.png',
    'rainy_window.mp4',
    'night_stars.jpg'
]
image = set()
video = set()
for i in range(len(media)):
    k = media[i]
    after= k[-3:]
    if after =='png' or after=='jpg':
        image.add(k)
    elif after=='mp4':
        video.add(k)
print(image)
print(video)

images_to_send = set(input("enter the images u want to send").split())
for i in images_to_send:
    if i not in image and i not in video:
        print(f"sorry {i} is not in both images and videos")
    else:
        print(f"{i} sent succesfully")

    
