# Starting up the Genomics Virtual Lab

## A quick video tutorial
These tutorials use the Genomics Virtual Lab inside the NeCTAR research cloud.
This is an Australian-centric system, available to most Australian researchers.
If you are outside Australia, the details will be different but many of the techniques should work in Amazon cloud instances as well.

Mark Crowe has created a [video tutorial](https://www.youtube.com/watch?v=m3_8q9n7Z7w)

Remember to use 'ubuntu' as the login name instead of admin.

A quick rundown of the video instructions is below.

### Get EC2 API security credentials from NeCTAR

1. [Log in to NeCTAR](ttp://dashboard.rc.nectar.org.au/)
2. Download security credentials for EC2 API & open in text editor

### Launch GVL instance via CloudMan

1. Go to [launch.genome.edu.au](http://launch.genome.edu.au)
2. Enter your EC2 credentials when prompted
3. Be patient (coffee might help)
4. Enter Galaxy web interface

## connecting via ssh

You should now be able to connect via ssh.
On Mac or Linux, open a terminal (This is in the Applications->Utilities folder on OS X).
Then type `ssh ubuntu@XXX.XXX.XX.X`, replacing the X's with the IP address of your NeCTAR instance as shown on the GVL Launcher monitor page

From Windows you will need to connect with the PuTTY client or another SSH client.

At this stage you can run commands on the server.

