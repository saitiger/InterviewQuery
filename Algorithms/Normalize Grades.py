def normalize_grades(grades):
    grade_values = [grade for name, grade in grades]
    
    min_grade = min(grade_values)
    max_grade = max(grade_values)
    
    normalized_grades = [
        (name, (grade - min_grade) / (max_grade - min_grade))
        for name, grade in grades
    ]
    
    return normalized_grades
