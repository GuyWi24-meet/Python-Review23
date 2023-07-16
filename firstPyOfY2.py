def create_youtube_video(title,description):
	newvid = {"title":title,"description":description,"likes":0,"dislikes":0,"comments": {"user":user,"comment":comment_text}}
	return newvid
title = input("Enter your video title: ")
description = input("Enter your video description: ")
print(create_youtube_video(title,description))

def like(newvid):
	if "likes" in newvid:
		newvid["likes"] +1
		return newvid
def dislike(newvid):
	if "dislikes" in newvid:
		newvid["dislikes"] +1
		return newvid

def comment(newvid,user,comment_text):
	if "comments" in newvid:
		user = input("enter username: ")
		comment_text = input("enter your comment")
		return newvid
x = input("if you wish to like, dislike or commnt on the video, just type one of the following [like] [dislike] [comment]")
if x == "like":
	like
elif x== "dislike":
	dislike
elif x== "comment":
	comment
else:
	print("error")