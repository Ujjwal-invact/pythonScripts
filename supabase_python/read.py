from config import supabase

def get_all_applications():
    response = supabase.table("unique_email_applications").select("*").execute()
    print("All Applications:", response.data)

def get_application_by_email(email):
    response = supabase.table("unique_email_applications").select("*").eq("email_id", email).execute()
    print("Application:", response.data)
