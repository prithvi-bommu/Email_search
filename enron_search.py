import mailbox
import os
import re
import sys


if os.getenv('ENRON_FILE'):
    path = ENRON_FILE

else:
    path = r'../test'

#function to parse through mbox files in the path
def _parser(string):
    count = 0
    directory = path
    for entry in os.scandir(directory):
        mbox = mailbox.mbox(entry)

        #extracting the body of the each mail
        for e_mail in mbox:
            body = e_mail.get_payload()
            email_list=[]


            for z in re.split(r'\s',body):
                #stripping special character on the left
                left_slash = z.lstrip("!@#$%^&*().,")

                # stripping special character on the right
                full_slash = left_slash.rstrip("!@#$%^&*().,")

                #converting to lower case
                full_slash = full_slash.lower()

                email_list.append(full_slash)

            #loop to search for words and return
            for i in string:
                if i in email_list:

                    if string.index(i)==len(string)-1:
                        print("{name} <{email}>, {time}".format(name=e_mail['X-From'], email=e_mail['From'],time= e_mail['date']))
                        count = count+1
                    else:
                        pass
                else:
                    break
    print("Results found:",count)

#Driver Code
search_string = (sys.argv)
search_string.pop(0)

#removing dupicates and converting to lower case with list comprehenssion
search_string = list(set([i.lower() for i in search_string]))
_parser(search_string)
