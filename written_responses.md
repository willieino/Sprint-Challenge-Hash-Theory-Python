1. What is a regular expression and how does it work?

A regular expression or regex is a sequence of characters put together in order to define a pattern to be used in a search. The patterns are then used by string searching algorithms. 
Typically they will be used for FIND searches and also for input validation.  Many programming languages have regex capabilities built in or through 3rd party libraries.
They are also used in search engines and text editors. 

A user would typically define a pattern using a sequence of characters. The patterns can look very cryptic the first few times that you are exposed to them. 
They then apply this pattern to a string, block of text or web page. The output would then be a list of 
all the occurences matching the pattern. 


2. What is an array and how does it work?

An array in computer science is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. 
An array is stored such that the position of each element can be computed from its index tuple by a mathematical formula.

The simplest type of data structure is a linear array, also called one-dimensional array. It is much easier to explain an array by using graphics. This isn't possible
for this test so you are going to have to imagine what it looks like.  I sometimes picture a train on a railroad track. The train would be the array and each 
individual car would be an element. Each element has its own unique index. So the locomotive would be index 0 and the caboose would be the last element in the array.
This analogy only works for single dimension arrays. Unless you can imagine one of the boxcars having a whole train inside of it. 

Arrays can have the fastest access time of all the data structures if used properly. 

3. What is a hash table and how does it work?

In computing, a hash table (hash map) is a data structure that can map keys to values. A hash table uses a hash function to compute an index into an 
array of slots or elements, from which the desired value can be found. The hash function has the ability to convert any input into 
a numerical value. Using this value and the size of the hash table a index (or key) is generated. 

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, 
which might cause hash collisions where the hash function generates the same index for more than one key. The array can be made larger or
a linked list can be created in the index slot where the collision occurred. In effect, another dimension is added to the array. 
(these are just two examples of the ways collisions can be handled.)

In a well-dimensioned hash table, the average cost (number of instructions) for each lookup is independent of the number of elements stored in the table. 
This makes them very efficient and cost effective. In many situations, hash tables turn out to be on average more efficient than search trees or any other 
table lookup structure. For this reason, they are widely used in many kinds of computer software, particularly 
for associative arrays, database indexing, caches, and sets. 