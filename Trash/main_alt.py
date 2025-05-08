from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class FileType(Enum):

    PNG = "png"
    JPG = "jpg"
    GIF = "gif"
    MP3 = "mp3"
    MP4 = "mp4"

class MediaFile(ABC):

    def __init__(self, name, size):
        self.name = name

        now = datetime.now()
        self.__created_at = now
        self.__last_accessed_at = now
        self.__size = size

        self.__is_active = False

    @property
    @abstractmethod
    def format(self):
        ...
    
    @property
    def size(self):
        return self.__size

    @property
    def created_at(self):
        return self.__created_at

    @property
    def last_accessed_at(self):
        return self.__last_accessed_at
    
    def __str__(self):
        return (f"File '{self.name}'\n"
                f"\tSize: {self.size}"
                f"\tCreated at: {self.created_at}")
    
class PngFile(MediaFile):

    @property
    def format(self):
        return FileType.PNG