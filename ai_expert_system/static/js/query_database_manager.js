// script.js

// Function to fetch student data from Django backend
function fetchStudentData() {
    var students = {{ context|safe }};
    console.log(students)

    var currentIndex = 0;

    function showPreviousStudent() {
        if (currentIndex > 0) {
            currentIndex--;
            displayStudent();
        }
    }

    function showNextStudent() {
        if (currentIndex < students.length - 1) {
            currentIndex++;
            displayStudent();
        }
    }

    function displayStudent() {
        var student = students[currentIndex];
        document.getElementById('student_details').innerHTML = `
            ID Number: ${student.id}<br>
            Name: ${student.name}<br>
            Email: ${student.email}<br>
            School: ${student.school}<br>
            Programme: ${student.programme}
        `;
    }

    // Initial display of the first student
    displayStudent();

    // Add event listeners to the previous and next buttons
    document.getElementById('prev_button').addEventListener('click', showPreviousStudent);
    document.getElementById('next_button').addEventListener('click', showNextStudent);

}

// Call the fetchStudentData function when the window has finished loading
window.onload = fetchStudentData;
