import sqlite3 as sq

with sq.connect('deanary.db') as con:
    cur = con.cursor()

    # SQL-запросы на удаление данных из БД
    # cur.execute("DELETE FROM applicants WHERE data_postupleniya < '2021-01-01' ")
    # cur.execute("DELETE FROM syllabus WHERE id_speciality IS NULL")
    # cur.execute("DELETE FROM departments WHERE id_faculty IS NULL")
    # cur.execute("DELETE FROM syllabus WHERE id_subject NOT IN (SELECT id_subject FROM syllabus)")
    # cur.execute("DELETE FROM study_card WHERE grade IS NULL")
    # cur.execute("DELETE FROM study_card WHERE subjects = 'математика' AND submission_form = 'Экзамен'")
    # cur.execute("DELETE FROM study_card WHERE speciality IN (SELECT name FROM specialities WHERE id_departments =4)")
    # cur.execute("DELETE FROM study_card WHERE grade = 2 OR grade IS NULL")

    # cur.execute("DELETE FROM applicants WHERE speciality IS NULL AND data_postupleniya IS NULL")
    # 10 cur.execute("DELETE FROM study_card WHERE ") невозможен
    # 11cur.execute("DELETE FROM applicants WHERE ") невозможен
    # 12 cur.execute("DELETE FROM study_card WHERE ") невозможен
    # cur.execute("DELETE FROM study_card WHERE submission_form = 'Беседа'")
    # cur.execute("DELETE FROM applicants WHERE speciality IS NULL")
    # cur.execute("DELETE FROM  study_card WHERE speciality = 'БУ' AND grade < 4 AND subjects = 'информатика'")
    # cur.execute("DELETE FROM study_card WHERE subjects = 'физика' AND grade IS NULL")


    
