import re

def parse_resume(text):
    data = {}

    text_lower = text.lower()
    lines = text.split("\n")

    # ---------------- NAME ----------------
    data["name"] = "Not Found"
    for line in lines:
        line = line.strip()
        words = line.split()
        if 2 <= len(words) <= 3 and "@" not in line and not any(char.isdigit() for char in line):
            data["name"] = line.title()
            break

    # ---------------- EMAIL ----------------
    email_match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    data["email"] = email_match[0] if email_match else "Not Found"

    # ---------------- PHONE ----------------
    phone_match = re.findall(r"\+91[\s-]?\d{10}|\b\d{10}\b", text)
    data["phone"] = phone_match[0] if phone_match else "Not Found"

    # ---------------- SKILLS ----------------
    skills_list = [
        "python","java","c","c++","html","css","javascript",
        "sql","mongodb","excel","machine learning","data analysis"
    ]

    found_skills = []
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill.title())

    data["skills"] = list(set(found_skills))

    # ---------------- EDUCATION (FINAL FIX) ----------------
    education_data = []

    # BCA
    if "bachelor of computer applications" in text_lower or "bca" in text_lower:
        years = re.findall(r"(20\d{2})", text)

        if len(years) >= 2:
            education_data.append(f"BCA - Bachelor of Computer Applications ({years[0]} - {years[1]})")
        elif len(years) == 1:
            education_data.append(f"BCA - Bachelor of Computer Applications - {years[0]}")
        else:
            education_data.append("BCA - Bachelor of Computer Applications")

    # MCA
    if "master of computer applications" in text_lower or "mca" in text_lower:
        years = re.findall(r"(20\d{2})", text)

        if len(years) >= 2:
            education_data.append(f"MCA - Master of Computer Applications ({years[0]} - {years[1]})")
        elif len(years) == 1:
            education_data.append(f"MCA - Master of Computer Applications - {years[0]}")
        else:
            education_data.append("MCA - Master of Computer Applications")

    data["education"] = list(set(education_data))

    # ---------------- EXPERIENCE ----------------
    experience = []
    for line in lines:
        if "intern" in line.lower():
            if len(line.strip()) > 5:
                experience.append(line.strip())

    data["experience"] = list(set(experience))

    # ---------------- CERTIFICATIONS ----------------
    certifications = []
    for line in lines:
        line = line.strip()
        if ("certif" in line.lower() or "course" in line.lower()) and len(line) > 10:
            certifications.append(line.title())

    data["certifications"] = list(set(certifications))

    return data