#%%
from ArticutAPI import Articut
import json
import re

#%%
class API:
    def __init__(self) -> None:
        with open("resources/account.json") as file:
            accountDict = json.loads(file.read())
        
        username = accountDict["email"]
        apikey = accountDict["apikey"]
        self.atc = Articut(username=username, apikey=apikey)

    def parse(self, str: str, level: str ='lv2'):
        self.result = self.atc.parse(str, level=level, chemicalBOOL=False)

    def getAllAttributes(self):
        attributes = []
        for sentence in self.result["result_obj"]:
            for word in sentence:
                if word["pos"] not in attributes:
                    attributes.append(word["pos"])
        attributes.sort()
        return attributes

    def getWordWithAttributes(self, attribute: str):
        ans = []
        for sentence in self.result["result_obj"]:
            for word in sentence:
                if word["pos"] == attribute and word["pos"] not in ans:
                    ans.append(word["text"])
        return ans

    def getResultWithTags(self, join: bool =False):
        if join:
            return ''.join(self.result["result_pos"])
        else:
            return self.result["result_pos"]

    def __removeTags(self, preString: str):
        regx = "<[^<]*?>"
        return re.sub(regx, '', preString)

    def getLawReason(self):
        for regx in self.regxs1:
            for match in regx.findall(self.getResultWithTags(join=True)):
                print(self.__removeTags(match))

    def getNouns(self) -> list:
        return self.atc.getNounStemLIST(self.result)
    
