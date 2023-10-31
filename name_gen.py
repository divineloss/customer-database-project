import random
from sqlalchemy import create_engine
from sqlalchemy import text
from person import Person



##### VARIABLES #####
firstnames = []
lastnames = []
age = [x for x in range(1, 100)]

###### FUNCTIONS & MAIN ######
with open("./web-scraping/firstnames.txt", "r") as fn, open(
    "./web-scraping/lastnames.txt", "r"
) as ln:
    for line in fn:
        firstnames.append(line)
    for line in ln:
        lastnames.append(line)


def write_person(
    json,
):  # function that tells the connection to execute a task where the data for each person is written as a json document
    connection.execute(
        text(
            "INSERT INTO customers VALUES(NULL, :fname, :lname, :age, :gender, :income, :status)"
        ),
        json,
    )
    print(
        f"{json['fname']} {json['lname']} written"
    )  # print each first and last name as a string that tests if the first and last name parameters are being inserted correctly using json


def generate_person():
    p = Person(
        fname=random.choice(firstnames).strip(
            "\n"
        ),  # strip is a method that removes or truncates characters from beg and end of string
        lname=random.choice(lastnames).capitalize().strip("\n"),
        age=random.choice(age),
        gender=random.choice(["M", "F", "NB"]),
        income=random.randrange(10_000, 300_000),
        status=random.choice(["S", "M", "U", "D"]),
    )
    return p


# this is the main
if __name__ == "__main__":
    connection_string = "mysql+mysqlconnector://sql:sqlpass@127.0.0.1:3306/cust"  # this is a variable containing what database type, dialect, specific address, port and database the data will connect to
    engine = create_engine(connection_string, echo=True)

    # Create person array where _ is used as a placeholder for a variable in the iteration
    people = [generate_person() for _ in range(200)]

    # close the database connection after writing the people data
    with engine.connect() as connection:
        # Write each person to database using a for loop that uses the write_person method to write data for each person in the people array
        for i in people:
            write_person(i.return_json())

        connection.commit()
# saves data to the database
