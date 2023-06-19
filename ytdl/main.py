import sys
import argparse
from pytube import YouTube
from pytube.cli import on_progress

def run(link,itag,auto):
    yt=YouTube(link,on_progress_callback=on_progress)
    #Video
    print('--------------')
    print('|    Video    |')

    lv=[i for i in yt.streams.filter(
        type='video',file_extension='mp4')]
    lv.sort(key=lambda i: int(i.resolution.rstrip('p')),reverse=True)

    print('itag progressive video_codec audio_codec res')
    for i in lv:
        print(i.itag,i.is_progressive,i.video_codec,i.audio_codec,i.resolution)

    #Audio
    print('--------------')
    print('|    Audio    |')
    la=[i for i in yt.streams.filter(
        type='audio',file_extension='mp4')]
    la.sort(key=lambda i: int(i.bitrate),reverse=True)
    print('itag progressive video_codec audio_codec bitrate abr')
    for i in la:
        print(i.itag,i.is_progressive,i.video_codec,i.audio_codec,i.bitrate,i.abr)
        #print(i.itag,i.is_progressive,i.video_codec,i.audio_codec,i.resolution)

    if itag:
        stream=yt.streams.get_by_itag(itag)
        stream.download()

    if auto:
        print('Download the highest resolution video')
        stream=yt.streams.get_by_itag(lv[0].itag)
        print(lv[0].itag)
        fv=stream.download()
        print(fv)
        print(type(fv))

        print('Download the highest resolution audio')
        print(la[0].itag)
        stream=yt.streams.get_by_itag(la[0].itag)
        fa=stream.download(filename_prefix='audio_')
        print(fa)

def cli():
    parser=argparse.ArgumentParser(description='Download Youtube Videos')
    parser.add_argument('-l','--link',help='Link',required=True)
    parser.add_argument('-i','--itag',help='Itag',type=int,required=False)
    parser.add_argument('-a','--auto',action='store_true',default=False)

    args=parser.parse_args()
    run(args.link,args.itag,args.auto)

if __name__=='__main__':
    cli()
