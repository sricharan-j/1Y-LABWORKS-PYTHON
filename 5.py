import statistics

sensor_data = [24.5, 25.1, 26.3, 27.0, 28.2,
               29.1, 27.8, 26.5, 25.7, 30.2]
print("Sensor Data:", sensor_data)
print("Mean :", round(statistics.mean(sensor_data), 2))
print("Median :", round(statistics.median(sensor_data), 2))
print("Minimum :", min(sensor_data))
print("Maximum :", max(sensor_data))
print("Std. Dev. :", round(statistics.pstdev(sensor_data), 2))
threshold = 28.0
high_values = [value for value in sensor_data if value > threshold]
print("Values above", threshold, ":", high_values)