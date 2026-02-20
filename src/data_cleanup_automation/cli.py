import click
import psycopg2
from .core import cleanup_stale_data, Config

@click.command()
@click.option('--threshold', default=30, help='Number of days to consider data as stale.')
@click.option('--db-url', required=True, help='Database connection string.')
def cli(threshold: int, db_url: str) -> None:
    """Command line interface for cleaning up stale data."""
    config = Config()
    config.threshold_days = threshold

    try:
        conn = psycopg2.connect(db_url)
        cleanup_stale_data(conn, config)
    except Exception as e:
        click.echo(f"Failed to connect to the database: {e}")

if __name__ == '__main__':
    cli()