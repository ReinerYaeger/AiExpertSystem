%Matthew Samuels - 2005744
%Chevaughn Gibson - 1900396
%Monique Levy - 1603342
%Gail-Ann Archer - 2002407

%facts
%students('STA3001','2005744','2022',1,4.3).
%students('STA3002','2005744','2022',1,1.3).
%students('STA3003','2005744','2022',1,2.3).
%students('STA3004','2005744','2022',1,3.3).
%students('STA3005','2005744','2022',1,3.7).

%module('STA3001',3).
%module('STA3002',4).
%module('STA3003',2).
%module('STA3004',1).
%module('STA3005',3).


% Predicate to sum credits for a specific semester and student
sum_credits(Semester, StudentID, TotalCredits) :-
    findall(Credits,
            (students(Module, StudentID, Year, Semester, _),
             module(Module, Credits)),
            CreditsList),
    sum_list(CreditsList, TotalCredits).

% Predicate to calculate GPA for a specific semester
calculate_gpa(StudentID, Semester, GPA) :-
    findall(GradePoint,
            (students(Module, StudentID, Year, Semester, GradePoint),
             module(Module, Credits)),
            Grades),
    sum_list(Grades, TotalGrade),
    sum_credits(Semester, StudentID, TotalCredits),

    (TotalCredits = 0 -> GPA is 0 ; GPA is TotalGrade / TotalCredits).

% Predicate to calculate cumulative GPA for both semesters
cumulative_gpa(StudentID, CumulativeGPA) :-
    calculate_gpa(StudentID, 1, GPA1),
    calculate_gpa(StudentID, 2, GPA2),

    % Find the TotalCredits for both semesters
    sum_credits(1, StudentID, TotalCredits1),
    sum_credits(2, StudentID, TotalCredits2),

    % Calculate Cumulative GPA as the sum of total grade points for both semesters divided by the total credits
    CumulativeGPA is (GPA1 * TotalCredits1 + GPA2 * TotalCredits2) / (TotalCredits1 + TotalCredits2).