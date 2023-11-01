# Set the initial default GPA
default_gpa(2.2).

# GPA Calculation for Semester 1
gpa(StudentID, 1, GPA) :-
    write('Calculating GPA for Semester 1 for Student ID: '), write(StudentID), nl,
    findall(Credits * GradePoints,
            (module_details(Module, Year, 1, StudentID, GradePoints),
             module_master(Module, Credits)),
            CreditGradePointList),

    # Display the CreditGradePointList
    write('CreditGradePointList: '), write(CreditGradePointList), nl,

    # Calculate the total grade points for Semester 1
    sum_grade_points(CreditGradePointList, TotalGradePoints),

    # Calculate the total credits for Semester 1
    sum_credits(1, StudentID, TotalCredits),

    # Display TotalGradePoints and TotalCredits
    write('TotalGradePoints: '), write(TotalGradePoints), nl,
    write('TotalCredits: '), write(TotalCredits), nl,

    # Calculate GPA for Semester 1 as the ratio of TotalGradePoints to TotalCredits
    (TotalCredits = 0 -> GPA is 0 ; GPA is TotalGradePoints / TotalCredits).

# GPA Calculation for Semester 2
gpa(StudentID, 2, GPA) :-
    write('Calculating GPA for Semester 2 for Student ID: '), write(StudentID), nl,
    findall(Credits * GradePoints,
            (module_details(Module, Year, 2, StudentID, GradePoints),
             module_master(Module, Credits)),
            CreditGradePointList),

    % Display the CreditGradePointList
    write('CreditGradePointList: '), write(CreditGradePointList), nl,

    % Calculate the total grade points for Semester 2
    sum_grade_points(CreditGradePointList, TotalGradePoints),

    % Calculate the total credits for Semester 2
    sum_credits(2, StudentID, TotalCredits),

    % Display TotalGradePoints and TotalCredits
    write('TotalGradePoints: '), write(TotalGradePoints), nl,
    write('TotalCredits: '), write(TotalCredits), nl,

    % Calculate GPA for Semester 2 as the ratio of TotalGradePoints to TotalCredits
    (TotalCredits = 0 -> GPA is 0 ; GPA is TotalGradePoints / TotalCredits).

# Predicate to sum grade points
sum_grade_points([], 0).
sum_grade_points([GradePoints | Rest], Total) :-
    sum_grade_points(Rest, Subtotal),
    Total is Subtotal + GradePoints.

# Predicate to sum credits for a specific semester and student
sum_credits(Semester, StudentID, TotalCredits) :-
    findall(Credits,
            (module_details(Module, Year, Semester, StudentID, _),
             module_master(Module, Credits)),
            CreditsList),
    sum_list(CreditsList, TotalCredits).

# Predicate to calculate cumulative GPA for a student
cumulative_gpa(StudentID, CumulativeGPA) :-
    % Calculate total grade points for Semester 1
    gpa(StudentID, 1, GPA1),

    # Calculate total grade points for Semester 2
    gpa(StudentID, 2, GPA2),

    # Find the TotalCredits for both semesters
    sum_credits(1, StudentID, TotalCredits1),
    sum_credits(2, StudentID, TotalCredits2),

    # Calculate Cumulative GPA as the sum of total grade points for both semesters divided by the total credits
    CumulativeGPA is (GPA1 * TotalCredits1 + GPA2 * TotalCredits2) / (TotalCredits1 + TotalCredits2).