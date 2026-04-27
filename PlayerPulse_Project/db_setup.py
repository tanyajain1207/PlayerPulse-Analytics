import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

print("Loading CSV into Pandas...")
df = pd.read_csv('player_telemetry.csv')

print("Connecting to MySQL database...")
# The @ symbol is URL-encoded as %40, connecting directly to the 'players' database
engine = create_engine('mysql+pymysql://root:Power%40321t@localhost:3306/players')

print("Writing data to MySQL (this might take a minute for 176k rows)...")
# Load the dataframe into a table named 'player_events', replacing it if it exists
df.to_sql('player_events', con=engine, if_exists='replace', index=False)

print("Adding indexes for performance...")
with engine.connect() as conn:
    # Adding (50) tells MySQL the max length to index for these TEXT columns
    conn.execute(text("CREATE INDEX idx_player_id ON player_events(player_id(50));"))
    conn.execute(text("CREATE INDEX idx_event_name ON player_events(event_name(50));"))

print("Data successfully loaded and indexed into MySQL!")
