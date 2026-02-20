import psycopg2
import logging
from datetime import datetime, timedelta
from typing import Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    """Configuration class for cleanup settings."""
    threshold_days: int = 30

def cleanup_stale_data(db_conn: psycopg2.extensions.connection, config: Config) -> None:
    """Cleans up stale data in the database.

    Args:
        db_conn: The database connection.
        config: The configuration settings for cleanup.

    Returns:
        None

    Raises:
        psycopg2.Error: If there is an error executing the SQL.
    """
    threshold_date = datetime.now() - timedelta(days=config.threshold_days)
    logger.info(f"Cleaning up data older than {threshold_date.isoformat()}")
    
    try:
        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM my_table WHERE last_updated < %s", (threshold_date,))
            logger.info("Cleanup complete. Records deleted.")
    except psycopg2.Error as e:
        logger.error(f"Error during cleanup: {e}")
        db_conn.rollback()
    else:
        db_conn.commit()