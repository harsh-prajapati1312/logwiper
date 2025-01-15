
# Log wiper and Disable Service Script

The Log Wiper and Service Disabler Script is a powerful tool designed to help manage and clear logs on Linux-based systems. It is tailored for users who need to disable logging services, prevent persistent logs, and overwrite sensitive log files. This script provides a way to ensure that no system logs are retained, either by stopping logging services, redirecting logs to /dev/null, or by manually clearing existing logs.


## Disclaimer

This script is intended solely for educational purposes and should be used with caution. It modifies critical system configurations, disables logging services, and clears log files, which may be required for system auditing, troubleshooting, or security monitoring. Running this script may cause irreversible changes to your system and may impact system stability, security, and compliance.

Before executing this script, ensure that you fully understand the potential consequences and risks. Only use this script in a controlled environment, such as virtual machines or test systems, where the impact of changes can be safely assessed and managed.

The author and contributors are not responsible for any unintended consequences, damage, or loss of data resulting from the use of this script.


## Features

- Banner Display: Displays a custom banner when the script runs.
- Stopping and Disabling Logging Services: Stops and disables rsyslog and systemd-journald to prevent logging.
- Disabling Persistent Logging for systemd-journald: Configures systemd-journald to not persist logs.
- Disabling Log Rotation: Renames the logrotate cron job to prevent log rotation.
- Redirecting Logs to /dev/null: Apache and MySQL logs are redirected to /dev/null to prevent logs from being written.
- Clearing and Overwriting Log Files:  A predefined list of system log files is overwritten 10 times to remove previous log data.
- Logs that are not found will be skipped.



## Requirements

- Python 3.x (Recommended version: 3.6+) 
- sudo privileges to run the system commands (ensure the user running this script has sufficient permissions).
## Installation

- Clone the repository: Clone the repository from GitHub using the following command:

```bash
git clone https://github.com/harsh-prajapati1312/logwiper.git

cd logwiper

```
    
## Usage/Examples

- Clone or download this repository to your local system.
- Execute the script with elevated privileges:
```Bash
sudo python3 logwiper.py
```
-The script will:

    - Display a banner with a system information message.
    - Stop and disable logging services (rsyslog and systemd-journald).
    - Modify systemd-journald configuration to prevent persistent logging.
    - Rename the logrotate cron job to disable log rotation.
    - Redirect Apache and MySQL logs to /dev/null.
    - Overwrite a predefined set of log files 10 times to erase any data.

-Upon completion, the script will report that all specified log files have been cleared and overwritten.




## Log Files Cleared
```bash
/var/log/auth.log
/var/log/secure
/var/log/syslog
/var/log/messages
/var/log/kern.log
/var/log/boot.log
/var/log/daemon.log
/var/log/faillog
/var/log/dpkg.log
/var/log/yum.log
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/wtmp
/var/log/btmp
/var/log/lastlog
/var/log/mail.log
/var/log/mail.err
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/mysql/error.log
/var/log/audit/audit.log
```
## Security Considerations

- Root Access: The script requires sudo to modify system settings and clear log files. Ensure that only authorized users can execute it.
- Irreversible Changes: This script irreversibly clears and overwrites log files. Once executed, the original log contents cannot be recovered.
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://harsh-prajapati1312.github.io/myportfolio/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harshprajapati13)



## Authors

- This script is developed and maintained by: Harsh Prajapati


## License

This project is licensed under the MIT [License](https://choosealicense.com/licenses/mit/) - see the LICENSE file for details



