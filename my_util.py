import shutil, os
import time
import zipfile
def zip(src_path, dest_file):
    """
    src_path: ziped path
    dest_file: 
    """
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath);
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()
    return "ok"

"""
src_path = 'C:\\mylab\\book\\automate_basic\\download\\2020\\09\\18'

f_name='send'
dest_file = 'C:\\mylab\\book\\automate_basic\\send_temp\\'+ f_name + '.zip'

zip(src_path, dest_file) #src_path, dest_file
"""    

def mkdir_rm(path0):
    if os.path.exists(path0):
        shutil.rmtree(path0)
    time.sleep(0.5)
    # os.mkdir(path0)
    os.makedirs(path0)
    