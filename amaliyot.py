import psycopg2
class DataBase:
    def init(self):
        self.database = psycopg2.connect(
            database='shop',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_table_teachers(self):
        sql = '''create table if not exists teachers(
        teacher_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        teacher_name varchar(150) NOT NULL
        );'''

        self.manager(sql, commit=True)

    def create_table_students(self):
        sql = '''create table if not exists students(
        student_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        student_name varchar(150) NOT NULL
        );'''

        self.manager(sql, commit=True)

    def create_table_classes(self):
        sql = '''create table if not exists classes(
        class_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        student_id integer references students(student_id),
        teacher_id integer references teachers(teacher_id)
        );'''

        self.manager(sql, commit=True)

db = DataBase()
db.create_table_classes()
db.create_table_students()
db.create_table_teachers()