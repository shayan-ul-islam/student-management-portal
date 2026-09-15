
from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = "student_management_portal_secret"

# ============================================================
# BASIC DATA
# ============================================================

admin_username = "Shayan"
admin_password = "ABCDE"

student_username = "Shayan"
student_password = "12345"

notification = ""

subjects = [
    "Physics",
    "Math",
    "Chemistry",
    "English",
    "Urdu",
    "Islamiat"
]

# ============================================================
# STUDENTS
# ============================================================

students = [
    {
        "name": "Jack",
        "father": "Mushtaq",
        "contact": "03000000001",
        "roll": "1001",
        "class": "Green",
        "status": "Registered",
        "marks": [82, 88, 79, 63, 67, 47]
    },
    {
        "name": "Ali",
        "father": "Hamid",
        "contact": "03000000002",
        "roll": "1002",
        "class": "Green",
        "status": "Registered",
        "marks": [78, 91, 84, 60, 65, 48]
    },
    {
        "name": "Asif",
        "father": "Tauseef",
        "contact": "03000000003",
        "roll": "1003",
        "class": "Green",
        "status": "Registered",
        "marks": [85, 80, 81, 64, 68, 45]
    },
    {
        "name": "Ayan",
        "father": "Sami",
        "contact": "03000000004",
        "roll": "1004",
        "class": "Green",
        "status": "Registered",
        "marks": [90, 86, 88, 66, 69, 50]
    },
    {
        "name": "Rayan",
        "father": "Saeed",
        "contact": "03000000005",
        "roll": "1005",
        "class": "Blue",
        "status": "Registered",
        "marks": [75, 83, 77, 59, 62, 44]
    },
    {
        "name": "Ahmed",
        "father": "Danish",
        "contact": "03000000006",
        "roll": "1006",
        "class": "Blue",
        "status": "Registered",
        "marks": [88, 90, 85, 65, 70, 49]
    },
    {
        "name": "Abdullah",
        "father": "Firoz",
        "contact": "03000000007",
        "roll": "1007",
        "class": "Blue",
        "status": "Registered",
        "marks": [80, 87, 83, 61, 66, 46]
    },
    {
        "name": "Junaid",
        "father": "Akram",
        "contact": "03000000008",
        "roll": "1008",
        "class": "Blue",
        "status": "Registered",
        "marks": [92, 89, 90, 68, 71, 51]
    },
    {
        "name": "Shayan",
        "father": "Waris Ali",
        "contact": "03099475847",
        "roll": "6789",
        "class": "Green",
        "status": "Sample",
        "marks": [95, 98, 97, 74, 75, 51]
    }
]

# ============================================================
# CLASSES
# ============================================================

classes = {
    "Green": ["Jack", "Ali", "Asif", "Ayan"],
    "Blue": ["Rayan", "Ahmed", "Abdullah", "Junaid"]
}

# ============================================================
# COMMON HTML
# ============================================================

HTML_START = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Management Portal</title>
</head>

<body>

<h1>Student Management Portal</h1>

{% if notification %}
    <p>
        <strong>Notification:</strong>
        {{ notification }}
    </p>
{% endif %}

<hr>
"""

HTML_END = """
<hr>
<p>Student Management Portal</p>

