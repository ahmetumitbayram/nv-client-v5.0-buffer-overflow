NVClient v5.0 - Stack Buffer Overflow (DoS)
Overview:

    Vulnerability Type: Stack Buffer Overflow (Local)
    Software: NVClient v5.0
    Software Manual: Documentation
    Tested Version: 5.0
    Tested On: Windows 10 64bit
    Discovery Date: 2023-08-19
    Discovered by: Ahmet Ümit BAYRAM

Description:

A local stack buffer overflow vulnerability was discovered in NVClient v5.0 software. When an excessive amount of data is input into the "Contact" box under the "Add Users" configuration, the software crashes, leading to a denial of service.
Steps to Reproduce:

    Run the provided Python script to create an exploit.txt file.
    Launch the NVClient application and log in.
    Navigate to "Config" in the upper menu.
    Click on the "User" button just below.
    Proceed to "Add users" in the lower left.
    Fill in the required Username, Password, and Confirm fields.
    Copy and paste the characters from exploit.txt into the Contact box.
    Click OK and witness the software crash.

Mitigation:

Users of NVClient v5.0 are advised to wait for a patch or update from the vendor that addresses this issue. Until then, avoid inputting untrusted or large amounts of data into the application.

Disclaimer:

This research is shared for educational purposes only. Unauthorized access or misuse of the information provided can violate local, state, and federal law.
