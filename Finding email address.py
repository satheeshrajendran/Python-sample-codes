import re 
#line = "afsd dfasdf sfdfsdaof sadofjds ram@gamil.com, sdfsadf@gmail.com " \ 
 #      "ramaraj@123.com.,accenture@abc.co" 
 
 
line = "xyz intensive.learnings@cig.comna.com purple monkey" 
match = re.findall(r'[\w\.-]+@[\w\.]+', line)
for i in match: 
    print(i) 
  
