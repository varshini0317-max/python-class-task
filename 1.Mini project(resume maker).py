#TO CREATE A DOC
from docx import Document
doc = Document()
doc.save("C:\\Users\\Hp\\Desktop\\Resume.docx")
print("Resume created successfully")
#FOR PHOTO
photo = input("Enter photo path: ")

print("Photo added successfully")
doc.save("C:\\Users\\Hp\\Desktop\\Resume.docx")
print("Details added successfully")
#FOR NAME AND PERSONAL INFO
name = input("Enter Your Name: ")
phone = input("Enter Your Phone Number: ")

if len(phone) == 10 and phone.isdigit():
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
    exit()
email = input("Enter Email Address: ")
  
if "@" not in email:
    print("Invalid Email Address")
    exit()
address = input("Enter Address: ")

languages = input("Enter languages you know (comma separated): ")

hobbies = input("Enter your hobbies (comma separated): ")

doc.add_heading(name, 0)
doc.add_paragraph("📞Phone Number: " + phone)
doc.add_paragraph("📧Email Address: " + email)
doc.add_paragraph("Address: " + address)
doc.add_paragraph("Languages: " + languages)
doc.add_paragraph("Hobbies: " + hobbies)
#FOR SKILLS AND EXPERIENCE
education = input("Education: ")
college = input("College/School: ")
experience = input("Experience: ")
skills = input("Skills (comma separated): ")
projects = input("Projects: ")
languages = input("Languages: ")
hobbies = input("Hobbies: ")

intro_para = f"""
A motivated individual with a strong academic background in {education} from {college}. 
The individual has experience in {experience} and demonstrates strong technical and practical skills.

Key skills include {skills}.I have worked on projects such as {projects}. 
They are proficient in languages like {languages} and actively engage in hobbies such as {hobbies}.
"""

doc.add_heading("RESUME", 0)

doc.add_heading("Profile Summary", 1)
doc.add_paragraph(intro_para)

doc.add_heading("Contact Details", 1)
doc.add_paragraph(f"Phone: {phone}\nEmail: {email}")

doc.add_heading("Education", 1)
doc.add_paragraph(f"{education} - {college}")

doc.add_heading("Experience", 1)
doc.add_paragraph(experience)

doc.add_heading("Skills", 1)
doc.add_paragraph(skills)

doc.add_heading("Projects", 1)
doc.add_paragraph(projects)

doc.add_heading("Languages", 1)
doc.add_paragraph(languages)

doc.add_heading("Hobbies", 1)
doc.add_paragraph(hobbies)

doc.save("C:\\Users\\Hp\\Desktop\\Resume.docx")
print("Details added successfully")
