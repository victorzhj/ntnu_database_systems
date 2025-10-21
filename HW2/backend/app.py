from init_db import init_db
from crud import add_department, add_employee, add_project, get_employee_details, delete_employee, update_employee, get_departments, get_projects
from flask import Flask, render_template, request, redirect, url_for
init_db()

app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

# Employee related routes
@app.route('/addEmployee', methods=['GET', 'POST'])
def add_employee_route():
    if request.method == 'GET':
        return render_template('addEmployee.html')
    elif request.method == 'POST':
        employee_data = request.form.to_dict()
        add_employee(employee_data["name"], employee_data["department_id"])
        print("Employee added successfully")
        return redirect(url_for('show_employees'))

@app.route('/employees', methods=['GET'])
def show_employees():
    employees = get_employee_details()
    return render_template('employees.html', employees=employees)

@app.route('/updateEmployee', methods=['GET', 'POST'])
def update_employee_route():
    employee_id = int(request.form['employee_id'])
    if request.method == 'GET':
        return render_template('updateEmployee.html', employee_id=employee_id)
    elif request.method == 'POST':
        employee_data = request.form.to_dict()
        name = None
        department_id = None
        if employee_data.get("name"):
            name = employee_data.get("name")
        if employee_data.get("department_id"):
            department_id = employee_data.get("department_id")
        if name is None and department_id is None:
            return redirect(url_for('show_employees'))
        update_employee(employee_id, name=name, department_id=department_id)
        print("Employee updated successfully")
        return redirect(url_for('show_employees'))

@app.route('/deleteEmployee/<int:employee_id>', methods=['POST'])
def delete_employee_route(employee_id):
    delete_employee(employee_id)
    print("Employee deleted successfully")
    return redirect(url_for('show_employees'))

# Department related routes
@app.route('/departments', methods=['GET'])
def show_departments():
    departments = get_departments()
    return render_template('departments.html', departments=departments)

@app.route('/addDepartment', methods=['GET', 'POST'])
def add_department_route():
    if request.method == 'GET':
        return render_template('addDepartment.html')
    elif request.method == 'POST':
        department_data = request.form.to_dict()
        add_department(department_data["department_name"])
        print("Department added successfully")
        departments = get_departments()
        return render_template('departments.html', departments=departments)

# Project related routes
@app.route('/addProject', methods=['GET', 'POST'])
def add_project_route():
    if request.method == 'GET':
        return render_template('addProject.html')
    elif request.method == 'POST':
        project_data = request.form.to_dict()
        add_project(project_data["project_name"], project_data["employee_id"], project_data["department_id"])
        print("Project added successfully")
        return redirect(url_for('show_projects'))

@app.route('/projects', methods=['GET'])
def show_projects():
    projects = get_projects()
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)





