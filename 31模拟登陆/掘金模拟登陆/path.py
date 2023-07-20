import os

path = r'File/File1/File2/test.txt'
# if os.path.exists(path):
#     pass
# else:
#     # os.makedirs(path)创建多个文件夹
#     os.mkdir(path)
# with open(file=path, mode='w') as f:
#     f.write('dsd')
#     f.close()

Dir = 'Downloads/'  # 目录
path = Dir + 'filename.png'  # 文件路径
if not os.path.exists(Dir):
    os.makedirs(Dir)
