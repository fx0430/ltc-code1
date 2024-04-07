# # 监测心率
# import numpy as np
# import time
# from datetime import datetime
# # 模拟数据生成函数
# def generate_heartbeat_signal(heart_rate):
#     """生成模拟的心率信号"""
#     # 简化处理
#     signal = np.sin(2 * np.pi * heart_rate * np.arange(0, 10) / 60)
#     return signal
# # 心率计算函数
# def calculate_heart_rate(signal):
#     """根据信号计算心率"""
#     # 假设信号峰值之间的时间间隔对应心跳周期
#     peaks = np.where(signal > 0.5)[0]
#     if len(peaks) < 2:
#         return None
#         # 计算两个峰值之间的平均时间间隔（秒）
#     interval = np.mean(np.diff(peaks)) / 10
#     # 将时间间隔转换为心率（次/分钟）
#     heart_rate = 60 / interval
#     return heart_rate
# # 模拟手表检测心率
# def simulate_watch_heart_rate_detection():
#     while True:
#         # 生成模拟心率信号，这里假设心率是 75 次/分钟
#         signal = generate_heartbeat_signal(75)
#
#         # 计算心率
#         heart_rate = calculate_heart_rate(signal)
#
#         if heart_rate is not None:
#             print(f"当前心率: {heart_rate:.2f} BPM")
#             print("检测时间：",datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
#             # 等待一段时间再次检测
#         time.sleep(10) # 每10秒检测一次
#     # 运行模拟
# simulate_watch_heart_rate_detection()
import time
import random

# 假设的心率阈值
HEART_RATE_THRESHOLD = 115
HEART_RATE_THRESHOLD1 = 70
# 模拟从设备或API读取心率数据的函数
def get_heart_rate_from_device():
    # 这里我们简单地返回一个随机心率值作为示例
    # 在实际应用中，你应该从设备或API获取真实的心率数据
    return random.randint(60, 120)

def main():
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        heart_rate = get_heart_rate_from_device()

        print(f"当前时间: {current_time}, 心率: {heart_rate} 次/分钟")

        if heart_rate > HEART_RATE_THRESHOLD:
            print("警告：心率过高！")
        elif heart_rate < HEART_RATE_THRESHOLD1:
            print("警告：心率过低！")

            # 等待一段时间再次检测，这里设置为1秒
        time.sleep(1)

if __name__ == "__main__":
    main()