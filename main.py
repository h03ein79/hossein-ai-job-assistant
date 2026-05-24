job = input("Paste job title: ")

keywords = ["Python", "SQL", "Excel", "Communication"]

print("\nSuggested Keywords:\n")

for word in keywords:
    print("-", word)

print("\nGenerating Cover Letter...\n")

cover = f"""
Dear Hiring Manager,

I am excited to apply for the {job} position.

My background in technology, problem solving, and fast learning makes me a strong candidate for this role.

I am especially interested in working with tools such as Python, SQL, and Excel.

I would welcome the opportunity to discuss my qualifications further.

Best regards,
Hossein
"""

print(cover)