#Defining a function that tell us the that what type of file is it by checking the last name of file
def Mishra():
    Extension = input("File Name: ").lower().split(".")[-1]

    match Extension:
        case "gif":
            return("image/gif")
        case "jpg" | ".jpeg":
            return("image/jpg")
        case "png":
            return("image/png")
        case "pdf":
            return("file.pdf")
        case "txt":
            return("file.txt")
        case _:
            return("application/octet-stream")
        
print(Mishra())