from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MediaFile(ABC):

    def __init__(self, name, size = 0):
        """
            Initialize a MediaFile instance.

            Args:
                name (str): The name of the media file.
                size (int, optional): The size of the media file. Defaults to 0.

            Attributes:
                name (str): The name of the media file.
                size (int): The size of the media file.
                created_at (datetime): The time the media file was created.
                accessed_at (datetime): The time the media file was accessed.
                _is_active (bool): A flag indicating if the media file is currently open.
        """
        self.name = name
        self.size = size
        
        now = datetime.now()
        self.__created_at = now
        self.__accessed_at = now

        self._is_active = False

    @property
    def created_at(self):
        """
            Get the creation time of the media file.

            Returns:
                datetime: The timestamp when the media file was created.
        """
        return self.__created_at

    @property
    def accessed_at(self):
        """
            Get the last access time of the media file.

            Returns:
                datetime: The timestamp when the media file was last accessed.
        """
        return self.__accessed_at
    
    @property
    def is_active(self):
        """
            Check if the media file is currently open.

            Returns:
                bool: True if the media file is currently open, False otherwise.
        """
        return self._is_active

    @property
    @abstractmethod
    def format(self):
        """
            Get the format of the media file.

            This is an abstract property that must be implemented by subclasses
            to specify the media file format.

            Returns:
                str: The format of the media file as a string.
        """
        return "NONE"
    
    def rename(self, new_name):
        """
            Rename the media file with a new name.

            Args:
                new_name (str): The new name for the media file.
        """
        self.name = new_name

    @abstractmethod
    def open(self):
        """
            Open the media file for use.

            If the file is not currently open, set the accessed_at timestamp to now and mark the file as active.
            If the file is already open, do nothing.

            Returns:
                str: A message indicating the result of the operation
        """
        if not self._is_active:
            self.__accessed_at = datetime.now()
            self._is_active = True
            return (f"File {self.name}.{self.format} has been opened.")
        else:
            return (f"File {self.name}.{self.format} is already open!")

    @abstractmethod
    def close(self):
        """
            Close the media file.

            If the file is currently open, update the accessed_at timestamp to now,
            deactivate the file, and return a message indicating the file has been closed.
            If the file is not open, return a message indicating that the file is not open.

            Returns:
                str: A message indicating the result of the operation.
        """

        if self._is_active:
            self.__accessed_at = datetime.now()
            self._is_active = False
            return (f"File {self.name}.{self.format} has been closed.")
        else:
            return (f" > ## File {self.name}.{self.format} is not open! ##")

class PngFile(MediaFile):
    
    def __init__(self, name, size, height, width):
        """
            Initialize a PngFile instance.

            Args:
                name (str): The name of the png file.
                size (int): The size of the png file.
                height (int): The height of the png.
                width (int): The width of the png.

            Attributes:
                height (int): The height of the png.
                width (int): The width of the png.
        """
        super().__init__(name, size)
        self.height = height
        self.width = width

    @property
    def format(self):
        """
            Get the format of the media file.

            Returns:
                str: The format of the media file as a string.
        """
        return "png"

    def open(self):
        """
            Open the media file for use.

            If the file is not currently open, set the accessed_at timestamp to now and mark the file as active.
            If the file is already open, do nothing.

            Returns:
                str: A message indicating the result of the operation
        """
        super().open()

    def close(self):
        """
            Close the media file.

            If the file is currently open, update the accessed_at timestamp to now,
            deactivate the file, and return a message indicating the file has been closed.
            If the file is not open, return a message indicating that the file is not open.

            Returns:
                str: A message indicating the result of the operation.
        """
        super().close()

class Mp4File(MediaFile):

    def __init__(self, name, size, height = 0, width = 0, duration = timedelta(0)):
        """
            Initialize an Mp4File instance.

            Args:
                name (str): The name of the mp4 file.
                size (int): The size of the mp4 file.
                height (int, optional): The height of the mp4. Defaults to 0.
                width (int, optional): The width of the mp4. Defaults to 0.
                duration (timedelta, optional): The duration of the mp4. Defaults to 0.

            Attributes:
                height (int): The height of the mp4.
                width (int): The width of the mp4.
                duration (timedelta): The duration of the mp4.
                is_playing (bool): A flag indicating if the mp4 is currently playing.
                is_muted (bool): A flag indicating if the mp4 is currently muted.
        """
        super().__init__(name, size)
        self.height = height
        self.width = width
        self.duration = duration
        self.is_playing = False
        self.is_muted = False

    @property
    def format(self):
        """
            Get the format of the media file.

            Returns:
                str: The format of the media file as a string.
        """
        return "mp4"

    def open(self):
        """
            Open the media file for use.

            If the file is not currently open, set the accessed_at timestamp to now and mark the file as active.
            If the file is already open, do nothing.

            Returns:
                str: A message indicating the result of the operation
        """
        super().open()

    def close(self):
        """
            Close the media file and stop playback.

            If the file is not open, do nothing.
            If the file is open, stop playback, unmute the file, and close the file.

            Returns:
                str: A message indicating the result of the operation
        """
        self.is_playing = False
        self.is_muted = False
        super().close()
    
    def toggle_pause(self):
        """
            Toggle the playback state of the file.

            If the file is currently open, it toggles the playback state between
            playing and paused. If the file is now playing, it returns a message
            indicating that playback has resumed; if paused, it returns a message
            indicating the pause.

            If the file is not open, it returns a message indicating that the file
            is not open.

            Returns:
                str: A message indicating the result of the toggle operation.
        """
        if self._is_active:
            self.is_playing = not self.is_playing
            if self.is_playing:
                return (f" > {self.name}.{self.format} has been resumed.")
            else:
                return (f" > {self.name}.{self.format} has been paused.")
        else:
            return (f" > ## File {self.name}.{self.format} is not open! ##")
        
    def toggle_mute(self):
        """
            Toggle the mute state of the file.

            If the file is currently open, it toggles the mute state between
            muted and unmuted. If the file is now muted, it returns a message
            indicating that the file has been muted; if unmuted, it returns a
            message indicating that the file has been unmuted.

            If the file is not open, it returns a message indicating that the file
            is not open.

            Returns:
                str: A message indicating the result of the toggle operation.
        """
        if self._is_active:
            self.is_muted = not self.is_muted
            if self.is_muted:
                return (f" > {self.name}.{self.format} has been muted.")
            else:
                return (f" > {self.name}.{self.format} has been unmuted.")
        else:
            return (f" > ## File {self.name}.{self.format} is not open! ##")

            
