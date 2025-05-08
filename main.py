from mediafile import PngFile, Mp4File, Mp3File, GifFile


MediaFileType = PngFile | Mp4File | Mp3File | GifFile

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
        
        details = (
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
                user_input = int(input(details + error_message + choices).strip())
                if user_input > len(self.children) or user_input < 0:
                    error_message = "\t > ## Please input an valid choice! ##"
                else:
                    break
            except ValueError:
                error_message = "\t > ## Please input an integer! ##"

        return user_input
    
    
    def create_mediafile(self):
        ...

    def open_mediafile_details(self, index):
        try:
            mediafile: MediaFileType = self.children[index]

            title = f"[Mediafile: {mediafile.name}.{mediafile.format}]\n"
            error_message = str()

            details_list = [
                ("Currently Open", mediafile.is_active),
                ("Size", mediafile.size),
                ("Created At", mediafile.created_at),
                ("Last Accessed At", mediafile.accessed_at)
            ]

            while True:

                match mediafile.format:
                    case 'png':
                        properties_list = [
                            ("Dimensions", f"{mediafile.width}x{mediafile.height}")
                        ]
            
                        choices = (
                            f" [1] Close"
                            f" [2] Delete"
                            f" [3] Rename"
                            f" [0] Return to Main Menu\n"
                            f"\n"
                            f">> Input: "
                        )

                        max_choice = 3

                    case 'mp4':

                        properties_list = [
                            ("Dimensions", f"{mediafile.width}x{mediafile.height}")
                        ]
                        
                        if mediafile.is_active:
                            if mediafile.is_playing:
                                play_symbol = '⏸️'
                            else:
                                play_symbol = '▶️'

                            if mediafile.is_muted: 
                                unmute_symbol = '🔈' 
                            else: 
                                unmute_symbol = '🔇'

                            properties_list.append(("Playback", f"{play_symbol} {unmute_symbol}"))
            
                        choices = (
                            f" [1] Close\n"
                            f" [2] Delete\n"
                            f" [3] Rename\n"
                            
                            f" [4] Toggle Play/Pause\n"
                            f" [5] Toggle Mute/Unmute\n"

                            f" [0] Return to Main Menu\n"
                            f"\n"
                            f">> Input: "
                        )

                        max_choice = 5
                    case 'mp3':
                        ...
                    case 'gif':
                        ...

        except IndexError:
            input("## Index out of range ##")
            return 0



def main():

    while True:
        ...

if __name__ == '__main__':
    main()