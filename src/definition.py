import json

class Definition:
    def __init__(self):
        with open("resources/definition.json",'r') as jfile:
            self.dic=json.load(jfile)
        print(self.dic)

    def search(self,key):
        return self.dic.get(key,f"Sorry, no definition found for {key}.")
        
