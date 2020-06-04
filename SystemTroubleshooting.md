### Mouse scroll speed:
https://dev.to/bbavouzet/ubuntu-20-04-mouse-scroll-wheel-speed-536o

### Mouse scroll acceleration:
Was not able to find how to change. Will use Scroll Speed for now.

### System dual boot break:
Every system needs a special "boot" partition that knows how to load it.
There are variaus ways to have it. One can set up to boot Windows out of Linux boot partition.
Then Windows boot partition can be removed.
If boot partition is corrupted or when moving the system to another drive the easy way to restore boot partition is
to reserve space for it, use Live USB System Installation to create boot partition on the new drive and then point it to 
the system partition.

For Windows look at ```$bootrec /rebuildbcd``` in Repairs Command Line.

On EFI systems Windows can only be installed to GPT tabled disks.
