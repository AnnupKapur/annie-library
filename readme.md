# TASK 3

## Part 1

We have written a remove_books function.

It asks for the ISBN
It checks that ISBN exists
IF it does
  it tells the name
  it asks for quantity to remove
  then its removes that amount
ELSE
  it tells it does not exist in the library

### BUT WAIT ???

What if I input an ISBN, then it tells me the name of the book
BUT I realise I made a mistake, and I want to type in a different ISBN ?

Your task is to implement this functionality.

It should ask me, "Do you wanna remove some <<BOOK_NAME>>?".
IF yes
  do the removal
IF no
  Ask for the ISBN again ... and again ... and again.


