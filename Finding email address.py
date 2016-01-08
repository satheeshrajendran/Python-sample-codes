import re 
#line = "afsd dfasdf sfdfsdaof sadofjds satheesh@gamil.com, sdfsadf@gmail.com " \ 
 #      "satg@fhdskfhdsfhkds.com.,accenture@abc.co" 
 
 
line = "xyz intensive.learnings@cig.comna.com purple monkey" 
match = re.findall(r'[\w\.-]+@[\w\.]+', line)
for i in match: 
    print(i) 
  
