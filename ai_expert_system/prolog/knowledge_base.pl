% Set the initial default GPA
:- dynamic(default_gpa/1).
:- dynamic(gpa/3).
:- dynamic(cumulative_gpa/2).
:- dynamic(sum_grade_points/2).
:- dynamic(sum_credits/3).
:- dynamic(cumulative_gpa/2).
default_gpa(2.2).

% GPA Calculation for Semester 1
gpa(student_id, 1, GPA) :-
   write('Calculating GPA for Semester 1 for Student ID: '), write(student_id), nl,
   findall(no_of_credits * grade_points,
           (student_progress(module, student_id, academic_year, 1, grade_points),
           module(module, no_of_credits)),
           CreditGradePointList),

   % Display the CreditGradePointList
   write('CreditGradePointList: '), write(CreditGradePointList), nl,

   % Calculate the total grade points for semester 1
   sum_grade_points(CreditGradePointList, TotalGradePoints),

   % Culculate the total credits for Semester 1
   sum_credits(1, student_id, TotalCredits),

       % Display TotalGradePoints and TotalCredits
    write('TotalGradePoints: '), write(TotalGradePoints), nl,
    write('TotalCredits: '), write(TotalCredits), nl,

    % Calculate GPA for Semester 1 as the ratio of TotalGradePoints to TotalCredits
    (TotalCredits = 0 -> GPA is 0 ; GPA is TotalGradePoints / TotalCredits).

% GPA Calculation for Semester 2
gpa(student_id, 2, GPA) :-
   write('Calculating GPA for Semester 2 for Student ID: '), write(student_id), nl,
   findall(no_of_credits * grade_points,
           (student_progress(module, student_id, academic_year, 2, grade_points),
           module(module, no_of_credits)),
           CreditGradePointList),

   % Display the CreditGradePointList
   write('CreditGradePointList: '), write(CreditGradePointList), nl,

   % Calculate the total grade points for semester 1
   sum_grade_points(CreditGradePointList, TotalGradePoints),

   % Culculate the total credits for Semester 1
   sum_credits(2, student_id, TotalCredits),

       % Display TotalGradePoints and TotalCredits
    write('TotalGradePoints: '), write(TotalGradePoints), nl,
    write('TotalCredits: '), write(TotalCredits), nl,

    % Calculate GPA for Semester 1 as the ratio of TotalGradePoints to TotalCredits
    (TotalCredits = 0 -> GPA is 0 ; GPA is TotalGradePoints / TotalCredits).

% Predicate to sum grade points
sum_grade_points([], 0).
sum_grade_points([GradePoints | Rest], Total) :-
    sum_grade_points(Rest, Subtotal),
    Total is Subtotal + GradePoints.

% Predicate to sum credits for a specific semester and student
sum_credits(semester, student_id, TotalCredits) :-
    findall(num_credits,
             (student_progress(module, student_id, academic_year, semester, _),
             module(module, no_of_credits)),
             CreditsList),
    sum_list(CreditsList, TotalCredits).

% Predicate to calculate cumulative GPA for a student
cumulative_gpa(student, CumulativeGPA) :-
    %Calculate total grade points for semester 1
    gpa(student_id, 1, GPA1),
    %Calculate total grade points for semester 2
    gpa(student_id, 2, GPA2),

    sum_credits(1, student_id, TotalCredits1),
    sum_credits(2, student_id, TotalCredits2),

    %Calculate Cumulative GPA as the sum of total grade points for both semesters divided by the total credits
    CumulativeGPA is (GPA1 * TotalCredits1 + GPA2 * TotalCredits2) / (TotalCredits1 + TotalCredits2).