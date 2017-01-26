# Toy Box 
Toy box is a collection of interesting or temporary stuffs.

## AWS Tools

Folder "aws-tools" holds the utilities created and/or verified for general AWS practices and learning.
   
- "lambda" the Lambda function scripts:
	- [Verified] s3_trigger_email_nodejs.js
	
	  A Javascript sample code to send email when S3 bukcets have creation/modification (C+U) events. Note that the email address shall be **verified** as a prerequesite when SES account is still with **"sandbox"** access only in the particuplar region (as most developers on **free tier** account).

	  Notes: On errors of "parameter error in local address", it traced to sender address format issue to fix.

## Git

Git related configuration and alias templates.

## VIM Config

Folder "vim_config" with Vundle

## Bamboo XUnit Reader

The script used to fetch bamboo test results in XUnit common format and a reader to walk thru them 