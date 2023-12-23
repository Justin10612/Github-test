class Smoother:
    def __init__(self, window_size):
        self.window_size = window_size
        self.values = []

    def smooth(self, value):
        self.values.append(value)
        if len(self.values) > self.window_size:
            self.values = self.values[1:]
        return sum(self.values) / len(self.values)

# 在這裡設定移動平均窗口大小
window_size = 5
smoother = Smoother(window_size)

# 模擬輸出，這裡假設輸出是一個 list
output_values = [1, 0, 0, 3, 0, 0, 5, 6, 0, 0]

# 對每個輸出值進行平滑處理
smoothed_values = [smoother.smooth(value) for value in output_values]

# 輸出平滑處理後的值
print("原始輸出:", output_values)
print("平滑處理後的輸出:", smoothed_values)