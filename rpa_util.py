

#https://lifeonroom.com/diy/diy-software/lostark-window-focus/
# pywinauto set_focus
# rpa_util.py
import pywinauto as pwa
import time, sys, os
import pyautogui as pag
import shutil
import zipfile
def zip(src_path, dest_file):
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath);
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()


"""
ru.mkdir_rm(TEMP_DIR +'\\SEND')
f_name = datetime.now().strftime("%Y%m%d_%H%M%S")
z_file_path1 = TEMP_DIR +'\\SEND\\'+ f_name + '.zip'

targ_folder = ROOT_DIR+r'\Data_Export'  # D:\SEND_IFM\Data_Export
ru.zip(targ_folder, z_file_path1) #src_path, dest_file
"""

def mkdir_rm(path0):
    if os.path.exists(path0):
        shutil.rmtree(path0)
    time.sleep(0.5)
    # os.mkdir(path0)
    os.makedirs(path0)

def click_img(img, x_plus=100, confidence=0.7, sleep=0.0):
    location1 = pag.locateOnScreen(img, confidence=confidence)
    point1 = pag.center(location1)
    #print(point1)
    time.sleep(sleep)
    x, y = point1
    pag.click(x+x_plus, y)

def file_save_as_by_click(img_path, file_save_path, clicked_img):
    #----------------------------------------------------------------------------------
    # 조회한 내역(엑셀, zip파일 등) 다른 이름으로 저장
    #img='file_download_save.PNG'
    click_img(img_path+clicked_img,x_plus=0, confidence=0.85)
    pag.press('A') #다른 이름으로 저장
    time.sleep(0.5)
    #오늘 날짜로 저장한다.
    pag.typewrite(file_save_path) #pag.typewrite(r'd:\SEND_IFM\1111.xls')
    pag.press('enter')

# 특정 프로그램을 윈도우 Top으로 전환하는 함수
def setFocus(title_reg):
    app = pwa.application.Application()
    # title 이름 정규표현식
    t = title_reg

    print('find title : ' + str(title_reg))
    try:
        # title 을 기반으로 window handle 을 가져옴
        handle = pwa.findwindows.find_windows(title_re=t)[0]
        # 해당 윈도우 Control을 위해 라이브러리와 연결
        app.connect(handle=handle)
        print('title: ' + str(t) + 'handle: ' + str(handle) + ' Setted')
    except:
        print('No title exist on window ')

    # 어플리케이션의 window를 가져옴
    window = app.window(handle=handle)
    try:
        # 해당 윈도우를 탑으로 설정
        window.set_focus()
    except Exception as e:
        print('[error]setFocuse : ' + str(e))
    return window

def setFocus_test():
    # 타이틀의 정규표현식
    #t = u'LOST ARK .*'
    title_reg= u'계산기'
    return setFocus(title_reg)

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
# section='setup'; option='run_status'
# print(get_config(section, option))
## rpa를 전체적으로 중단하는데 사용한다.
def get_config(section, option):
    # instantiate
    config = ConfigParser()
    # parse existing file
    config.read('D:\\SEND_IFM\\SYSTEM_INFO\\run_config.ini')
    #option='run_config'
    rt = config.get(section, option)
    #print(rt)
    return rt

def get_user_info():
    # Load pickle
    with open("user_info.pickle","rb") as f:
        loaded_lm = pickle.load(f)

    login_mgr = loaded_lm[service]
    #print(ss.get_user_info())
    return login_mgr.get_user_info()


"""
if __name__=="__main__":
    setFocus_test()
"""
