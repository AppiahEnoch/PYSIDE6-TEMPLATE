from common_imports import *

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create app_user table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS app_user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            middle_names TEXT,
            last_name TEXT NOT NULL,
            mobile TEXT,
            email TEXT,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create subject table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subject (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject_name TEXT,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, subject_name),
            FOREIGN KEY (user_id) REFERENCES app_user(id)
        )
    ''')

    # Create class_name table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS class_name (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            class_name TEXT,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, class_name),
            FOREIGN KEY (user_id) REFERENCES app_user(id)
        )
    ''')

    # Create topic table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS topic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            class_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            topic_name TEXT NOT NULL,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(subject_id, topic_name),
            FOREIGN KEY (subject_id) REFERENCES subject(id)
        )
    ''')

    # Create subtopic table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subtopic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            
            
            subtopic_name TEXT NOT NULL,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(topic_id, subtopic_name),
            FOREIGN KEY (topic_id) REFERENCES topic(id)
        )
    ''')
    

    # Create question_type table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT NOT NULL UNIQUE,
            description TEXT,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert predefined question types
    question_types = [
        ("Multiple-Choice", "Questions with several answer options, where only one or more may be correct."),
        ("True/False", "Statements that require the respondent to choose whether they are true or false."),
        ("Short Answer", "Questions that require a brief written response, typically a few words or a sentence."),
        ("Essay", "Open-ended questions that require an in-depth written response.")

    ]

    cursor.executemany('''
    INSERT OR IGNORE INTO question_type (type_name, description)
    VALUES (?, ?)
    ''', question_types)

    # Add more table creation statements here as needed
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            question_type_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            class_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            subtopic_id INTEGER,
            user_id INTEGER NOT NULL,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_type_id) REFERENCES question_type(id),
            FOREIGN KEY (subject_id) REFERENCES subject(id),
            FOREIGN KEY (class_id) REFERENCES class_name(id),
            FOREIGN KEY (topic_id) REFERENCES topic(id),
            FOREIGN KEY (subtopic_id) REFERENCES subtopic(id),
            FOREIGN KEY (user_id) REFERENCES app_user(id)
        )
    ''')
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question_answer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL UNIQUE,
            correct_answer TEXT,
            image_url TEXT,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_id) REFERENCES question(id),
            CHECK (correct_answer IS NOT NULL OR image_url IS NOT NULL)
        )
    ''')
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS distractor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            distractor_text TEXT,
            image_url TEXT,
            record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_id) REFERENCES question(id),
            CHECK (distractor_text IS NOT NULL OR image_url IS NOT NULL)
        )
    ''')
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question_batch (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            generation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES app_user(id)
        )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS generated_link (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            generated_link TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            generation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES app_user(id)
        )
    ''')

    # Create question_batch_map table to link questions to batches
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question_batch_map (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            FOREIGN KEY (batch_id) REFERENCES question_batch(batch_id),
            FOREIGN KEY (question_id) REFERENCES question(id),
            UNIQUE(batch_id, question_id)
        )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS api_key (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_of_key TEXT NOT NULL,
            api_key TEXT NOT NULL,
            user_id INTEGER NOT NULL
        )
    ''')

    
    


    

    conn.commit()
    conn.close()
    
