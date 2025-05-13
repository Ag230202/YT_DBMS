import sqlite3

conn=sqlite3.connect("content.db")


cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL

    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_videos():
    name=input("Enter name: ")
    time=input("Enter the time: ")
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    print("Added Successfullu \n")
    conn.commit()


def update_videos():
    id=input("Enter id of video: ")
    name=input("Enter name to be updated: ")
    time=input("Enter the time to be updated: ")
    cursor.execute("UPDATE videos SET name=? ,time=? WHERE id=? ",(name,time,id))
    print("Updated Successfullu \n")
    conn.commit()

def delete_videos():
    id=input("Enter id of video to be deleted: ")
    cursor.execute("DELETE FROM videos WHERE id=?",(id,))
    print("Deleted Successfullu \n")
    conn.commit()




def main():
     while True:
        print("\n Youtube Manager| choose an option ")
        print("1. List all youtube videos")
        print("2. Add a Youtube video")
        print("3.Update a youtube video details")
        print("4.Delete a youtube video")
        print("5.Exit the app")
        choice=input("Enter your choice: ")


        if choice=='1':
            list_videos()

        elif choice=='2':
            add_videos()

        elif choice=='3':
            update_videos()
        
        elif choice=='4':
            delete_videos()

        elif choice=='5':
            cursor.close()
            break
        
        else:
            print("Invslid choice")
            


if __name__=="__main__":
    main()