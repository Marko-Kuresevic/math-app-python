import os
import sqlite3

class Auth:
    def __init__(self, db_path = None):
        if db_path is None:
            project_root = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
            db_path = os.path.join(
                project_root, "data", "users.db"
            )
        self.db_path = db_path

        os.makedirs(os.path.dirname(self.db_path), exist_ok = True)
    
    def authentication(self, username, password, operation):

        conn = None
        cursor = None
        success = False
        performed_operation = operation

        try:
            conn = sqlite3.connect(self.db_path)

            cursor = conn.cursor()

            create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
                """
            
            cursor.execute(create_table_query)

            for i in range(1, 11):
                test_username = f"testuser{i}"
                test_password = f"test{i}"
                
                cursor.execute(
                    "SELECT username FROM users WHERE username = ?",
                    (test_username,)
                )

                user = cursor.fetchone()
                
                if not user:
                    cursor.execute(
                        "INSERT INTO users (username, password) VALUES (?, ?)",
                        (test_username, test_password)
                    )

            if performed_operation == "signup":
                cursor.execute(
                    "SELECT username FROM users WHERE username = ?",
                    (username,)
                )

                user = cursor.fetchone()
                
                if user:
                    performed_operation = "login"
                else:
                    cursor.execute(
                        "INSERT INTO users (username, password) VALUES (?, ?)", 
                        (username, password)
                    )

                    conn.commit()

                    success = True

            elif performed_operation == "login":
                cursor.execute(
                    "SELECT username, password FROM users WHERE username = ? AND password = ?",
                    (username, password)
                )

                user = cursor.fetchone()

                success = user is not None
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        
        return success

if __name__ == "__main__":
    auth = Auth()
