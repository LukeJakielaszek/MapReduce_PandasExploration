#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import datetime
import sys

# always display all columns
pd.set_option('display.max_columns', None)

# allow pandas to autodetect width 
pd.set_option('display.width', None)

#limit the width of the columns
pd.set_option('display.max_colwidth', 25)

if __name__ == "__main__":
    # ensure the number of args supplied is correct
    if(len(sys.argv) != 4):
        print("ERROR: Invalid number of params - Required : 4 - Given : " +
              str(len(sys.argv)))
        print("\tFormat: python3 processing.py illinois_file ohio_file output_file")
        
        exit(-1)

    # input files
    illinois_filename = sys.argv[1]
    ohio_filename = sys.argv[2]

    # output file
    out_filename = sys.argv[3]

        
    # PROBLEM 3
    print("------------------------- PROBLEM 3 -------------------------")

    # load the illinois csv
    ill_df = pd.read_csv(illinois_filename)

    # load the ohio csv
    ohio_df = pd.read_csv(ohio_filename)

    # convert dates to datetime
    ohio_df['Date'] = pd.to_datetime(ohio_df['Date'])
    ill_df['Issued Date'] = pd.to_datetime(ill_df['Issued Date'])
    ill_df['Filed Date'] = pd.to_datetime(ill_df['Filed Date'])

    # display illinois df
    print("ILLINOIS DATAFRAME")
    print(ill_df)

    # display ohio df
    print()
    print("OHIO DATAFRAME")
    print(ohio_df)
    print()
    
    # PROBLEM 4
    print("------------------------- PROBLEM 4 -------------------------")
    print("ILLINOIS DATATYPES")
    print(ill_df.dtypes)
    print()

    print("OHIO DATATYPES")
    print(ohio_df.dtypes)
    print()

    # PROBLEM 5
    print("------------------------- PROBLEM 5 -------------------------")
    print("OHIO CSV BEFORE SORTING")
    # display unsorted data
    print(ohio_df.head(15))

    print()
    print("OHIO CSV AFTER SORTING")
    # sort descending by date column
    ohio_df = ohio_df.sort_values("Date", ascending=False)
    print(ohio_df.head(n=15))
    print()
    
    # PROBLEM 6
    print("------------------------- PROBLEM 6 -------------------------")
    print("A) HORIZONTAL FILTERING OF ILLINOIS")

    # display the unmodified data frame
    print('Before')
    print(ill_df.head())

    # Select everything but the Filed Date column
    ill_df = ill_df[['Executive Order', 'Brief Summary',
                     'Long Summary', 'Issued Date', 'Link']]

    # display the modified dataframe
    print("After")
    print(ill_df.head())

    print()
    print("B) VERTICAL FILTERING OF OHIO")

    # display the unmodified data frame
    print('Before')
    print(ohio_df.head(n=20))

    # Select all executive orders that occur on or after 2020 for Ohio
    ohio_df = ohio_df[ohio_df["Date"] >= datetime.datetime(2020, 1, 1)]

    # display the modified dataframe
    print("After")
    print(ohio_df.head(n=20))
    print()








    
    print("------------------------- PROBLEM 7 -------------------------")

    # rename columns for compatibility of merge
    ill_df = ill_df.rename(columns={"Issued Date" : "Date", "Long Summary" : "Summary"})
    
    # add a state column to track each state (this was given in the filename but since we are
    # merging, we should track what state each executive order corresponds to)
    ill_df['State'] = "Illinois"
    ohio_df['State'] = "Ohio"

    # print what each column looks like
    print("COLUMN NAMES")
    print("OHIO BEFORE MERGE")
    print("shape: ", ohio_df.shape)
    print(ohio_df.columns)
    print("\nILL BEFORE MERGE")
    print("shape: ", ill_df.shape)
    print(ill_df.columns)
    
    # perform an outer join to merge the dataframes
    merged_df = ohio_df.merge(ill_df, how="outer")

    # sort descending by date column (since its interesting)
    merged_df = merged_df.sort_values("Date", ascending=False)
    
    print()
    print("MERGED DATAFRAMES")
    print("shape: ", merged_df.shape)
    print(merged_df.columns)
    print(merged_df)

    print("------------------------- PROBLEM 8 -------------------------")

    # write it to csv
    merged_df.to_csv(out_filename, index=False)
    print("CSV Saved to " + out_filename)
