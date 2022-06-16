# point-of-sale
A simple CLI program that acts like a Point of sale system using Object Oriented programming. 

## Prerequis
## Description

This is a CLI program that does simple saving, retrieval and manipulation of data for purchases, customers and products and saves that data to txt files with each having its respecttive data saved to files.

## How it works
To execute the program run the ![Main file](main.py)

## Application Structure
### Folders:
~ main.py - runs the main program
~ customer.py - contains the customer object and has functions to save, retrieve and delete data<br>
~ product.py - contains the product object and has functions to save, retrieve and delete data <br>
~ purchase.py - contains the function that carries out the purchase request<br>
~ customer.txt - has the customer data save<br>
~ products.txt - has the product dat saved<br>
~ purchases.txt - has the orders made by the customers</br>
## Customer operations
This are included in the ![Customer class](customer.py) whereby we have function to add, delete and update customers and there info apart from the id which is always constant and unique for each customer.
The data is then saved in ![Customer data txt](customer.txt)

## Product operations
This are inceluded in the ![Product class](product.py) whereby functions such as adding, deleting and updating of the data for the different items are held.
The data is then saved in a corresponding ![Product data txt](products.txt)

## Purchase operations
This is the section in![Purchase class](purchase.py) where data from the product and customer classes id read and specific purchases are made according to the user who is purchasing. 
This is achieved by reading the customer id and validating then proceeding to the next where the cutomer is able to complete the purchase.
The data is then saved in ![Purchase data](purchases.txt)

## Running the program
![Main](mainmenu.py) is the start of the porgram and it 

## Support and contact details
For any queries and suggestions, please contact the support team via **Email: roysamson494@gmail.com**

## License
[MIT](https://choosealicense.com/licenses/mit/)

