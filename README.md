td.py
=====

Goal
----

This python tool parses todolist text files and puts them to a mongodb collection. To show these documents on a website the [tdgui.js] can be used.

I used create my todo lists to simple textfiles. The **name** of them is **&lt;year&gt;-&lt;month&gt;-&lt;day&gt;.txt** (e.g. **2012-FEB-10.txt**); here is an example of their **content format**:

>DONE 1, add express.js to tdgui.js  
DONE 2, select the proper template language  
DONE 3, create the page which shows the td list to a hardcoded date  
DONE 4, create a router which gets the date in url  
DONE 5, validate the string in the url to avoid something wrong  
DONE 6, create mongo query which finds the next available date in db   
SKIP 7, write some docs  
DONE 8, translate this query to the api of node-mongodb-native driver  
TODO 9, show the next/prev links on the page  
TODO 10, introduce step for better control flow  
TODO 11, add bootstrap 2.0 to get a more beatiful page  


Usage
-----
    python td.py path/to/file
e.g. on Windows:

    python td.py D:\todo\2012-FEB-10.txt


Result document in mongodb
--------------------------

Here is an example of the result document:

	{ _id: 4f383f0cb6a9501784000000,
	  date: '2012-FEB-10',
	  realdate: Fri, 10 Feb 2012 00:00:00 GMT,
	  tds: 
	   [ { status: 'DONE', text: 'add express.js to tdgui.js', number: 1 },
		 { status: 'DONE',
		   text: 'select the proper template language',
		   number: 2 },
		 { status: 'DONE',
		   text: 'create the page which shows the td list to a hardcoded date',
		   number: 3 },
		 { status: 'DONE',
		   text: 'create a router which gets the date in url',
		   number: 4 },
		 { status: 'DONE',
		   text: 'validate the string in the url to avoid something wrong',
		   number: 5 },
		 { status: 'DONE',
		   text: 'create mongo query which finds the next available date in db',
		   number: 6 },
		 { status: 'SKIP', text: 'write some docs', number: 7 },
		 { status: 'DONE',
		   text: 'translate this query to the api of node-mongodb-native driver',
		   number: 8 },
		 { status: 'TODO',
		   text: 'show the next/prev links on the page',
		   number: 9 },
		 { status: 'TODO',
		   text: 'introduce step for better control flow',
		   number: 10 },
		 { status: 'TODO',
		   text: 'add bootstrap 2.0 to get a more beatiful page',
		   number: 11 } ] }


[tdgui.js]: http://github.com/tfitos/tdgui.js
