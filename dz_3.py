# -*- coding: utf-8 -*-
"""dz_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jf5bT5zhdu5hXg5d3Kd8weaqguc5AKCR
"""

import sqlite3

def get_connection():
  connection = sqlite3.connect('students.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_data(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(sqlquery,(school_id,))
    records = cursor.fetchall()
    print ("Данные по школе")
    for row in records:
      print ("ID школы: ", row[0])
      print ("Название школы: ", row[1])
      print ("Количество мест: ", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)


def get_student_data(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM Student WHERE Student_Id = ?"
    cursor.execute(sqlquery,(student_id,))
    records = cursor.fetchall()
    print(records)
    print ("Данные по студенту")
    for row in records:
      print ("ID Студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)


get_student_data(201)