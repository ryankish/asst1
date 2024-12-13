import pandas as pd
import matplotlib.pyplot as plt

file_path = 'results.csv'
data = pd.read_csv(file_path)

data.columns = ['threads', 'time']

plt.figure(figsize=(10, 6))
plt.plot(data['threads'], data['time'], marker='o', linestyle='-', label='Execution Time')
plt.title('Execution Time vs Number of Threads')
plt.xlabel('Number of Threads')
plt.ylabel('Execution Time (ms)')
plt.legend()
plt.savefig('prog1_mandelbrot_threads.png')
plt.close()
