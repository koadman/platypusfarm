#Starting an instance on NeCTAR

You will need:

##1) Choose an image. 

For bioinformatics work, Genomics Virtual Laboratory (GVL) is a good choice. You can find the various releases of this image under the Dashboard's "_Images_" tab or in the "select image" drop down menu when launching an image. Unless otherwise required, using the latest image (highest version number) is best.

You might also consider starting from a snapshot -- an backup of an image that may already contain additional software or data you wish to use. Snapshots can be shared amongst users, maybe someone you know can save you some time by sharing a snapshot with you.

##2) A public/private key pair

Key-pairs replace passwords in the cloud environment. Key-pairs can be either created on the NeCTAR website under "_Access & Security_" or created on your local computer using the ```ssh-keygen``` command and imported into NeCTAR. In either case, you must possess the private key pertaining to the key-pair in question on your local machine. When created on NeCTAR, the private key is immediately sent to you as a download.

It is important to treat any private key as sensitive information. Although it is not transmitted over the network during authentication, it is still used to prove your identity. Its access permissions should be restricted to you alone. In fact, some clients will insist that permissions be restricted to the file owner only or refuse to execute (IE. ssh).

The following command sets the permissions of file to be readable only by the owner.
```bash
chmod 0400 [key-file]
```

The key-pair cannot be easily changed after launch. If you created the instance with a key-pair for which you no longer possess the private-key, there will be no way to log into the system. In this situation you should terminate the instance.

##3) Set the Security Group

Instances start-up following a policy for security set out by a "_Security Group_". This is a way of collecting a bunch of rules, which effect the security of your instance under a single banner. In NeCTAR, these refer to whether specific network ports (entryways of communication between computers) are open or closed. By default, all ports are closed.

|Port|Access Type|
|----|-----------|
| 22 | SSH |
| 80 | HTTP/web |
| 443 | secure HTTP/web |

Security groups and their rules can be changed after an image has been launched. If you forget to enable a port, you can always add this rule afterwards.

##4) Launch the instance

Now that you have attended to points 1-3, you can launch the instance. It will take anywhere from a few to perhaps 30 minutes depending on system load and instance size. You do not need to stay on the NeCTAR webpage once the process has gotten underway. The instance will complete initialization and remain waiting for you once ready.

##5) Connecting to the instance with SSH.

From the NeCTAR Dashboard, copy the IP address to your clipboard. You must use an SSH client which supports connections using a private key. On some GUI based clients, this open is buried in the settings menu.

To conenct with the standard command line tool:

```bash
ssh -i [my-private-key] ubuntu@[instance-ip-address]
```

Where you must replace [my-private-key] with the path to your private key used when launching the instance and [instance-ip-address] is the IP addres you copied from the NeCTAR Dashboard.
