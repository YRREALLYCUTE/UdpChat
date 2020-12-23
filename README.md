### 基于UDP的即时聊天程序

1. server文件夹中存在两个二进制文件users和groups

    分别存储了users和groups的信息，我在打包之后重新加入了部分用户信息，因此
    可以直接使用。

    用户：sjq, wyr, admin, test, test1, test2, test3, test4, test5
    密码：123456

    用户组：group1, sjq们，test_group

2. client文件夹中为客户端，为了方便测试，可以修改client代码中的SERVER_HOST
    变量为本机IP(当前设置)，直接在本机打开多个客户端进行测试。也可以重新设置
    服务器内网IP地址并打包，从而可以在内网环境下的不同机器上进行测试。

     >打包需要安装pyinstaller (`pip install pyinstaller`)
     >
     >命令：`pyinstaller -F -w -i .\1.ico -n udpChat_client-v1.0 Main.py`
    

3. server需要请求管理员权限，请务必同意。

4. 在服务器没有打开的情况下，客户端之间是不能通信的。如果发现客户端运行异常，
    首先请确定服务器已经正确打开并开启服务。

5. 服务器需要使用7215端口，请确定7215端口没有被其他程序占用。

6. client 选择联系人时请双击。


    **注意**                                                                                                      
    >  由于系统、环境存在差异，如果服务器无法打开，大概率是由于users、groups文
    >  件。可以将原文件删除，并新建同名的空文件，再重新尝试打开服务器。
    >  
    >  如果仍无法打开，请联系：1757268018@qq.com
