# delete-sonar-projects

Simple stupid scripts to fast delete from your Sonar 4.x and 7.x projects by list.

## Problem

Sonar (Community Edition at least) has a terrible and very slow user interface for
mass deletion projects. Fortunately there is an API. So, you have a list of project 
keys to delete.

## Solution

 1. Create empty text file with any name (projects.txt for example)
 2. Add sonar project keys of projects to delete to your text file

```
ci:svn:project1
ci:svn:project2
```

 3. Execute from cli (Python 2.x)

```
python delete_sonar_projects_msk.py [domain user] [your password] [file with projects]
```

For example,

```
python delete_sonar_projects_msk.py vama0616 password msk.txt
```

## Unlicense

This is a public domain. Do with this code what you want
