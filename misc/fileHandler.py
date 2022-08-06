import os

class FileHandler:
    def unzip(UID):
        if os.path.isfile(f"misc/asset/{UID}.tar"):
            os.system(f"tar xfv misc/asset/{UID}.tar")
        else:
            os.mkdir(f"misc/asset/{UID}")
    def zip(UID):
        os.system(f"tar cfv misc/asset/{UID}.tar misc/asset/{UID}")
    
    def load(UID, filename):
        res = None
        with open(f"misc/asset/{UID}/{filename}", "r", encoding="UTF-8") as ofs:
            res = ofs.read()
        return res
    
    def addFile(UID, MID, content):
        with open(f"misc/asset/{UID}/{MID}", "w+", encoding="UTF-8") as ofs:
            ofs.write(content)
    
    def driver(UID, MID, content):
        FileHandler.unzip(UID)
        # content = FileHandler.load(UID, "test.JPEG")
        FileHandler.addFile(UID, MID, content)
        FileHandler.addFile(UID, 1)
        FileHandler.zip(UID)

# FileHandler.driver(1, 2, content)