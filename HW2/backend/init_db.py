import mysql.connector

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'hw2'
}

def get_connection():
    return mysql.connector.connect(**db_config)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS Project")
    cursor.execute("DROP TABLE IF EXISTS Employee")
    cursor.execute("DROP TABLE IF EXISTS Department")

    cursor.execute("""
    CREATE TABLE hw2.Department (
        department_id INT AUTO_INCREMENT PRIMARY KEY,
        department_name VARCHAR(100) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE hw2.Employee (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department_id INT,
        FOREIGN KEY (department_id) REFERENCES Department(department_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE hw2.Project (
        project_id INT AUTO_INCREMENT PRIMARY KEY,
        project_name VARCHAR(100) NOT NULL,
        employee_id INT,
        department_id INT,
        FOREIGN KEY (employee_id) REFERENCES Employee(employee_id) ON DELETE CASCADE,
        FOREIGN KEY (department_id) REFERENCES Department(department_id)
    );
    """)

    cursor.execute("""
        INSERT INTO hw2.department (department_name) VALUES
        ('HR'),
        ('Finance'),
        ('IT');
    """)

    cursor.execute("""
        INSERT INTO hw2.Employee (name, department_id) VALUES
        ('Alice', 1),
        ('Bob', 2),
        ('Charlie', 3);
    """)

    cursor.execute("""
        INSERT INTO hw2.Project (project_name, employee_id, department_id) VALUES
        ('Data analysis', 1, 1),
        ('Web development', 2, 2),
        ('Mobile app development', 3, 3);
    """)

    conn.commit()
    cursor.close()
    conn.close()