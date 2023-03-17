import os
from pytube import YouTube
from pytube import Playlist

def mainEngine(url,location,fileType):


    loc = location if (location!="Default") else "../Download/"+fileType
    

    if fileType == "Playlist":
        pl = Playlist(url)
        for video in pl.videos:
            file = video.streams.first().download(location)
            new_file = mp3Converter(file)
            os.rename(file, new_file)        

    try:  
        yt = YouTube(url)
        downloadFile(yt,fileType,loc) 

    except Exception as e: 
        print(e) 
    

def downloadFile(yt,filetype,location):
    if filetype == "Music":

        file=yt.streams.filter(only_audio=True).first().download(location)
        new_file = mp3Converter(file)

    else:
        yt.streams.get_highest_resolution().download(location)

    os.rename(file, new_file)


def mp3Converter(file):
    base, ext = os.path.splitext(file)
    new_file = base + '.mp3'
    return new_file

# def main():
#     url = "https://youtube.com/playlist?list=PLIqy7ZKdJ54P9Z9e1oTlWFv0YlfxDYrxQ"
#     location = "Download/Music"
#     fileType = "Playlist"
#     mainEngine(url,location,fileType)

# if __name__ == '__main__':
#     main()
    