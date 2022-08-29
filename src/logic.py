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

    return dfs(1,nlp)

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
    path={
        1:0,
        3:0,
        4:1,
        8:0
    }
    if cur not in path.keys():
        return Content(cur).ask()
    if path[cur]<0:
        print("dfs finished, got negtive answer.")
        ret=Message()
        return ret.text("tmp.text")
    print(cur)
    q=Question(cur)
    assert path[cur]<q.size, "answer out of range"
    print("question",cur,"answered, moved on next question:", q.judge[path[cur]])
    return dfs(q.judge[path[cur]],path)


def welcome():
    ret=Message()
    msg="""您好，這裡是溫暖而富有人性的證據收集器"""
    return ret.text(msg)
    return ret.textqr(msg,'tf2.json')

    
# You don't need to implement the download feature.
