#!/usr/bin/python
# This is a module of bt5up for Additional Tools .
# Autor: bl4ck5w4n aka MaXFX in BT Forum
# Mail: bl4ck5w4n5@gmail.com
# Blog: http://bl4ck5w4n.blogspot.com/

import  os, time, inspect,sys,fileinput
from time import gmtime, strftime

global mods
mods = '/pentest/bt5up' # Path to bt5up

global tsleep 
tsleep = 2


if os.path.isfile(mods + '/bt5up.py'): #Just to make sure that bt5up.py is in the right path
  sys.path.append(mods)
	
else:
   	os.system('mkdir -p '+ mods)
   	os.system("cd /tmp && wget http://bl4ck5w4n.tk/wp-content/uploads/2011/07/bt5up.tar -c -q")
	if os.path.isfile("/tmp/bt5up.tar"):
	    os.system("tar -xvf /tmp/bt5up.tar -C " + mods)
	if os.path.isfile("/bin/bt5up"):
	    os.system("rm /bin/bt5up")
	os.system("ln -s " + mods + "/bt5up.py /bin/bt5up")
	os.system("chmod +x /bin/bt5up")
	    
   	sys.path.append(mods)
   
import bt5up


def get_version():
      curversion = 1
      return curversion
      
def lversion():
	i=0
	lversion = 0
	if os.path.isfile("/tmp/addtools_version.txt"):
	    ofile=open("/tmp/addtools_version.txt","r")
	    lversion=ofile.readline()
	else:
	    os.system("cd /tmp && wget http://bl4ck5w4n.tk/bt5up/addtools_version.txt -c -q")
	    ofile=open("/tmp/addtools_version.txt","r")
	    lversion=ofile.readline()
	    
	
	return lversion
	
def install_nessus():
    if(os.system("which nessus > /dev/null") == 0):
		print("\033[1;31m [>]\033[1;m Nessus is already installed!")
		time.sleep(tsleep)
	    
    else:
      print("\033[1;31m [>]\033[1;m Installing Nessus!")
      os.system("apt-get install nessus")
      print("\033[1;31m [>]\033[1;m You need to register nessus to get the activation code:")
      browser_nessus = raw_input("\033[1;31m [>]\033[1;m Would you like me to open Firefox for you? [n/Y] : ")
      if(browser_nessus.upper()=="Y"):
	os.system("firefox http://tenable.com/products/nessus/nessus-homefeed&")
      
      auth_key=""
      while(auth_key == ""):
	      auth_key = raw_input("\033[1;31m [>]\033[1;m Enter Activation Code that was sent to your Email: ")
	      os.system("/opt/nessus/bin/nessus-fetch --register " + auth_key)
	      print("\033[1;31m [>]\033[1;m Adding user")
	      os.system("/opt/nessus/sbin/nessus-adduser")
	      print("\033[1;31m [>]\033[1;m Staring Nessus service")
	      os.system("/etc/init.d/nessusd start")
	      print("\033[1;31m [>]\033[1;m To access Nessus Web Interface: https://127.0.0.1:8834")


def crypter():
    print("\033[1;31m [>]\033[1;m Installing Crypter, please wait.")
    time.sleep(tsleep)
    os.system("mkdir /tmp/crypter")
    if(os.system("cd /tmp/crypter && wget http://technicdynamic.com/wp-content/uploads/2012/04/script.zip && unzip script.zip") == 0):
	    os.system("")
	    print("\033[1;31m [>]\033[1;m Changeging MSF path in Crypter file..")
	    time.sleep(tsleep)	    
	    for lines in fileinput.FileInput("/tmp/crypter/script/crypter.py", inplace=1): 
		if "/pentest/exploits/framework3" in lines:
		  lines = lines.replace("/pentest/exploits/framework3","/opt/metasploit/msf3/")
		sys.stdout.write(lines)
	    os.system("cp /tmp/crypter/script/* /opt/metasploit/msf3/")
	    os.system("chmod +x /opt/metasploit/msf3/crypter.py")
	    print("\033[1;31m [>]\033[1;m Installing Crypter DEPS...")
	    os.system("apt-get install mingw32-runtime mingw-w64 mingw gcc-mingw32 mingw32-binutils -y")
	    print("\033[1;31m [>]\033[1;m Crypter installed successfully!")
	    print("\033[1;31m [>]\033[1;m To run Crypter go to /opt/metasploit/msf3/")
	    time.sleep(tsleep)
    else:
	  print("\033[1;31m [>]\033[1;m Failed to install Crypter.")
	  os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install Crypter' >> /root/bt5up.log")


