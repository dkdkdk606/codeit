import youtube_dl

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=X4tEu4ibrJg'])

#with open 으로 파일 열고닫은적이 있지
#vscode 외부 패키지 받는거 대충 할줄 알게됨