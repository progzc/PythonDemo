import traceback

# 使用traceback模块打印异常信息
# 注意顺序的随机性
try:
    print('-------------------------')
    print(1 / 0)
except:
    traceback.print_exc()