class Mp3File(MediaFile):

    def __init__(self, name, size, duration = timedelta(0)):
        """
            Initialize an Mp3File instance.

            Args:
                name (str): The name of the mp3 file.
                size (int): The size of the mp3 file.
                duration (timedelta, optional): The duration of the mp3. Defaults to 0.

            Attributes:
                duration (timedelta): The duration of the mp3.
                is_playing (bool): A flag indicating if the mp3 is currently playing.
                is_muted (bool): A flag indicating if the mp3 is currently muted.
        """
        super().__init__(name, size)
        self.duration = duration
        self.is_playing = False
        self.is_muted = False

    @property
    def format(self):
        """
            Get the format of the media file.

            Returns:
                str: The format of the media file as a string.
        """
        return "mp3"

    def open(self):
        """
            Open the media file for use.

            If the file is not currently open, set the accessed_at timestamp to now and mark the file as active.
            If the file is already open, do nothing.

            Returns:
                str: A message indicating the result of the operation
        """
        super().open()

    def close(self):
        """
            Close the media file and stop playback.

            If the file is not open, do nothing.
            If the file is open, stop playback, unmute the file, and close the file.

            Returns:
                str: A message indicating the result of the operation
        """
        self.is_playing = False
        self.is_muted = False
        super().close()
    
    def toggle_pause(self):
        """
            Toggle the playback state of the file.

            If the file is currently open, it toggles the playback state between
            playing and paused. If the file is now playing, it returns a message
            indicating that playback has resumed; if paused, it returns a message
            indicating the pause.

            If the file is not open, it returns a message indicating that the file
            is not open.

            Returns:
                str: A message indicating the result of the toggle operation.
        """
        if self._is_active:
            self.is_playing = not self.is_playing
            if self.is_playing:
                return (f" > {self.name}.{self.format} has been resumed.")
            else:
                return (f" > {self.name}.{self.format} has been paused.")
        else:
            return (f" > ## File {self.name}.{self.format} is not open! ##")
        
    def toggle_mute(self):
        """
            Toggle the mute state of the file.

            If the file is currently open, it toggles the mute state between
            muted and unmuted. If the file is now muted, it returns a message
            indicating that the file has been muted; if unmuted, it returns a
            message indicating that the file has been unmuted.

            If the file is not open, it returns a message indicating that the file
            is not open.

            Returns:
                str: A message indicating the result of the toggle operation.
        """
        if self._is_active:
            self.is_muted = not self.is_muted
            if self.is_muted:
                return (f" > {self.name}.{self.format} has been muted.")
            else:
                return (f" > {self.name}.{self.format} has been unmuted.")
        else:
            return (f" > ## File {self.name}.{self.format} is not open! ##")


class GifFile(MediaFile):

    def __init__(self, name, size, height = 0, width = 0, duration = 0):
        """
            Initialize a GifFile instance.

            Args:
                name (str): The name of the gif file.
                size (int): The size of the gif file.
                height (int, optional): The height of the gif. Defaults to 0.
                width (int, optional): The width of the gif. Defaults to 0.
                duration (int, optional): The duration of the gif. Defaults to 0.

            Attributes:
                height (int): The height of the gif.
                width (int): The width of the gif.
                duration (int): The duration of the gif.
                is_playing (bool): A flag indicating if the gif is currently playing.
        """

        super().__init__(name, size)
        self.height = height
        self.width = width
        self.duration = duration
        self.is_playing = False

    @property
    def format(self):
        """
            Get the format of the media file.

            Returns:
                str: The format of the media file as a string.
        """
        return "gif"

    def open(self):
        """
            Open the media file for use.

            If the file is not currently open, set the accessed_at timestamp to now and mark the file as active.
            If the file is already open, do nothing.

            Returns:
                str: A message indicating the result of the operation
        """
        super().open()

    def close(self):
        """
            Close the file and stop playback.

            If the file is not open, do nothing.

            If the file is open, stop playback and close the file.

            Returns: 
                A message indicating the result of the operation
        """
        self.is_playing = False
        super().close()

    def toggle_pause(self):
        """
            Toggle playback of the file.

            If the file is not open, do nothing.

            If the file is open, toggle playback.

            Returns: 
                A message indicating the result of the operation
        """
        if self._is_active:
            self.is_playing = not self.is_playing
            if self.is_playing:
                return (f" > {self.name}.{self.format} has been resumed.")
            else:
                return (f" > {self.name}.{self.format} has been paused.")
        else:
            return (f" > ## File {self.name}.{self.format} is not open! ##")

timedelta(seconds=30, minutes=3)