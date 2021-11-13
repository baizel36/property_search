import requests, json, webbrowser


cities = [32003, 32041, 32030]         #list of comma separated integers (zipcodes) to search
price_max = 320000                     #interger: maximum house value to search
viewed_houses = '/home/db/houses.txt'  #string: file path name to save the data. This is linux filepath
api_key = ''                           #string: api_key from x-rapidapi-key

 
def getKey(item):
    return item[0]


new = []

for i in cities:
    url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"
    headers = {'x-rapidapi-key': api_key,}
    params = {
        "sort": "relevance",
        "postal_code": i,
        "price_max": price_max,
    }
    response = requests.request("GET", url, headers=headers, params=params)
    data = response.json()
    properties = data["properties"]

    old_list = []
    with open(viewed_houses, "r") as z:
        content = z.readlines()
        for i in content:
            i = i.rstrip()
            old_list.append(i)

    j = 0
    for i in properties:
        price = i["price"]
        street_address = i["address"]["line"]
        city = i["address"]["city"]
        new_url = i["rdc_web_url"]
        if not street_address:
            street_address = "No Street Address"
        entry = "${:>7,}".format(price), "{:<20}".format(street_address), city
        if str(entry) not in old_list:
            new.append(entry)
            webbrowser.open_new_tab(new_url)
        j += 1

new_houses = sorted(new, key=getKey)
if new_houses:
    with open(viewed_houses, "a") as z:
        for x in new_houses:
            z.write(str(x) + "\n")
else:
    print("Sorry, there are no new listings today")
