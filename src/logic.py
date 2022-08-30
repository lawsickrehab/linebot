from message import Message
from session import Session
from question import Question
from content import Content

def react(lst,nlp):
    if len(lst)==1:
        # call nlp api by lst[0]
        ans={"test":"dictionary returned by nlp api, save it!"}
        nlp.writejson(ans)
    nlp=nlp.readjson()
    print(lst,nlp)
    init=1
    for i,ans in enumerate(lst):
        if not i:
            continue
        nxt=dfs(init,nlp)
        assert nxt>0
        nlp[nxt]=ans

    ask=dfs(init,nlp)
        
    if ask<0:
        return Message().text("tmp.txt")
        
    return Content(ask).ask()

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
    ans=path[cur]
    nxt=q.judge[ans]
    print(cur,nxt)
    if nxt<0:
        return nxt
    assert ans<q.size, "answer out of range"
    return dfs(nxt,path)


def welcome():
    ret=Message()
    msg="""您好，這裡是溫暖而富有人性的證據收集器"""
    return ret.text(msg)
    return ret.textqr(msg,'tf2.json')

    
# You don't need to implement the download feature.
