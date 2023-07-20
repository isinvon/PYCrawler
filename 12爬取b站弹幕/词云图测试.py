

from matplotlib import pyplot as plt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

string = 'Importance of relative word frequencies for font-size. With relative_scaling=0, only word-ranks are considered. With relative_scaling=1, a word that is twice as frequent will have twice the size. If you want to consider the word frequencies and not only their rank, relative_scaling around .5 often looks good.'
font = r'C:\WINDOWS\FONTS\ARLRDBD.TTF'
wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               ).generate(string)
wc.to_file('ss.png')  # 保存图片

# 使用以下代码可能会报错, 报错请参考https://blog.csdn.net/m0_37724919/article/details/128874187
# plt.imshow(wc)  # 用plt显示图片
# plt.axis('off')  # 不显示坐标轴
# plt.show()  # 显示图片

