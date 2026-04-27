import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import random

# --- Configuration ---
NUM_PLAYERS = 65000  # Will yield ~300k events total
START_DATE = datetime(2026, 3, 1)
CHANNELS = ['Organic', 'Facebook Ads', 'Google Ads', 'TikTok Ads']
DEVICES = ['iOS', 'Android']

# --- Conversion & Retention Probabilities ---
# We are intentionally creating a bad drop-off at Level 5 to analyze later
FUNNEL_PROBS = {
    'tutorial_complete': 0.85,
    'level_5_reached': 0.35,  # <-- The critical drop-off zone
    'store_page_viewed': 0.20,
    'in_app_purchase': 0.05
}

# --- Data Generation ---
events = []

print(f"Simulating telemetry for {NUM_PLAYERS} players...")

for _ in range(NUM_PLAYERS):
    player_id = str(uuid.uuid4())[:8]
    channel = random.choices(CHANNELS, weights=[0.4, 0.3, 0.2, 0.1])[0]
    device = random.choices(DEVICES, weights=[0.55, 0.45])[0]
    
    # Assign a random install date between March 1 and April 10, 2026
    install_offset = random.randint(0, 40)
    base_time = START_DATE + timedelta(days=install_offset, hours=random.randint(0,23), minutes=random.randint(0,59))
    
    def add_event(event_name, time_offset_minutes):
        event_time = base_time + timedelta(minutes=time_offset_minutes)
        events.append({
            'event_id': str(uuid.uuid4()),
            'player_id': player_id,
            'event_time': event_time.strftime('%Y-%m-%d %H:%M:%S'),
            'event_name': event_name,
            'device_type': device,
            'acquisition_channel': channel,
            'session_duration_seconds': random.randint(30, 300)
        })

    # 1. Funnel Events (Day 0)
    add_event('app_install', 0)
    
    if random.random() < FUNNEL_PROBS['tutorial_complete']:
        add_event('tutorial_complete', random.randint(2, 10))
        
        if random.random() < FUNNEL_PROBS['level_5_reached']:
            add_event('level_5_reached', random.randint(15, 45))
            
            if random.random() < FUNNEL_PROBS['store_page_viewed']:
                add_event('store_page_viewed', random.randint(50, 90))
                
                if random.random() < FUNNEL_PROBS['in_app_purchase']:
                    add_event('in_app_purchase', random.randint(95, 120))

    # 2. Retention Events (Day 1 and Day 7 Logins)
    # Organic users have higher retention than TikTok Ad users
    d1_prob = 0.45 if channel == 'Organic' else 0.30
    d7_prob = 0.20 if channel == 'Organic' else 0.10
    
    if random.random() < d1_prob:
        add_event('session_start', 24 * 60 + random.randint(0, 60)) # Day 1
        
    if random.random() < d7_prob:
        add_event('session_start', 7 * 24 * 60 + random.randint(0, 60)) # Day 7

# --- Export to CSV ---
df = pd.DataFrame(events)
# Sort by time to make it look like a real chronological database dump
df = df.sort_values(by='event_time').reset_index(drop=True)

print(f"Generated {len(df)} events!")
df.to_csv('player_telemetry.csv', index=False)
print("File 'player_telemetry.csv' saved successfully.")
