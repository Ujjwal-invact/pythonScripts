import supabase


def add_application():
    response = supabase.table("unique_email_applications").insert({
        "job_title": "Software Engineer",
        "date_of_application": "2024-01-25",
        "name": "John Doe",
        "email_id": "john.doe@example.com",  # Must be unique
        "phone_number": "+91 9876543210",
        "current_location": "Bangalore",
        "preferred_locations": "Mumbai, Delhi",
        "total_experience": "5 years",
        "curr_company_name": "TechCorp",
        "curr_company_designation": "Senior Developer",
        "department": "Engineering",
        "role": "Backend Developer",
        "industry": "IT Services",
        "key_skills": "Python, Django, PostgreSQL",
        "annual_salary": "12 LPA",
        "notice_period": "30 Days",
        "resume_headline": "Experienced Software Engineer",
        "summary": "Software Engineer with 5 years of experience in backend development...",
        "ug_degree": "B.Tech",
        "ug_specialization": "Computer Science",
        "ug_university": "IIT Delhi",
        "ug_graduation_year": 2018,
        "gender": "Male",
        "marital_status": "Single",
        "home_town": "New Delhi",
        "pin_code": "110001",
        "work_permit_usa": "No",
        "date_of_birth": "1995-06-15",
        "permanent_address": "123 Street, New Delhi"
    }).execute()
    
    print("Application Added:", response.data)

add_application()
