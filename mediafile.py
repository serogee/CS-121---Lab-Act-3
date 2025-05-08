from abc import ABC, abstractmethod
from datetime import datetime

class MediaFile(ABC):

    def __init__(self, name, size = 0):
        self.name = name
        self.size = size
        
        now = datetime.now()
        self.__created_at = now
        self.__accessed_at = now

        self._is_active = False

    @property
    def created_at(self):
        return self.__created_at

    @property
    def accessed_at(self):
        return self.__accessed_at
    
    @property
    def is_active(self):
        return self._is_active

    @property
    @abstractmethod
    def format(self):
        ...
    
    def rename(self, new_name):
        self.name = new_name

    @abstractmethod
    def open(self):
        if not self._is_active:
            self.__accessed_at = datetime.now()
            self._is_active = True
            print(f"File {self.name}.{self.format} has been opened.")
        else:
            print(f"File {self.name}.{self.format} is already open!")

    @abstractmethod
    def close(self):
        if self._is_active:
            self.__accessed_at = datetime.now()
            self._is_active = False
            print(f"File {self.name}.{self.format} has been closed.")
        else:
            print(f"File {self.name}.{self.format} is not open!")

class PngFile(MediaFile):
    
    def __init__(self, name, size, height, width):
        super().__init__(name, size)
        self.height = height
        self.width = width

    @property
    def format(self):
        return "png"

    def open(self):
        super().open()

    def close(self):
        super().close()

class Mp4File(MediaFile):

    def __init__(self, name, size, height = 0, width = 0, duration = 0):
        super().__init__(name, size)
        self.height = height
        self.width = width
        self.duration = duration
        self.__is_playing = False
        self.__is_muted = False

    @property
    def format(self):
        return "mp4"

    def open(self):
        super().open()

    def close(self):
        self.__is_playing = False
        self.__is_muted = False
        super().close()
    
    def toggle_pause(self):
        if self._is_active:
            self.__is_playing = not self.__is_playing
            if self.__is_playing:
                print(f" > {self.name}.{self.format} has been resumed.")
            else:
                print(f" > {self.name}.{self.format} has been paused.")
        else:
            print(f"File {self.name}.{self.format} is not open!")
        
    def toggle_mute(self):
        if self._is_active:
            self.__is_muted = not self.__is_muted
            if self.__is_muted:
                print(f" > {self.name}.{self.format} has been muted.")
            else:
                print(f" > {self.name}.{self.format} has been unmuted.")
        else:
            print(f"File {self.name}.{self.format} is not open!")

            
class Mp3File(MediaFile):

    def __init__(self, name, size, duration = 0):
        super().__init__(name, size)
        self.duration = duration
        self.__is_playing = False
        self.__is_muted = False

    @property
    def format(self):
        return "mp3"

    def open(self):
        super().open()

    def close(self):
        self.__is_playing = False
        self.__is_muted = False
        super().close()
    
    def toggle_pause(self):
        if self._is_active:
            self.__is_playing = not self.__is_playing
            if self.__is_playing:
                print(f" > {self.name}.{self.format} has been resumed.")
            else:
                print(f" > {self.name}.{self.format} has been paused.")
        else:
            print(f"File {self.name}.{self.format} is not open!")
        
    def toggle_mute(self):
        if self._is_active:
            self.__is_muted = not self.__is_muted
            if self.__is_muted:
                print(f" > {self.name}.{self.format} has been muted.")
            else:
                print(f" > {self.name}.{self.format} has been unmuted.")
        else:
            print(f"File {self.name}.{self.format} is not open!")


class GifFile(MediaFile):

    def __init__(self, name, size, height = 0, width = 0, duration = 0):
        super().__init__(name, size)
        self.height = height
        self.width = width
        self.duration = duration
        self.__is_playing = False

    @property
    def format(self):
        return "gif"

    def open(self):
        super().open()

    def close(self):
        self.__is_playing = False
        super().close()
    
    def toggle_pause(self):
        if self._is_active:
            self.__is_playing = not self.__is_playing
            if self.__is_playing:
                print(f" > {self.name}.{self.format} has been resumed.")
            else:
                print(f" > {self.name}.{self.format} has been paused.")
        else:
            print(f"File {self.name}.{self.format} is not open!")
