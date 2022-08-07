from genericpath import isfile
import os
import tarfile

class FileHandler:
    def checkAsset():
        if os.path.isdir(f"asset") == False:
            os.mkdir("asset")
    def unzip(UID):
        os.chdir(f"asset")
        os.mkdir(f"{UID}")
        if os.path.isfile(f"{UID}.tar"):
            os.system(f"mv {UID}.tar {UID}/{UID}.tar")
            os.chdir(f"{UID}")
            os.system(f"tar xvf {UID}.tar > tar.log")
            if os.path.isfile("tar.log"):
                os.system(f"rm tar.log")
            os.system(f"rm {UID}.tar")
            os.chdir("..")
        os.chdir("..")

    def zip(UID, MID):
        if os.path.isfile(f"asset/{UID}.tar"):
            os.system(f"rm asset/{UID}.tar")
        os.chdir(f"asset/{UID}")
        os.system(f"tar cvf {UID}.tar * > tar.log")
        if os.path.isfile("tar.log"):
            os.system(f"rm tar.log")
        os.chdir("..")
        os.system(f"mv {UID}/{UID}.tar {UID}.tar")
        os.chdir("..")
        os.system(f"rm -r asset/{UID}")
    
    def addFile(UID, MID, content):
        with open(f"asset/{UID}/{MID}", "w+", encoding="UTF-8") as ofs:
            ofs.write(content)
    
    def driver(UID, MID, content):
        FileHandler.checkAsset()
        FileHandler.unzip(UID)
        content = "test"
        FileHandler.addFile(UID, MID, content)
        FileHandler.zip(UID, MID)

FileHandler.driver(2, 5, "")
