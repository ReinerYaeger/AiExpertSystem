%Matthew Samuels - 2005744
%Chevaughn Gibson - 1900396
%Gail-Ann Archer - 2002407

% caculate the total credits for both semester
sum_credits(Semester, StudentID, TotalCredits) :-
    findall(Credits,
            (student_progress(Module, StudentID, Year, Semester, _),
             module(Module, Credits)),
            CreditsList),
    sum_list(CreditsList, TotalCredits).

% calculate gpa based on semester
calculate_gpa(StudentID, Semester, GPA) :-
    findall(GradePoint * Credits,  % Multiply GradePoint by Credits
            (student_progress(Module, StudentID, Year, Semester, GradePoint),
             module(Module, Credits)),
            WeightedGrades),  % Store the weighted grades
    sum_list(WeightedGrades, TotalWeightedGrade),
    sum_credits(Semester, StudentID, TotalCredits),
    (TotalCredits = 0 -> GPA is 0 ; GPA is TotalWeightedGrade / TotalCredits).

% calculate cumulatibe gpa based on both semester
cumulative_gpa(StudentID, CumulativeGPA) :-
    calculate_gpa(StudentID, 1, GPA1),
    calculate_gpa(StudentID, 2, GPA2),
    sum_credits(1, StudentID, TotalCredits1),
    sum_credits(2, StudentID, TotalCredits2),
    (TotalCredits1 + TotalCredits2 = 0 -> CumulativeGPA is 0 ;
     CumulativeGPA is (GPA1 * TotalCredits1 + GPA2 * TotalCredits2) / (TotalCredits1 + TotalCredits2)).