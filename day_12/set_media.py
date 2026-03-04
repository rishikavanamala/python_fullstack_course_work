media=["sunrise.png","sunset.png","komali.mp4","sun.png","set.mp4","list.mp4","web.png","klmn.mp4","len.png"]
photos=[]
videos=[]

for i in media:
    if i.endswith('.mp4'):
        videos.append(i)
    else:
        photos.append(i)
print('\n-------photos-------')
for i in photos:
    print(i)
print('\n-------videos-------')
for i in videos:
    print(i)
select=set(input("Enter the files to share(using comma):").split(','))
for i in select:
    if i in media:
        print(f"{i}-sent")
    else:
        print("not sent")

