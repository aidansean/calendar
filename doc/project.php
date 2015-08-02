<?php
include_once($_SERVER['FILE_PREFIX']."/project_list/project_object.php") ;
$github_uri   = "https://github.com/aidansean/calendar" ;
$blogpost_uri = "http://aidansean.com/projects/?tag=calendar" ;
$project = new project_object("calendar", "Photo calendar", "https://github.com/aidansean/calendar", "http://aidansean.com/projects/?tag=calendar", "calendar/images/project.jpg", "calendar/images/project_bw.jpg", "One of my friends suggested I make a calendar featuring some of the photos I had taken while in Geneva.  Here is the result.  She wanted me to make some money from it, but I didn't the quality of the images was good enough, so instead I just made it available for free.  Future years might see a paid option.", "Photography,Tools", "MSOffice") ;
?>