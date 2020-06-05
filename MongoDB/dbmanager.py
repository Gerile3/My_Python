from connection import client


class My_mongo():
    """
    My mongodb manager that i made to learn how to interract with mongodb using pymongo.
    Currently supports creating collection,showing collections, inserting single/multi elements
    finding/deleting/showing elements. 
    """
    def __init__(self, db_name, col_name):
        self.client = client
        self.my_db = client[db_name]
        self.collection = self.my_db[col_name]

    def create_collection(self, name):
        col_list = self.my_db.list_collection_names()
        if name in col_list:
            print("The collection exists.")
            self.collection = self.my_db[name]
        else:
            print("The collection created.")
            self.collection = self.my_db[name]

    def show_collections(self):
        col_list = self.my_db.list_collection_names()
        for i in col_list:
            print(i)
        return col_list

    def insert_element(self, element):
        inserted = self.collection.insert_one(element)
        print(f"id: {inserted.inserted_id} inserted to dabatase")

    def insert_elements(self, elements):
        inserted = self.collection.insert_many(elements)
        print(f"{len(elements)} element added to database.\nInserted ids: {inserted.inserted_ids}")

    def show_elements(self):
        elements = self.collection.find()
        for i in elements:
            print(i)
        return elements

    def find_element(self, my_filter):
        element = self.collection.find_one(my_filter)
        if element:
            return element
        else:
            print("Element not found")

    def find_elements(self, my_filter, number=10):
        elements = self.collection.find(my_filter).limit(number)
        if elements:
            for i in elements:
                print(i)
        else:
            print("Element not found")
        return elements

    def delete_element(self, element):
        element = self.collection.find_one(element)
        if element:
            print("Found element:", element)
            user_input = input("Want to delete this element? (Y/N)\n>>")
            if user_input.lower() == "y":
                self.collection.delete_one(element)
                print("Element Deleted..")
            else:
                print("Element not deleted")


if __name__ == "__main__":
    db = My_mongo("test_db", "products")
    # db.create_collection("products")
    # db.show_collections()
    # product = {"Name": "Dell 4860", "Price": 2000, "Date": "03/02/2016", "Status": "intel i7, 8gb, 1tb hdd"}
    # db.insert_element(product)
    # products = [{"Name": "Samsung s7", "Price": 3000, "Date": "03/02/2016", "Status": "Used"},
    #             {"Name": "Iphone 6", "Price": 5000, "Date": "03/02/2018", "Status": "Screen Shattered"},
    #             {"Name": "Nokia 3", "Price": 1000, "Date": "03/02/2018", "Status": "None"}]
    # db.insert_elements(products)
    # db.show_elements()
    my_filter = {"Price": 5000}
    # element = db.find_element(my_filter)
    # print(element)
    # elements = db.find_elements(my_filter, number=2)
    # db.delete_element(my_filter)

