import mysql.connector

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'hw2'
}

def get_connection():
    return mysql.connector.connect(**db_config)

def add_department(department_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Department (department_name) VALUES (%s)"
    cursor.execute(query, (department_name,))
    conn.commit()
    cursor.close()
    conn.close()

def get_departments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Department"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def add_employee(name, department_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Employee (name, department_id) VALUES (%s, %s)"
    cursor.execute(query, (name, department_id))
    conn.commit()
    cursor.close()
    conn.close()

def add_project(project_name, employee_id, department_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Project (project_name, employee_id, department_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (project_name, employee_id, department_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_projects():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT p.project_id, 
           p.project_name,
           p.department_id,
           d.department_name,
           e.employee_id,
           e.name
    FROM Project p
    LEFT JOIN Department d ON p.department_id = d.department_id
    LEFT JOIN hasproject hp ON p.project_id = hp.project_id
    LEFT JOIN Employee e ON hp.employee_id = e.employee_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    conn.close()
    return results

def update_employee(employee_id, name=None, department_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    params = []
    if name is not None:
        updates.append("name=%s")
        params.append(name)
    if department_id is not None:
        updates.append("department_id=%s")
        params.append(department_id)
    params.append(employee_id)
    print(params)
    query = f"UPDATE Employee SET {', '.join(updates)} WHERE employee_id=%s"
    cursor.execute(query, tuple(params))
    conn.commit()
    cursor.close()
    conn.close()

def get_employee_details():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # Final SELECT with join across Employee, Department, and Project:
    query = """
    SELECT e.employee_id, e.name, d.department_name, hp.project_id, p.project_name
    FROM Employee e
    LEFT JOIN Department d ON e.department_id = d.department_id
    LEFT JOIN HasProject hp ON e.employee_id = hp.employee_id
    LEFT JOIN Project p ON hp.project_id = p.project_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def delete_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Employee WHERE employee_id=%s"
    cursor.execute(query, (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()

def add_employee_to_project(employee_id, project_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO HasProject (employee_id, project_id) VALUES (%s, %s)"
    cursor.execute(query, (employee_id, project_id))
    conn.commit()
    cursor.close()
    conn.close()