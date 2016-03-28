# osx_web_cmd

Imagine the unimaginable scenario where a teenager fails to respond to requests to get off their Mac when asked to.
This application was create for that very scenario.

Once installed on the target Mac the app provides the following functions via a basic web interface served from the Mac.
- Lock the screen
- Sleep the screen
- Sleep the Mac
- Printouts of a few basic system commands 

Any user on the same network as the Mac will be able to browse to the app web interface.
The app does not provide any authentication or access restriction functionality. Its meant for use around the home.

Once running the app home page can be found on port 8080 of the target Mac.
e.g. http://192.168.1.x:8080

![ScreenShot](https://raw.githubusercontent.com/davecoutts/osx_web_cmd/master/osx_web_cmd_screenshot.png)

##Application and package file installation steps on the target Mac

```console
sudo mkdir /usr/local/osx_web_cmd
cd /usr/local/osx_web_cmd
sudo curl -O https://raw.githubusercontent.com/amoffat/sh/master/sh.py
sudo curl -O https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py
sudo curl -O https://raw.githubusercontent.com/davecoutts/osx_web_cmd/master/osx_web_cmd.py
```

##Configure to automatically start when the Mac starts via 'Automator'

- Start Automator
- Select "New Document"
- Select "Application"
- Under Library->Utilities select "Run shell script"
- In the command box replace 'cat' with '/usr/bin/python /usr/local/osx_web_cmd/osx_web_cmd.py'
- Test it by selecting the run button and browsing to the app home page
- Save the automation as 'osx_web_cmd_start'
- Quit Automator
- Go to System Preferences -> Users & Groups -> Login items
- Add(+) and tick 'osx_web_cmd_start' (You might find it in  iCloud Drive -> Automator)
- Restart the Mac and browse to the app home page to make sure it has automatically launched on start-up



