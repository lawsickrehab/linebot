import json

def react(lst):
    print("action histroy: ",lst)
    # decide what to return here, a text message or a flex messge
    # return a pair<type in string, message>
    if len(lst)==1:
        return text("this is the first message")
    elif len(lst)==2:
        return text("second message: You can send me any text message, and I will reply you in fixed sequence. Good tool for demo, isn't it?")
    elif len(lst)==3:
        return text("this is the third, the next one will be a flex message")
    elif len(lst)==4:
        return flex("tmp.json")
    elif len(lst)==5:
        return text("I have no idea what to test next")
    elif len(lst)==6:
        return text("Do you want to know how to restart session?")
    else:
        return text("You can type \"delete\" (without space) to clear your history.")
    
    return text("tmp.json")

def flex(fname):
    with open('resources/flex/'+fname,'r') as jfile:
        content=json.load(jfile)
    return "FLEX",content

def text(content):
    return "TEXT",content

