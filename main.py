from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image, ImageChops
if __name__ == '__main__':
    #Изначальное видео
    clipname = "input.mp4"
    clip = VideoFileClip(clipname)
    #Референсный кадр
    clip.save_frame("ref.png", t=2)
    ref = Image.open("ref.png")
    reference=ref.resize([4,4])
    #Извлечение первичного видео
    ffmpeg_extract_subclip(clipname, 0.0, 1, targetname="result.mp4")
    len=clip.duration
    print(len)
    i=1
    final = VideoFileClip("result.mp4")
    withmen=VideoFileClip("withmen.mp4")
    flag=False
    while i!=len-1:
        try:
            #Вырезается фрагмент
            ffmpeg_extract_subclip(clipname, i, i+0.5, targetname="cut.mp4")
            partial=VideoFileClip("cut.mp4")
            #Из фрагмента берется кадр
            partial.save_frame("comp.png")
            comp = Image.open("comp.png")
            compatible = comp.resize([4, 4])
            #Находится разница в виде кортежа координат ненулевых пикселей на
            #изображении-разнице образца и вырезанного
            #Если изображения одинаковы, то изображение-разница пустое/полностью черное
            comparison = ImageChops.difference(reference, compatible).getbbox()
            if comparison == None:
                #приклеивание части, в которой нет человека, к результирующему видео
                final = concatenate_videoclips([final,partial])
            i+=0.5
        except Exception:
            final.write_videofile("result.mp4")
            i=len-1
            flag=True
    if flag==False:            
        final.write_videofile("result.mp4")
