## **How the script operates**

The script will search for properties in the defined zip codes.  When a "new" property is identified it will be opened in a webbrowser so you can view the property.  All of those properties will be logged into the file you defined in the script.  The next time you run the script, it reads in the list of houses you have looked at previously.  It queries the API and compares the results to the previous list.  If that entry appears in the list, you will not be shown that property again.  Because the entry includes the address and price, you will be shown the property again if the price changes(drops) because that would be considered a new entry.  The first time you run the script you will be shown all the properties in those zip codes. Each time after, it will only return properties that you have not seen or have had a price change.  Anytime there is a "new" property, the script will automatically open the website so you can view the property.  

## **Configuration**

At the top of the script you will need to define some variables before running the script.  You will need to obtain a free api key from Rapid API.  There is a limit to the amount of queries each key is permitted to make each month.  I actually got 3 keys and rotated them in the script.  I commented out two of the keys. When I hit the limit on the first key, I would comment it out and uncomment the other key, etc.  You will also need to supply a list of cities (integers).   You have to have a minimum of one zip code.  The more zip codes you have in the list, the faster you will reach the API key limit.  You also need to specify the maximum value (integer) for the houses you want to see.  Last but not least you will need to supply a file path/filename to store the script data.

You can run the script by:
	```python3 property```
	
This script was developed on Ubuntu Linux. It may work on Windows but it hasn't been tested.  At the very least you will have to specify the file path using Windows file path syntax (i.e //).
