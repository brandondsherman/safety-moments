import sqlite3
import json
from pathlib import Path

DB_PATH = "safety_moments.db"
OUTPUT_JSON = "safety_moments.json"


def export_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, category, message
        FROM safety_moment
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()

    messages = [
        {"id": row[0], "category": row[1], "message": row[2]}
        for row in rows
    ]

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

    conn.close()
    print(f"✅ Export complete! Wrote {len(messages)} messages → {OUTPUT_JSON}")

if __name__ == "__main__":
    export_messages()