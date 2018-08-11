# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata
_session = requests.session()
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#================EvVcY4Nk9hKiJZYdRMW3.TAVOkm2wqPizxdXz1JiGmW.4QUmFeBLiOjPKtdV7+ddmEw6IuVk/aIHke+OWKLmu/Q===============================================================#
#line = LINE()
#line = LINE("เมล","พาส")
line = LINE('')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login Succes")

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

oepoll = OEPoll(line)
#call = Call(line)

Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u4722f77c4dab0fa1e12e3961c908451d",lineMID]
admin=['u4722f77c4dab0fa1e12e3961c908451d',lineMID]
RfuFamily = RfuBot + Family
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#

settings = {
    "autoAdd": False,
    "autoBlock": False,
    "autoJoin": True,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": True,
    "autoRead": False,
    "autoReply": False,
    "botcancel": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": True,
    "delayMention": False,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "Nk": False,
    "Api": False,
    "Aip": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "detectMentionPM": False,
    "dwhitelist": False,
    "gift": False,
    "likeOn": False,
    "timeline": False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile": False,    
    "changeVideo": False,
    "chatMessage": "dih",
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome":"คุณยังไม่ได้ตั้งข้อความคนเข้า",
    "kick":"คุณยังไม่ได้ตั้งข้อความคนลบ",
    "bye":"คุณยังไม่ได้ตั้งข้อความคนออก",
    "Respontag":""" β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭 """,
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับ ⓉⒾⒼⒺⓇ⑥⑨ โดยพิมคำสั่ง */ผส*เพื่อแสดง คท ของผู้สร้างหรือสะดวกโทร 0899515060",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "notag": False,
    "pcancel": False,
    "pinvite": False,
    "pmMessage": "ว่าไงครับว่างเดื้ยวเห็นข้อความจะมาตอบนะครับ",
    "qrp": False,
    "readerPesan": " แอบทำไมครับ✧ออกมาคุยกันหน่อย",
    "replyPesan": "Sorry , i'm busy right now.",
    "responGc": True,
    "responcall": False,
    "responcallgc": False,
    "restartPoint": "u44284195e461bf2a7aab393a4cddff05",
    "server": "VPS",
    "ksticker": False,
    "timeRestart": "18000",
    "message1":"✧ⓉⒾⒼⒺⓇ⑥⑨✧",
    "message":"บัญชีนี้ถูกป้องกันโดย ✧ⓉⒾⒼⒺⓇ⑥⑨✧ ระบบได้ทำการบล็อคคุณอัตโนมัติเนื่องจากคุณยังไม่ได้ยืนยันตัวตนกับผู้สร้างบอท\n╔══════════════════╠\nβ¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭\n╠══════════════════\n╠❂รับติดตั้งบอทป้องกันกลุ่มไลน์\n╠❂รับติดตั้งบอทแทค&ต้อนรับ\n╠❂รับทำบอทโต้ตอบ\n╠❂รับทำบอท SELFBOT\n╠❂จำหน่ายตั๋ว siri v10\n╠❂เช่าเซิฟเวอร์ python3 JP\n╠❂รับปรึกษาปัญหาบอท\n╚══════════════════\n\n🎀สนใจรีบทัก🎀🎉บอทpython3ฟังชั่นล้นหลาม\nคุณภาพแน่นปึ๊ก🎁กำลังรอให้คุณเป็นเจ้าของ....🎋\nสนใจรีบโทร📲0899515060📞",
    "comment":"""β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭""",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addPesan": "β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " ว่าไง? ",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "52002736",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "leaveSticker": {
                "STKID": "51626494",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "51626530",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "readerSticker": {
                "STKID": "13188540",
                "STKPKGID": "1327110",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "33158349",
                "STKPKGID": "10788",
                "STKVER": "1"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "22832841",
                "STKPKGID": "1705396",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    }
}
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
    "autoBlock": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
                        
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(lineMID).pictureStatus, line.getContact(lineMID).displayName)
                    except Exception as error:
                        logError(error)
                        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    line.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            line.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def myhelp():
    myHelp = """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
      ⇱✎คำสั่งทั่วไป✎⇲
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸      
✎ คำสั่ง คำสั่งทั้งหมด
✎ คำสั่ง1 คำสั่งเซลบอท
✎ คำสั่ง2 คำสั่งในกลุ่ม
✎ คำสั่ง3 คำสั่งตั้งค่า
✎ คำสั่ง4 คำสั่งโซเชล
✎ คำสั่ง5 คำสั่งพูดMp3
✎ คำสั่ง6 คำสั่งแปลภาษา
✎ ตั้งค่า เชคการตั้งค่า
✎ คท/ตัวเรา
✎ ผส คท.ผู้สร้าง
✎ ข้อมูล ข้อมูลตัวเอง
✎ ข้อมูล @ ข้อมูลคนแทค
✎ มิด @ แล้วแทคร่าง
✎ ชื่อ @ แล้วแทคร่าง
✎ ตัส @ แล้วแทคร่าง
✎ รูป @ แล้วแทคร่าง
✎ ปก @ แล้วแทคร่าง
✎ คท @ แล้วแทคร่าง
✎ วีดีโอ @ แล้วแทคร่าง
✎ มิดล่อง พิมส่งลงห้อง
✎ คทล่อง พิมส่งลงห้อง
✎ แทคล่อง พิมส่งลงห้อง
✎ วันที่ ดูเวลาวันที่ปฏิทิน
✎ Mimic on/off
✎ เชคเลียนแบบ ดูที่เราเลียนแบบ
✎ เลียนแบบ @แทคคนที่เลียน
✎ ลบเลียนแบบ @แทคคนที่เลียน
✎ ส่งเสียงกลุ่ม พิมข้อความส่ง
✎ ส่งเสียงแชท พิมข้อความส่ง
✎ ประกาศกลุ่ม พิมข้อความส่ง
✎ ประกาศแชท พิมข้อความส่ง
✎ ส่งรูปภาพตามกลุ่ม ลิ้งรูป
✎ ส่งรูปภาพตามแชท ลิ้งรูป
✎ เริ่มใหม่ รีบูสระบบใหม่
✎ ออน เช็คเวลาออน
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
    ⊰⊹⊰⊹หมายเหตุ⊰⊹⊰⊹
    
✎วิธีใช้ใส่/ด้านหน้าคำสั่งทุกครั้งครับ\n!ระบบขัดข้องโทรแจ้ง📲0899515060
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"""
    return myHelp

def listgrup():
    listGrup = """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
      ⇱❦คำสั่งในกลุ่ม❦⇲
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸      
❦ แอด
❦ ชื่อกลุ่ม
❦ ไอดีกลุ่ม
❦ เปิดลิ้ง
❦ ปิดลิ้ง
❦ ลิ้ง
❦ ลิ้งกลุ่ม
❦ รายการกลุ่ม
❦ สมาชิกกลุ่ม
❦ ข้อมูลกลุ่ม
❦ รูปกลุ่ม
❦ แทก
❦ แทค
❦ เชคไอดี
❦ ไอดีล่อง
❦ คทล่อง
❦ แทคล่อง
❦ แทค จำนวน @
❦ คลอ จำนวน
❦ โทร จำนวน
❦ แทคล่อง
❦ คนแอบ
❦ คนอ่าน
❦ รีคนอ่าน
❦ แอบ
❦ คำห้ามพิม ข้อความ
❦ เชคคำห้ามพิม
❦ ล้างคำห้ามพิม ข้อความ
❦ แจก จำนวน @
❦ เปลี่ยนรูปกลุ่ม
❦ เปิด/ปิดแสกน
❦ เปิด/ปิดต้อนรับ
❦ เปิด/ปิดคนออก
❦ ปิด/ปิดทักเตะ
❦ เปิด/ปิดApi
❦ เปิด/ปิดตรวจสอบ
❦ เปิด/ปิดรปภ
❦ เชคดำ
❦ ลงดำ
❦ ล้างดำ
❦ ไล่ดำ
❦ คทดำ
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
    ⊰⊹⊰⊹หมายเหตุ⊰⊹⊰⊹
    
✎วิธีใช้ใส่/ด้านหน้าคำสั่งทุกครั้งครับ\n!ระบบขัดข้องโทรแจ้ง📲0899515060
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"""
    return listGrup

