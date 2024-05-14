import json
import os
import re
from datetime import datetime

class LogQueryInterface:
    def __init__(self, log_files):
        self.logs = []
        for log_file in log_files:
            if os.path.exists(log_file):
                with open(log_file, 'r') as file:
                    self.logs.extend([json.loads(line.strip()) for line in file])
            else:
                print(f"Warning: {log_file} does not exist and will be skipped.")

    def filter_logs(self, level=None, log_string=None, start_time=None, end_time=None, source=None):
        filtered_logs = self.logs
        
        if level:
            filtered_logs = [log for log in filtered_logs if log['level'] == level]
        if log_string:
            filtered_logs = [log for log in filtered_logs if re.search(log_string, log['log_string'])]
        if start_time:
            start_time = datetime.fromisoformat(start_time.replace('Z', ''))
            filtered_logs = [log for log in filtered_logs if datetime.fromisoformat(log['timestamp'].replace('Z', '')) >= start_time]
        if end_time:
            end_time = datetime.fromisoformat(end_time.replace('Z', ''))
            filtered_logs = [log for log in filtered_logs if datetime.fromisoformat(log['timestamp'].replace('Z', '')) <= end_time]
        if source:
            filtered_logs = [log for log in filtered_logs if log['metadata']['source'] == source]
        
        return filtered_logs

    def search(self, **kwargs):
        results = self.filter_logs(**kwargs)
        if results:
            for result in results:
                print(json.dumps(result, indent=4))
        else:
            print("No logs found matching the criteria.")

def main():
    log_files = [f'logs/log{i}.log' for i in range(1, 10)]
    query_interface = LogQueryInterface(log_files)
    
    # Sample queries
    print("Error logs:")
    query_interface.search(level='error')
    
    print("\nLogs containing 'Failed to connect':")
    query_interface.search(log_string='Failed to connect')
    
    print("\nLogs from 2023-09-10 to 2023-09-15:")
    query_interface.search(start_time='2023-09-10T00:00:00Z', end_time='2023-09-15T23:59:59Z')
    
    print("\nInfo logs from API1:")
    query_interface.search(level='info', source='logs/log1.log')

if __name__ == "__main__":
    main()



