#!/usr/bin/python
#
# Instructions & Requirements
# ---------------------------
# Complete the code to fulfill the below Acceptance Criteria.

# Acceptance Criteria
#-------------
# 1.) Program can accept a json file (ie. data1.json) from the command line.
# 2.) Program can verify that json file exists and is in expected format.
# 3.) Program can clean json file:
#   a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
#   b) Use allowable names (V_NAMES, I_NAMES, PF_NAMES) provided below to clean keys.
# 4.) Program creates a new dictionary that has the same location as the primary key, but the value is three new
#       calculated quantities:
#           s = apparent power
#           p = real power
#           q = reactive power
# 5.) Use the "calc_power" function to handle the calculations for the new dictionary.
#   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
# 6.) Complete the TODO in calc_power. Use the calc_power doc string for more information.
# 7.) Program outputs the new dictionary in a user readable manner.

# Notes
# -----
# Treat this code as if you were going to put this into production. We want to see how you would code with us.
# Write the code so that it is testable and show some examples of unit tests (full coverage not expected).
# Make the code robust (e.g. Error handling, managing unexpected input, etc)
# Make the code readable. Remember, comments aren't the only way to make code readable.
# Make the code clean. Don't be afraid to clean up code that is already written.
# Make the code reusable. It's not easy to reuse a main function.
# Don't spend more than an hour on this.
# If there are refactorings or improvements that you would do if you had more time, make notes of that.


from copy import copy
import sys
import json
import math
import argparse

# Allowable names for voltage, current, and power factor
V_NAMES = {'v', 'V', 'Volts', 'Voltage'}
I_NAMES = {'i', 'I', 'Amps', 'Amperes', 'Current'}
PF_NAMES = {'pf', 'PF', 'Power Factor'}


def calc_power(volts, amps, pf):
    '''Returns tuple of (p, q, s) powers from the inputs.

        Note that the relationship between p, q, and s can be described with a right triangle.
            \
            | \
            |   \
          q |     \  s
            |       \
            |_        \
            |_|_________\
                 p
    '''
    try:
        s = volts * amps
        p = s * pf
        q = s * math.sqrt(1-math.pow(pf,2))

        return([round(x, 2) for x in (p, q, s)])
    except (ValueError, TypeError):
        return (None, None, None)

def hash_values(vals):
    keys = list(vals.keys())

    try:
        if keys[0] in V_NAMES:
            v = vals[keys[0]]
        if keys[1] in I_NAMES:
            i = vals[keys[1]]

        if len(keys) > 2:
            if keys[2] in PF_NAMES:
                pf = vals[keys[2]]
                return v,i,pf

        return v,i,0.9
    except:
        print("Incorrect keys")


def print_out(out_dict):
    ''' print output dictionary in human readable format'''
    for key in out_dict:
        print(f"{key}: \n"
              f"    True Power = {out_dict[key]['p']} W\n"
              f"    Reactive Power = {out_dict[key]['q']} VAR\n"
              f"    Apparent Power = {out_dict[key]['s']} VA"  )

def iter_dict(data):
    out = {}

    for key in data:
        # map values to according to allowable names
        volts, amps, pf = hash_values(data[key])

        # mapping output of values to output dictionary
        out[key] = dict(zip(['p', 'q', 's'], calc_power(volts, amps, pf)))

    return out

def main():
    # input via argeprase
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as file:
        data = json.load(file)


    # iterate through dicitary
    out = iter_dict(data)

    #print dictionary neatly
    print_out(out)

# do stuff here
# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
    main()
