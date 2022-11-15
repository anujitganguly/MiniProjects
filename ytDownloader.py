import pytube

url = input("Enter complete URL: ")
yt = pytube.YouTube(url)
yt.streams.first().download()

print('Downloaded', url)

#### Future Scope: Need to explore ways to download in high quality