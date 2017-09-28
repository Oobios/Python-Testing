print ("This is some sort of test right?");

number = 1
name = "Anthony"

#\t tab
#\n new line
#\" quotation
#\\ backslash

list = ['one', 'two', 'three', 'four']

#lists are mutable, order matters, homogeneous (same data type)
#tuple are immutabl, heterogenous data types

tuple = ['cars', 'clothes', 'money', 'hoes']
#tuple = ['one',1 , 1.000]

states = {
    'Texas' : 'TX',
    'California' : 'CA',
    'New York' : 'NY',
}

cities = {
    'TX' : ['Austin', 'Dallas'],
    'CA' : ['Los Angeles', 'San Diego'],
    'NY' : ['New York City', 'Brooklyn'],
}

#dictionary maps keys to values
#order does not matter , sort of hash table type


def printstuff():
    print (states.keys())
    #prints the keys
    print (states.values())
    print (cities.values())
    #prints the values
    print (states)
    #prints all keys and values
    return
    
    
print ("Guess a number from 1-10")
newnumber = input()
getnumber(newnumber)

def getnumber(newnumber):
    
    print ("your number is", newnumber)
    
    if (newnumber > 10):
        print ("It's bigger than 10, try again")

    if (newnumber < 10):
        print (newnumber)

    return

