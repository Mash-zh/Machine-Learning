import matplotlib.pyplot as plt
import numpy as np

epochs = 30  # 迭代次数

# 创建数据
x_linear = np.linspace(-10, 10, 100)  # 生成从-10到10的100个均匀分布的数


def f(x):
    return x ** 2 + 2 * x + 1  # 计算二次函数值


y_linear = f(x_linear)


def grad(x):
    return 2 * x + 2  # 梯度函数


x_history = []
y_history = []
x = -7  # 初始x值

# 打开交互模式
plt.ion()
fig, (ax, table_ax) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 2]}, figsize=(14, 12))

# 绘制函数曲线
ax.plot(x_linear, y_linear, label=r'$x^2 + 2x + 1$', color='blue')

# 设置表格区域
table_ax.axis('off')  # 关闭表格坐标轴

# 定义每行显示的最大数据数量
max_columns = 10  # 每行最多显示10个数据点
num_columns = max_columns + 1  # 表格列数 = 数据点数量 + 1 (标签)

# 动态绘制散点和更新表格
for i in range(epochs):
    x_history.append(x)
    y_history.append(f(x))

    # 更新散点图
    ax.scatter(x, f(x), color='red', marker='o')  # 绘制当前散点
    ax.draw_artist(ax.lines[-1])  # 重新绘制最新的散点

    # 将数据分为多行
    x_rows = [x_history[j:j + max_columns] for j in range(0, len(x_history), max_columns)]
    y_rows = [y_history[j:j + max_columns] for j in range(0, len(y_history), max_columns)]

    # 创建表格数据
    table_data = []

    # 表头
    header = ['Index'] + [f'Point {j + 1}' for j in range(max_columns)]
    table_data.append(header)

    # 添加x和y数据行
    for j in range(len(x_rows)):
        row_x = ['x'] + [f'{xi:.2f}' for xi in x_rows[j]] + [''] * (num_columns - len(x_rows[j]) - 1)
        row_y = ['y'] + [f'{yi:.2f}' for yi in y_rows[j]] + [''] * (num_columns - len(y_rows[j]) - 1)
        table_data.append(row_x)
        table_data.append(row_y)

    # 确保每行列数一致
    for row in table_data:
        while len(row) < num_columns:
            row.append('')

    # 创建背景颜色矩阵
    cell_colours = []
    color1 = 'lightgrey'
    color2 = 'white'

    for row_idx in range(len(table_data)):
        if row_idx == 0:
            # 表头行，不使用背景颜色
            cell_colours.append([None] * num_columns)
        elif (row_idx - 1) % 2 == 0:
            # 从第二行开始，每两行涂上相同的背景颜色
            color = color1 if (row_idx // 2) % 2 == 0 else color2
            cell_colours.append([color] * num_columns)
        else:
            cell_colours.append([color] * num_columns)

    # 删除旧表格并绘制新表格
    table_ax.clear()
    table = table_ax.table(cellText=table_data, cellLoc='center', loc='center', cellColours=cell_colours)
    table.auto_set_font_size(False)
    table.set_fontsize(20)  # 增加字体大小
    table.scale(1, 3)  # 放大表格

    # 确保显示边框
    for (i, j), cell in table._cells.items():
        cell.set_edgecolor('black')  # 设置边框颜色
        cell.set_linewidth(1)  # 设置边框宽度

    # 隐藏表格区域的所有坐标轴标签和刻度
    table_ax.set_xticks([])  # 移除x轴刻度
    table_ax.set_yticks([])  # 移除y轴刻度
    table_ax.spines['top'].set_visible(False)  # 隐藏上边框
    table_ax.spines['right'].set_visible(False)  # 隐藏右边框
    table_ax.spines['left'].set_visible(False)  # 隐藏左边框
    table_ax.spines['bottom'].set_visible(False)  # 隐藏下边框

    # 刷新图表
    plt.draw()  # 刷新图表
    plt.pause(0.3)  # 暂停0.3秒以显示动态效果

    # 更新x值
    x = x - 0.1 * grad(x)

# 设置x轴刻度从-10到10，间隔为1
ax.set_xticks(np.arange(-10, 11, 1))

# 添加标题和标签
ax.set_title('Dynamic Gradient Descent Visualization')  # 图表标题
ax.set_xlabel('X')  # X轴标签
ax.set_ylabel('y')  # Y轴标签
ax.legend()  # 显示图例
ax.grid(True)  # 显示网格

# 关闭交互模式并显示最终图形
plt.ioff()
plt.show()
