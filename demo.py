from mediafile import PngFile, Mp4File, Mp3File, GifFile
from datetime import timedelta

def png_demo():
    input(">> PNG Demo: Start demo for a PNG file")
    print()


    input("Create PNG file")
    img = PngFile("landscape", 512, 1080, 1920)
    input(f"[ACTION] PngFile('landscape', 512, 1080, 1920)")
    input(f"[INFO] Created PNG file: {img.name}.{img.format}, Size: {img.size}KB, Opened: {img.is_active}, Dimensions: {img.height}x{img.width}")
    print()

    input("Open the file")
    input(f"[ACTION] img.open()")
    input(f"[RESPONSE] {img.open()}")
    input(f"[INFO] Created PNG file: {img.name}.{img.format}, Size: {img.size}KB, Opened: {img.is_active}, Dimensions: {img.height}x{img.width}")
    print()

    input("Close the file")
    input(f"[ACTION] img.close()")
    input(f"[RESPONSE] {img.close()}")
    input(f"[INFO] Created PNG file: {img.name}.{img.format}, Size: {img.size}KB, Opened: {img.is_active}, Dimensions: {img.height}x{img.width}")
    print()

def mp4_demo():
    input(">> MP4 Demo: Start demo for a MP4 file")
    print()

    input("Create MP4 file")
    video = Mp4File("video", 1024, 1080, 1920, timedelta(seconds=42, minutes=10))
    input(f"[ACTION] Mp4File('video', 1024, 1080, 1920)")
    print(f"[INFO] Created MP4 file: {video.name}.{video.format}, Size: {video.size}KB, Opened: {video.is_active}, Dimensions: {video.height}x{video.width}, Duration {video.duration}")
    input(f"       Playing: {video.is_playing}, Muted: {video.is_muted}")
    print()

    input("Open the file")
    input(f"[ACTION] video.open()")
    input(f"[RESPONSE] {video.open()}")
    print(f"[INFO] Created MP4 file: {video.name}.{video.format}, Size: {video.size}KB, Opened: {video.is_active}, Dimensions: {video.height}x{video.width}, Duration {video.duration}")
    input(f"       Playing: {video.is_playing}, Muted: {video.is_muted}")
    print()

    input("Pause/Resume the file")
    input(f"[ACTION] video.toggle_pause()")
    input(f"[RESPONSE] {video.toggle_pause()}")
    print(f"[INFO] Created MP4 file: {video.name}.{video.format}, Size: {video.size}KB, Opened: {video.is_active}, Dimensions: {video.height}x{video.width}, Duration {video.duration}")
    input(f"       Playing: {video.is_playing}, Muted: {video.is_muted}")
    print()

    input("Mute/Unmute the file")
    input(f"[ACTION] video.toggle_mute()")
    input(f"[RESPONSE] {video.toggle_mute()}")
    print(f"[INFO] Created MP4 file: {video.name}.{video.format}, Size: {video.size}KB, Opened: {video.is_active}, Dimensions: {video.height}x{video.width}, Duration {video.duration}")
    input(f"       Playing: {video.is_playing}, Muted: {video.is_muted}")
    print()

    input("Close the file")
    input(f"[ACTION] video.close()")
    input(f"[RESPONSE] {video.close()}")
    print(f"[INFO] Created MP4 file: {video.name}.{video.format}, Size: {video.size}KB, Opened: {video.is_active}, Dimensions: {video.height}x{video.width}, Duration {video.duration}")
    input(f"       Playing: {video.is_playing}, Muted: {video.is_muted}")
    print()

def mp3_demo():
    input(">> MP3 Demo: Start demo for an MP3 file")
    print()

    input("Create MP3 file")
    song = Mp3File("lofi", 320, timedelta(minutes=3, seconds=45))
    input(f"[ACTION] Mp3File('lofi', 320, 0:03:45)")
    print(f"[INFO] Created MP3 file: {song.name}.{song.format}, Size: {song.size}KB, Opened: {song.is_active}, Duration: {song.duration}")
    input(f"       Playing: {song.is_playing}, Muted: {song.is_muted}")
    print()

    input("Open the file")
    input(f"[ACTION] song.open()")
    input(f"[RESPONSE] {song.open()}")
    print(f"[INFO] MP3 file: {song.name}.{song.format}, Opened: {song.is_active}, Duration: {song.duration}")
    input(f"       Playing: {song.is_playing}, Muted: {song.is_muted}")
    print()

    input("Pause/Resume the file")
    input(f"[ACTION] song.toggle_pause()")
    input(f"[RESPONSE] {song.toggle_pause()}")
    print(f"[INFO] MP3 file: {song.name}.{song.format}, Opened: {song.is_active}, Duration: {song.duration}")
    input(f"       Playing: {song.is_playing}, Muted: {song.is_muted}")
    print()

    input("Mute/Unmute the file")
    input(f"[ACTION] song.toggle_mute()")
    input(f"[RESPONSE] {song.toggle_mute()}")
    print(f"[INFO] MP3 file: {song.name}.{song.format}, Opened: {song.is_active}, Duration: {song.duration}")
    input(f"       Playing: {song.is_playing}, Muted: {song.is_muted}")
    print()

    input("Close the file")
    input(f"[ACTION] song.close()")
    input(f"[RESPONSE] {song.close()}")
    print(f"[INFO] MP3 file: {song.name}.{song.format}, Opened: {song.is_active}, Duration: {song.duration}")
    input(f"       Playing: {song.is_playing}, Muted: {song.is_muted}")
    print()

def gif_demo():
    input(">> GIF Demo: Start demo for a GIF file")
    print()

    input("Create GIF file")
    gif = GifFile("dancing_cat", 150, 500, 500, timedelta(seconds=12))
    input(f"[ACTION] GifFile('dancing_cat', 150, 500, 500, 0:00:12)")
    print(f"[INFO] Created GIF file: {gif.name}.{gif.format}, Size: {gif.size}KB, Opened: {gif.is_active}, Dimensions: {gif.height}x{gif.width}, Duration: {gif.duration}")
    input(f"       Playing: {gif.is_playing}")
    print()

    input("Open the file")
    input(f"[ACTION] gif.open()")
    input(f"[RESPONSE] {gif.open()}")
    print(f"[INFO] GIF file: {gif.name}.{gif.format}, Opened: {gif.is_active}, Dimensions: {gif.height}x{gif.width}, Duration: {gif.duration}")
    input(f"       Playing: {gif.is_playing}")
    print()

    input("Pause/Resume the file")
    input(f"[ACTION] gif.toggle_pause()")
    input(f"[RESPONSE] {gif.toggle_pause()}")
    print(f"[INFO] GIF file: {gif.name}.{gif.format}, Opened: {gif.is_active}, Dimensions: {gif.height}x{gif.width}, Duration: {gif.duration}")
    input(f"       Playing: {gif.is_playing}")
    print()

    input("Close the file")
    input(f"[ACTION] gif.close()")
    input(f"[RESPONSE] {gif.close()}")
    print(f"[INFO] GIF file: {gif.name}.{gif.format}, Opened: {gif.is_active}, Dimensions: {gif.height}x{gif.width}, Duration: {gif.duration}")
    input(f"       Playing: {gif.is_playing}")
    print()


if __name__ == "__main__":
    png_demo()
    input("\n"*10)
    mp4_demo()
    input("\n"*10)
    mp3_demo()
    input("\n"*10)
    gif_demo()