import os

class FileHandler:
    def checkAsset():
        if os.path.isdir(f"asset") == False:
            os.mkdir("asset")
    def unzip(UID):
        if os.path.isfile(f"asset/{UID}.tar"):
            os.system(f"tar xfv asset/{UID}.tar")
        else:
            os.mkdir(f"asset/{UID}")
    def zip(UID):
        if os.path.isfile(f"asset/{UID}.tar"):
            os.system(f"rm asset/{UID}.tar")
        os.system(f"tar cfv asset/{UID}.tar asset/{UID}")
        os.system(f"rm -r asset/{UID}")
    
    def addFile(UID, MID, content):
        with open(f"asset/{UID}/{MID}", "w+", encoding="UTF-8") as ofs:
            ofs.write(content)
    
    def driver(UID, MID, content):
        FileHandler.checkAsset()
        FileHandler.unzip(UID)
        # content = FileHandler.load(UID, "test.JPEG")
        FileHandler.addFile(UID, MID, content)
        FileHandler.zip(UID)

# FileHandler.driver(1, 2, content)
