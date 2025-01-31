from supabase import create_client, Client

# Replace with your Supabase credentials
SUPABASE_URL="https://oemyktdkqsrsuuudswog.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9lbXlrdGRrcXNyc3V1dWRzd29nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgxMjY3NDEsImV4cCI6MjA1MzcwMjc0MX0.corwK7BwGhBiM8AE-wvkM_Bwmgm9Bvcmu3v8BE29VGU"


# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
