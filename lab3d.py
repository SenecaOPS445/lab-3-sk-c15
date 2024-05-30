#!/usr/bin/env python3
# Author ID: sk-c15

import subprocess

def free_space():
    df_command = "df -h"
    grep_command = "grep '/$'"
    awk_command = "awk '{print $4}'"

    df_process = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    grep_process = subprocess.Popen(['grep', '/$'], stdin=df_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    awk_process = subprocess.Popen(['awk', '{print $4}'], stdin=grep_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    df_process.stdout.close()
    grep_process.stdout.close()

    output, error = awk_process.communicate()

    if error:
        return f"Error: {error.decode('utf-8').strip()}"
    else:
        return output.decode('utf-8').strip()

if __name__ == "__main__":
    print(free_space())