def socmedia():
    socMedia = """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
       『♬คำสั่งโซเชลมีเดี่ย♬』
♬ วันที่
♬ ภาพ
♬ รูปภาพ พิมสั้ง
♬ ค้นหารูปภาพ พิมสั้ง
♬ ยูทูป พิมสั้ง
♬ ฟังเพลง พิมสั้ง
♬ Lyric พิมสั้ง
♬ ค้นหาเว็ป  พิมสั้ง
♬ หนัง พิมสั้ง
♬ วีดีโอ พิมสั้ง
♬ ภาพ พิมสั้ง
♬ ไอจี ชื่อยูส
♬ แบน
♬ กลูเกลิ พิมสั้ง
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
    ⊰⊹⊰⊹หมายเหตุ⊰⊹⊰⊹
    
✎วิธีใช้ใส่/ด้านหน้าคำสั่งทุกครั้งครับ\n!ระบบขัดข้องโทรแจ้ง📲0899515060
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"""
    return socMedia

def helpset():
    helpSet = """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
         ⇱❧คำสั่งบอท❧⇲
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸         
❧ ตัวเรา         
❧ มิด
❧ ชื่อ
❧ ตัส
❧ รูป
❧ ปก
❧ เรว
❧ สปีด
❧ ทักเข้า
❧ ติ๊กคนเข้า
❧ ลบติ๊กคนเข้า
❧ ทักออก
❧ ติ๊กคนออก
❧ ลบติ๊กคนออก
❧ ทักเตะ
❧ ติ๊กคนเตะ
❧ ลบติ๊กคนเตะ
❧ คอมเม้น
❧ ข้อความแทค
❧ ติ๊กคนแทค
❧ ลบติ๊กคนแทค
❧ ข้อความแอด
❧ ติ๊กคนแอด
❧ ลบติ๊กคนแอด
❧ ข้อมูล @ แทคคน
❧ ชื่อ: พิมสั้ง
❧ ตัส: พิมสั้ง
❧ ตั้งเข้า: พิมสั้ง 
❧ ตั้งติ๊กคนเข้า: พิมสั้ง
❧ ตั้งออก: พิมสั้ง
❧ ตั้งติ๊กคนออก พิมสั้ง
❧ ทักเตะ: พิมสั้ง
❧ ตั้งติ๊กคนเตะ พิมสั้ง
❧ ตั้งแทค: พิมสั้ง
❧ ตั้งติ๊กคนแทค พิมสั้ง
❧ ตั้งคนแอด: พิมสั้ง
❧ ตั้งติ๊กคนแอด พิมสั้ง
❧ คอมเม้น: พิมสั้ง
❧ ออน
❧ ดำ
❧ ขาว
❧ แบน @
❧ ลบแบน @
❧ บลอค @
❧ ลบรัน
❧ ดึง
❧ ทัก [จำนวน] (แชท.สต)
❧ เตะ1 @
❧ เตะ2 @
❧ เตะ3 @
❧ เตะ3 @
❧ ไวรัส
❧ แปลงโฉม
❧ เพื่อน
❧ ไอดีเพื่อน
❧ ไอดีไลน์
❧ Gcancel:(จำนวนสมาชิก)
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
    ⊰⊹⊰⊹หมายเหตุ⊰⊹⊰⊹
    
✎วิธีใช้ใส่/ด้านหน้าคำสั่งทุกครั้งครับ\n!ระบบขัดข้องโทรแจ้ง📲0899515060
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"""
    return helpSet

def helpsetting():
    helpSetting = """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
        ⇱❃คำสั่งการตั้งค่า❃⇲
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸        
❃ เปิดกัน/ปิดกัน
❃ กันยก/ปิดกันยก
❃ กันเชิญ/ปิดกันเชิญ
❃ กันลิ้ง/ปิดกันลิ้ง
❃ กันเข้า/ปิดกันเข้า
❃ เปิดหมด/ปิดหมด
❃ เปิดกทม/ปิดรปภ
❃ เปิดเข้า/ปิดเข้า
❃ เปิดออก/ปิดออก
❃ เปิดติ๊ก/ปิดติ๊ก
❃ เปิดบลอค/ปิดบลอค
❃ เปิดมุด/ปิดมุด
❃ เปิดยกเลิก/ปิดยกเลิก
❃ เปิดอ่าน/ปิดอ่าน
❃ เปิดApi/ปิดApi
❃ เปิดแทค/ปิดแทค
❃ เปิดแทค2/ปิดแทค2
❃ เปิดแทค3/ปิดแทค3
❃ เปิดแทคเตะ/ปิดแทคเตะ
❃ เปิดคท/ปิดคท
❃ เปิดตรวจสอบ/ปิดตรวจสอบ
❃ เปิดเชคโฟส/ปิดเชคโฟส
❃ เปิดแสกน/ปิดแสกน
❃ เปิดต้อนรับ/ปิดต้อนรับ
❃ เปิดคนออก/ปิดคนออก
❃ เปิดแทคเตะ/ปิดแทคเตะ
❃ เปิดยกเลิก/ปิดยกเลิก
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
    ⊰⊹⊰⊹หมายเหตุ⊰⊹⊰⊹
    
✎วิธีใช้ใส่/ด้านหน้าคำสั่งทุกครั้งครับ\n!ระบบขัดข้องโทรแจ้ง📲0899515060
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"""
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
   ⇱คำสั่งพูดMp3ภาษาต่างๆ⇲
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸   
✧ af : แอฟริกัน
✧ sq : อัลเบเนีย
✧ hy : อาเมเนีย
✧ bn : เบนจาลี
✧ zh-cn : จีน
✧ zh-tw : ใต้หวัน
✧ cs : เช็ก
✧ nl : ดัช
✧ en : อังกฤษ
✧ en-us : สหรัฐ
✧ el : กรีก
✧ id : อินโดนีเซีย
✧ it : อิตาลี
✧ ja : ญี่ปุ่น
✧ ko : เกาหลี
✧ la : ลาติน
✧ ro : โรมาเนีย
✧ ru : รัสเซีย
✧ sr : เซอเบียร์
✧ th : ไทย
✧ vi : เวียดนาม
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
✎ระบบขัดข้องโทรแจ้ง📲0899515060📞
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸

⇱วิธีใช้ : say-th สวัสดีครับ⇲"""
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    """β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭
       ⇱คำสั่งแปลภาษา⇲
✧ af : แอฟริกัน
✧ sq : อัลเบเนีย
✧ ar : อราบิค
✧ hy : อาเมเนีย
✧ bn : บังการี่
✧ bs : บอสเนีย
✧ bg : บังแกเรีย
✧ zh-cn : จีน
✧ zh-tw : ใต้หวัน
✧ cs : เช็ก
✧ nl : ดัช
✧ en : อังกฤษ
✧ et : เอสโตเนียน
✧ el : กรีก
✧ id : อินโดนีเซีย
✧ ga : ไอริส
✧ it : อิตาลี
✧ ja : ญี่ปุ่น
✧ kn : แคนาดา
✧ la : ลาติน
✧ lv : ลัตเวีย
✧ ms : มาเลเซีย
✧ mt : มอลเตส
✧ mn : มองโกเลีย
✧ my : พม่า
✧ fa : เปอร์เซีย
✧ pt : โปรตุเกศ
✧ ro : โรมาเนีย
✧ ru : รัสเซีย
✧ th : ไทย
✧ zu : ซูลู
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
✎ระบบขัดข้องโทรแจ้ง📲0899515060📞
⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸
 
