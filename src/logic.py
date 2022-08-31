from message import Message
from session import Session
from question import Question
from content import Content
from definition import Definition
from nlp import NLP

from content import ASK_DEF,UNDERSTAND,UNUNDERSTAND

init=1

def react(lst,nlp):
    ans=gen(lst,nlp)
    print(lst,ans)
    ask=dfs(init,ans)
    if ask<0:
        return Message().text("ans.txt")
    return Content().ask(ask,definition=True)

def gen(lst,nlp):
    if len(lst)==1:
        ans=NLP().parse(lst[0],[])
        nlp.writejson(ans)
    ans=nlp.readjson()
    for i,rep in enumerate(lst):
        if not i:
            continue
        nxt=dfs(init,ans)
        assert nxt>0
        ans[nxt]=rep
    return ans

    

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
    msg="""您好，這裡是溫暖而富有人性的證據收集器。\n\n請問您遇到了什麼困難，說出來說不定我們能夠幫助您喔～"""
    return ret.text(msg)
    return ret.textqr(msg,'tf2.json')

    
# You don't need to implement the download feature.
