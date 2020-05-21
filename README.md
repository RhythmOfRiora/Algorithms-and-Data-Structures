# Algorithms-and-Data-Structures
Practise of basic algorithms and data structures I haven't touched since my CS degree. 



### Linked Lists

Linked lists are an ordered collection of objects, but they differ in structure from normal Python Lists and Arrays. Linked Lists
store references to the next element of the list as a part of each node. In general, a Linked List Node wil have two parts to it: 

- Data: The value that is stored in the Node.
- A pointer or reference to the next Node in the list. 

A Linked List is a collection of these Nodes. The beginning Node in the list is called the Head, and the last Node in the List is distinguished by the fact that its Next reference will point to None or NULL.

Other data structures such as Queues, Stacks and even Graphs are all implementations of Linked Lists. They can also be useful for caches and lifecycle management within the OS.

Linked Lists can be singly or doubly linked; with doubly linked lists simply having a pointer to the previous Node as well as the Next.