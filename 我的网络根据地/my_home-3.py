'我的主页'

import streamlit as st
import time

from PIL import Image

page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])
tab4,tab5,tab6=st.tabs(["最爱游戏","图片","音乐"])

def page_1():
    with tab4:
        st.write("最爱的游戏")
        st.write(':green[我的世界]')    
        st.write(':blue[Minecraft （《我的世界》）是由 Mojang Studios开发的一款3D\n沙盒电子游戏 。玩家可在游戏中无拘无束地在3个维度内与由方\n块和实体构成的世界互动。多种玩法可供玩家选择，带来无限可\n能。 Minecraft当前可分为Java版 、基岩版和教育版 ，另有为中\n国大陆玩家提供的中国版 。 ]')
        #st.write('https://www.minecraft.net/zh-hans')  
        go = st.selectbox('请选择我的世界类型', ['国际版', '网易版','其它'])
        if go == '国际版':
            st.link_button('进入国际版', 'https://www.minecraft.net/zh-hans')
        elif go == '网易版':
            st.link_button('进入网易版', 'https://mc.163.com/fab/')
        elif go=='其它':
            st.link_button('进入HMCL','https://hmcl.huangyuhui.net/')
    with tab6:
        with open('111.mp3','rb') as f:
            mymp3=f.read()
        st.audio(mymp3,format="audio/mp3",start_time=0)
    with tab5:
        st.image('down.jpeg')
        st.image('icon.png')
        st.image('00.jpeg')
        st.image('114.png')

def page_2():        
    ex = st.toggle('是否开启处理程序')
    if ex:

        st.write(":sunglasses:图片/音频处理小程序：sunglasses")
        uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg','gif'])
        uploaded_file1=st.file_uploader("上传音频mp3(未完全做好)",type=['mp3'])

        if uploaded_file:
            img=Image.open(uploaded_file)
            #st.image(img)
            #st.image(img_change(img,0,2,1))
            tab1,tab2,tab3,tab4=st.tabs(["原图","改色001","改色002","改色003"])

            with tab1:
                st.image(img)
            
            with tab2:
                st.image(img_change(img,0,2,1))
            with tab3:
                st.image(img_change(img,1,0,2))
            with tab4:
                st.image(img_change(img,1,2,0))

def page_3():
    st.write("智慧词典")
    with open('words_space.txt',encoding='utf-8')as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')


    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8')as f:
        times_list=f.read().split('\n')
        
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
        

    word=st.text_input("请输入查询单词：(里面有亿堆彩蛋)")
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 2):
        time.sleep(0.001)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')

    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8')as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        
        if word == 'mini' :
            st.code('''竟敢输入我最痛恨的游戏英文缩写！！！他是mc的敌对游戏''')
        if word == 'mc' :
            st.code('''这是mo款游戏缩写，猜猜它的全称吧''')
        if word == 'minecraft' :
            st.code('''恭喜你输入了我最爱的游戏我的世界的全称''')

        if word == 'unikun' :
            st.code('''请看下面''')
            st.image("1234.png")
        if word == 'zhangruixuan':
            st.balloons()
        if word== 'python':
            st.snow()

        if word== 'jietu4':
            st.image("jt4.png")

        if word =='mcupdate':
            st.image('114.png')
            

def page_4():
    st.write('我的留言区')
    
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        messages_list=f.read().split('\n')

        
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
        
    for i in messages_list:
        if i[1]=='鸡你太美':
            with st.chat_message('🐔'):
                st.write(i[1],':',i[2])
        elif i[1]=='小黑子':
            with st.chat_message('👤'):
                st.text(i[1]+i[2])
     
    

    name=st.selectbox('我是……',['鸡你太美','小黑子'])
    new_message=st.text_input('想要说的话……')
    
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])


        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)

    begin, end = st.slider('选择显示的留言信息(功能未完善)：', 1, len(messages_list), (len(messages_list)-1,len(messages_list) ))
    for i in range(begin-1, end):
        st.write(messages_list[i]) 


            
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

if page=='我的兴趣推荐':
    page_1()

if page=='我的图片处理工具':
    page_2()

if page=='我的智慧词典':
    page_3()

if page=='我的留言区':
    page_4()
