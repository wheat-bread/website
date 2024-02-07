import streamlit as st
from PIL import Image, ImageDraw, ImageFont,ImageOps,ImageFilter
from maze import*

#python -m streamlit run D:\1a张麦\python\张麦_我的网络根据地\zhangmai_.py [ARGUMENTS]

page=st.sidebar.radio('我的首页',['我的视频/推荐模组','Phigros曲绘','数学','植物大战僵尸PE阵型','图片处理','词典','留言','迷宫计算器'])

def page1():
    with open('aapa.mp3','rb') as f:
        music=f.read()
    st.audio(music,format='audio/mp3',start_time=0)
    st.write("Rrhar'il")
    st.image("Rrhar'il.jpg")
    st.write("concvssion")
    st.image("concvssion.png")
    st.write("Aleph-0")
    st.image("Aleph-0.png")

def page2():
    st.write("诱导公式")
    st.image("ydgs.jpg")
    st.write("和差角公式")
    st.image("hcjgs.jpg")
    st.write("二倍角公式")
    st.image("ebjgs.jpg")

def page3():
    st.write("经典八炮 节奏：ch6(PP丨I-PP丨PP丨I-PP)")
    st.image("jd8.png")
    st.write("传统四炮")
    st.image("ct4.png")
    st.write("石英钟无炮")
    st.image("syz.png")
    st.write("机械钟无炮")
    st.image("jxz.png")

def page4():
    st.write(':sunglasses:图片处理:sunglasses:')
    file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if file:
        fname=file.name
        ftype=file.type
        fsize=file.size
        img=Image.open(file)
        t1,t2,t3,t4,t5,t6=st.tabs(['原图','改色1','改色2','改色3','字符画','素描'])
        with t1:
            st.image(img)
        with t2:
            st.image(imgchange(img,0,2,1))
        with t3:
            st.image(imgchange(img,1,2,0))
        with t4:
            st.image(imgchange(img,1,0,2))
        with t5:
            st.image(wordimg(img))
        with t6:
            st.image(sketchimg(img))

def page5():
    st.write('智慧词典')
    with open('words.txt',encoding='utf-8') as f:
        wordlist=f.read().split('\n')
    wordl=[wordlist[i].split('#') for i in range(len(wordlist))]
    words={i[1]:[int(i[0]),i[2]] for i in wordl}
    with open('times.txt',encoding='utf-8') as f:
        timelist=f.read().split('\n')
    timel=[timelist[i].split('#') for i in range(len(timelist))]
    times={int(i[0]):int(i[1]) for i in timel}
    word=st.text_input('请输入要查询的单词')
    if word in words:
        n=words[word][0]
        times[n]=times[n]+1 if n in times else 1
        st.write('释义：',words[word][1],'，此单词查询次数：',times[n])
        with open('times.txt','w',encoding='utf-8') as f:
            msg=''
            for k,v in times.items():
                msg+=f'{k}#{v}\n'
            msg=msg[:-1]
            f.write(msg)
        if word=='phigros':
            st.balloons()
        
def page6():
    st.write('留言区')
    with open('msgs.txt',encoding='utf-8') as f:
        msgl=f.read().split('\n')
    msgs=[msgl[i].split('#') for i in range(len(msgl))]
    for i in msgs:
        with st.chat_message('🌞'):
            st.write(i[1],':',i[2])
    name=st.text_input('我是')
    msg=st.text_input('要说的话')
    if st.button('留言'):
        msgs.append([str(int(msgs[-1][0])+1),name,msg])
        with open('msgs.txt','w',encoding='utf-8') as f:
            msg=['#'.join(i) for i in msgs]
            msg='\n'.join(msg)
            f.write(msg)
