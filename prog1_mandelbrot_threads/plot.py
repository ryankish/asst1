import os
import pandas as pd
import matplotlib.pyplot as plt

for file_path in ['results_view1.csv', 'results_view2.csv']:
    data = pd.read_csv(file_path)

    data.columns = ['threads', 'time']

    plt.figure(figsize=(10, 6))
    plt.plot(data['threads'], data['time'], marker='o', linestyle='-', label='Execution Time')
    plt.title('Execution Time vs Number of Threads')
    plt.xlabel('Number of Threads')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.savefig(os.path.splitext(file_path)[0] + '.png')
    plt.close()
