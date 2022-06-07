### Chall Desc: 
I wanna reach a million cookies!

### File attached: 

#### Soln: (Author FusterCluck)

We run the program to see an application open with a large cookie picture. Upon clicking the picture a few times, we see that it keeps track of the number of times the cookie was clicked. So the final goal would be to get this number to a million. 

The initial thought is to use a automatic mouse clicker but if we look through the settings, we see a save interval option with text saying that it isn't recommended to set the value to 2s. Naturally, we set this to 2s and if we shutdown the application, we find a new save.xlsx file containing the data from the application. Change the number of clicks to any number greater than a million to get a base64 encoded line of text (bjAwYnp7WXVtbXlDMDBraWV6fQ==). Decode this to get the flag.

`Flag: n00bz{YummyC00kiez}`

Thank you