</body>
</html>
"""

# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML_START + """

        <h2>Welcome to the Student Management Portal</h2>

        <p>
            <a href="{{ url_for('admin_login') }}">
                <button>Admin Login</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('student_login') }}">
                <button>Student Login</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('how_to_register') }}">
                <button>How to Register</button>
            </a>
        </p>

        {% if notification %}

            <hr>

            <h3>Latest Message</h3>

            <p>
                {{ notification }}
            </p>

        {% endif %}

        """ + HTML_END,

        notification=notification
    )

# ============================================================
# HOW TO REGISTER
# ============================================================

@app.route("/register-info")
def how_to_register():

    return render_template_string(
        HTML_START + """

        <h2>How to Register</h2>

        <p>
            Contact to the Admin Office to register your self.
        </p>

        <p>
            <a href="{{ url_for('home') }}">
                <button>Back to Home</button>
            </a>
        </p>

        """ + HTML_END,

        notification=notification
    )

# ============================================================
# ADMIN LOGIN
# ============================================================

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == admin_username and password == admin_password:

            session["admin_logged_in"] = True

            return redirect(url_for("admin_dashboard"))

        else:

            message = "Try again. Incorrect username or password."

    return render_template_string(
        HTML_START + """

        <h2>Admin Login</h2>

        <h3>Sample Account Login</h3>

        <p>Name: Shayan</p>

        <p>Password: ABCDE</p>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        <form method="POST">

            <p>

                <label>Username:</label>

                <input
                    type="text"
                    name="username"
                    required
                >

            </p>

            <p>

                <label>Password:</label>

                <input
                    type="password"
                    name="password"
                    required
                >

            </p>

            <button type="submit">
                Login
            </button>

        </form>

        <p>
            <a href="{{ url_for('home') }}">
                <button>Back</button>
            </a>
        </p>

        """ + HTML_END,

        message=message,
        notification=notification
    )

# ============================================================
# ADMIN DASHBOARD
# ============================================================

@app.route("/admin")
def admin_dashboard():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    return render_template_string(
        HTML_START + """

        <h2>Admin Page</h2>

        <h3>Admin Profile</h3>

        <p>
            Profile Picture
        </p>

        <hr>

        <h3>Admin Options</h3>

        <p>
            <a href="{{ url_for('add_student') }}">
                <button>Add Student</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('remove_student') }}">
                <button>Remove Student</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('new_class') }}">
                <button>New Class</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('list_students') }}">
                <button>List of Students</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('new_message') }}">
                <button>New Message</button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('change_password') }}">
                <button>Change Password</button>
            </a>
        </p>

        <hr>

        <h3>Portal Statistics</h3>

        <p>
            <a href="{{ url_for('list_students') }}">
                <button>
                    Registered Students: {{ student_count }}
                </button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('show_classes') }}">
                <button>
                    Classes: {{ class_count }}
                </button>
            </a>
        </p>

        <p>
            <a href="{{ url_for('show_subjects') }}">
                <button>
                    Subjects: {{ subject_count }}
                </button>
            </a>
        </p>

        <hr>

        <p>
            <a href="{{ url_for('logout') }}">
                <button>Logout</button>
            </a>
        </p>

        """ + HTML_END,

        student_count=len(students),
        class_count=len(classes),
        subject_count=len(subjects),
        notification=notification
    )

# ============================================================
# ADD STUDENT
# ============================================================

@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    message = ""

    if request.method == "POST":

        name = request.form.get("name")
        father = request.form.get("father")
        contact = request.form.get("contact")
        student_class = request.form.get("class")

        # Generate a new roll number
        existing_rolls = []

        for student in students:

            try:

                existing_rolls.append(
                    int(student["roll"])
                )

            except ValueError:

                pass

        if existing_rolls:

            new_roll = str(
                max(existing_rolls) + 1
            )

        else:

            new_roll = "1001"

        new_student = {

            "name": name,

            "father": father,

            "contact": contact,

            "roll": new_roll,

            "class": student_class,

            "status": "New",

            "marks": [
                0,
                0,
                0,
                0,
                0,
                0
            ]
        }

        students.append(new_student)

        if student_class not in classes:

            classes[student_class] = []

        classes[student_class].append(name)

        message = (
            "Student saved successfully. "
            "Roll number assigned: "
            + new_roll
        )

    return render_template_string(
        HTML_START + """

        <h2>Add Student</h2>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        <form method="POST">

            <p>

                <label>Student Name:</label>

                <input
                    type="text"
                    name="name"
                    required
                >

            </p>

            <p>

                <label>Father Name:</label>

                <input
                    type="text"
                    name="father"
                    required
                >

            </p>

            <p>

                <label>Contact Number:</label>

                <input
                    type="text"
                    name="contact"
                    required
                >

            </p>

            <p>

                <label>Class:</label>

                <select name="class">

                    {% for class_name in classes %}

                        <option value="{{ class_name }}">
                            {{ class_name }}
                        </option>

                    {% endfor %}

                </select>

            </p>

            <p>
                Status: New
            </p>

            <button type="submit">
                Save
            </button>

        </form>

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back to Admin Page</button>
            </a>

        </p>

        """ + HTML_END,

        message=message,
        classes=classes,
        notification=notification
    )

# ============================================================
# REMOVE STUDENT
# ============================================================

@app.route("/remove-student")
def remove_student():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    return render_template_string(
        HTML_START + """

        <h2>Remove Student</h2>

        <table border="1">

            <tr>

                <th>Name</th>

                <th>Father Name</th>

                <th>Roll Number</th>

                <th>Class</th>

                <th>Status</th>

                <th>Delete</th>

            </tr>

            {% for student in students %}

            <tr>

                <td>{{ student.name }}</td>

                <td>{{ student.father }}</td>

                <td>{{ student.roll }}</td>

                <td>{{ student.class }}</td>

                <td>{{ student.status }}</td>

                <td>

                    <a href="{{ url_for(
                        'delete_student',
                        roll=student.roll
                    ) }}">

                        <button>
                            Delete
                        </button>

                    </a>

                </td>

            </tr>

            {% endfor %}

        </table>

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        students=students,
        notification=notification
    )