def page7():
    st.write('我的视频')
    c1, c2 = st.columns([1,1])
    with c1:
        st.write('植物大战僵尸ZM版发布视频')
        st.image('vd2.jpg')
        st.link_button('跳转', 'https://www.bilibili.com/video/BV1WP4y1e7BH/')
    with c2:
        st.write('4x5x6 机械动力匠魂焦黑砖工厂')
        st.image('vd3.jpg')
        st.link_button('跳转', 'https://www.bilibili.com/video/BV1vk4y1w7fA/')
    c1, c2 = st.columns([1,1])
    with c1:
        st.write('【冰与火之舞自制谱】LeaF-Armageddon')
        st.image('vd1.jpg')
        st.link_button('跳转', 'https://www.bilibili.com/video/BV1Lk4y1N7tv/')
        
    
    st.write('mc模组推荐')
    a=st.radio('选择网站:',['mc百科', 'curseforge'])
    c1, c2= st.columns([1,1])
    with c1:
        st.write('[IC2]工业时代2 Industrial Craft 2')
        st.image('mc1.jpg')
        if a=='mc百科':
            st.link_button('跳转', 'https://www.mcmod.cn/class/2.html')
        else:
            st.link_button('跳转', 'https://www.curseforge.com/minecraft/mc-mods/industrial-craft')
    with c2:
        st.write('机械动力 Create')
        st.image('mc2.jpg')
        if a=='mc百科':
            st.link_button('跳转', 'https://www.mcmod.cn/class/2021.html')
        else:
            st.link_button('跳转', 'https://www.curseforge.com/minecraft/mc-mods/create')
    c1, c2= st.columns([1,1])
    with c1:
        st.write('[Mek]通用机械 Mekanism')
        st.image('mc3.jpg')
        if a=='mc百科':
            st.link_button('跳转', 'https://www.mcmod.cn/class/187.html')
        else:
            st.link_button('跳转', 'https://www.curseforge.com/minecraft/mc-mods/mekanism')

def page8():
    st.write('自动走迷宫！左上角是起点，右下角是终点，勾选的框是障碍物')
    w=st.text_input('请输入迷宫的列数')
    h=st.text_input('请输入迷宫的行数(不超过20)')
    if w=='':
        w=5 
    if h=='':
        h=5 
    try:
        w,h=int(w),int(h)
        if 2<=h<=20 and w>=2:
            maze=[]
            i=0
            for row in range(w):
                if h!=20:
                    cols=st.columns([1]*h+[20-h])
                else:
                    cols=st.columns([1]*h)
                colmaze=[]
                for col in cols[:-1]:
                    i+=1
                    with col:
                        colmaze.append(st.checkbox(' '*i))
                maze.append(colmaze)
            if st.button('开始计算'):
                st.write('计算中...')
                mazeobj = Maze(maze=maze)
                # try:
                if 1:
                    res = mazeobj.search().path()
                    acttxt='计算完成，路线为：'
                    for act in mazeobj.search().path(lambda self:self.act):
                        if act=='right':
                            acttxt+='向右'
                        elif act=='left':
                            acttxt+='向左'
                        elif act=='up':
                            acttxt+='向上'
                        else:
                            acttxt+='向下'
                        acttxt+='，'
                    st.write(acttxt[:-1]+'。')
                # except AttributeError:
                #     st.write('此迷宫无解！')
        else:
            st.write('请重新输入!')
    except ValueError:
        st.write('请重新输入!')

def imgchange(img,rc,gc,bc):
    w,h=img.size
    imgarray=img.load()
    for x in range(w):
        for y in range(h):
            r=imgarray[x,y][rc]
            g=imgarray[x,y][gc]
            b=imgarray[x,y][bc]
            imgarray[x,y]=(r,g,b)
    return img

def wordimg(img1):
    img=img1.convert('L')
    img = img.resize((int(img.width/8), int(img.height/8)))
    ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
    new_img = Image.new('RGB', size=img1.size, color=(255, 255, 255))
    for y in range(img.height):
        for x in range(img.width):
            pos = (x, y)
            gray = img.getpixel(pos)
            index = int(gray/256*70)
            draw = ImageDraw.Draw(new_img)
            draw.text((x*8,y*8), ASCII_HIGH[index], fill=(0,0,0), font=ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 9))
    return new_img

def sketchimg(img):
    w,h=img.size
    img_gray = img.convert('L')
    img_invert = ImageOps.invert(img_gray)
    img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))
    img_gray1 = img_gray
    for x in range(w):
        for y in range(h):
            pos = (x, y)
            A = img_gray.getpixel(pos)
            B = img_gaussian.getpixel(pos)
            img_gray1.putpixel(pos, min(int(A + A * B / (255 - B)), 255))
    return img_gray1

if page=='Phigros曲绘':
    page1()
elif page=='数学':
    page2()
elif page=='植物大战僵尸PE阵型':
    page3()
elif page=='图片处理':
    page4()
elif page=='词典':
    page5()
elif page=='留言':
    page6()
elif page=='我的视频/推荐模组':
    page7()
elif page=='迷宫计算器':
    page8()