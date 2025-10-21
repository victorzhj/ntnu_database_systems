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
    cursor.execute("DROP TABLE IF EXISTS HasProject")
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
        department_id INT,
        FOREIGN KEY (department_id) REFERENCES Department(department_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE hw2.HasProject (
        project_id INT,
        employee_id INT,
        PRIMARY KEY (project_id, employee_id),
        FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE,
        FOREIGN KEY (employee_id) REFERENCES Employee(employee_id) ON DELETE CASCADE
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
        INSERT INTO hw2.Project (project_name, department_id) VALUES
        ('Data analysis', 1),
        ('Web development', 2),
        ('Mobile app development', 3);
    """)

    cursor.execute("""
        INSERT INTO hw2.HasProject (project_id, employee_id) VALUES
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 2),
        (3, 3),
        (2, 1);
    """)

    conn.commit()
    cursor.close()
    conn.close()