# ============================================================
# DELETE STUDENT
# ============================================================

@app.route("/delete-student/<roll>")
def delete_student(roll):

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    global students

    student_to_delete = None

    for student in students:

        if student["roll"] == roll:

            student_to_delete = student

            break

    if student_to_delete:

        name = student_to_delete["name"]

        student_class = student_to_delete["class"]

        students.remove(student_to_delete)

        if student_class in classes:

            if name in classes[student_class]:

                classes[student_class].remove(name)

    return redirect(url_for("remove_student"))

# ============================================================
# NEW CLASS
# ============================================================

@app.route("/new-class", methods=["GET", "POST"])
def new_class():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    message = ""

    if request.method == "POST":

        class_name = request.form.get("class_name")

        if class_name in classes:

            message = "This class already exists."

        else:

            classes[class_name] = []

            message = "New class added successfully."

    return render_template_string(
        HTML_START + """

        <h2>Add New Class</h2>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        <form method="POST">

            <p>

                <label>Class Level:</label>

                <input
                    type="text"
                    name="class_name"
                    required
                >

            </p>

            <button type="submit">
                Add New Class
            </button>

        </form>

        <hr>

        <h3>Existing Classes</h3>

        {% for class_name, class_students in classes.items() %}

            <h4>{{ class_name }}</h4>

            {% if class_students %}

                <ul>

                    {% for student_name in class_students %}

                        <li>
                            {{ student_name }}
                        </li>

                    {% endfor %}

                </ul>

            {% else %}

                <p>
                    No students added yet.
                </p>

            {% endif %}

        {% endfor %}

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        classes=classes,
        message=message,
        notification=notification
    )

# ============================================================
# LIST STUDENTS
# ============================================================

@app.route("/students")
def list_students():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    return render_template_string(
        HTML_START + """

        <h2>List of Students</h2>

        <p>
            Total Students: {{ students|length }}
        </p>

        <table border="1">

            <tr>

                <th>Name</th>

                <th>Father Name</th>

                <th>Contact</th>

                <th>Roll Number</th>

                <th>Class</th>

                <th>Status</th>

            </tr>

            {% for student in students %}

            <tr>

                <td>{{ student.name }}</td>

                <td>{{ student.father }}</td>

                <td>{{ student.contact }}</td>

                <td>{{ student.roll }}</td>

                <td>{{ student.class }}</td>

                <td>{{ student.status }}</td>

            </tr>

            {% endfor %}

        </table>

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        students=students,
        notification=notification
    )

# ============================================================
# SHOW CLASSES
# ============================================================

