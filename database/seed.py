from database import create_database, add_entry

create_database()

entries = [
    (
        "photosynthesis",
        "science",
        "Photosynthesis is the process by which green plants make their food using sunlight, water, and carbon dioxide."
    ),
    (
        "gravity",
        "science",
        "Gravity is the force that attracts objects toward the Earth."
    ),
    (
        "voltage",
        "electronics",
        "Voltage is the electrical potential difference between two points."
    ),
    (
        "transistor",
        "electronics",
        "A transistor is a semiconductor device used for switching or amplifying electrical signals."
    ),
    (
        "computer",
        "general",
        "A computer is an electronic machine that processes data and performs instructions."
    ),
    (
        "environment",
        "general",
        "The environment is the surroundings and conditions in which living organisms exist."
    )
]

for word, category, meaning in entries:
    add_entry(word, category, meaning)

print("VoiceLearn database created successfully.")
print(f"Added {len(entries)} educational entries.")