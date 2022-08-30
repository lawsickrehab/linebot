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
        nlp.writejson(ans)
    nlp=nlp.readjson()
    init=1
    for i,ans in enumerate(lst):
        if not i:
            continue
        nxt=dfs(init,nlp)
        if nxt<0:
            return Message().text("closed.txt")
        nlp[nxt]=ans
    print(lst,nlp)
    ask=dfs(init,nlp)
    if ask<0:
        return Message().text("ans.txt")
    return Content().ask(ask,definition=True)

def dfs(cur,path):
    if cur not in path.keys():
        return cur
    q=Question(cur)
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
