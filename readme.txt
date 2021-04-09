This file has the following information:
-> Team information
-> About the program
-> Instructions to run the program
-> How the program runs?


Team Information:           student_id

1. Prithvi Bommu            A04214501
2. Bhargav Sunkara          A04212338
3. Vineet Reddy Karri       A04201031


About the program:
The program requires python3 to run.
The program runs with basic modules and no external packages are required.




Use the following commands to run the program:
1. Navigate to the program's directory from cmd line or terminal and type the following command:
    ~ make

2. <make> according to the makefile will create the executable file in a dynamically created folder "dist".
    The following command will change the directory to dist:
    ~ cd dist
    To run the executable with search string as argument:
    ~ ./enron_search <enter input here>

3. The above command will search for the words in mbox files in the path and returns output in the following format:
    Phillip K Allen <phillip.allen@enron.com>, Mon, 7 May 2001 06:23:00 -0700 (PDT)
    Phillip K Allen <phillip.allen@enron.com>, Mon, 7 May 2001 06:23:00 -0700 (PDT)
    Results found: 3



How the program runs:
1. If no environment variable is set the program executes on a sample mbox file which is the the folder "test".
2. The given command line argument is broken into multiple words and converting them to lower case and removing the duplicates and is then converted to a list "search_string".
3. Function "_parser" looks for each element of the list "search_string" and then searches in the all mbox files in the path.
4. The program prints the email information if all the words entered are found in the email's body.
5. The email information is dynamically returned each time before the next file in the path is loaded.
6. In the end the program returns the total number of searches found at the end of last file in the directory.







