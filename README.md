<center> <h1>HBNB - The Console</h1> </center>

## Project Description
This project is a clone of the AirBnB website, developed as part of a student project to understand backend interfaces, data management, and persistent storage using JSON serialization/deserialization.

---

<center><h3>Repository Contents</h3> </center>- 

[Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Installation
To install and run this project locally, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/airbnb-clone.git
    cd airbnb-clone
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

### Starting the Console
To start the console, run:
```bash
./console.py

<br
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### * **create** - Creates an instance based on a given class.
Usage: create <class_name>
  ```
  (hbnb) create BaseModel
  ```
###### * **destroy** - Destroys an object based on class and UUID.
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```
* **show** - Shows an object based on class and UUID.
```bash
(hbnb) show <ClassName> <id>
````
* **all** - Shows all objects the program has access to, or all objects of a given class.
```bash
(hbnb) User.all
````

* **update** - Updates existing attributes of an object based on class name and UUID
```bash
(hbnb) update <ClassName> <id> <attribute_name>=<attribute_value>
````

* **quit**  - Exits the program (EOF will as well).
```bash
(hbnb) quit
````

* **EOF** - Exits the program by reaching end-of-file.
```bash
(hbnb) EOF
````

* **count** - Counts the number of instances of a class.
```bash
(hbnb) count <ClassName>
````

* **help**- Provides a description of commands.
```bash
(hbnb) help [<command>]
````

* **update** (alternate syntax) - Updates existing attributes of an object using a dictionary representation.
```bash
(hbnb) update <ClassName> <id> <attribute_name> <attribute_value>
(hbnb) update <ClassName> <id> <dictionary_representation>
````

* **shell** - Starts an interactive Python shell.
```bash
(hbnb) shell
````

* **reset** - Resets the database.
```bash
(hbnb) reset
````