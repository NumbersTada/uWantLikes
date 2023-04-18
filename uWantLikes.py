from distutils.command.upload import upload
import time,requests,random,string,base64,hashlib
from json import loads
from threading import Thread
from itertools import cycle
from urllib3 import connection

print("uWantLikes Bot by NumbersTada (run this on daily level)")
un = input("Enter your Geometry Dash username: ")
pw = input("Enter your Geometry Dash password: ")
percentage = input("Enter your fake percentage (0 = None): ")

def request(self, method, url, body=None, headers=None):
    if headers is None:
        headers = {}
    else:
        # Avoid modifying the headers passed into .request()
        headers = headers.copy()
    super(connection.HTTPConnection, self).request(method, url, body=body, headers=headers)
connection.HTTPConnection.request = request

def comment_chk(*,username,comment,levelid,percentage,type):
	part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
	return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def xor(data, key):
	return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
	return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
	return xor(base64.b64decode(data.encode()).decode(),"37526")

def getGJUsers(target):
    data={
        "secret":"Wmfd2893gb7",
        "str":target
    }
    request =  requests.post("http://www.boomlings.com/database/getGJUsers20.php",data=data,headers={"User-Agent": ""}).text.split(":")[1::2]
    print(request)
    username = request[0]
    uuid = request[2]
    accountid = request[10]
    return (username,accountid,uuid)

def uploadGJComment(name,passw,comment,perc,level):
        try:
                accountid = getGJUsers(name)[1]
                gjp = gjp_encrypt(passw)
                c = base64.b64encode(comment.encode()).decode()
                chk = comment_chk(username=name,comment=c,levelid=str(level),percentage=perc,type="0")
                data={
                    "secret":"Wmfd2893gb7",
                    "accountID":accountid,
                    "gjp":gjp,
                    "userName":name,
                    "comment":c,
                    "levelID":level,
                    "percent":perc,
                    "chk":chk
                }
                return requests.post("http://www.boomlings.com/database/uploadGJComment21.php",data=data,headers={"User-Agent": ""}).text
        except:
                return "problem"
                
def commands(level):
    url=f"http://gdbrowser.com/api/comments/{level}?count=1"
    r=loads(requests.get(url).text)[0]
    u=r['username']
    com=r['content']
    perc=percentage

    msgcom = ['"Like if" comments are overrated', 'lmaoooo', 'dislike if you hate me', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'daily chat goes nuts', 'poll: i am gay (vote with likes/dislikes)', 'insert comment', ' ', 'like if you ever posted a like if comment (lmao)', 'lemme surpass top comment', 'laughterhouse', 'iWantLikes', '69% gang', 'coin 4: be a furry', 'LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT', 'you cant spell slaughter without ugh', 'is this place DC or WC?', 'pro tip: say UwU', 'hasgzuasdgauzsduzagsduzaduzgbcjhyxg', 'worlds smallest violin sucks', 'ayy lmao', 'kek', 'it annoys me when someone posts a like if comment and gets top comment (now like this comment if you agree, lmao)', 'mario movie is cool', 'this chat is sponsored by raid shadow legends', 'why do mods ban everyone who uses autoworks', 'This is the comment help. You are welcome.']
    randcom = random.choice(msgcom)

    uploadGJComment(un,pw,randcom,perc,level)

lvl=input("Enter the ID of the level where the bot will run: ")

while 1:
    try:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(28)
    except:
        print("Error")
