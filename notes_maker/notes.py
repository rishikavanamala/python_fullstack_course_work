
notes={}
name = input("enter name")
print(f" hey {name} welcome to the notes maker")

while(True):
    if notes :
        for i in notes:
            print(f"{i} : {notes[i]}")
    else:
        print(" your notes is empty")
            
    print("[U]pdate")
    print("[A]dd")
    print("[D]elete")
    print("[B]ack to exit")
    k = input("enter ur choice").upper()
    if k =='U':
        new_note = input("enter the notes u want to update")
        if new_note not in notes:
            print("sorry this notes is not avaliable in  our notes")
        else:
            new_tought = input("enter the new taights")
            notes[new_note] = new_tought
    elif k=='A':
        new_note = input("enter the new note to add")
        new_taught = input("enter the new tought")
        notes[new_note] = new_taught
        print("succesfully added new tought")
    elif k =='D':
        note_to_delete = input("enter the note to delete")
        if note_to_delete in notes:
            notes.pop(note_to_delete)
            print("succesfully deleted")
        else:
            print("no such note to delete")
    elif k=='B':
        print("yeah, thankyou for using the notes, we are exiting")
        break
    
