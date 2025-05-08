from mediafile import PngFile, Mp4File, Mp3File, GifFile

def clear():
    print("\n"*200)

class MediaFileSystem:

    def __init__(self):
        self.format_keys = self.formats.keys()

        self.children = []

        self.__str_display_formats = "\n".join([f" [{i+1}] {format}" for i, format in enumerate(self.format_keys)])

    
    @property
    def formats(self):
        return {
            'png': PngFile, 
            'mp4': Mp4File,
            'mp3': Mp3File,
            'gif': GifFile
        }
    
    def show_mediafiles(self):
        
        instructions = (
            f"[All Mediafiles]\n"
            f"\t > Enter a number to view the corresponding file.\n"
        )
        error_message = str()
        choices = (
            f"\n{self.__str_display_formats}\n"
            f" [0] Return to Main Menu\n"
            f"\n"
            f">> Input: "
        )

        while True:

            try: 
                user_input = int(input(instructions + error_message + choices).strip())
                if user_input > len(self.children) or user_input < 0:
                    error_message = "\t## Please input an valid choice! ##"
                else:
                    break
            except ValueError:
                error_message = "\t## Please input an integer! ##"

        return user_input

    def open_mediafile_details(self, index):
        try:
            mediafile = self.children[index]
            

        except IndexError:
            input("## Index out of range ###")
            return 0

    def create_mediafile(self):
        ...
    
    


def main():

    while True:
        ...

if __name__ == '__main__':
    main()