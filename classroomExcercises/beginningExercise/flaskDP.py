from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'Admin',
    'password': 'admin',
    'host': 'localhost',
    'database': 'employeesystem'
}

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/addEmployee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('addEmployee.html')
    elif request.method == 'POST':
        employee_data = request.form.to_dict()
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'INSERT INTO employees (name, age, country, position, wage) VALUES ("{employee_data["name"]}", {employee_data["age"]}, "{employee_data["country"]}", "{employee_data["position"]}", {employee_data["wage"]})')
        conn.commit()
        print("Employee added successfully")
        return redirect(url_for('show_employees'))
    
@app.route('/employees', methods=['GET'])
def show_employees():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('employees.html', employees=employees)

if __name__ == "__main__":
    app.run(port=8080)
