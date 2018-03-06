# Getting online at UTS and around the world

If you have just joined UTS you will have been assigned a student or staff ID number.
This number can be used to log into the UTS-WPA wireless network and the *eduroam* network while at other academic institutions around the world.

## Connecting to UTS-WPA wifi with Android & Linux

A few custom settings are needed to connect to the campus wifi. For authentication type select "TTLS" or "Tunneled TLS", then for the stage 2 authentication, select "MSCHAP" or "MSCHAPv2". The username is your staff or student ID number, along with your campus password.

## UTS email IMAP settings

UTS uses Microsoft Exchange email services, however there are IMAP & SMTP servers available for use with third-party mail apps such as Evolution, Thunderbird, K9 mail, etc.

Receiving mail:

* IMAP server: outlook.office365.com
* Security: STARTTLS
* Port: 143
* Username: your UTS email address

Sending mail:

* Server address: smtp-mail.outlook.com
* Security: STARTTLS
* Port: 587
* Username: your UTS email address

## Connecting to eduroam from an Android device

When connecting to eduroam from an Android device it is necessary to set a few configuration options to ensure the authentication works.

* EAP method: TTLS (Tunneled TLS)
* Phase 2 authentication: PAP
* Identity: staff/studentID @uts.edu.au

## Connecting to eduroam from an iPhone

You will first have to obtain and install the UTS "mobile configuration file".

Chrome does not recognise this file type as something special and will simply offer to download it. Therefore, use Safari and click on this link to [the UTS ios config page](http://m.uts.edu.au/current-students/managing-your-course/using-uts-systems/uts-wireless/eduroam/connecting-ios-device)

On that page you will find a link to the mobile config file. Click on it and follow the prompts in iOS to install the configuration. You will be asked for your UTS authentication details during this process. This will be your staff/student number followed by @uts.edu.au and your password will be the one you use to login into UTS services like NEO.

## Connecting to eduroam from a linux device

The process and settings required to connect from linux are very similar to Android devices.

## Reading papers from closed access academic journals

The UTS library runs an ezproxy but the interface can be very cumbersome to use. Alternatively, it is possible to use [google scholar via the ezproxy](https://scholar-google-com-au.ezproxy.lib.uts.edu.au/) to find the paper you would like to read
