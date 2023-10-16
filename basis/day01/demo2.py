#!/usr/bin/python3

# input("\n\n按下enter键后退出！")

# import sys;
# x='runoob'; sys.stdout.write(x+'\n'+'hello world\n');



x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()


print('---------')
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
# https://www.runoob.com/python3/python3-data-type.html

