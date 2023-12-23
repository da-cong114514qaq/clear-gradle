# 引用
import os # 关于系统的必备库
import shutil # 执行文件操作使用的库

# 赋值
name = os.environ.get( "USERNAME" ) # 获取Windows用户名
gradle = 'C:\\Users\\' + name + '\\.gradle' # 赋值路径，为了美观（bushi

# 执行删除
shutil.rmtree(gradle)
