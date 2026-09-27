

# **How to Set Configuration in Git CMD?**

1. **Open Git CMD:**
   - Open Git Bash or Git CMD on Windows, or your terminal if you're on macOS/Linux.

2. **Set Your Username:**
   - Run the following command to set your Git username:
     ```bash
     git config --global user.name "Your Name"
     ```
   - Replace `"Your Name"` with your actual name. This name will be displayed with your commits.

3. **Set Your Email:**
   - Run the following command to set your email:
     ```bash
     git config --global user.email "youremail@example.com"
     ```
   - Replace `"youremail@example.com"` with the email address you used to create your GitHub account.

4. **Verify Your Configuration:**
   - To confirm that your settings have been applied, run:
     ```bash
     git config --global --list
     ```
   - This will display the current global settings, including your username and email.

Now Git is configured and ready for use with your username, email, and preferred editor!