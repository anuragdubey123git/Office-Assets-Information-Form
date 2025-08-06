import os

db_file = "assets.db"

if os.path.exists(db_file):
    os.remove(db_file)
    print("✅ assets.db deleted successfully.")
else:
    print("⚠️ assets.db does not exist.")
