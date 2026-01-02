import yt_dlp
yt_dlp.YoutubeDL({"format": "best"}).download([input("URL: ")])