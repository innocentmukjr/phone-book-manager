# Step 1
phonebook = {"Alice Nambi": {"phone": "0702120080", "city": "Kampala"},
             "Innocent Mukwaya": {"phone": "0774177602", "city": "Wakiso"},
             "Elisa Kato": {"phone": "0740379912", "city": "Masaka"}}

# Step 2
print("=== All Contacts ===")
for name, dict in phonebook.items():
    print(f"{name} | Phone: {dict['phone']} | City: {dict['city']}")

# Step 3
print("\n--- Safe Lookup ---")
print(phonebook.get("Alice Nambi", "Contact Not Found"))

# Step 4
phonebook["Noah Katumba"] = {"phone": "0760960583", "city": "Lukwanga"}
print(f"\nTotal contacts after adding: {len(phonebook)}")

# Step 5
phonebook["Alice Nambi"]["city"] = "Bwaise"
print(f"Updated: Alice Nambi | Phone: {phonebook['Alice Nambi']['phone']} | City: {phonebook['Alice Nambi']['city']}")

# Step 6
removed = phonebook.pop("Alice Nambi")
print(f"\nDeleted: {removed}")
print(f"Remaining contacts: {len(phonebook)}")

# Step 7
print("\n--- Kampala Contacts ---")
for name, details in phonebook.items():
    if details['city'] == 'Kampala':
        print(f"Kampala Contacts: {name}")

# Personal notes
print("\n✨ Energy level: 9/10")
print("✅ My win today: I have removed fear about looping through nested dictionaries")
