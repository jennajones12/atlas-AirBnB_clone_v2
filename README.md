<center> <h1>HBNB - The Console</h1> </center>

This project is a clone of the AirBnB website, developed as part of a student project to understand backend interfaces, data management, and persistent storage using JSON serialization/deserialization. 

<center><h2>Repository Contents</h2> </center>

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

<center><h1>Installation</h1> </center>
To install and run this project locally, follow these steps:

#### 1. Clone the repository:
```
git clone https://github.com/yourusername/airbnb-clone.git
```
#### 2. Start the Console:
```
$ ./console.py
```
#### 3. When this command is run, the following prompt should appear:
```
(hbnb)
```
 This prompt designates you are in the "HBnB" console. 
There are a variety of commands available within the console program.

# Usage
## Primary Syntax Commands
---
### **Create -** creates an instance based on a given class.  
'*create <class_name>*'
#### Example:
    create BaseModel

### **Destroy -** destroys an object based on class and UUID.
'*destroy <class_name> <_id>*'
#### Example:
    (hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8

### **Show -** shows an object based on class and UUID.
'*show <class_name> <_id>*'
#### Example:
    (hbnb) show BaseModel 3aa5babc-efb6-4041#### Example:
    (hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"

### **Update -** updates existing attributes of an object based on class name and UUID.
'*update <class_name> <_id>*'
#### Example:
    (hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"

## Alternative Syntax Commands
---
### **All -** shows all objects the program has access to, or all objects of a given class.
'*<class_name>.all()*'       
#### Example:
    (hbnb) User.all()

### **Destroy -** destroys a user object based on its class name and ID.
'*<class_name>.destroy(<_id>)*'       
#### Example:
    (hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")

### **Update (by attribute) -** updates attributes of a user object based on its class name, ID, attribute name, and new attribute value.
'*<class_name>.update(<_id>, <attribute_name>, <attribute_value>)*'        
#### Example:
    (hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")

### **Update (by dictionary) -**
updates attributes of a user object based on its class name, ID, and a dictionary representation of attributes

'*<class_name>.update(<_id>, <dictionary>)*'       
#### Example:
    (hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})

# AirBnB Clone - Web Framework

This project involves creating a web framework for an AirBnB clone using Flask.

## 0. Hello Flask!

This script starts a Flask web application that listens on 0.0.0.0, port 5000, and displays "Hello HBNB!" on the root route.

To run the application:
```bash
python3 -m web_flask.0-hello_route

