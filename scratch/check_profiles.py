import requests
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

print(f"Checking URL: {SUPABASE_URL}")
r = requests.get(f"{SUPABASE_URL}/rest/v1/profiles", headers=headers)

if r.status_code == 200:
    profiles = r.json()
    print(f"Found {len(profiles)} profiles:")
    for p in profiles:
        print(f"- {p.get('id')}: {p.get('nome_completo')} ({p.get('congregacao')})")
else:
    print(f"Error {r.status_code}: {r.text}")
