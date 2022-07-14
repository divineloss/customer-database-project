# Customer DB Project

This is a data project which utilizes data scrapped from the internet to create artificial customer data. The content contained within this repo is used for that purpose.

# Project Objective

Create 10 million artificial customers using the code housed in this repo.

# Table of Contents

| Folder | Description |
| [tf-project](https://github.com/divineloss/customer-database-project/tree/main/tf-project) | Terraform project which builds a VM in AWS Cloud to run the customer code |
| [web-scraping](https://github.com/divineloss/customer-database-project/tree/main/web-scraping) | Python code which is used to scrape data from the internet |
| api | Golang code using "Gorillia/Mux" for API development |
| schema | MySQL code to house our customer schema |

# Example API/Customer Data Reponse

```json
[
		{
			firstname: John
			lastname: Smith
			age: 32
			status: married
			gender: male
			income: 175000
		},
		{
			firstname: Jane
			lastname: Smith
			age: 31
			status: married
			gender: female
			income: 175000
		},
	]
```