『วิธีใช้ : tr-th hello』"""
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.findAndAddContactsByMid(op.param1)
            if settings["autoBlock"] == True:
                line.blockContact(op.param1)
            msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, sver, spkg, sid)
        if op.type == 13:
            print ("[ 13 ] มีคนเชิญคุณเข้ากลุ่ม")
            group = line.getGroup(op.param1)
            contact = line.getContact(op.param2)
            if settings["autoJoin"] and lineMID in op.param3:
                line.acceptGroupInvitation(op.param1)
                line.sendMessage(op.param1, op.param2, "สวัสดีครับ", ", ขอบคุณที่เชิญผมเข้ากลุ่มนะ")
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 15:
            #print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["Lv"] == True:
                if "{gname}" in settings['bye']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['bye'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                    if "@!" in settings['bye']:
                        msg = msg.split("@!")
                        return sendMention(op.param2, op.param2, msg[0], msg[1])
                    return sendMention(op.param2, op.param2, "Hallo ", msg)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                #sendMention(op.param1, op.param2, "Bye", "\n{}".format(str(settings['leavePesan'])))
        if op.type == 19:
            #print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["Nk"] == True:
                if "{gname}" in settings['kick']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['kick'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                    if "@!" in settings['kick']:
                        msg = msg.split("@!")
                        return sendMention(op.param2, op.param2, msg[0], msg[1])
                    return sendMention(op.param2, op.param2, "Hallo ", msg)
                msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                #sendMention(op.param1, op.param2, "อุ๊ต๊ะ", "\n{}".format(str(settings['kick'])))
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Wc"] == True:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
#      if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendText(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendText(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendText(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendText(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendText(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"ลบจากรายการที่ถูกแบนแล้ว")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
       # if op.type == 26:
#            if settings ["mutebot2"] == True:
           # msg = op.message
           # try:
               # if msg.toType == 0:
                  #  line.log("[%s]"%(msg._from)+str(msg.text))
               # else:
                  #  group = line.getGroup(msg.to)
                    #contact = line.getContact(msg._from)
                  #  line.log("[%s]"%(msg.to)+"\nGroupname: "+str(group.name)+"\nNamenya: "+str(contact.displayName)+"\nPesannya: "+str(msg.text))
               # if msg.contentType == 0:
            #Save message to dict
                    #msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                #if msg.contentType == 7:
                    #stk_id = msg.contentMetadata['STKID']
                    #stk_ver = msg.contentMetadata['STKVER']
                   # pkg_id = msg.contentMetadata['STKPKGID']
                    #ret_ = "="
                    #ret_ += "\nSTICKER ID : {}".format(stk_id)
                  #  ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    #ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    #ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    #ret_ += "\n"
                    #msg_dict[msg.id] = {"text":str(ret_),"from":msg._from,"createdTime":msg.createdTime}
            #except Exception as e:
                #print(e)                    
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if "/พูด " in msg.text.lower():
                    spl = re.split("/พูด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == '/คำสั่ง':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                    line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/~james69696", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~james69696', 'type': 'mt', 'subText': "Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭", 'a-installUrl': 'https://line.me/ti/p/~james69696', 'a-installUrl': ' https://line.me/ti/p/~james69696', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~james69696', 'i-linkUri': 'https://line.me/ti/p/~james69696', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~james69696'}, contentType=19)
                elif text.lower() == '/คำสั่ง1':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == '/คำสั่ง2':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == '/คำสั่ง3':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                elif text.lower() == '/คำสั่ง4':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                elif text.lower() == '/คำสั่ง5':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == '/คำสั่ง6':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == '/สปีด':
                    start = time.time()
                    line.sendMessage(to, "✯͜͡S͜͡p͜͡e͜͡e͜͡e͜͡d✯͜͡ѕ͜͡є͜͡ʟ͜͡ғ͜͡в͜͡о͜͡т͜͡✯")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, " %s Sp    " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ")
                elif text.lower() == '/เรว':
                    start = time.time()
                    line.sendMessage(to, "✯͜͡S͜͡p͜͡e͜͡e͜͡e͜͡d✯͜͡ѕ͜͡є͜͡ʟ͜͡ғ͜͡в͜͡о͜͡т͜͡✯")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, " %s Sp    " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ")
                elif text.lower() == '/รีบอท':
                    line.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    line.sendMessage(to, "β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                    restartBot()
                elif text.lower() == '/ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ระยะเวลาการทำงานของบอท\n\n✧ⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧\n {}".format(str(runtime)))
                elif text.lower() == '/ข้อมูล':
                    try:
                        arr = []
                        owner = "u44284195e461bf2a7aab393a4cddff05"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"
                        ret_ += "\n╠۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ] ═ {}".format(contact.statusMessage)
                        ret_ += "\n╠۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸"
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == '/ตั้งค่า':
                    try:
                        ret_ = "╔⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠ ออโต้แอด✔"
                        else: ret_ += "\n╠ ออโต้แอด   ✘ "
                        if settings["autoBlock"] == True: ret_ += "\n╠ ออโต้บล็อค✔"
                        else: ret_ += "\n╠ ออโต้บล็อค   ✘ "
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠ มุดลิ้ง✔"
                        else: ret_ += "\n╠ มุดลิ้ง   ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠ เข้าห้องออโต้ ✔"
                        else: ret_ += "\n╠ เข้าห้องออโต้    ✘ "
                        if settings["Api"] == True: ret_ += "\n╠ บอท api✔"
                        else: ret_ += "\n╠ บอท api   ✘ "
                        if settings["Aip"] == True: ret_ += "\n╠ แสกนคำพูด+คำสั่งบิน✔"
                        else: ret_ += "\n╠ แสกนคำพูด+คำสั่งบิน   ✘ "
                        if settings["Wc"] == True: ret_ += "\n╠ ข้อความต้อนรับสมาชิก ✔"
                        else: ret_ += "\n╠ ข้อความต้อนรับสมาชิก    ✘ "
                        if settings["Lv"] == True: ret_ += "\n╠ ข้อความอำลาสมาชิก ✔"
                        else: ret_ += "\n╠ ข้อความอำลาสมาชิก    ✘ "
                        if settings["Nk"] == True: ret_ += "\n╠ ข้อความแจ้งเตือนคนลบ ✔"
                        else: ret_ += "\n╠ ข้อความแจ้งเตือนคนลบ    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠ ปฏิเสธกลุ่มเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n╠ ปฏิเสธกลุ่มเชิญ    ✘ "						
                        if settings["autoLeave"] == True: ret_ += "\n╠ ออกแชทรวม ✔"
                        else: ret_ += "\n╠ ออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠ อ่านออโต้ ✔"
                        else: ret_ += "\n╠ อ่านออโต้   ✘ "				
                        if settings["checkContact"] == True: ret_ += "\n╠ อ่านคท ✔"
                        else: ret_ += "\n╠ อ่านคท        ✘ "
                        if settings["checkPost"] == True: ret_ += "\n╠ เช็คโพส ✔"
                        else: ret_ += "\n╠ เช็คโพส        ✘ "
                        if settings["checkSticker"] == True: ret_ += "\n╠ Sticker ✔"
                        else: ret_ += "\n╠ Sticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠ ตอบกลับคนแทค ✔"
                        else: ret_ += "\n╠ ตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠ แสดงภาพคนแทค ✔"
                        else: ret_ += "\n╠ แสดงภาพคนแทค ✘ "
                        if settings["kickMention"] == True: ret_ += "\n╠ เตะคนแทค ✔"
                        else: ret_ += "\n╠ เตะคนแทค ✘ "
                        if settings["delayMention"] == True: ret_ += "\n╠ แทคกลับคนแทค ✔"
                        else: ret_ += "\n╠ แทคกลับคนแทค ✘ "
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠ กันเชิญ ✔"
                        else: ret_ += "\n╠ กันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠ กันยกเชิญ ✔"
                        else: ret_ += "\n╠ กันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠ ป้องกัน ✔"
                        else: ret_ += "\n╠ ป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠ ป้องกันสมาชิก ✔"
                        else: ret_ += "\n╠ ป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✘ "
                        if settings["unsendMessage"] == True: ret_ += "\n╠ ดูข้อความที่ยกเลิก ✔"
                        else: ret_ += "\n╠ ดูข้อความที่ยกเลิก ✘"
                        ret_ += "\n╚⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸┛"
                        line.sendMessage(to, str(ret_))
                        line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/~james69696", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~james69696', 'type': 'mt', 'subText': "🐯🆃🅸🅖🅴🆁❻❾🐯", 'a-installUrl': 'https://line.me/ti/p/~james69696', 'a-installUrl': ' https://line.me/ti/p/~james69696', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'james69696': 'https://line.me/ti/p/~james69696', 'i-linkUri': 'https://line.me/ti/p/~james69696', 'id': 'james69696', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~james69696'}, contentType=19)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))

                elif text.lower() == '/เปิดยกเลิก':
                    settings["unsendMessage"] = True
                    settings["unsendMessage"] = False
                    RfuProtect["unsendMessage"] == True
                    RfuProtect["unsendMessage"] == False
                    line.sendMessage(to, "⇱ได้ทำการเปิดคนยกเลิกข้อความ􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/ปิดยกเลิก':
                    settings["unsendMessage"] = False
                    settings["unsendMessage"] = False
                    RfuProtect["unsendMessage"] == True
                    RfuProtect["unsendMessage"] == False
                    line.sendMessage(to, "⇱ทำการปิดคนยกเลิกข้อความ􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif text.lower() == '/เปิดแอด':
                    settings["autoAdd"] = True
                    settings["autoBlock"] = False
                    RfuProtect["autoAdd"] == True
                    RfuProtect["autoBlock"] == False
                    line.sendMessage(to, "⇱ได้ทำการเปิดแอด􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/เปิดบลอค':
                    settings["autoBlock"] = True
                    settings["autoAdd"] = False
                    RfuProtect["autoBlock"] == True
                    RfuProtect["autoAdd"] == False
                    line.sendMessage(to, "⇱ได้ทำการเปิดบล็อค􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/ปิดแอด':
                    settings["autoAdd"] = False
                    RfuProtect["autoAdd"] == False
                    line.sendMessage(to, "⇱ทำการปิดแอด􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif text.lower() == '/ปิดบลอค':
                    settings["autoBlock"] = False
                    RfuProtect["autoBlock"] == False
                    line.sendMessage(to, "⇱ทำการปิดบล็อค􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif text.lower() == '/เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "⇱ได้ทำการเปิดเข้า􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "⇱ทำการปิดเข้า􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"ปิดใช้งานระบบปฏิเสธคำเชิญตามจำนวนสมาชิก")
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == '/เปิดออก':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "เปิดระบบออกแชทรวมอัตโนมัติ⇱ได้ทำการ􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/ปิดออก':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "⇱ทำการ􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif text.lower() == '/เปิดอ่าน':
                    settings["autoRead"] = True
                    line.sendMessage(to, "⇱ได้ทำการ􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/ปิดอ่าน':
                    settings["autoRead"] = False
                    line.sendMessage(to, "⇱ทำการ􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif text.lower() == '/เปิดติ๊ก':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "⇱ได้ทำการ􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif text.lower() == '/ปิดติ๊ก':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "⇱ทำการ􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif text.lower() == '/เปิดมุดลิ้ง':
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "⇱ได้ทำการ􀔃􀅤เปิด􏿿เปิดมุดลิ้งแล้ว⇲")
                elif text.lower() == '/ปิดมุดลิ้ง':
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "⇱ทำการ􀔃􀅪ปิด􏿿ปิดมุดลิ้งแล้ว⇲")
#==============================================================================#
                elif msg.text.lower() == "/ตัวเรา":
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"👇ชื่อของเรา👇")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(msg.to,"👇สเตตัส👇\n" + me.statusMessage)
                    line.sendContact(to, lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    cover = line.getProfileCoverURL(lineMID)
                    line.sendImageWithURL(msg.to, cover)
                    line.sendMessage(msg.to,str(settings["comment"]))
                elif text.lower() == "/เรา":
                    line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/~james69696", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~james69696', 'type': 'mt', 'subText': "🐯🆃🅸🅖🅴🆁❻❾🐯", 'a-installUrl': 'https://line.me/ti/p/~james69696', 'a-installUrl': ' https://line.me/ti/p/~james69696', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'james69696': 'https://line.me/ti/p/~james69696', 'i-linkUri': 'https://line.me/ti/p/~james69696', 'id': 'james69696', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~james69696'}, contentType=19)
                elif text.lower() == "/69":
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                    line.sendMentionFooter(to, '「Me」\n', sender, str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                    line.sendMusic(to, line.getContact(sender).displayName, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, str(userid), "TIGER69 BOT", line.getContact(sender).displayName)
                elif text.lower() == '/คท':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == '/ผส':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "u44284195e461bf2a7aab393a4cddff05")
                elif text.lower() == '/มิด':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == '/ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == '/ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == '/รูป':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == '/วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == '/ปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif text.lower() == '/คอมเม้น':
                    line.sendMessage(msg.to,str(settings["comment"]))
                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"52114123","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                elif text.lower() == '/ทักเข้า':
                    line.sendMessage(msg.to, str(settings["welcome"]))
                elif text.lower() == '/ทักออก':
                    line.sendMessage(msg.to, str(settings["bye"]))
                elif text.lower() == '/ทักเตะ':
                    line.sendMessage(msg.to, str(settings["kick"]))
                elif text.lower() == '/ข้อความแอด':
                    line.sendMessage(msg.to, str(settings["message"]))
                elif text.lower() == '/ข้อความแทค':
                    line.sendMessage(msg.to, str(settings["Respontag"]))
                elif text.lower() == '/แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂\n\n✧ⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == '/ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน🤗\n\n✧ⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == '/คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂\n\n✧ⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif msg.text.lower().startswith("/คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("/มิด "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("/ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("/ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("/รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("/วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("/ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif "/โฟส " in msg.text:
                    tl_text = msg.text.replace("/โฟส ","")
                    line.sendText(msg.to,"line://home/post?userMid="+lineMID+"&postId="+line.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                elif "/คัลลอก " in msg.text:
                  if msg._from in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "Success...")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            settings["changePictureProfile"] = True
                            me = line.getContact(target)     
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

                elif msg.text in ["/คืนร่าง"]:
                    try:
                        line.updateProfile.pictureStatus(myProfile["pictureStatus"])
                        line.updateProfile.statusMessage(myProfile["statusMessage"])
                        line.updateProfile.displayName(myProfile["displayName"])
                        line.sendMessage(msg.to, "กลับร่างเดิมแล้ว")
                    except Exception as e:
                        line.sendText(msg.to, str (e))
                        
                elif msg.text in ["/เปิดรปภ","/เปิดกทม"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True 
                        RfuProtect["linkprotect"] = True 
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด เปิด👌\n\nβ¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
						
                elif msg.text in ["/ปิดรปภ","/ปิดกทม"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False 
                        RfuProtect["linkprotect"] = False 
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด ปิด👌\n\nβ¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                        
                elif msg.text in ["Allmsg on","/เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True 
                        settings["checkContact"] = True 
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด เปิด👌\n\nβ¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
						
                elif msg.text in ["Allmsg off","/ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False 
                        settings["checkContact"] = False 
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด ปิด👌\n\nβ¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
#==============================================================================#
                elif msg.text.lower().startswith("/เลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("/ลบเลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == '/เชคเลียนแบบ':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
                elif '/เพลสโต ' in msg.text.lower():
                        tob = msg.text.lower().replace('/เพลสโต ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : Google Play\nลิ้งโหลด : https://play.google.com/store/search?q=" + tob)
                        line.sendText(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
                elif "/คท:" in msg.text:
                    mmid = msg.text.replace("/คท:","")
                    line.sendMessage(to, text=None, contentMetadata={'mid': mmid}, contentType=13)
                elif "/ค้นหาไอดี " in msg.text:
                    msgg = msg.text.replace("/ค้นหาไอดี ",'')
                    conn = line.findContactsByUserid(msgg)
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        line.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                        line.sendMessage(to,msg)
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
#==============================================================================#
                elif text.lower() == '/แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "☝คนนี้แหล่ะคนสร้างกลุ่มนี้")
                elif text.lower() == '/ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ไอดีกลุ่ม \n" + gid.id)
                elif text.lower() == '/รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == '/ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ชื่อกลุ่ม -> \n" + gid.name)
                elif text.lower() == '/ลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งของกลุ่ม\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == '/เปิดลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย✔")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย✔")
                elif text.lower() == '/ปิดลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย✘")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == '/ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == '/สมาชิก':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == '/เชคกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))				
                elif "/เชิญคลอ" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")
                elif "/คลอ" in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            line.sendMessage(msg.to,"กำลังดำเนินการ...")
                        except:
                            pass
                        for var in range(num):
                            group = line.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            line.acquireGroupCallRoute(msg.to)
                            line.inviteIntoGroupCall(msg.to, contactIds=members)
                        line.sendMessage(msg.to,"เชิญคอลสำเร็จแล้ว(｀・ω・´)")
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass
                elif msg.text.lower() == '/เชิญแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่ม")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว")
                elif msg.text.lower().startswith("/ไอดีไลน์ "):
                    id = msg.text.lower().replace("ไอดีไลน์ ","")
                    conn = line.findContactsByUserid(id)
                    if True:                                      
                        line.sendMessage(to,"http://line.me/ti/p/~" + id)
                        line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith("ถาม "):
                    kata = msg.text.lower().replace("asking", "")
                    sch = kata.replace(" ","+")
                    with _session as web:
                        urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                        r = _session.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                        data = r.text
                        data = json.loads(data)
                        url = data["shorturl"]
                        ret_ = "「Ask」"
                        ret_ += "\n\nLink : {}".format(str(url))
                        line.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("/บลอคไอดี "):
                    user = msg.text.lower().replace("/บลอคไอดี ","")
                    line.blockContact(user)
                    line.sendMessage(to, "ทำการบลอคไอดีนั้นแล้ว")
                elif msg.text.lower().startswith("/ไวรัส: "):
                    number = msg.text.lower().replace("ไวรัส: ","")
                    groups = line.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = line.getGroup(group)
                        try:
                            line.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                        except:
                            line.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                        line.sendMessage(to, "「 Remote Crash 」\n\nGroup : " + G.name)
                    except Exception as error:
                        line.sendMessage(to, str(error))          
                elif msg.text.lower() == "getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif "/ข้อมูล " in msg.text.lower():
                    spl = re.split("/ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                
                elif "รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\nราคาดูที่หน้างาน\n👉มีบริการให้เช่าบอท⇱ℾⅈℐℰℛ❻❾⇲\nราคา89บาทต่อเดือน\n#เพิ่มคิกเกอร์ตัวละ60👌\nสนใจรีบทัก..บอทpython3ฟังชั่นล้นหลาม👏กำลังรอให้คุณเป็นเจ้าของ\nselfbot by:\n╔══════════════┓\n╠✧ⓈⒺⓁⒻⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧\n╚══════════════┛" in msg.text:
                    spl = msg.text.split("รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\nราคาดูที่หน้างาน\n👉มีบริการให้เช่าบอท⇱ℾⅈℐℰℛ❻❾⇲\nราคา89บาทต่อเดือน💖\n#เพิ่มคิกเกอร์ตัวละ60👌\nสนใจรีบทัก..บอทpython3ฟังชั่นล้นหลาม👏กำลังรอให้คุณเป็นเจ้าของ\nselfbot by:\n╔══════════════┓\n╠✧ⓈⒺⓁⒻⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧\n╚══════════════┛")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)
                elif "/รัน @" in msg.text:
                    print ("[Command]covergroup")
                    _name = msg.text.replace("/รัน @","")
                    _nametarget = _name.rstrip('  ')
                    gs = line.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                               thisgroup = line.getGroups([msg.to])
                               Mids = [target for contact in thisgroup[0].members]
                               mi_d = Mids[:33]
                               line.createGroup("ℾⅈℐℰℛ❻❾",mi_d)
                               line.sendText(msg.to,"🐯ቜ፤ᎶᏋ⅊🐯❻❾")
                               line.createGroup("ℾⅈℐℰℛ❻❾",mi_d)
                               line.sendText(msg.to,"🐯ቜ፤ᎶᏋ⅊🐯❻❾")
                               line.sendText(msg.to,"รันเรียบร้อยสำเร็จ")
                            except:
                                pass
                    print ("[Command]covergroup]")
                elif "/รันแชท @" in msg.text:
                    _name = msg.text.replace("/รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = line.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭") 
                           line.sendText(g.mid,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                           line.sendText(msg.to, "⇱ถูกรันแชทเรียบร้อย👍􀔃􀅤เปิด􏿿สำเร็จ⇲")
                           print (" Spammed !")
                elif "/ดึงห้อง" in msg.text:
                    thisgroup = line.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    line.createGroup("β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭", mi_d)
                    line.sendText(msg.to,"welcome to room β¥:Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                elif "/ไม่รับเชิญ " in msg.text.lower():
                    spl = re.split("/ไม่รับเชิญ ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif "/เตะ1" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif "/เตะ2" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == "mid":
                    line.sendText(msg.to,user1)
                
                elif "/name " in msg.text.lower():
                    spl = re.split("/name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif "/nmx " in msg.text.lower():
                    spl = re.split("/nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif "/มุด " in msg.text.lower():
                    spl = re.split("/มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))
                elif msg.text.lower().startswith("/โทร "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "เชิญแล้ว👍".format(str(jml)))
                elif msg.text.lower().startswith("/แทก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = line.getContact(receiver)
                                RhyN_(to, contact.mid)
                
                elif msg.text.lower().startswith("/แจก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, text=None, contentMetadata=None, contentType=9)
                                line.sendMessage(to, "ส่งของขวัญใน ส.ต แล้วนะแจ๊ะ👍".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("/ไวรัส "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendContact(receiver, text=None, contentMetadata={'mid': 'u1f41296217e740650e0448b96851a3e2'}, contentType=13)
                                line.sendMessage(to, "ไปดู ส.ต ด้วย👍".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("/ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = line.getContact(to)
                        RhyN_(to, name.mid)
                elif msg.text.lower() == "/":
                    if msg.toType == 0:
                        sendMention(to, to, "", "")
                    elif msg.toType == 2:
                        group = line.getGroup(to)
                        contact = [mem.mid for mem in group.members]
                        mentionMembers(to, contact)
                elif msg.text.lower().startswith("/คำห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    line.sendMessage(to,"%s พิมคำนี้อาจมีการเตะเกิดขึ้นนะ."%wban)
                elif msg.text.lower().startswith("/ล้างคำห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        line.sendMessage(to,"%s ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        line.sendMessage(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == '/เชคคำห้ามพิม':
                    tst = "คำห้ามพิม:\n"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "- %s"%word
                        line.sendMessage(msg.to,tst)
                    else:
                        line.sendMessage(msg.to,"คำที่ห้ามพิมทั้งหมด")
                elif msg.text.lower().startswith("/ส่งข้อความ "):
                    pnum = re.split("/ส่งข้อความ ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                line.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                line.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                line.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                line.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == "groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif "groupurl " in msg.text.lower():
                    spl = re.split("groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")
                if "gift " in msg.text.lower():
                    red = re.compile(re.escape('gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
#==============================================================================#
                elif text.lower() == '/แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "จำนวนแทคทั้งหมด {} คน👍".format(str(len(nama))))  
                elif text.lower() == '/คนแอบ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == '/รีคนอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == '/คนอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == '/แอบ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)

#==============================================================================#
                elif "/ประกาศกลุ่ม " in msg.text:
                    bc = msg.text.replace("/ประกาศกลุ่ม ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendText(i,"ขออนุญาติเจ้าของห้อง\n\n"+bc+"\n\n✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧")
                    
                elif "/ประกาศแชท " in msg.text:
                    bc = msg.text.replace("/ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendText(i,"ขออนุญาติเจ้าของแชท\n\n"+bc+"\n\n✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧")
            
                elif "/ส่งรูปภาพตามกลุ่ม: " in msg.text:
                    bc = msg.text.replace("/ส่งรูปภาพตามกลุ่ม: ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                    
                elif "/ส่งรูปภามตามแชท: " in msg.text:
                    bc = msg.text.replace("/ส่งรูปภาพตามแชท: ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                elif "/ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace("/ส่งเสียงกลุ่ม ", "")
                    bc = ("สนใจติดบอทไลน์..เชลบอทเสือ69..โทรมาที่เบอร์0899515060..อย่าโทรมาเล่นโอเคนะ")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "/ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace("/ส่งเสียงแชท ", "")
                    bc = ("ร้องเพลงกันไหม เขามีคนใหม่แล้วจื่อแหน่ใจ่..สิเฮ็ดจั่งได่เขาก้อบ่อกลับคืนมา..ลืมเขาสาเถาะ จื่อแหน่ใจ่ ออยเลอ")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')
                    
                elif text.lower() == '/วันที่':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "📆ปฏิทินโดย✧ⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧\n\n" + "\n\n📅" + hasil + "\n📅 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🕚 เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "🕥" + "\n\n✧ⓈⒺⓁⒻⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧"
                    line.sendMessage(msg.to, readTime)

                elif "/ค้นหาเว็ป " in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])

                elif "/รูปภาพ " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "/ภาพ " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
      
                elif "/ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "Google " in msg.text.lower():
                    spl = re.split("Google ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        line.sendText(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        line.sendText(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก Google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        line.sendText(msg.to,str(text))
                                    else:
                                        line.sendText(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
                        
                elif "/วีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "วีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "/หนัง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "หนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "/ฟังเพลง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "/ฟังเพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["/เปิดแสกน"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")
                elif msg.text in ["/ปิดแสกน"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")

                elif text.lower() == '/ปิดเชล':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)
                elif text.lower() == "/ลบแชท":
                        if msg._from in lineMID:
                            try:
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"ลบทุกการแชทเรียบร้อย")
                            except:
                                pass
                                print ("/ลบแชท")
                elif text.lower() == '/เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎รายชื่อเพื่อนทั้งหมด🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎รายชื่อเพื่อนทั้งหมด🎎\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["/เชคบลอค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════ไม่มีรายการบัญชีที่ถูกบล็อค═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════รายการบัญชีที่ถูกบล็อค════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["/ไอดีเพื่อน"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════รายการไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════รายการ ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "/18+":
                	line.sendMessage(receiver,"❂เวปหนังโป๊สำหรับสายหื่นเสือหกเก้าจัดให้แล้วดูให้ตาแฉะช่ะ❂\nCommentbyjames.เงี่ยนก้อชักอยากก้อเยส\n\n❂͜͡☆➣ nekopoi.host\n❂͜͡☆➣ sexvideobokep.com\n❂͜͡☆➣ memek.com\n❂͜͡☆➣ pornktube.com\n❂͜͡☆➣ faketaxi.com\n❂͜͡☆➣ videojorok.com\n❂͜͡☆➣ watchmygf.mobi\n❂͜͡☆➣ xnxx.com\n❂͜͡☆➣ pornhd.com\n❂͜͡☆➣ xvideos.com\n❂͜͡☆➣ vidz7.com\n❂͜͡☆➣ m.xhamster.com\n❂͜͡☆➣ xxmovies.pro\n❂͜͡☆➣ youporn.com\n❂͜͡☆➣ pornhub.com\n❂͜͡☆➣ youjizz.com\n❂͜͡☆➣ thumzilla.com\n❂͜͡☆➣ anyporn.com\n❂͜͡☆➣ brazzers.com\n❂͜͡☆➣ redtube.com\n❂͜͡☆➣ youporn.com\n\n✧ⓈⒺⓁⒻⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧")
                elif msg.text == "/ประกาศ":
                	line.sendMessage(msg.to,str(settings["message1"]))
                elif msg.text.lower() == '/ดึงแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["/ขอออกนะ"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass
                elif msg.text in ["/เชคไอดี"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
                    
                elif msg.text in ["/เปิดแทคเตะ"]:
                    settings["kickMention"] = True
                    line.sendMessage(msg.to,"⇱เปิดแทคระบบเจ็บ􀔃􀅤เปิด􏿿สำเร็จ⇲")
                
                elif msg.text in ["/ปิดแทคเตะ"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"⇱ปิดแทคระบบเจ็บ􀔃􀅪ปิด􏿿เรียบร้อย⇲")
                    
                elif msg.text in ["/เปิดแทค","Tag on"]:
                        settings['detectMention'] = True
                        line.sendMessage(msg.to,"⇱เปิดแทค􀔃􀅤เปิด􏿿สำเร็จ⇲")
                
                elif msg.text in ["/ปิดแทค","Tag off"]:
                        settings['detectMention'] = False
                        line.sendMessage(msg.to,"⇱ปิดแทค􀔃􀅪ปิด􏿿เรียบร้อย⇲")

                elif msg.text in ["/เปิดแทค2"]:
                    settings["potoMention"] = True
                    line.sendMessage(msg.to,"⇱เปิดแทค2􀔃􀅤เปิด􏿿สำเร็จ⇲")
                
                elif msg.text in ["/ปิดแทค2"]:
                    settings["potoMention"] = False
                    line.sendMessage(msg.to,"⇱ปิดระบบแทค2􀔃􀅪ปิด􏿿เรียบร้อย⇲")
                    
                elif msg.text in ["/เปิดแทค3"]:
                    settings["delayMention"] = True
                    line.sendMessage(msg.to,"⇱เปิดแทค3􀔃􀅤เปิด􏿿สำเร็จ⇲")
                
                elif msg.text in ["/ปิดแทค3"]:
                    settings["delayMention"] = False
                    line.sendMessage(msg.to,"⇱ปิดระบบแทค3􀔃􀅪ปิด􏿿เรียบร้อย⇲")
                elif msg.text.lower() == "/เปิดแทคแชท":
                    settings["detectMentionPM"] = True
                    line.sendMessage(msg.to,"⇱เปิดแทคแชท􀔃􀅤เปิด􏿿สำเร็จ⇲")
                elif msg.text.lower() == "/ปิดแทคแชท":
                    settings["detectMentionPM"] = False
                    line.sendMessage(msg.to,"⇱ปิดแทคแชท􀔃􀅪ปิด􏿿เรียบร้อย⇲")
                elif msg.text.lower().startswith("/ตั้งแทคแชท: "):
                    text = msg.text.lower().replace("/ตั้งแทคแชท: ","")
                    settings["pmMessage"] = text
                    line.sendMessage(msg.to, "⇱คำแทคแชท⇲ สต คือ : {}".format(str(settings["pmMessage"])))
                elif msg.text.lower().startswith("setrespongroup: "):
                    text = msg.text.lower().replace("setrespongroup: ","")
                    settings["respMessage"] = text
                    line.sendMessage(msg.to, "Success Update Response Group to : {}".format(str(settings["respMessage"])))
                    
                elif msg.text in ["/เปิดตรวจสอบ"]:
                    settings["Aip"] = True
                    line.sendMessage(msg.to,"⇱ได้ทำการเปิดตรวจสอบคำเสี่ยงพวกลบห้อง\nและคำหยาบคายกับบอทบิน􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                
                elif msg.text in ["/ปิดตรวจสอบ"]:
                    settings["Aip"] = False
                    line.sendMessage(msg.to,"⇱ทำการปิดตรวจสอบหยาบคายกับบอทบิน􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                    
                elif msg.text in ["/เปิดApi"]:
                    settings["Api"] = True
                    line.sendMessage(msg.to,"⇱เปิดระบบAPI􀔃􀅤เปิด􏿿สำเร็จ⇲")
                
                elif msg.text in ["/ปิดApi"]:
                    settings["Api"] = False
                    line.sendMessage(msg.to,"⇱ปิดระบบAPI􀔃􀅪ปิด􏿿เรียบร้อย⇲")
                    
                elif '/ตั้งคนแอด: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('/ตั้งคนแอด: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "⇱เปิดตั้งคนแอดมา􀔃􀅤เปิด􏿿สำเร็จ⇲")
                     else:
                         settings["message"] = spl
                         line.sendMessage(msg.to, "✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n\n👇ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้👇\n\n👉{}".format(str(spl)))
                         
                elif '/คอมเม้น: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('/คอมเม้น: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "⇱เปิดตั้งคอมเม้น􀔃􀅤เปิด􏿿สำเร็จ⇲")
                     else:
                         settings["comment"] = spl
                         line.sendMessage(msg.to, "✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n\n👇ตั้งข้อความคอมเม้นของคุณแล้ว ดังนี้👇\n\n👉{}".format(str(spl))) 
                    
                elif '/ตั้งคนแทค: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('/ตั้งคนแทค: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "⇱เปิดตั้งคนแทค􀔃􀅤เปิด􏿿สำเร็จ⇲")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n\n👇ตั้งข้อความตอบโต้เมื่อมีคนแทคแล้ว👇\n\n👉{}".format(str(spl)))
                         
                elif '/ตั้งคนลบ: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('/ตั้งคนลบ: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "⇱เปิดคั้งข้อความคนลบสมาชิก􀔃􀅤เปิด􏿿สำเร็จ⇲")
                     else:
                          settings["kick"] = spl
                          line.sendMessage(msg.to, "✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n\nตั้งค่าข้อความเมื่อมีคนลบสมาชิกแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)))

                elif '/ตั้งคนออก: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('/ตั้งคนออก: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "⇱เปิดคั้งข้อความคนออก􀔃􀅤เปิด􏿿สำเร็จ⇲")
                     else:
                          settings["bye"] = spl
                          line.sendMessage(msg.to, "✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n\nตั้งค่าข้อความเมื่อมีคนออกจากกลุ่มแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)))

                elif '/ตั้งคนเข้า: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('/ตั้งคนเข้า: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "⇱เปิดคั้งข้อความคนเข้า􀔃􀅤เปิด􏿿สำเร็จ⇲")
                     else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "✧⇷⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇹⇸✧\n\nตั้งค่าข้อความเมื่อมีคนเข้ากลุ่มแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)))
                elif msg.text.lower() == "เปิดกันติ๊ก":
                        settings["sticker"] = True
                        line.sendMessage(to,"⇱ได้ทำการเปิดรันติ๊ก􀔃􀅤เปิด􏿿เปิดแล้ว⇲")
                elif msg.text.lower() == "ปิดกันติ๊ก":
                        settings["sticker"] = False
                        line.sendMessage(to,"⇱ทำการปิดรันติ๊ก􀔃􀅪ปิด􏿿ปิดแล้ว⇲")
                elif msg.text.lower() == "sleepmode":
                    if settings["replyPesan"] is not None:
                        line.sendMessage(to,"Your Sleepmode is : " + str(settings["replyPesan"]))
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                    else:
                        line.sendMessage(to,"My Sleepmode : No messages are set")
                elif msg.text.lower() == "addsleepmodesticker":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "sleepSticker"
                    line.sendMessage(to, "โปรดส่งสติ๊กเกอร์ที่คุณต้องการเพิ่มด้วยนะ")
                elif msg.text.lower() == "delsleepmodesticker":
                    settings["messageSticker"]["listSticker"]["sleepSticker"] = None
                    line.sendMessage(to, "ลบรายการสติ๊กเกอร์เรียบร้อย􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower().startswith("setsleepmode: "):
                    text_ = msg.text.lower().replace("setsleepmode:", "")
                    try:
                        settings["replyPesan"] = text_
                        line.sendMessage(to,"Sleep mode changed to : " + text_)
                    except:
                        line.sendMessage(to,"SleepMode \nFailed to replace message")
                elif msg.text.lower() == "/ติ๊กคนออก":
                        msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "/ตั้งติ๊กคนออก":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "leaveSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนออก":
                    settings["messageSticker"]["listSticker"]["leaveSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower() == "/ติ๊กคนเตะ":
                        msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "/ตั้งติ๊กคนเตะ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "kickSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนเตะ":
                    settings["messageSticker"]["listSticker"]["kickSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเตะแล้ว􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower() == "/ติ๊กคนเข้า":
                        msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "/ตั้งติ๊กคนเข้า":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "welcomeSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนเข้า":
                    settings["messageSticker"]["listSticker"]["welcomeSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower()== "/ติ๊กคนแอด":
                        msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower()== "/ตั้งติ๊กคนแอด":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "addSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนแอด":
                    settings["messageSticker"]["listSticker"]["addSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower() == "/ติ๊กคนแทค":
                        msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "/ตั้งติ๊กคนแทค":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "responSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนแทค":
                    settings["messageSticker"]["listSticker"]["responSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower() == "/ตั้งติ๊กคนแอบ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "readerSticker"
                    line.sendMessage(to, "ส่งสติ๊กเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนแอบ":
                    settings["messageSticker"]["listSticker"]["readerSticker"] = None
                    line.sendMessage(to, "ลบสติ๊กเกอรคนแอบอ่านแล้ว􀔃􀅤เปิด􏿿สำเร็จ")
                elif msg.text.lower() == "/ติ๊กคนแอบ":
                        msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "/กะดิบ " in msg.text:
                    txt = msg.text.replace("/กะดิบ ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["/ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == "/ยกเชิญ":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == "/บอทยก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
                elif msg.text in ["/ดำ"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["/ขาว"]:
                  if msg._from in admin: 
                    settings["dblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["/ล้างดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")
                elif msg.text.lower() == "/คทดำ":
                    if msg._from in lineMID:
                        if settings["blacklist"] == []:
                            line.sendMessage(to, "Nothing boss")
                        else:
                            for bl in settings["blacklist"]:
                                line.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif '/เตะ3' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")

                elif '/เตะ4' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif '/เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")
                elif "/บลอค @" in msg.text:
                    if msg.toType == 2:
                        print ("[block] OK")
                        _name = msg.text.replace("/บลอค @","")
                        _nametarget = _name.rstrip('  ')
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMassage(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                   line.blockContact(target)
                                   sendMessage(msg.to, "Success block contact~")
                                except Exception as e:
                                   print (e)
                elif msg.text.lower() == '/บลอค':
                    blockedlist = line.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                        msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                        sendMessage(msg.to, msgs)
                elif "/ไทยแลน" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("/ไทยแลน","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"THAILANDSKYTIGER69FUCK")
                         line.sendMessage(receiver,"!!! Fuck Fuck Fuck !!!")
                         line.sendMessage(receiver,"THAILANDSKYTIGER69FUCK")
                         line.sendMessage(receiver,"!!! Fuck Fuck Fuck !!!")
                         line.sendMessage(receiver,"THAILANDSKYTIGER69FUCK")
                         line.sendMessage(to, "Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭")
                         line.sendContact(to, "u44284195e461bf2a7aab393a4cddff05")
                         line.sendContact(to, "u06674aa29389ac587e345c393321ddcb")
                         line.sendContact(to, "ufdb157ac442758047f249417da4ceb89")
                         line.sendContact(to, "ubfbf21647916c822ecd2ef6b990e40de")
                         line.sendContact(to, "u1f2c064728907ff9a2d9a1ffb0c6fd19")
                         line.sendContact(to, "uf7188175de24966da0430b16e708a25e")
                         line.sendContact(to, "u9817c82588f58ac5575959b8a3030654")
                         line.sendContact(to, "u68380694f1a0266b6b3e32048d4ef0ee")
                         line.sendContact(to, "u3f826e88f86366ecb15b1221fb39a6cf")
                         line.sendContact(to, "ufbeec41476b2bf0217cd470e3d9b121b")
                         line.sendContact(to, "u8ff6a34e05a1b48fe3761c0652a9e9bd")
                         line.sendContact(to, "u80ac41d20bbb669f53e337cad3f7ecdc")
                         line.sendContact(to, "ue8beb1bfd60fed91dbfbf520438f0406")
                         line.sendContact(to, "u7e0bd3122ce08e08ed321978e7392d16")
                         line.sendContact(to, "u5d3335239f07d65410bf437200008625")
                         line.sendContact(to, "u515920f5a0b769d163238abf763d0c2e")
                         line.sendContact(to, "ue368ae01f7748f4ec34433023de2328a")
                         line.sendContact(to, "u0d7193abfb3e03e05bc079e864be3803")
                         line.sendContact(to, "ue368ae01f7748f4ec34433023de2328a")
                         line.sendContact(to, "u0d7193abfb3e03e05bc079e864be3803")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["/ไล่ดำ"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")
                elif "/ชื่อ: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Update to " + string)
                        print ("อัฟเดฟชื่อสำเร็จ")

                elif "/ตัส: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Succes Update 👉 " + string)
                        print ("อัฟเดฟสเตตัสเรียบร้อย")

#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == '/เปิดกัน':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")

                elif msg.text.lower() == '/ปิดกัน':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")

                elif msg.text.lower() == '/กันยก':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == '/ปิดกันยก':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == '/กันเชิญ':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == '/ปิดกันเชิญ':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == '/กันลิ้ง':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == '/ปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == '/กันกลุ่ม':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == '/ปิดกันกลุ่ม':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == '/กันเข้า':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == '/ปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == '/เปิดหมด':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

                elif msg.text.lower() == '/ปิดหมด':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == '/เปิดต้อนรับ':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ")
                elif msg.text.lower() == '/ปิดต้อนรับ':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ")
                                
                elif msg.text.lower() == '/เปิดทักเตะ':
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...")
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...")
                                
                elif msg.text.lower() == '/ปิดทักเตะ':
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว..")
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว...")

                elif msg.text.lower() == '/เปิดคนออก':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ")
                elif msg.text.lower() == '/ปิดคนออก':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ")
                                
                elif msg.text.lower() == '/เปิดคท':
                        if settings["checkContact"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทค ")
                        else:
                            settings["checkContact"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว ")
                elif msg.text.lower() == '/ปิดคท':
                        if settings["checkContact"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทค ")
                        else:
                            settings["checkContact"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว ")
                elif msg.text.lower() == '/เปิดเชคโฟส':
                        if settings["checkPost"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์" )
                        else:
                            settings["checkPost"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์อยู่แล้ว ")
                elif msg.text.lower() == '/ปิดเชคโฟส':
                        if settings["checkPost"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์ ")
                        else:
                            settings["checkPost"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์ไว้อยู่แล้ว ")
                elif text.lower() == "/แปลงโฉม":
                    settings["changePictureProfile"] = True
                    line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับผม")
                elif text.lower() == "/เปลี่ยนรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับ")
                elif text.lower() == "/ไวรัส":
                    line.sendContact(to, "ub621484bd88d2486744123db00551d5e',")

                elif text.lower() == '/ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้ว")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
			
                elif "/ลงดำ" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("/ลงดำ","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"แบนสมาชิกทุกคนในห้องนี้แล้ว＼（○＾ω＾○）／")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")
										   
                elif '/แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif '/ล้างแบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")
                
                elif msg.text in ["/เชคดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))

            elif msg.contentType == 13:
                if settings["/เชคคท"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "[ รายการทั้งหมดจากการสำรวจด้วย คท ]"
                        ret_ += "\n ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n ตัส : {}".format(str(contact.statusMessage))
                        ret_ += "\n รูปโปรไฟล : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n  รูปปก : {}".format(str(cover))
                        ret_ += "\n[ สิ้นสุดการสำรวจ ]"
                        line.sendMessage(to, str(ret_))
                    except:
                        line.sendMessage(to, "เกิดข้อผิดพลาดในการสำรวจ")
                #for image in images:
                    #if text.lower() == image:
                        #line.sendImage(to, images[image])
                #for sticker in stickers:
                    #if text.lower() == sticker:
                        #sid = stickers[sticker]["STKID"]
                       # spkg = stickers[sticker]["STKPKGID"]
                       # sver = stickers[sticker]["STKVER"]
                        #sendSticker(to, sver, spkg, sid)
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        line.updateGroupPicture(to, path)
                        line.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "Success Added " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                   
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)              
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)             
#==============================================================================#
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])
        
        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])

        if op.type == 5:
            if RfuProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["comment"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["comment"]))
        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendText(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 25:
#            if settings ["mutebot2"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "Success Added " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(msg._from)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "เกิดข้อผิดพลาดในการเช็คโพสนี้")
                            
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if settings ["Aip"] == True:
            	    if msg.text in ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]:
                        line.kickoutFromGroup(receiver,[sender])
                        line.sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
                if settings ["Aip"] == True:
                    if msg.text in ["ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้เรส","ไอ้เหี้ยเรส","ไอ่เรส","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ"]:
                        line.kickoutFromGroup(receiver,[sender])
                        line.sendText(msg.to,"ตรวจพบคำพูดหยาบคายไม่สุภาพ จำเป็นต้องนำออกเพื่อความสงบสุขของสมาชิก (｀・ω・´)")
#                if settings ["Api"] == True:
#            	    if msg.text in ["ป๊า","ป๊าเรส","ลุง","เรส","นาย","เพื่อน","จาร์ย","อาจาร์ย","เฮีย"]:
#                       line.sendMessage(msg.to, str(settings["comment"]))
#                if settings ["Api"] == True:
#                    if msg.text in ["บอท","เซล","เซลบอท","selfbot","คนรึบอท","Help","help",".help","/help","คำสั่ง"]:
#                        line.sendMessage(msg.to, str(settings["comment"]))
                if settings ["Api"] == True:
                    if msg.text in ["55","555","5555","55555","55+","555+","5555+","ขำ",".ขำ"]:
                        line.sendText(msg.to,"😁ขำๆ😁")
#                if settings ["Api"] == True:
#                    if msg.text in [".ประกาศ","โฆษณา","ประชาสัมพัน","ประกาศ"]:
#                    	line.sendMessage(msg.to, str(settings["comment"]))
                if settings["Api"] == True:
                    if msg.text in ["เชลใคร","บอทใคร","คนขายบอท"]:
                        line.sendText(msg.to,"Ŧ€₳M฿❂Ŧ🆃🅸🅖🅴🆁❻❾🇹🇭\n\nสนใจติดตั้งบอทเชลบอทบินบอทรัน\nโทรมาอย่างเดียว0899515060")
                if settings["Api"] == True:
                    if msg.text in ["เชค","อยู่ไหม"]:
                        line.sendText(msg.to,"อยู่ตลอด 🕛จะไปไหนได้ละรอเตงเชคนี่แหละ คริคริ")
                if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)				
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "Sticker Info"
                        ret_ += "\nSTICKER ID : {}".format(stk_id)
                        ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                        line.sendMessage(to, text=None, contentMetadata={'STKID':'107', 'STKVER':'100', 'STKPKGID':'1'}, contentType=7)
                    elif msg.contentType == 1:
                        line.sendMessage(to, text=None, contentMetadata={"STKID": "190", "STKVER": "100", "STKPKGID": "3"}, contentType=7)
                    else:
                        if text is not None:
                            txt = text
                            line.sendMessage(msg.to,txt)
                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            line.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            line.sendMessage(to, str(ret_))                            
                        except Exception as error:
                            line.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in lineMID:
                            try:
                                line.kickoutFromGroup(msg.to,[sender])
                                line.sendMessage("คุณพูดคำต้องห้าม จำเป็นต้องนำออก sorry(╯°□°）╯︵ ┻━┻")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "เรามุดลิ้งเข้าไปในกลุ่มเตงแระ👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.toType == 0 and settings["autoReply"] and sender != lineMID:
                    contact = line.getContact(sender)
                    rjct = ["auto", "ngetag"]
                    validating = [a for a in rjct if a.lower() in text.lower()]
                    if validating != []: return
                    if contact.attributes != 32:
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                        if "@!" in settings["replyPesan"]:
                            msg_ = settings["replyPesan"].split("@!")
                            sendMention(to, sender, "Sleep Mode :\n" + msg_[0], msg_[1])
                        sendMention(to, sender, "Sleep Mode :\nจ๊ะเอ๋", settings["replyPesan"])
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    if settings["detectMentionPM"] == True:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                sendMention(sender, sender, "「ตอบแทคอัตโนมัติ」\n", "\n" + str(settings["pmMessage"]))
                                break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if settings['kickMention'] == True:
        		             contact = line.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" + cName + "\n🙏ต้องขออภัยด้วยจริงๆ🙏Bye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break                                  
        			               if mention['M'] in lineMID:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          line.sendContact(msg.to, mi_d)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『แสดงชื่อคนแทค』\n " + cName + "\n\n『ตอบแทคอัตโนมัติ』"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          line.sendMessage(to,str(settings["Respontag"]))
                                          msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                          if msgSticker != None:
                                              sid = msgSticker["STKID"]
                                              spkg = msgSticker["STKPKGID"]
                                              sver = msgSticker["STKVER"]
                                              sendSticker(to, sver, spkg, sid)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          break
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1, str(settings["welcome"]) +"\n".format(str(dan.displayName),str(tgb.name)))
             line.sendContact(op.param1, op.param2)
#             line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,str(settings["kick"]) + "\n".format(str(dan.displayName)))
             line.sendContact(op.param1, op.param2)
#             line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Lv"] == True:
             if op.param2 in lineMID:
                 return
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,str(settings["bye"]) + "\n".format(str(dan.displayName),str(tgb.name)))
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath)) 
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['จ๊ะเอ๋','รู้นะว่าแอบอยู่','เล่นซ่อนแอบกันเหรอ','คิดว่าเป็นนินจารึไง','ว่าไง','อ่านอย่างเดียวเลยนะ','ออกมาคุยหน่อยอย่าเล่นซ่อนแอบ','ออกมาหำน้อยหอยใหญ่ออกมาเดี๋ยวนี้']
                            sendMessageWithMention(op.param1, op.param2)
                            line.sendMessage(op.param1, str(random.choice(pref)) + '\n♪ ♬ ヾ(´︶`♡)ﾉ ♬ ♪')
                            line.sendContact(op.param1, op.param2)
                            msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                            if msgSticker != None:
                                sid = msgSticker["STKID"]
                                spkg = msgSticker["STKPKGID"]
                                sver = msgSticker["STKVER"]
                                sendSticker(op.param1, sver, spkg, sid)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("✧ⒷⓄⓉⓉⒾⒼⒺⓇ⑥⑨✧")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)

        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            ginfo = line.getGroup(at)
                            contact = line.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "\nคุณได้ทำการยกเลิกข้อความ"
                                ret_ += "\nชื่อ : {}".format(str(contact.displayName))
                                ret_ += "\nชื่อกลุ่ม : {}".format(str(ginfo.name))
                                ret_ += "\nเวลา : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\n\nประเภท 􀄃􀉘ขวา􏿿 {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nข้อความที่สมาชิกยกเลิก \n\n {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            line.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ, ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <")
                except Exception as error:
                    logError(error)

#        if op.type == 65:
#            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
#            if settings["unsendMessage"] == True:
#                try:
#                    at = op.param1
#                    msg_id = op.param2
#                    if msg_id in msg_dict1:
#                        if msg_dict1[msg_id]["from"]:
#                                ginfo = line.getGroup(at)
#                                ariftj = line.getContact(msg_dict1[msg_id]["from"])
#                                ret_ =  "「 Sticker Dihapus 」\n"
#                                ret_ += "• Pengirim : {}".format(str(ariftj.displayName))
#                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
#                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
#                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
#                                line.sendMessage(at, str(ret_))
#                                line.sendImage(at, msg_dict1[msg_id]["data"])
#                        del msg_dict1[msg_id]
#                except Exception as e:
#                    print(e)
#==============================================================================#
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
