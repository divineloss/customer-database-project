from random_address import real_random_address
from sqlalchemy import create_engine
from sqlalchemy import text

"""
# defining Address class
class Address:
    def __init__(
        self,
        address1,
        address2,
        city,
        state,
        postalCode,
    ):  # attributes
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.postalCode = postalCode

    def return_json(
        self,
    ):
        data = {
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "postalCode": self.postalCode,
        }
        return data
"""


def write_address(
    json,
):  # function that tells the connection to execute a task where the data for each address is written as a json document
    connection.execute(
        text(
            "INSERT INTO addresses VALUES(NULL, :address1, :address2, :city, :state, :postalCode)"
        ),
        json,
    )
    print(f"{json['address1']} {json['city']} written")


if __name__ == "__main__":
    connection_string = "mysql+mysqlconnector://sql:sqlpass@127.0.0.1:3306/cust"  # this is a variable containing what database type, dialect, specific address, port and database the data will connect to
    engine = create_engine(connection_string, echo=True)

    # Create address array where _ is used as a placeholder for a variable in the iteration
    address = [real_random_address() for _ in range(200)]

    # close the database connection after writing the address data
    with engine.connect() as connection:
        # Write each address to database using a for loop that uses the write_address method to write data for each address in the people array
        for i in address:
            write_address(json=i)

        connection.commit()
