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

    msgcom = ['"Like if" comments are overrated', 'lmaoooo', 'dislike if you hate me', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'daily chat goes nuts', 'poll: i am gay (vote with likes/dislikes)', 'insert comment', ' ', 'like if you ever posted a like if comment (lmao)', 'lemme surpass top comment', 'laughterhouse', 'iWantLikes', '69% gang', 'coin 4: be a furry', 'LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT LONG COMMENT', 'you cant spell slaughter without ugh', 'is this place DC or WC?', 'pro tip: say UwU', 'hasgzuasdgauzsduzagsduzaduzgbcjhyxg', 'worlds smallest violin sucks', 'ayy lmao', 'kek', 'it annoys me when someone posts a like if comment and gets top comment (now like this comment if you agree, lmao)', 'mario movie is cool', 'this chat is sponsored by raid shadow legends', 'why do mods ban everyone who uses autoworks', 'This is the comment help. You are welcome.', 'uhhhhhhh', 'gimmie these sweet likes UwU', 'controversal statement', 'something offensive', 'mario', 'i hate "like my profile post" comments', '69420 likes and I will do ABSOLUTELY NOTHING.', 'what to comment', 'how to get likes on a comme (insert windows nt)', '9 + 10 = {comment.likeCount}', 'sakujes', 'person above will fall in love with the concept', 'person below will like this comment', '#AdvyOut', 'spam #AdvyOut, and like every #AdvyOut comment', 'GG', 'fvck putin (like = agree)', 'this comment has 69 likes', 'DC is now WC?', 'hi, bye', 'hi daily chat', 'numberstada sucks', 'i am pooping on a toilet', 'unsabscribe mohammed ja kalem', 'insert a randomish cringe comment', 'mario movie is actually good', 'bramblepee', 'bobb719 is cringe', 'this is my 69420th comment', 'check my profile (VANYADFYZ REFERENCE)', 'no cap bro', 'like for messi, dislike for ronaldo', 'W', 'claim your "here before 696969 likes" ticket *gets tickets to ohio instead*', '1 like and the daily chat becomes 1% less cringe', 'the chances of this getting top comment is lower than the chance of RobTop releasing 2.2 in the next 30 years', 'join giantmode (gmd team account)', 'vy vsichni sakujete dikisy', 'acheron does not deserve to be top 1', '#NumbersTadaOut', 'sikky is too old to play gd', 'i hacked this comment so it is absolutely normal', 'i hate wave practice vsc jokes', 'topkek', 'play 69696969', 'motorku', 'person above is swagistic', 'BROOOOOOOOOOOOOOOOOOOO', 'linode01 is poop', 'dislike this comment if I am gayish', 'like = pro, dislike = noob, ignore = hacker/fvcker', 'Google Translate: "A man is running" to Dailychatese: "K furry is UwUing"', 'insert comment v2', 'swag', 'join silvrps', 'gmd', 'i feel like leaving daily chat', 'Hey guys, I am Dad', 'Like or dislike this comment, it does not matter.']
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
