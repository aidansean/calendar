from project_module import project_object, image_object, link_object, challenge_object

p = project_object('calendar', 'Photo calendar')
p.domain = 'http://www.aidansean.com/'
p.path = 'calendar'
p.preview_image    = image_object('%s/images/project.jpg'   %p.path, 150, 250)
p.preview_image_bw = image_object('%s/images/project_bw.jpg'%p.path, 150, 250)
p.folder_name = 'aidansean'
p.github_repo_name = 'calendar'
p.mathjax = True
p.tags = 'Photography,Tools'
p.technologies = 'MSOffice'
p.links.append(link_object(p.domain, 'calendar/', 'Live page'))
p.introduction = 'One of my friends suggested I make a calendar featuring some of the photos I had taken while in Geneva.  Here is the result.  She wanted me to make some money from it, but I didn\'t the quality of the images was good enough, so instead I just made it available for free.  Future years might see a paid option.'
p.overview = '''These are twelve photos of Geneva, arranged into a calendar using Powerpoint.  I might make an application that generates a calendar automatically, importing special days if I get the time.  Large (90 MB) copy available upon request.'''

p.challenges.append(challenge_object('However this is made, it needs at least twelve pages.', 'I was under time pressure to make this before January 1st 2014, so I used Powerpoint for the sake of speed.', 'Resolved'))
