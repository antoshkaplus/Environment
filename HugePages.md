Huge Pages on Linux
https://stackoverflow.com/questions/32652833/how-to-allocate-huge-pages-for-c-application-on-linux/32658827

Linus Huge Pages Guide
https://linuxgazette.net/155/krishnakumar.html

Transparent Huge Pages
https://www.kernel.org/doc/Documentation/vm/transhuge.txt

Stats on Huge Pages
https://kerneltalks.com/services/what-is-huge-pages-in-linux/

Use Programatically
https://techoverflow.net/2017/02/18/advantages-and-disadvantages-of-hugepages/


Need large mappings that they will do random access to, cuz it's worst possible case for TLB (Translation Lookaside Buffer).

hugetlbfs - to allocate

4 KB - regular
2 MB or 1 GB - huge page size, can't mix

Region-based memory management
