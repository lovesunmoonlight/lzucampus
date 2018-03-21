# -*- coding: utf-8 -*-
#校园网自动登陆

import requests
import tkinter
from tkinter import messagebox

url="http://10.10.1.6/include/auth_action.php"
data={"action":"login","username":"xxx","domain":"@cernet","password":"xxx","ac_id":"1","user_ip":"","nas_ip":"","user_mac":"","save_me":"1","ajax":"1"}
res=requests.post(url,data=data)
messagebox.showinfo('提示', '成功登录到校园网')