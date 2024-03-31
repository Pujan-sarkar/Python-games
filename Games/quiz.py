print("welcome to my cyber quiz !")

playing = input("Do you want to continue ? ")
if playing.upper() != "YES":
    
    quit()
    
print("Okay ! Let's play :)")    
score = 0

answer = input("What does VPN stand for? ? ")
if answer.upper() == "VIRTUAL PRIVATE NETWORK":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does HTTPS stand for ?")
if answer.upper() == "HYPERTEXT TRANSFER PROTOCOL SECURE":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does FTP stand for ? ")
if answer.lower() == " file transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does LAN stand for ? ")
if answer.lower() == "local area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does WAF stand for ? ")
if answer.lower() == "web application firewall":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score /5) * 100) + "%.")    
    
    
    
