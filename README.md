![enter image description here](https://s11.gifyu.com/images/SQS05.gif)

Imagine a mischievous little program called C2-Fun, designed to bring joy and laughter to your family and friends. This unique creation, developed using Python and hosted on a local server using Flask, is designed solely for harmless pranks and playful antics.

C2-Fun may sound like your typical rat (remote administration tool), but don't be fooled. Unlike its counterparts, C2-Fun is incapable of being used for malicious purposes. Its sole intent is to create light-hearted pranks that will leave everyone chuckling without causing any harm or distress.

With an array of entertaining features, C2-Fun can turn any ordinary day into a memorable event. Want to catch your loved ones off guard? It can crash computers or browsers, open CD trays at the most unexpected moments, and even play amusing sounds or adjust the volume to create humorous surprises.

But the fun doesn't stop there! C2-Fun has more tricks up its sleeve. It can cleverly turn off monitors and disable mice temporarily, leaving your unsuspecting friends wondering what's happening. You can even suspend the taskbar and open random applications, adding an extra touch of unpredictability to your pranks.

Rest assured, C2-Fun is built with the utmost consideration for everyone's well-being. It strictly adheres to ethical guidelines, ensuring that no harm is caused, and that pranks are lighthearted and enjoyable for all involved. It's crucial to obtain the consent and cooperation of your prank victims, respecting their boundaries and ensuring a positive and fun-filled experience.

So, if you're seeking harmless pranks and memorable moments with your loved ones, give C2-Fun a try. Let the laughter ensue as you embark on a journey of joyful pranks, all while keeping the spirit of fun and camaraderie alive!

## Setup

**To ensure C2-Fun works seamlessly on the victim's computer, it's important to make a few code adjustments, primarily related to the IP address of the host machine. By default, C2-Fun assumes the IP address of the host to be 192.168.0.116. However, if your IP address or the victim's IP address is different, you'll need to modify line 90 in the `main.py` file.**

**To change the IP address in C2-Fun, follow these steps:**
1.  **Open the `main.py` file in your preferred Python editor.**
2.  **Locate line 90 in the code.**
3.  **Look for the section that initializes the IP address variable. It may look something like this: `host_ip = '192.168.0.116'`.**
4.  **Modify the IP address within the quotation marks to match the actual IP address of the host or victim's machine. For example, if the IP address is 192.168.0.123, the line would be updated as follows: `host_ip = '192.168.0.123'`.**
5.  **Save the changes to the `main.py` file.**

**By updating the IP address on line 90, C2-Fun will establish the necessary connection with the correct host or victim's machine, enabling successful prank execution.**

**Remember, it's crucial to respect privacy and obtain consent from all parties involved before using C2-Fun. Additionally, ensure that the modified code is used responsibly and for harmless pranks only.**


>you also have to run setup.bat after ip change and go to dist and run the main.

## How to use
After setting up the main file on the victim's computer, it is important to run it with administrator privileges to ensure it has the necessary permissions to function properly. To do this, locate the main file and right-click on it. From the context menu, select "Run as administrator." If the User Account Control (UAC) prompts for permission, click "Yes" to grant administrative privileges.

Once the program is running on the victim's computer, you can access its dashboard from any device connected to the same network. Whether it's another computer or a mobile device, ensure it is connected to the shared network. Open a web browser on your device and enter the IP address of the victim's computer, followed by ":5000," in the address bar. For instance, if the victim's computer has the IP address 192.168.1.100, you would enter "192.168.1.100:5000" in the browser's address bar.

Press Enter or click Go, and the program's dashboard should appear on your device. From there, you can interact with the program's features and functionality. It is important to note that accessing someone's computer without proper authorization and running programs as an administrator can be considered unethical and potentially illegal. Always ensure you have appropriate consent and adhere to applicable laws and regulations.
