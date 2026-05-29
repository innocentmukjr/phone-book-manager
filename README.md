# phone-book-manager
A Python phone book using nested dictionaries – add, update, delete, search by city. Mini-project from my AI/ML learning journey.
# 📞 Phone Book Manager

A Python mini‑project that manages a phone book using nested dictionaries.  
Supports adding, updating, deleting, viewing all contacts, and filtering by city.

## 🎯 Project Overview
This program simulates a simple phone book. It demonstrates:
- Nested dictionaries (name → {phone, city})
- Looping through key‑value pairs
- Adding new contacts
- Updating existing contact details
- Deleting a contact with `.pop()`
- Searching by city
- Using `.get()` for safe lookups

## 📚 Topics Applied
- Python dictionaries (nested)
- `for` loops and `.items()`
- Dictionary methods: `.get()`, `.pop()`, `len()`
- Insert/update syntax: `dict[key] = value`
- Conditional filtering inside loops

## 🧠 How I Built It (step‑by‑step)
1. Created an initial phone book with 3 contacts (name → phone + city).
2. Printed all contacts in a formatted way.
3. Used `.get()` to retrieve a contact safely.
4. Added a new contact and printed total count.
5. Updated the city of an existing contact.
6. Removed a contact using `.pop()` and confirmed deletion.
7. Filtered and printed contacts living in Kampala.
8. Added personal notes: energy level 9/10 and my daily win.

## 🚧 Challenges & Solutions
- **Challenge:** Remembering that nested dictionary values are accessed with double brackets `[name][key]`  
  **Solution:** I practiced by writing explicit print statements for each step.
- **Challenge:** Avoiding KeyError when looking up a missing contact  
  **Solution:** Used `.get()` with a fallback message.

## ✅ What I Learned
- How to store structured data (phone + city) inside a dictionary.
- That `.pop()` returns the deleted value – useful for logging.
- How to filter a dictionary without creating a new one.
- Removing fear of looping through nested dictionaries (my win today 🎉)

## 🖥️ How to Run
```bash
python main.py
