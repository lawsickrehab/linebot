import json

def react(lst):
    print("action histroy: ",lst)
    # decide what to return here, a text message or a flex messge
    # return a pair<type in string, message>
    
    return text("tmp.json")

def flex(fname):
    with open('resources/flex/'+fname,'r') as jfile:
        content=json.load(jfile)
    return "FLEX",content

def text(content):
    return "TEXT",content

