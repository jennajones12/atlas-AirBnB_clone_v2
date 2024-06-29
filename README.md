<center> <h1>HBNB - The Console</h1> </center>

## This project is a clone of the AirBnB website, developed as part of a student project to understand backend interfaces, data management, and persistent storage using JSON serialization/deserialization.
---
<center><h2>Repository Contents</h2> </center>

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

<center> <h1>Installation</h1> </center>

### To install and run this project locally, follow these steps:
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
*  * This prompt designates you are in the "HBnB" console. 
    
    There are a variety of commands available within the console program.

<center> <h1>Usage</h1> </center>

### Primary Syntax Commands
---
#### 1. Create 
###### Creates an instance based on a given class.

##### **Usage:**
create <class_name>

**Example:** 
```
(hbnb) create BaseModel
```
#### 2. Destroy
-- *destroys an object based on class and UUID.*
##### Usage: destroy <class_name> <_id>
###### Example:
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```

#### 3. Show an Object 
##### Shows an object based on class and UUID.
###### Usage: show <class_name> <_id>    
```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```
#### 4. Update an Object   
##### Updates existing attributes of an object based on class name and UUID.
###### Usage: update <class_name> <_id>    
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
```

### Alternative Syntax Commands

#### 1. Show All 
##### Shows all objects the program has access to, or all objects of a given class.
###### Usage:  <class_name>.all()        
```
(hbnb) User.all()
```
#### 2. Destroy a User 
##### Destroys a user object based on its class name and ID.
###### Usage: <class_name>.destroy(<_id>)        
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
```
#### 3. Update User (by attribute)
##### Updates attributes of a user object based on its class name, ID, attribute name, and new attribute value.
###### Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)        
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
```
#### 4. Update User (by dictionary) 
##### Updates attributes of a user object based on its class name, ID, and a dictionary representation of attributes.
###### Usage: <class_name>.update(<_id>, <dictionary>)        
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
```