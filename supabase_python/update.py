from config import supabase

def update_application(email, new_salary):
    response = supabase.table("unique_email_applications").update({
        "annual_salary": new_salary
    }).eq("email_id", email).execute()
    
    print("Updated Application:", response.data)
