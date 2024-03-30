import base64
import json
import requests
from rich import print
from  sky_version import get_version as sky_version

class LoginHandler():
    
    def __init__(self, login_type):
        self.login_type = login_type


    def login_nintendo(self, code):
        code_json = json.loads(code)
        id = code_json["id"]
        signature = code_json["token"]
        datos_user = {"type":"Nintendo","external_credentials":{"external_account_type":"Nintendo","player_id":f"{id}","key_url":"","signature":f"{signature}","salt":"","timestamp":0,"alias":""},"user":"00000000-0000-0000-0000-000000000000","device":"00000000-0000-0000-0000-000000000000","key":"0000000000000000000000000000000000000000000000000000000000000000","device_name":"M2012K11AI","device_token":"cKN45n7UTSKHNoyzdugWNE:APA91bFg8MGDK26uj-RjRrRSANDGST4AqE29kh3ygCzN0IZWLgGis2K16aD9JoYXnaRBD2LgghA18Bc0ZG76AuWEzr3eAMTSRen8SsBPjtPftUVnuXECrjVfhd9z_WeDbx9MaHUO7GS9","production":True,"tos_version":4,"device_key":"AzsVI0WrO7ogCD1XQc4x7UP8NFvWkgprHKr9Dy3EldUs","sig_ts":1654180945,"sig":"MEQCIAMQ36cVdxjL+/jCGsfKmjhtEQVZFMIW2ICzHzhuADhbAiAlDdhjLkrxVTPer/EPmeIOqrU8f5yJyBCmsBaqw6pFxQ==","hashes":[1135420871,4291554428,1662465570,2939294528,2864712656,784335679,1246829562,4147059363,191933768,3062676827,3931787622,2766223387,576746911,2275726205,1729690551,2495669098,2669125820,495611257,1810499009,3661381049,943977965,3914553296,2198427157,1330181820],"integrity":True}
        info = requests.post('https://live.radiance.thatgamecompany.com/account/auth/login', headers=self.get_headers(), json=datos_user).text
        x = json.loads(info)
        print(x)
        if "result" in x:
            sesiones = x["result"]
            userid = x["result"]
        else:
            sesiones = x["session"]
            userid = x["authinfo"]["user"]
        return userid, sesiones


    def lua_handler(self, code):
        valor1 = list(base64.b64decode(code))
        def des(cadena):
            valor = cadena[::-1]
            valorn = []
            if not str(valor[0]).isnumeric():
                for i in valor:
                    valorn.append(ord(i))
                valor = valorn
            num = int(valor[0] / 2)
            desi = []
            for i in valor[1:]:
                desi.append(chr(i - num))
                p = str(i)
                num = int(p[len(p) - 1])
            return desi
        valuer = ''.join(des(des(des(valor1))))
        var = json.loads(valuer)
        return var['uid'],var['session']

    def get_headers(self):
        print(sky_version())
        return {
            'Host': 'live.radiance.thatgamecompany.com',
            'User-Agent': f'Sky-Live-com.tgc.sky.android/{sky_version()} (Xiaomi MI 9; android 29.0.0; es)',
            'X-Session-ID': 'aeee648a-ea1f-4700-b970-ebe955750601',
            'x-sky-install-source': 'com.android.vending',
            'Content-type': 'application/json'
    }

    def login_google(self, code):
        code_json = json.loads(code)
        id = code_json["id"]
        signature = code_json["token"]
        datos_user = {"type":"Google","external_credentials":{"external_account_type":"Google","player_id":f"{id}","key_url":"","signature":f"{signature}","salt":"","timestamp":0,"alias":""},"user":"00000000-0000-0000-0000-000000000000","device":"00000000-0000-0000-0000-000000000000","key":"0000000000000000000000000000000000000000000000000000000000000000","device_name":"M2012K11AI","device_token":"cKN45n7UTSKHNoyzdugWNE:APA91bFg8MGDK26uj-RjRrRSANDGST4AqE29kh3ygCzN0IZWLgGis2K16aD9JoYXnaRBD2LgghA18Bc0ZG76AuWEzr3eAMTSRen8SsBPjtPftUVnuXECrjVfhd9z_WeDbx9MaHUO7GS9","production":True,"tos_version":4,"device_key":"AzsVI0WrO7ogCD1XQc4x7UP8NFvWkgprHKr9Dy3EldUs","sig_ts":1654180945,"sig":"MEQCIAMQ36cVdxjL+/jCGsfKmjhtEQVZFMIW2ICzHzhuADhbAiAlDdhjLkrxVTPer/EPmeIOqrU8f5yJyBCmsBaqw6pFxQ==","hashes":[1135420871,4291554428,1662465570,2939294528,2864712656,784335679,1246829562,4147059363,191933768,3062676827,3931787622,2766223387,576746911,2275726205,1729690551,2495669098,2669125820,495611257,1810499009,3661381049,943977965,3914553296,2198427157,1330181820],"integrity":True}
        info = requests.post('https://live.radiance.thatgamecompany.com/account/auth/login', headers=self.get_headers(), json=datos_user).text
        x = json.loads(info)
        print(x)
        if "result" in x:
            sesiones = x["result"]
            userid = x["result"]
        else:
            sesiones = x["session"]
            userid = x["authinfo"]["user"]
        return userid, sesiones