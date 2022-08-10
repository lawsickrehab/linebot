from genericpath import isfile
import os
import tarfile

class FileHandler:
    def checkAsset():
        if os.path.isdir(f"asset") == False:
            os.mkdir("asset")
    def unzip(param):
        UID = param.get('UID', '')
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

    def zip(param):
        UID = param.get('UID', '')
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
    
    def get(param):
        UID = param.get('UID', '')
        MIDS = os.listdir(f'asset/{UID}')
        ret = {}
        for MID in MIDS:
            with open(f"asset/{UID}/{MID}", "r", encoding="UTF-8") as ifs:
                ret[MID] = ifs.read()
        return ret
    
    def post(param):
        UID = param.get('UID', '')
        MID = param.get('MID', '')
        content = param.get('content', '')
        with open(f"asset/{UID}/{MID}", "w+", encoding="UTF-8") as ofs:
            ofs.write(content)
        return "Success"
    
    def view(Method, param):
        FileHandler.checkAsset()
        FileHandler.unzip(param)
        if Method == "GET":
            res = FileHandler.get(param)
        elif Method == "POST":
            res = FileHandler.post(param)
        print(res)
        FileHandler.zip(param)

param = {
    'UID': 1,
    'MID': 8,
    'content': 'test8'
}
FileHandler.view("GET", param)
