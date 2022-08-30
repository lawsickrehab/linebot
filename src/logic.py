from message import Message
from session import Session
from question import Question
from content import Content
from definition import Definition
from nlp import NLP

from content import ASK_DEF,UNDERSTAND,UNUNDERSTAND

def react(lst,nlp):
    if len(lst)==1:
        ans=NLP().parse(lst[0],[])
        print(ans)
        nlp.writejson(ans)
    nlp=nlp.readjson()
    init=1
    print(lst,nlp)
    for i,ans in enumerate(lst):
        if not i:
            continue
        if ans==UNDERSTAND or ans==UNUNDERSTAND or ans[0:len(ASK_DEF)]==ASK_DEF:
            if ans==UNDERSTAND or ans==UNUNDERSTAND:
                continue
            if ans[0:len(ASK_DEF)]==ASK_DEF and i==len(lst)-1:
                return Content().define(ans[len(ASK_DEF):])
            continue
        nxt=dfs(init,nlp)
        if nxt<0:
            return Message().text("closed.txt")
        nlp[nxt]=ans
    print(lst,nlp)
    ask=dfs(init,nlp)
    if ask<0:
        return Message().text("terminate.txt")
    return Content().ask(ask,definition=True)

    ret=Message()
    return ret.text("tmp.txt")
    
    print("action histroy: ",lst)
    if len(lst) == 1:
        return ret.flexqr('message5.json', 'tf2.json')
    elif len(lst) == 2:
        return ret.flexqr('message6.json', 'tf2.json')
    elif len(lst) == 3:
        return ret.flexqr('message7.json', 'tf2.json')
    elif len(lst) == 4:    
        return ret.flexqr('message8.json', 'tf2.json')
    elif len(lst) == 5:
        return ret.flex('message100.json')
    # return ret.textqr('test message','tf2.json')
    # return ret.text('test message')
    # return ret.flexqr('message8.json','tf2.json')
    return ret.text('')


def dfs(cur,path):
    if cur not in path.keys():
        return cur
    q=Question(cur)
    if path[cur][0:len(ASK_DEF)]==ASK_DEF:
        return cur
    try:
        ans=q.options.index(path[cur])
        nxt=q.judge[ans]
    except ValueError:
        ans=q.exception
        nxt=q.exception
    if nxt<0:
        return nxt
    return dfs(nxt,path)


def welcome():
    ret=Message()
    msg="""您好，這裡是溫暖而富有人性的證據收集器"""
    return ret.text(msg)
    return ret.textqr(msg,'tf2.json')

    
# You don't need to implement the download feature.