def ghostphisher():
        print("\033[1;31m [>]\033[1;m Installing Ghost Phisher, please wait.")
        time.sleep(tsleep)
        
        if(os.system("cd /tmp && wget https://ghost-phisher.googlecode.com/files/Ghost-Phisher_1.5_all.deb") == 0):
		if(os.system("cd /tmp && dpkg -i Ghost-Phisher_1.5_all.deb") == 0):
			check_folder()	
			os.system("ln -s /opt/Ghost-Phisher/ghost.py " + mods + "/tools/ghostphisher; chmod +x "+ mods + "/tools/ghostphisher")
	  		print("\033[1;31m [>]\033[1;m Ghost Phisher installed successfully!")
	  		time.sleep(tsleep)
		else:
	  		print("\033[1;31m [>]\033[1;m Failed to install Ghost Phisher .")
	  		os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install Ghost Phisher' >> /root/bt5up.log")
	  		time.sleep(tsleep)
	
	else:
	  print("\033[1;31m [>]\033[1;m Failed to install Ghost Phisher .")
	  os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install Ghost Phisher' >> /root/bt5up.log")
	  time.sleep(tsleep)


def tmnt():
        print("\033[1;31m [>]\033[1;m Installing The Teenage Mutant Ninja Turtles project, please wait.")
        time.sleep(tsleep)
        check_folder()
        if(os.system("cd "+ mods + "/tools/ && wget https://teenage-mutant-ninja-turtles.googlecode.com/files/tmnt_v1.8.zip") == 0):
		os.system("cd "+ mods + "/tools/ && unzip tmnt_v1.8.zip && rm tmnt_v1.8.zip")
		print("\033[1;31m [>]\033[1;m The Teenage Mutant Ninja Turtles project installed successfully!")
		print("\033[1;31m [>]\033[1;m Installed at "+ mods + "/tools/tmnt_v1.8")
	  	time.sleep(tsleep)
			
	else:
	  print("\033[1;31m [>]\033[1;m Failed to install The Teenage Mutant Ninja Turtles project.")
	  os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install The Teenage Mutant Ninja Turtles project' >> /root/bt5up.log")
	  time.sleep(tsleep)



def themole():
        print("\033[1;31m [>]\033[1;m Installing The Mole, please wait.")
        time.sleep(tsleep)
        os.system('apt-get install python3-dev')
        
        if(os.system("cd /tmp && wget http://lxml.de/files/lxml-2.3.4.tgz") == 0):
	      os.system("cd /tmp && tar -xvf lxml-2.3.4.tgz")
	      os.system("cd /tmp/lxml-2.3.4 && python3 setup.py install")
	      check_folder()
	      if(os.system("cd "+ mods + "/tools/ && wget http://downloads.sourceforge.net/project/themole/themole-0.3/themole-0.3-lin-src.tar.gz") == 0):
		      os.system("cd "+ mods + "/tools/ && tar -xvf  themole-0.3-lin-src.tar.gz && rm themole-0.3-lin-src.tar.gz")
		      print("\033[1;31m [>]\033[1;m The Mole installed successfully!")
		      print("\033[1;31m [>]\033[1;m Installed at "+ mods + "/tools/themole-0.3 run as python3 mole.py")
		      time.sleep(tsleep)
			      
	      else:
		print("\033[1;31m [>]\033[1;m Failed to install The Mole.")
		os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install The Mole' >> /root/bt5up.log")
		time.sleep(tsleep)
	else:
		print("\033[1;31m [>]\033[1;m Failed to install The Mole.")
		os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install The Mole' >> /root/bt5up.log")
		time.sleep(tsleep)
		
		
