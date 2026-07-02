# It is project focused on making a project manager.
import json

create_file = 'youtube.txt'
def load_data():
    try:
        with open(create_file,'r') as file:
            test =  json.load(file) #loads the data inside the parsed file and converts it into json format
            print(test,type(test))
            return test
    except FileNotFoundError: 
        return []

def save_data_helper(videos):
    with open(create_file,'w') as file:
        json.dump(videos,file)  # here, the videos content has to be written in the file (which was converted into json format)
        

def list_all_videos(videos):
    print()
    print("*"*70)
    print("Your List:")
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']} Duration: {video['time']}")
    
    print()
    print("*"*70)

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    print("Video added successfully!!")

def update_video(videos):
    list_all_videos(videos)
    index  = int(input("Enter the video number to update: "))
    if 1<=index<=len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
        print("Video updated successfully!!")
    else:
        print("Video number doesnot exist")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1<=index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully!!")
    else:
        print("Invalid Video number.")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager")
        print("Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        #print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print('Thank You')
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()