import pandas as pd  
import matplotlib.pyplot as plt

# 读取 csv 文件  
data = pd.read_csv('your_file.csv')

# 按照 Task Group 分组  
grouped_data = data.groupby('Task Group')

# 提取创建、打开和关闭的任务总数  
created_tasks = grouped_data['Project'].count()  
open_tasks = grouped_data['Status'].count()  
closed_tasks = grouped_data['Status'].count()

# 准备数据  
created_tasks_dict = dict(created_tasks)  
open_tasks_dict = dict(open_tasks)  
closed_tasks_dict = dict(closed_tasks)

# 生成条形图  
fig, ax = plt.subplots()  
ax.bar(['创建', '打开', '关闭'], [created_tasks_dict, open_tasks_dict, closed_tasks_dict])

# 设置图例和坐标轴标签  
ax.legend([f'创建 ({created_tasks_dict[group]:,.0f})', f'打开 ({open_tasks_dict[group]:,.0f})', f'关闭 ({closed_tasks_dict[group]:,.0f})'], loc='upper left')  
ax.set_xlabel('任务状态')  
ax.set_ylabel('任务数量')

# 显示图形  
plt.show()  
