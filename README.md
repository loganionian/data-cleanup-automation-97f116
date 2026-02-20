# data-cleanup-automation

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automation script that cleans up stale data in databases, reducing storage costs and improving query performance.

## The Problem

Stale data in databases can lead to increased storage costs and slower query performance. Manual cleanup is tedious and error-prone. This script automates the process, ensuring data is fresh and relevant.

## How It Works

The script will connect to various databases (e.g., PostgreSQL, MongoDB) and identify stale records based on defined criteria (e.g., last updated date). It will then safely remove or archive these records.

## Features

- Configurable threshold for identifying stale data (e.g., last updated date).
- Safe execution with rollback options in case of errors.
- Logging of cleanup activities for audit and debugging purposes.
- Support for multiple databases to maximize utility.

## Installation

```bash
pip install data-cleanup-automation
```

Or install from source:

```bash
git clone https://github.com/YOUR_USERNAME/data-cleanup-automation.git
cd data-cleanup-automation
pip install -e .
```

## Quick Start

```python
import psycopg2
from datetime import datetime, timedelta

def cleanup_stale_data(db_conn):
    threshold_date = datetime.now() - timedelta(days=30)
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM my_table WHERE last_updated < %s", (threshold_date,))
    db_conn.commit()

# Usage
conn = psycopg2.connect("dbname=test user=postgres")
cleanup_stale_data(conn)
```

## Tech Stack

- psycopg2 for PostgreSQL connections
- offering a familiar interface for Python developers.
- SQLite for lightweight local testing and prototyping.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.
