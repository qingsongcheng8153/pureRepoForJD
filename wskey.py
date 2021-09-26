mport requests
import json
import urllib3
urllib3.disable_warnings()

while True:
        wskey=input("请输入wskey（样例：pin=xxxxxxx;wskey=xxxxx）：")
            headers={
                            "user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"
                                }
                url="https://jdsign.tk/getck"
                    data={"wskey":wskey}
                        data=json.dumps(data)
                            r=requests.post(url,headers=headers,data=data, verify=False)
                                print(r.text)


                                    
