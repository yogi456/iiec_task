import pyttsx3
import os

pyttsx3.speak("Welcome user ....")


while True:
       pyttsx3.speak("how can i help u")
       print("How can I help you :" , end=' ' )
       p= input()
       

       if  (("run" in p) or  ("open" in p) or ("launch" in p))  and  (("chrome " in p) or  ("browser" in p)) :
         pyttsx3.speak("Opening chrome for you plz wait")
         os.system("chrome")
       elif  (("run" in p) or ("open" in p) or  ("launch" in p))  and  (("notepad" in p) or  ("editor" in p)):
         pyttsx3.speak("Opening notepad for you plz wait")
         os.system("notepad")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  (("video player " in p) or  ("video" in p)) :
         pyttsx3.speak("Opening videoplayer for you plz wait")
         os.system("wmplayer")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("codeblocks " in p):
         pyttsx3.speak("Opening codeblocks for you plz wait")
         os.system("codeblocks.exe")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("Powerpoint " in p) :
         pyttsx3.speak("Opening Powerpoint  for you plz wait")
         os.system("PowerPoint")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("linkedin" in p) :
         pyttsx3.speak("Opening your linked account  you plz wait")
         os.system("chrome linked.in")
        
       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("ms excel" in p) :
         pyttsx3.speak("Opening ms excel plz wait")
         os.system("Excel")
     
       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("my website" in p) or ("lookbook" in p) :
         pyttsx3.speak("Opening Your website for you please wait")
         os.system("chrome https://bookgiveaway.online")
       
       elif  (("run" in p) or  ("open" in p) or ("launch" in p) or ("play" in p)) and  ("dil meri na sune" in p) or ("dil" in p) :
         pyttsx3.speak("Opening Video song for you please wait")
         os.system("chrome https://youtu.be/YZLKoG_vhDY")

       elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("ec2" in p) :
         pyttsx3.speak("Launching Ec2 Instance for you")
         os.system("aws ec2 run-instances --image-id ami-0ebc1ac48dfd14136 --count 1 --instance-type t2.micro --key-name myiiec --security-groups allowall")

        
       elif (("hii" in p) or ("hello" in p) or ("hey" in p)):
         pyttsx3.speak("hiii yogesh now tell me how can I help you")

  

       elif ("exit" in p) or ("stop" in p) or ("quit" in p):
         pyttsx3.speak("Exiting now")
         break
       else:
         pyttsx3.speak("this application is not supported in your computer plz tell again")
