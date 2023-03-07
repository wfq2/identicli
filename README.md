# identic-cli

This repository uses:
Pipenv for dependency management, python 3.9.11  
I recommend using pycharm to code here.

# Given an arbitrary string, create an image that can serve as a unique identifier for a user of a B2B productivity app like slack, notion, etc.

**Requirements**

- Define a set of objectives to accomplish with your *identicon.* There's no right or wrong answer here. Here are some hypothetical objectives:
    - Legibility at some scale or set of scales - what sizes should the icon be shown at?
    - Uniqueness vs similarity - should similar strings look similar "John" vs "Jon" or should they be different?
    - Appearance - how do we avoid generating images that look bad?
- Given an arbitrary string, generate an image (as a jpg, gif, png, or in a web page using canvas, webgl, or whatever other display strategy you prefer)
- Images should be reasonably unique, for instance the strings "John", "Jane", and "931D387731bBbC988B31220" should generate three distinct images
- Any languages may be used, any libraries may be used, recommend javascript or python

**Initial thoughts**  
Use a language I know (python), and re-use a library to create an identicon.  I found pydenticon as this library, it works
decently well, and can be swapped out fairly easily.

***What string do I create the identicon with?***

We have two options here, going deterministic or non-deterministic.  Overall for a web application it's going to be easier
for a non-deterministic option.  Why?  Users might not like their identicons, and can re assign them.  We can make beautiful identicons  
and assign them to any string.  We can decide how similar identicons are based on the string / what assigns them.  Here are my rules:

- Identicons are similar based on the order they are created.  People love being the first on a platform, so my string that I pass into
the library is the count of users created.  We can modify this in the future to have only the first 1k users get a black and white identicon.
What if 