import os
from mutagen.mp4 import MP4, MP4Cover

def getFileName(string):
    return string.split(".")[0]

if __name__ == '__main__':
    folder = input()
    for videoName in os.listdir(folder):
        if videoName.endswith('.mp4'):
            videoPath = os.path.join(folder, videoName)
            if os.path.isfile(videoPath[:-3] + "png"):
                imagePath = videoPath[:-3] + "png"
            elif os.path.isfile(videoPath[:-3] + "jpg"):
                imagePath = videoPath[:-3] + "jpg"
            else:
                continue
            video = MP4(videoPath)
            with open(imagePath, "rb") as f:
                video["covr"] = [
                    MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)
                ]
                video.save()