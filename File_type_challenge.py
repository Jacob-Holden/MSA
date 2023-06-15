#Prompt the user to enter the filename with extenstion "File name: "
#convert the file name to all lowecase
#find and determine the file type
#Print the file type to the user

#.gif (image/gif)
#.jpg (image/jpg)
#.jpeg (image/jpeg)
#.png (image/png)
#.pdf (document/pdf)
#.txt (document/txt)
#.zip (file/zip)

file_name= input("File name: ").lower()
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg"):
    print("image/jpg")
elif file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("document/pdf")
elif file_name.endswith(".txt"):
    print("document/txt")
elif file_name.endswith(".zip"):
    print("file/zip")
else:
    print("application/octet-stream")