#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
========================================================================
UsernameGenerator.py — Corporate Username Pattern Generator for Pentesting

Purpose:
    Generate targeted username wordlists from employee name lists extracted
    during information disclosure phases of penetration tests. Commonly used
    after discovering leaked documents (EmployeeHandbook.php, HR files, etc.)
    that contain employee names.

Methodology:
    For each name pair (first_name + surname) in the input file, generates
    52 username variations covering:
    - 26 lowercase variations (. _ - combinations, initial+surname patterns)
    - 26 uppercase variants of the same patterns

Context:
    Used during PWNEDsteps Web Application Penetration Test (CyberStepsVuln lab).
    Demonstrated the attack chain from information disclosure → credential stuffing →
    account takeover via brute-force attacks on /EmployeeHandbook.php endpoint.

Author: e-Itohan
License: MIT — Educational use ONLY in authorized lab environments
    
⚠️ WARNING: This script is for educational purposes ONLY in authorized
penetration testing engagements. Unauthorized access to computer systems
is illegal in most jurisdictions. Always obtain written permission
before testing any system you don't own.

Usage:
    python3 UsernameGenerator.py [input_file] [output_file]
    
    Examples:
    python3 UsernameGenerator.py employees.txt usernames.txt
    python3 UsernameGenerator.py staff_names.txt wordlist.txt

Input Format:
    One name pair per line: "FirstName LastName"
    
    Example input (employees.txt):
    -----
    Marek Kowalski
    Mati Hautameki
    Elias Vainio
    -----

Output Format:
    Plain text file with one username per line.
    Duplicate names are NOT deduplicated (keep all variants for brute-forcing).

Requirements:
    - Python 3.x (no external dependencies)
    - Input file must have "FirstName LastName" per line (2 words minimum)
