from config import supabase

def delete_application(email):
    response = supabase.table("unique_email_applications").delete().eq("email_id", email).execute()
    print("Deleted Application:", response.data)
