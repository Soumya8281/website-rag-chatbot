import json

def chunk_text(filename, chunk_size=500):

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    with open("chunks.json", "w", encoding="utf-8") as file:
        json.dump(chunks, file, indent=4)

    print(f"✅ Created {len(chunks)} chunks.")