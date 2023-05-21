import matplotlib.pyplot as plt
import numpy as np

# 已有数据
x = np.array([5, 10, 20, 40, 60, 80,100,120,360])
y = np.array([0.181980309730487,0.362801919222153,0.719243355989499,1.44000144000144,2.14769194258468,2.86277997764527,3.58138642452197,4.29951033951621,12.880622391674])

# 计算线性回归拟合参数
p = np.polyfit(x, y,1)
a, b = p

# 计算相关指数
r = np.corrcoef(x, y)[0, 1]

# 绘制散点图
plt.scatter(x, y)

# 生成线性回归拟合直线的x和y坐标
x_fit = np.linspace(0, 120 )
y_fit = a * x_fit + b

# 绘制线性回归拟合直线
plt.plot(x_fit, y_fit, color='r')

# 在图右下角标注线性回归拟合直线方程和相关指数
plt.text(0.6, 0.1, 'y = {}x + {}\nr$^2$= {}'.format(round(a, 2), round(b, 2), round(r, 2)), transform=plt.gca().transAxes, color='red')

# 添加标题和轴标签
plt.title('Cu(Ⅱ) standard curve line')
plt.xlabel('C')
plt.ylabel('Abs')

# 显示图形
plt.show()
