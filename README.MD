# Gather Up

> Command line tool to gather up files buried in subdirectories.

### Description

I built this tool to help with a common problem with my photo files, though it works for most file types. Choose a single directory to clean up, then run this tool to gather all files contained within and move them to a newly-created top level folder.

### Usage

First, clone this repo to your local machine, then cd into it.

You can use the 'testdir' directory to test this tool's usage.

So, for example, use your command line to:
`python gather-up.py ./testdir`

(Don't use folders with spaces in their name!)

You should see a new folder appear called '\_Gathered-Files' get populated with all files found within this folder's several levels.
