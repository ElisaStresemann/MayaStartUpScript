import maya.cmds as cmds
import CG1MeshAnalyser05 as meshAna
import os
import mtoa.utils as mutils


def callAutosave(*args):
    print("Button is clicked.")
    prompt_display = cmds.promptDialog(t="Autosave", message="Please enter destination folder:", button=["Save","Search","Cancel"])
    print("User clicks on button: " + prompt_display)
    # save Folderstring/ Query=True, Text=True
    folderName= cmds.promptDialog(q=1, tx=1)
    
    if prompt_display=="Save": 
          
        # int=300 set the interval between auto-saves to 5 minutes
        # The default interval is 600 seconds (10 minutes)
        cmds.autoSave(enable=True,int=300,dst=1,folder=folderName)
        print("Autosave enabled")
      
    if prompt_display=="Search":
        #cmds.fileDialog2(dir='path/to/dir', dialogStyle=2, fileMode =4)
        singleFilter = "All Files (*.*)"
        dir=cmds.fileDialog2(fileFilter=singleFilter, dialogStyle=2, fileMode=3)
  
        # using list comprehension 
        listToStr = ' '.join(map(str, dir)) 
        print(listToStr)
        
        cmds.autoSave(enable=True,int=300,dst=1,folder=listToStr)
        print("Autosave enabled")
        
def callUndo(*args):
    cmds.undoInfo(state=True, infinity=True)
    print("Undo enabled")
    
def callAnimationPrefs(*args):
    #cmds. fps, autokey? anything else?
    #set the current unit to 24 fps = 'film'  [25 fps=PAL (TV)]
    cmds.currentUnit( time='film' )
    print("Set 24 fps")
    
    #set the current playback speed to 24x1 and the timeline from 0 to 24 & Update View All Viewports
    cmds.playbackOptions(min=0, max=24, ps=1,view="all")
    print("Set playback speed to 24 fps x 1\nSet the timeline from 0 to 24 Frames\nSet Option: Update View All Viewports") #Realtime [x0.5 | x2]
    
    #set Preferences->Time Slider->Channel Box Sync : (enable) sync timeline display
    # todo
    #cmds.optionVar("toggleChannelBoxTimelineSync #1",value=True)
    #print a
    
#def callLightsetup(*args):
#    mutils.createLocator("aiSkyDomeLight", asLight=True)
#   cmds.setAttr( 'aiSkyDomeLightShape1.intensity', 1.312849)
#    print("Default Arnold Light enabled")
             
def callMeshAna(*args):
    meshAna.ui() 
    print("Open MeshAnalyser")    
def callICloud(*args):
    cmds.webBrowser(width=800, height=600, sf=True, url='https://icloud2.informatik.htw-dresden.de/')
    print("Open Opal Homepage")   
def callOpal(*args):
    cmds.webBrowser(width=800, height=600, sf=True, url='https://bildungsportal.sachsen.de/opal')
    print("Open iCloud Homepage")
def callClose(*args):
    cmds.CloseFrontWindow()
    print("Close StartUpScript")
    
    
# Creates a new Scene by execute this command
#cmds.file(force=1, new=1)

# newWindow and layout
# title, width & height, min- & maxButton, backcolor(RGB)
myWin=cmds.window(t="MayaStartUpScript", wh=(450,700), minimizeButton=True, maximizeButton=True, backgroundColor=[0, 0.5, 0.5])
cmds.columnLayout(rs=10, columnWidth=130)

# what path we need ?-> C:\Users\estre\OneDrive\Dokumente\maya\scripts
# returns the home-path : C:\Users\estre\OneDrive\Dokumente
homePath=os.environ['HOME']

#complete path string
completePath=homePath+"/maya/scripts/"
#print completePath
imagePath=completePath+"pic_upScript3_450x100.png"

#show image
#cmds.image( imagePath)
cmds.picture(w=450, h=100, image=imagePath)

#returns the current Version, if needed for other path
currVersion=cmds.about(version=True)
#print currVersion

# button labels and function calls
# label=name, bgc=backColor(RGB), sbm(MayaStatusbarMessage), w=width, h=height, command->call def
cmds.text(l='Autosave: automatic save every 5 min')
cmds.button(l="Autosave", bgc=[0.2,0.2,0.2], sbm="Autosave in a Folder", w=450, h=50, command=callAutosave)
cmds.text(l='Undo: set undo-steps to infinity. [default: 25]')
cmds.button(l="Undo", bgc=[0.2,0.2,0.2], sbm="Infinity Undos", w=450, h=50, command=callUndo)
cmds.text(l="AnimationPreferences: set 24 fps,playbackspeed 24x1,timeline 0-24,update all viewports")
cmds.button(l="AnimationPreferences", bgc=[0.2,0.2,0.2], sbm="Set significant Base-Animation-Preferences", w=450, h=50, command=callAnimationPrefs)
cmds.text(l='Meshanalyser: check your mesh for any modelling mistakes')
cmds.button(l="Meshanalyser", bgc=[0.2,0.2,0.2], sbm="Analyse your Mesh", w=450, h=50, command=callMeshAna)
cmds.text(l='HTW iCloud: open the iCloud homepage')
cmds.button(l="HTW iCloud", bgc=[0.2,0.2,0.2], sbm="Go to iCloud", w=450, h=50, command=callICloud)

#cmds.button(l="Lightsetup", bgc=[0.2,0.2,0.2], sbm="Go to iCloud", w=450, h=50, command=callLightsetup)
#cmds.button(l="Reset All", bgc=[0.2,0.2,0.2], sbm="Reset All", w=450, h=50, command=resetAll)
cmds.text(l='Opal: open the Opal homepage')
cmds.button(l="Opal", bgc=[0.2,0.2,0.2], sbm="Go to Opal", w=450, h=50, command=callOpal)
cmds.text(l='')
cmds.button(l="Close", bgc=[0.2,0.2,0.2], sbm="Exit", w=450, h=50, command=callClose)

cmds.showWindow()