========================================================================
"""

import sys
from os import path


def main():
    """Main execution function."""
    
    # Banner
    print("\nUsernameGenerator.py - Simple username generator based on a list of name and surname")
    print("-" * 70)
    
    # Argument validation
    if len(sys.argv) != 3:
        print("Usage: python3 UsernameGenerator.py [user_file] [output_file]")
        print("\nExample:")
        print("  python3 UsernameGenerator.py employees.txt usernames.txt")
        sys.exit(1)
    
    # Parse arguments
    user_file = str(sys.argv[1])
    output_file = str(sys.argv[2])
    
    print(f"Input file:  {user_file}")
    print(f"Output file: {output_file}")
    print("-" * 70)
    
    # Check if output file already exists (prevent accidental overwrite)
    if path.exists(output_file):
        print(f"[ERROR] The file '{output_file}' already exists!")
        print("        Delete this file before running this script.")
        print("-" * 70)
        sys.exit(1)
    
    # Check if input file exists
    if not path.exists(user_file):
        print(f"[ERROR] Input file '{user_file}' not found!")
        sys.exit(1)
    
    # Open output file
    try:
        output = open(output_file, 'w', encoding='utf-8')
    except IOError as e:
        print(f"[ERROR] Could not create output file: {e}")
        sys.exit(1)
    
    # Process input file
    nb_user = 0
    
    with open(user_file, 'r', encoding='utf-8') as fp:
        line = fp.readline().lower()
        
        while line:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                line = fp.readline().lower()
                continue
            
            # Parse name pair (firstName + surname)
            list_name = line.split()
            
            if len(list_name) != 2:
                print(f"[WARNING] Line '{line}' inside {user_file} is malformed.")
                print("          Expected format: [first name] [surname]")
                line = fp.readline().lower()
                continue
            
            first_name = list_name[0]
            last_name = list_name[1]
            
            # ============================================================
            # LOWERCASE VARIATIONS (26 patterns)
            # ============================================================
            output.write(last_name + '\n')                              # Just the Name
            output.write(first_name + '\n')                            # Just the firstname
            output.write(first_name + "." + last_name + '\n')           # firstname.name
            output.write(last_name + "." + first_name + '\n')           # name.firstname
            output.write(first_name + "-" + last_name + '\n')           # firstname-name
            output.write(last_name + "-" + first_name + '\n')           # name-firstname
            output.write(first_name + last_name + '\n')                # firstnamename
            output.write(last_name + first_name + '\n')                # namefirstname
            output.write(first_name + "_" + last_name + '\n')           # firstname_name
            output.write(last_name + "_" + first_name + '\n')           # name_firstname
            output.write(first_name[0] + "." + last_name + '\n')        # F.name
            output.write(last_name[0] + "." + first_name + '\n')        # N.firstname
            output.write(last_name + "." + first_name[0] + '\n')        # name.F
            output.write(first_name + "." + last_name[0] + '\n')        # firstname.N
            output.write(first_name[0] + "-" + last_name + '\n')        # F-name
            output.write(last_name[0] + "-" + first_name + '\n')        # N-firstname
            output.write(last_name + "-" + first_name[0] + '\n')        # name-F
            output.write(first_name + "-" + last_name[0] + '\n')        # firstname-N
            output.write(first_name[0] + last_name + '\n')             # Fname
            output.write(last_name[0] + first_name + '\n')             # Nfirstname
            output.write(last_name + first_name[0] + '\n')             # nameF
            output.write(first_name + last_name[0] + '\n')             # firstnameN
            output.write(first_name[0] + "_" + last_name + '\n')        # F_name
            output.write(last_name[0] + "_" + first_name + '\n')        # N_firstname
            output.write(last_name + "_" + first_name[0] + '\n')        # name_F
            output.write(first_name + "_" + last_name[0] + '\n')        # firstname_N
            
            # ============================================================
            # UPPERCASE VARIATIONS (26 patterns - capitalized)
            # ============================================================
            first_name_cap = first_name.capitalize()
            last_name_cap = last_name.capitalize()
            
            output.write(last_name_cap + '\n')                        # Just the Name
            output.write(first_name_cap + '\n')                      # Just the firstname
            output.write(first_name_cap + "." + last_name_cap + '\n') # firstname.name
            output.write(last_name_cap + "." + first_name_cap + '\n') # name.firstname
            output.write(first_name_cap + "-" + last_name_cap + '\n') # firstname-name
            output.write(last_name_cap + "-" + first_name_cap + '\n') # name-firstname
            output.write(first_name_cap + last_name_cap + '\n')      # firstnamename
            output.write(last_name_cap + first_name_cap + '\n')      # namefirstname
            output.write(first_name_cap + "_" + last_name_cap + '\n') # firstname_name
            output.write(last_name_cap + "_" + first_name_cap + '\n') # name_firstname
            output.write(first_name_cap[0] + "." + last_name_cap + '\n') # F.name
            output.write(last_name_cap[0] + "." + first_name_cap + '\n') # N.firstname
            output.write(last_name_cap + "." + first_name_cap[0] + '\n') # name.F
            output.write(first_name_cap + "." + last_name_cap[0] + '\n') # firstname.N
            output.write(first_name_cap[0] + "-" + last_name_cap + '\n') # F-name
            output.write(last_name_cap[0] + "-" + first_name_cap + '\n') # N-firstname
            output.write(last_name_cap + "-" + first_name_cap[0] + '\n') # name-F
            output.write(first_name_cap + "-" + last_name_cap[0] + '\n') # firstname-N
            output.write(first_name_cap[0] + last_name_cap + '\n')     # Fname
            output.write(last_name_cap[0] + first_name_cap + '\n')     # Nfirstname
            output.write(last_name_cap + first_name_cap[0] + '\n')     # nameF
            output.write(first_name_cap + last_name_cap[0] + '\n')     # firstnameN
            output.write(first_name_cap[0] + "_" + last_name_cap + '\n') # F_name
            output.write(last_name_cap[0] + "_" + first_name_cap + '\n') # N_firstname
            output.write(last_name_cap + "_" + first_name_cap[0] + '\n') # name_F
            output.write(first_name_cap + "_" + last_name_cap[0] + '\n') # firstname_N
            
            # Increment counter (52 patterns per person)
            nb_user += 52
            
            # Read next line
            line = fp.readline().lower()
    
    # Close output file
    output.close()
    
    # Final summary
    print(f"\n[SUCCESS] Usernames written to output file: {output_file}")
    print(f"[INFO]    Number of users created: {nb_user}")
    print("-" * 70)


if __name__ == "__main__":
    main()
