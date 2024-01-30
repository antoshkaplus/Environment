Mobo: GIGABYTE Z790 AORUS Elite AX 
CPU: i7-14700K


#### BIOS disable:
* Hyper-Threading
* Vanderpool Tech (Intel (VMX) Virtualization Tech)
* Turbo Boost Max 3.0 - Enables a couple of cores to reach higher turbo.
    Could be good for gaming but otherwise we don't really need that for day to day 
    tasks.
* Dynamic Tuning Technology - system software drivers configured by the system manufacturer 
  (also known as OEM) to dynamically optimize the system for performance, battery life, and thermals.
  Maybe good for laptops in certain configurations.


The CPU is heating a lot during load. It's hard to cool all cores during Prime95.
CPU is throttling a lot. 


Core indexes start with 0. 
Performance cores: 0,4,8,12,16,20,24,28
Efficient cores: 32,33,34,35|36,37,38,39|40,41,42,43

Cores 0 and 4 are coldest - probably located on the edge.
Cores 20, 28 are hottest - mid cores, one of the edges, 
    probably caused by unequal pressure. 
