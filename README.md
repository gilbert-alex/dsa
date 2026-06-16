# DSA


## Introduction

This repo is purely for my own education in, and practice with, data structures and 
algorithms. Generally, each module implements a Class for the named DSA. Additinoally, 
I took this opportunity to practice various techniques. For instance, stacks & queues
inherit linked lists, every module has related tests, and I've attempted to use
OOP throughout.

As these are only my notes, you'll find verbose comments about time/space complexity 
or other ovservations. Also, you'll probably find simplified, interesting, odd, or 
round-about code I used to explore some particular nuance. Please look for nearby
comments, the caller, or the section's README for an explaination where I felt my 
choices may have been strange for a typical, or production, environment. 

Each child directory contains a dedicated README to more throughly discuss the 
named structure or algorithm. 

Thank you for taking the time to read this and I'm open to all constructive feedback.


## Simplified Directory Tree

<!-- TREE_START -->
```
./
├── src/
│   ├── graphs/
│   ├── hash_maps/
│   │   ├── tests/
│   │   │   ├── test_hashmap.py
│   │   │   └── test_hashset.py
│   │   ├── hashmap.py
│   │   └── hashset.py
│   ├── heaps/
│   ├── linked_lists/
│   │   ├── tests/
│   │   │   ├── test_doubly_linked_list.py
│   │   │   └── test_singly_linked_list.py
│   │   ├── README.md
│   │   ├── doubly_linked_list.py
│   │   └── singly_linked_list.py
│   ├── sorting/
│   ├── stacks_and_queues/
│   │   ├── tests/
│   │   │   ├── test_linked_list_queue.py
│   │   │   ├── test_linked_list_stack.py
│   │   │   ├── test_list_queue.py
│   │   │   └── test_list_stack.py
│   │   ├── README.md
│   │   ├── queue.py
│   │   └── stack.py
│   └── trees/
│       ├── tests/
│       │   └── test_binary_search_tree.py
│       └── binary_search_tree.py
└── README.md
```
<!-- TREE_END -->
