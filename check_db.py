import sqlite3

conn = sqlite3.connect('knowledge_base.db')
cursor = conn.cursor()

cursor.execute("SELECT topic_title, chunk_index FROM discourse_chunks WHERE content LIKE '%GA4%' AND content LIKE '%bonus%' AND content LIKE '%dashboard%' ORDER BY chunk_index LIMIT 10;")
print(cursor.fetchall())

conn.close()
