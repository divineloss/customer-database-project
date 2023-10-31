# Customer DB Project

This is a data project which utilizes data scrapped from the internet to create artificial customer data. The content contained within this repo is used for that purpose.

# Project Objective

Create artificial customers using the code housed in this repo.

# Table of Contents

| Folder | Description |
| - | - |
| [tf-project](https://github.com/divineloss/customer-database-project/tree/main/tf-project) | Terraform project which builds a VM in AWS Cloud to run the customer code |
| [web-scraping](https://github.com/divineloss/customer-database-project/tree/main/web-scraping) | Python code which is used to scrape data from the internet |
| api | Golang code using "Gorillia/Mux" for API development |
| schema | MySQL code to house our customer schema |

# Example API/Customer Data Reponse

```json
[
  {
  	"firstname": "John",
  	"lastname": "Smith",
  	"age": 32,
  	"status": "married",
  	"gender": "male",
  	"income": 175000
  },
  {
  	"firstname": "Jane",
  	"lastname": "Smith",
  	"age": 31,
  	"status": "married",
  	"gender": "female",
  	"income": 175000
  },
]
```

# Project Status

| Task | Description | Status |
| - | - | - |
<<<<<<< HEAD
| Create addresses table that is populated with randomly generated addresses in order to join with customers table | Complete |
| Populate customers table with first and last names along with randomly generated data including age, status, gender, income | Complete |
| Fabricate fake name using name txt files | Using txt files generate it from python create fake names | Complete |
=======
| Fabricate fake name using name txt files | Using txt files generate, it from python to create fake names | Complete |
>>>>>>> 58592dac51bc4f7a9957086834297a2cd81c5c36
| Create last names | Write python script to create last names | Complete |
| Create first names | Write python script to create first names | Complete |