@app.route("/classes")
def show_classes():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    return render_template_string(
        HTML_START + """

        <h2>Classes</h2>

        {% for class_name, class_students in classes.items() %}

            <h3>
                {{ class_name }}
            </h3>

            {% if class_students %}

                <ol>

                    {% for student_name in class_students %}

                        <li>
                            {{ student_name }}
                        </li>

                    {% endfor %}

                </ol>

            {% else %}

                <p>
                    No students in this class.
                </p>

            {% endif %}

        {% endfor %}

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        classes=classes,
        notification=notification
    )

# ============================================================
# SHOW SUBJECTS
# ============================================================

@app.route("/subjects")
def show_subjects():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    return render_template_string(
        HTML_START + """

        <h2>Subjects</h2>

        <ol>

            {% for subject in subjects %}

                <li>
                    {{ subject }}
                </li>

            {% endfor %}

        </ol>

        <p>
            Total Subjects: {{ subjects|length }}
        </p>

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        subjects=subjects,
        notification=notification
    )

# ============================================================
# NEW MESSAGE
# ============================================================

@app.route("/new-message", methods=["GET", "POST"])
def new_message():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    global notification

    message = ""

    if request.method == "POST":

        notification = request.form.get("message")

        message = (
            "Message displayed and saved successfully."
        )

    return render_template_string(
        HTML_START + """

        <h2>New Message</h2>

        <p>
            Write a message to display on interface.
        </p>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        <form method="POST">

            <p>

                <textarea
                    name="message"
                    rows="6"
                    cols="50"
                    required
                ></textarea>

            </p>

            <button type="submit">
                Display and Save
            </button>

        </form>

        {% if notification %}

            <h3>
                Current Interface Message
            </h3>

            <p>
                {{ notification }}
            </p>

        {% endif %}

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        message=message,
        notification=notification
    )

# ============================================================
# CHANGE PASSWORD
# ============================================================

@app.route("/change-password", methods=["GET", "POST"])
def change_password():

    if not session.get("admin_logged_in"):

        return redirect(url_for("admin_login"))

    global admin_password

    message = ""

    if request.method == "POST":

        previous_password = request.form.get(
            "previous_password"
        )

        new_password = request.form.get(
            "new_password"
        )

        if previous_password == admin_password:

            admin_password = new_password

            message = (
                "Password changed successfully."
            )

        else:

            message = (
                "Previous password is incorrect."
            )

    return render_template_string(
        HTML_START + """

        <h2>Change Password</h2>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        <form method="POST">

            <p>

                <label>
                    Previous Password:
                </label>

                <input
                    type="password"
                    name="previous_password"
                    required
                >

            </p>

            <p>

                <label>
                    New Password:
                </label>

                <input
                    type="password"
                    name="new_password"
                    required
                >

            </p>

            <button type="submit">
                Save
            </button>

        </form>

        <p>

            <a href="{{ url_for('admin_dashboard') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        message=message,
        notification=notification
    )

# ============================================================
# STUDENT LOGIN
# ============================================================

