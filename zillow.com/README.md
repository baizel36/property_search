# **Introduction**

The first script I wrote to search for real estate used the realtor.com API.  It makes it super easy to get the information you need quickly.  However, I wasn't able to pull for sale by owner listings.  So I tried to do the same for Zillow.  For the little bit of effort I put into it, the Zillow API wasn't adequate, which I believe is intentional.  So I decided to go down the webscraping route just for fun.  One issue with this technique, is the script will get flagged as a bot and be presented a captcha which renders the script useless.  To get around this issue, I wrote the script to rotate the user_agent presented to the website. So each request is made with a different user_agent from the previous request. The other prevention method implemented, was I put a random pause in between each request (between 2 - 5 seconds).  This makes the request look less like a bot and more like a human. With those two measures it works 99% of the time.  However, the random delay makes the script run slower than I would like.  I will work on that in the future.

The script will search for properties in the defined zip codes. When a "new" property is identified it will be opened in a webbrowser so you can view the property. All of those properties will be logged into the file you defined in the script. The next time you run the script, it reads in the list of houses you have looked at previously. It queries Zillow and compares the results to the previous list. If that entry appears in the list, you will not be shown that property again. Because the entry includes the address and price, you will be shown the property again if the price changes(drops) because that would be considered a new entry. The first time you run the script you will be shown all the properties in those zip codes. Each time after, it will only return properties that you have not seen or have had a price change. Anytime there is a "new" property, the script will automatically open the website so you can view the property. The script will search both realtor and for sale by owner listings.

# **Configuration**

At the top of the script you will need to define some variables before running the script. You will need to supply a file path/filename to store the script data. You will also need to provide a list of zipcodes (minimum of one).  The list of zip_codes will be a string. They need to be in quotes. You will also have to point the script to the gecko driver.  All those variables are at the top of the script.

The script does use Selenium. You will need to set up your Gecko driver for selenium to work.  There are many tutorials on the web on how to install the Gecko driver depending on whether your using Linux or Windows. This script was developed on Ubuntu Linux. It may work on Windows but it hasn't been tested. At the very least you will have to specify the file path using Windows file path syntax (i.e //).

After you get the script operational, you may get an Index Error on the fake_useragent when you run the script.  The script will continue to run. You can fix the error by modifying the fake_useragent packages utils.py file.

Open a python terminal:

```import fake_useragent```

```print(fake_useragent.__file__)```

This will return a file location. For example:

    /home/db/.local/lib/python3.8/site-packages/fake_useragent/__init__.py

Navigate to that fake_useragent directory and edit the utils.py file. You need to modify line 99 of the utils.py file. 

```99     html = html.split('<table class="w3-table-all notranslate">')[1]```

On line 99 you will change the "w3" to "ws":

```99     html = html.split('<table class="ws-table-all notranslate">')[1]```

That will resolve the issue. 


