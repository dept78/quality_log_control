# Quality Log Control

## Overview

Quality Log Control is a system designed to capture and manage logs from various APIs. The system supports log ingestion from multiple sources, storing them in different log files, and provides a query interface to search through these logs based on various criteria.

## Features

- **Log Ingestor**
  - Integrates multiple APIs to capture logs at different stages.
  - Standardizes log format across all APIs.
  - Configurable logging levels and file paths.
  - Robust error handling to ensure uninterrupted application functionality.
  - Scalability to handle high volumes of logs.

- **Query Interface**
  - Full-text search across logs.
  - Filters based on:
    - Level
    - Log string
    - Timestamp
    - Source
  - Efficient and quick search results.
  - Additional functionalities:
    - Search within specific date ranges.
    - Use of regular expressions for search.
    - Combining multiple filters.

## System Design

### Log Ingestor

The Log Ingestor is responsible for capturing logs from multiple APIs and storing them in specified log files. Each API logs messages at different levels (info, error, etc.), and the logs are stored in JSON format for consistency.

### Query Interface

The Query Interface allows users to search through the logs using various filters. It supports filtering by log level, message content, timestamps, and source of the logs. The interface is designed to be user-friendly and efficient, providing quick search results.

## File Structure

quality_log_control/
│
├── logs/
│ ├── log1.log
│ ├── log2.log
│ ├── log3.log
│ └── ... (more log files)
│
├── config.json
├── log_ingestor.py
├── query_interface.py
└── README.md


## How to Run the Project

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd quality_log_control
2. **Set up a virtual environment:**

python -m venv venv
source venv/bin/activate 
3. **Install dependencies:**


pip install -r requirements.txt



Sure, here is a README.md file for your project:

markdown
Copy code
# Quality Log Control

## Overview

Quality Log Control is a system designed to capture and manage logs from various APIs. The system supports log ingestion from multiple sources, storing them in different log files, and provides a query interface to search through these logs based on various criteria.

## Features

- **Log Ingestor**
  - Integrates multiple APIs to capture logs at different stages.
  - Standardizes log format across all APIs.
  - Configurable logging levels and file paths.
  - Robust error handling to ensure uninterrupted application functionality.
  - Scalability to handle high volumes of logs.

- **Query Interface**
  - Full-text search across logs.
  - Filters based on:
    - Level
    - Log string
    - Timestamp
    - Source
  - Efficient and quick search results.
  - Additional functionalities:
    - Search within specific date ranges.
    - Use of regular expressions for search.
    - Combining multiple filters.

## System Design

### Log Ingestor

The Log Ingestor is responsible for capturing logs from multiple APIs and storing them in specified log files. Each API logs messages at different levels (info, error, etc.), and the logs are stored in JSON format for consistency.

### Query Interface

The Query Interface allows users to search through the logs using various filters. It supports filtering by log level, message content, timestamps, and source of the logs. The interface is designed to be user-friendly and efficient, providing quick search results.

## File Structure

quality_log_control/
│
├── logs/
│ ├── log1.log
│ ├── log2.log
│ ├── log3.log
│ └── ... (more log files)
│
├── config.json
├── log_ingestor.py
├── query_interface.py
└── README.md

markdown
Copy code

## How to Run the Project

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd quality_log_control
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:


pip install -r requirements.txt
Configuration
config.json:
Define the APIs and their respective log file paths and log levels. Example configuration:

**you can find the code in config.jon file**

**Running the Log Ingestor**

python log_ingestor.py
This script will generate log entries for the defined APIs and store them in the specified log files.

**Running the Query Interface**

python query_interface.py
This script will provide output based on the predefined queries. 
