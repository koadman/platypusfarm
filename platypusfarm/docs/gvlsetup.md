# Starting up the Genomics Virtual Lab

## A quick video tutorial
These tutorials use the Genomics Virtual Lab inside the NeCTAR research cloud.
This is an Australian-centric system, available to most Australian researchers.
If you are outside Australia, the details will be different but many of the techniques should work in Amazon cloud instances as well.

Mark Crowe has created a [video tutorial](https://www.youtube.com/watch?v=m3_8q9n7Z7w)

Remember to use 'ubuntu' as the login name instead of admin.

A quick rundown of the instructions, adapted to launch the microbial GVL are below.

### Get EC2 API security credentials from NeCTAR

1. [Log in to NeCTAR](http://dashboard.rc.nectar.org.au/)
2. Download security credentials for EC2 API (From Compute->Access&Security->API access tab) & open in text editor

### Launch a GVL instance via CloudMan

1. Go to [launch.genome.edu.au](http://launch.genome.edu.au)
2. Fill out the form, copy in your EC2 credentials
3. In "advanced options"->Flavor, select "GVL 4.2.0 Beta"
4. Click "Create a cluster".
5. Be patient (coffee might help), when the cluster has fully booted click the web console link
6. Enter Galaxy web interface

Occasionally the GVL web launcher fails to recognize that your GVL instance has completed launching. When this happens the GVL web console can be accessed by copying the IP address from the [NeCTAR dashboard](http://dashboard.rc.nectar.org.au/) and pasting it into the address bar in a new web browser tab.

## (Optional) connecting via ssh

You should now be able to connect via ssh.
On Mac or Linux, open a terminal (This is in the Applications->Utilities folder on OS X).
Then type `ssh ubuntu@XXX.XXX.XX.X`, replacing the X's with the IP address of your NeCTAR instance as shown on the GVL Launcher monitor page

From Windows you will need to connect with the PuTTY client or another SSH client.

At this stage you can run commands on the server.

