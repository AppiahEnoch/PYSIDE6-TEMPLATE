import os
import sqlite3
import sys

def get_user_home_dir():
    """Get the user's home directory."""
    return os.path.expanduser('~')

# Define paths
APP_DIR = os.path.join(get_user_home_dir(), 'SMART_QUESTIONS')
DATABASE_FILENAME = 'questions_bank_v3.db'
DATABASE_FILE = os.path.join(APP_DIR, DATABASE_FILENAME)

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    try:
        # Ensure the directory exists
        os.makedirs(APP_DIR, exist_ok=True)
        
        # Connect to the database (this will create the file if it doesn't exist)
        conn = sqlite3.connect(DATABASE_FILE)
        conn.row_factory = sqlite3.Row  # Enable access by column name
        
     
        
        return conn
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}", file=sys.stderr)
    except OSError as e:
        print(f"An error occurred while creating the directory: {e}", file=sys.stderr)
    
    return None






def remove_duplicate_questions():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Start a transaction
        cursor.execute("BEGIN TRANSACTION")

        # Find duplicate questions
        cursor.execute("""
        SELECT question_text, MIN(id) as keep_id, GROUP_CONCAT(id) as all_ids
        FROM question
        GROUP BY question_text
        HAVING COUNT(*) > 1
        """)

        duplicates = cursor.fetchall()

        total_removed = 0

        for duplicate in duplicates:
            question_text, keep_id, all_ids = duplicate
            ids_to_remove = [int(id) for id in all_ids.split(',') if int(id) != keep_id]

            # Remove entries from distractor table
            cursor.execute("""
            DELETE FROM distractor
            WHERE question_id IN ({})
            """.format(','.join('?' * len(ids_to_remove))), ids_to_remove)
            
            # Remove entries from question_answer table
            cursor.execute("""
            DELETE FROM question_answer
            WHERE question_id IN ({})
            """.format(','.join('?' * len(ids_to_remove))), ids_to_remove)
            
            # Remove duplicate entries from question table
            cursor.execute("""
            DELETE FROM question
            WHERE id IN ({})
            """.format(','.join('?' * len(ids_to_remove))), ids_to_remove)

            total_removed += len(ids_to_remove)

        # Commit the transaction
        conn.commit()

        print(f"Successfully removed {total_removed} duplicate questions.")

    except sqlite3.Error as e:
        # If there's an error, roll back the changes
        conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()

# Call the function
