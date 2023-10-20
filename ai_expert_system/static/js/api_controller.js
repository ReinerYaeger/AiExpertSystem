function loadStudents() {
    $.ajax({
        url: '/get_student_data/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {

            var studentsHtml = '';
            data.students.forEach(function(student) {
                studentsHtml += '<br>';
                studentsHtml += '<div>ID Number: ' + student.id + '</div>';
                studentsHtml += '<div>Name: ' + student.name + '</div>';
                studentsHtml += '<div>Email: ' + student.email + '</div>';
                studentsHtml += '<div>School: ' + student.school + '</div>';
                studentsHtml += '<div>Programme: ' + student.programme + '</div>';
                studentsHtml += '<br>';
            });
            $('#student_details').html(studentsHtml);
        }
    });
}

function loadModules() {
    $.ajax({
        url: '/get_module_data/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            var modulesHtml = '';
            data.modules.forEach(function(module) {
                modulesHtml += '<br>';
                modulesHtml += '<div>Module Name: ' + module.module_name + '</div>';
                modulesHtml += '<div>Credits: ' + module.credit + '</div>';
                modulesHtml += '<br>';
            });
            $('#module_details').html(modulesHtml);
        }
    });
}

function loadStudentProgress() {
    $.ajax({
        url: '/get_student_progress_data/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {

            let studentHtml = '';
            data.student_details.forEach(function(grade) {
                studentHtml += '<br>';
                studentHtml += '<div>Student ID: ' + grade.student_id + '</div>';
                studentHtml += '<div>Academic Year: ' + grade.academic_year + '</div>';
                studentHtml += '<div>Semester: ' + grade.semester + '</div>';
                studentHtml += '<div>Test 1: ' + grade.test_1 + '</div>';
                studentHtml += '<div>Test 2: ' + grade.test_2 + '</div>';
                studentHtml += '<div>Grade Points: ' + grade.grade_points + '</div>';
                studentHtml += '<br>';
            });
            $('#progress_details').html(studentHtml); // Update the content of the div with id "student_details"
        }
    });
}