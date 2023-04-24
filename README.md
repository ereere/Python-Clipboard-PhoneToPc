# Python-Clipboard-PhoneToPc
## 主要功能：通过网络方式将手机剪切板复制到电脑剪切板
 电脑端需要先安装python，然后pip install 安装头部引用的模块。
 
 安卓手机端是用“HTTP Request Shortcuts”app 中文名是“HTTP 快捷方式” ，可以导入shortcuts.json，也可以自己填写，简单验证配合读取手机剪切板权限，一键发送到电脑剪切板。修改http://192.168.1.2:8087/topc 的地址为电脑端ip
 
 监听地址改为“::”可以侦听外网ipv6
 
 电脑端锁屏情况下没权限复制内容到电脑剪切板（win10下）
 
 极度简单，没有安全措施。
 
 手机端拉取电脑端剪切板修改代码也能简单实现。