@app.route("/student-login", methods=["GET", "POST"])
def student_login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")

        password = request.form.get("password")

        if (
            username == student_username
            and password == student_password
        ):

            session["student_logged_in"] = True

            return redirect(
                url_for("student_profile")
            )

        else:

            message = (
                "Try again. "
                "Incorrect username or password."
            )

    return render_template_string(
        HTML_START + """

        <h2>Student Login</h2>

        <h3>Sample Login</h3>

        <p>
            Name: Shayan
        </p>

        <p>
            Password: 12345
        </p>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        <form method="POST">

            <p>

                <label>
                    Username:
                </label>

                <input
                    type="text"
                    name="username"
                    required
                >

            </p>

            <p>

                <label>
                    Password:
                </label>

                <input
                    type="password"
                    name="password"
                    required
                >

            </p>

            <button type="submit">
                Login
            </button>

        </form>

        <p>
            If you haven't registered,
            contact the Admin Office.
        </p>

        <p>

            <a href="{{ url_for('home') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        message=message,
        notification=notification
    )

# ============================================================
# STUDENT PROFILE
# ============================================================

@app.route("/student-profile")
def student_profile():

    if not session.get("student_logged_in"):

        return redirect(url_for("student_login"))

    return render_template_string(
        HTML_START + """

        <h2>Student Profile</h2>

        <h3>Profile Picture</h3>

        <p>
            Student: Shayan
        </p>

        <hr>

        <h3>Student Options</h3>

        <p>

            <a href="{{ url_for('my_data') }}">
                <button>My Data</button>
            </a>

        </p>

        <p>

            <a href="{{ url_for('check_result') }}">
                <button>Check Result</button>
            </a>

        </p>

        <p>

            <a href="{{ url_for('logout') }}">
                <button>Logout</button>
            </a>

        </p>

        """ + HTML_END,

        notification=notification
    )

# ============================================================
# MY DATA
# ============================================================

@app.route("/my-data")
def my_data():

    if not session.get("student_logged_in"):

        return redirect(url_for("student_login"))

    shayan = None

    for student in students:

        if student["roll"] == "6789":

            shayan = student

            break

    return render_template_string(
        HTML_START + """

        <h2>My Data</h2>

        {% if student %}

            <p>
                <strong>Name:</strong>
                {{ student.name }}
            </p>

            <p>
                <strong>Father Name:</strong>
                {{ student.father }}
            </p>

            <p>
                <strong>Contact:</strong>
                {{ student.contact }}
            </p>

            <p>
                <strong>Roll No:</strong>
                {{ student.roll }}
            </p>

            <p>
                <strong>Class:</strong>
                {{ student.class }}
            </p>

        {% else %}

            <p>
                Student data not found.
            </p>

        {% endif %}

        <p>

            <a href="{{ url_for('student_profile') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        student=shayan,
        notification=notification
    )

# ============================================================
# CHECK RESULT
# ============================================================

@app.route("/check-result", methods=["GET", "POST"])
def check_result():

    if not session.get("student_logged_in"):

        return redirect(url_for("student_login"))

    result_student = None

    message = ""

    if request.method == "POST":

        roll_number = request.form.get("roll")

        class_level = request.form.get(
            "class_level"
        )

        for student in students:

            if (
                student["roll"] == roll_number
                and
                student["class"].lower()
                == class_level.lower()
            ):

                result_student = student

                break

        if result_student is None:

            message = (
                "No result found. "
                "Check your roll number "
                "and class level."
            )

    return render_template_string(
        HTML_START + """

        <h2>Check Result</h2>

        <form method="POST">

            <p>

                <label>
                    Roll Number:
                </label>

                <input
                    type="text"
                    name="roll"
                    required
                >

            </p>

            <p>

                <label>
                    Level of Class:
                </label>

                <input
                    type="text"
                    name="class_level"
                    required
                >

            </p>

            <button type="submit">
                Check Result
            </button>

        </form>

        {% if message %}

            <p>
                <strong>{{ message }}</strong>
            </p>

        {% endif %}

        {% if student %}

            <hr>

            <h3>
                Student Result
            </h3>

            <p>
                Name: {{ student.name }}
            </p>

            <p>
                Father Name: {{ student.father }}
            </p>

            <p>
                Roll Number: {{ student.roll }}
            </p>

            <p>
                Class: {{ student.class }}
            </p>

            <table border="1">

                <tr>

                    <th>
                        Subject
                    </th>

                    <th>
                        Marks
                    </th>

                </tr>

                {% for i in range(subjects|length) %}

                <tr>

                    <td>
                        {{ subjects[i] }}
                    </td>

                    <td>
                        {{ student.marks[i] }}
                    </td>

                </tr>

                {% endfor %}

            </table>

            <h3>

                Total:
                {{ student.marks|sum }}/505

            </h3>

        {% endif %}

        <p>

            <a href="{{ url_for('student_profile') }}">
                <button>Back</button>
            </a>

        </p>

        """ + HTML_END,

        student=result_student,
        subjects=subjects,
        message=message,
        notification=notification
    )

# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)  
if __name__ == "__main__":

    app.run(debug=True)    