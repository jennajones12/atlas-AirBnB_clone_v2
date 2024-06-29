<center> <h1>HBNB - The Console</h1> </center>

## Project Description
This project is a clone of the AirBnB website, developed as part of a student project to understand backend interfaces, data management, and persistent storage using JSON serialization/deserialization.

---

<center><h3>Repository Contents</h3> </center>

- [Installation](#installation)
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
```

## Examples

### Primary Command Syntax

* **create** - Creates an instance based on a given class.
- Usage: create <class_name>
    ```
  (hbnb) create BaseModel
  ```
* **destroy** - Destroys an object based on class and UUID.
- Usage: destroy <class_name> <_id>
    ```
    (hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
    ```
* **show** - Shows an object based on class and UUID.
- Usage: show <class_name> <_id>
    ```
    (hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
    ```
* **update** - Updates existing attributes of an object based on class name and UUID.
- Usage: update <class_name> <_id>
    ```
   (hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
    ```

    ### Alternative Syntax