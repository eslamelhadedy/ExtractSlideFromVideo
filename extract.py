# Opens the Video file
import cv2
import os
import img2pdf
import sys
if sys.platform in ["linux", "linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'

else:
	W = ''
	G = ''
	R = ''

print(G + r'''

 _______  _                 _______  ______   _______  ______           
(  ____ \( \      |\     /|(  ___  )(  __  \ (  ____ \(  __  \ |\     /|
| (    \/| (      | )   ( || (   ) || (  \  )| (    \/| (  \  )( \   / )
| (__    | |      | (___) || (___) || |   ) || (__    | |   ) | \ (_) / 
|  __)   | |      |  ___  ||  ___  || |   | ||  __)   | |   | |  \   /  
| (      | |      | (   ) || (   ) || |   ) || (      | |   ) |   ) (   
| (____/\| (____/\| )   ( || )   ( || (__/  )| (____/\| (__/  )   | |   
(_______/(_______/|/     \||/     \|(______/ (_______/(______/    \_/   
   Fb:https://www.facebook.com/eslam.elhadedy.18/
   twitter:https://twitter.com/eslamelhadedy50                                                                     
   tel:+0201157601798

''')

filename=sys.argv[1] #Argument
os.system('ffmpeg -i '+filename+' -vf mpdecimate,setpts=N/FRAME_RATE/TB out.mp4')
cap= cv2.VideoCapture(filename+'out.mp4')
i=0
imgs=[]
while(cap.isOpened()):

	ret, frame = cap.read(500)
	if ret == False:
		break
	cv2.imwrite('kang'+str(i)+'.jpg',frame)
	imgs.append('kang'+str(i)+'.jpg')


	i+=1
with open("out.pdf", "ab") as f:
	f.write(img2pdf.convert(imgs))
cap.release()
cv2.destroyAllWindows()
