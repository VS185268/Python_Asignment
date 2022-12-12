import pytube
'''Here I created one function to download video from links and
by using files concept I read urls from the text file and passing
each url to that download function then finally downloading video in
videos folder'''


def download(link):
    Ytobject=pytube.YouTube(link)
    Ytobject=Ytobject.streams.get_highest_resolution()
    Saving_FolderPath=r'C:\Users\VST\OneDrive\Desktop\automationassignment\videos'
    Ytobject.download(Saving_FolderPath)

with open('File_links.txt') as Lfile:
    Links=Lfile.readlines()
    for i in Links:
        download(i)
print("Successfully we downloaded the videos")