def minidwep():
        print("\033[1;31m [>]\033[1;m Installing MinidWep-GTK")
	print("\033[1;31m \n          Please choose your system.\n-----------------------------------------------\033[1;m")
	print("\033[1;31m [>]\033[1;m 1. 32Bits")
	print("\033[1;31m [>]\033[1;m 2. 64Bits")
	bits=raw_input("\033[1;31m [>]\033[1;m Enter your choice: ")
        time.sleep(tsleep)
	
	if(bits=="1"):
		filename="minidwep-gtk-30513-bt5-32bit"
		if(os.system("cd /tmp && wget http://bl4ck5w4n.tk/bt5up/tools/minidwep-gtk-30513-bt5-32bit.deb") == 0):
			os.system("cd /tmp && dpkg -i minidwep-gtk-30513-bt5-64bit.deb")
			print("\033[1;31m [>]\033[1;m MinidWep-gtk installed successfully!")
		  	time.sleep(tsleep) 
	if(bits=="2"):

		if(os.system("cd /tmp && wget http://bl4ck5w4n.tk/bt5up/tools/minidwep-gtk-30513-bt5-64bit.deb") == 0):
			os.system("cd /tmp && dpkg -i minidwep-gtk-30513-bt5-64bit.deb")
			print("\033[1;31m [>]\033[1;m MinidWep-gtk installed successfully!")
		  	time.sleep(tsleep)          

		
		else:
	  		print("\033[1;31m [>]\033[1;m Failed to install MinidWep-GTK.")
	  		os.system("echo '"+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) +" - Failed to install MiniWep-GTK' >> /root/bt5up.log")
	  		time.sleep(tsleep)
	  	
def check_folder(): #check if path to tools exists
	if (os.path.isdir(mods + "/tools") == False):
	    os.system("mkdir -p " + mods + "/tools")	


def check_tools():
	print("\033[1;31m [>]\033[1;m Updating Tools List.")
	
	
	if (os.system("cd /"+mods+"/mods && rm tools.py && wget http://bl4ck5w4n.tk/bt5up/mods/tools.py -c -q")==0): 
			    
		curfile = inspect.getfile(inspect.currentframe())
	
		pwd = os.getcwd() + str(curfile)
	
		print("\033[1;31m [>]\033[1;m Update successfully! bt5up will restart, please wait...")
		time.sleep(tsleep)
		python = sys.executable
		os.execl(python, python, * sys.argv)	      

def add_tools():
	print("                        Section: Additional Tools")
	if (int(get_version()) < int(lversion())):
		print("		         \033[1;31m [New Tools Available] \033[1;m \n") 
		
	print("\033[1;31m [>]\033[1;m 1. Nessus.")
	print("\033[1;31m [>]\033[1;m 2. Crypter.") 
	print("\033[1;31m [>]\033[1;m 3. Ghost Phisher.")
	print("\033[1;31m [>]\033[1;m 4. The Teenage Mutant Ninja Turtles project.")
	print("\033[1;31m [>]\033[1;m 5. MinidWep-GTK.")
	print("\033[1;31m [>]\033[1;m 6. The Mole.")
	print("\033[1;31m [>]\033[1;m 98. Install All.")
	print("\033[1;31m [>]\033[1;m 99. Update Tools List.")
	print("\033[1;31m [>]\033[1;m 0. Back.")
	choice_var=raw_input("\033[1;31m [>]\033[1;m Enter your choice: ")

	if(choice_var=="1"):
	    install_nessus()
	    bt5up.additional_tools()
	if(choice_var=="2"):
	    crypter()
	    bt5up.additional_tools()
	
	if(choice_var=="3"):	    
	    ghostphisher() 
 	    bt5up.additional_tools()

	if(choice_var=="4"):	    
	    tmnt() 
 	    bt5up.additional_tools()
	if(choice_var=="5"):	    
	    minidwep() 
 	    bt5up.additional_tools()
	if(choice_var=="6"):	    
	    themole() 
 	    bt5up.additional_tools()
	if(choice_var=="98"):	    
	    install_nessus()
	    crypter()
	    ghostphisher()
	    themole()
	    tmnt()
	    minidwep()
 	    bt5up.additional_tools()

	if(choice_var=="99"):
		check_tools()
		bt5up.additional_tools()
	if(choice_var=="0"):
	    bt5up.main()
