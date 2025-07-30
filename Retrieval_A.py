#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on Mon Feb 19 15:24:25 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'Retrieval A'  # from the Builder filename that created this script
expInfo = {
    'Participant ID': '',
    'Task': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Retrieval A/%s_%s_%s' % (expInfo['Participant ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mc151/Library/CloudStorage/Box-Box/Leal Lab/Studies/In-Person Study Folders/123_ABBA study/Behavioral Task/A+B/Retrieval_A.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2240, 1260], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instructions" ---
text = visual.TextStim(win=win, name='text',
    text='Now we will test memory for the images you saw earlier\n\n\nV = Exact same \nN = New / Different \n\n\nThe image will be on the screen for 3 seconds. Be sure to respond while the image is on the screen.\n\nPress the space bar for examples',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Example" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='RetrievalA_Ex1.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='Imagine this is an image you saw in that first set of images',
    font='Arial',
    pos=(0, -0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "Example_Trial" ---
Example_Test = visual.ImageStim(
    win=win,
    name='Example_Test', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Ex_Key = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='V = EXACT SAME    N = NEW / DIFFERENT',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "StartScreen" ---
start_text = visual.TextStim(win=win, name='start_text',
    text='The test will now start\n\nThis will take about 20 minutes\n\nThere will be a break halfway through\n\nAny questions?\n\nPress the space bar to begin',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_key = keyboard.Keyboard()

# --- Initialize components for Routine "Test_1" ---
stimuli = visual.ImageStim(
    win=win,
    name='stimuli', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
respkey = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='V = EXACT SAME   N = NEW / DIFFERENT',
    font='Arial',
    pos=(0, -0.4), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Break" ---
pause_instru = visual.TextStim(win=win, name='pause_instru',
    text='You can take a quick break\n\nInstructions are the same \n\nV = Exact same\nN = New/Different\n\nPress the space bar to continue',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Test_2" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
respkey2 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='V = EXACT SAME   N = NEW / DIFFERENT',
    font='Arial',
    pos=(0, -0.4), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "End" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='END OF THE TEST \n\nPlease ring the doorbell to notify your experimenter that you are finished.\n\nTHANK YOU',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Example" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
ExampleComponents = [image_3, text_5, key_resp_5]
for thisComponent in ExampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Example" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    
    # if image_3 is starting this frame...
    if image_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3.started')
        # update status
        image_3.status = STARTED
        image_3.setAutoDraw(True)
    
    # if image_3 is active this frame...
    if image_3.status == STARTED:
        # update params
        pass
    
    # *text_5* updates
    
    # if text_5 is starting this frame...
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        # update status
        text_5.status = STARTED
        text_5.setAutoDraw(True)
    
    # if text_5 is active this frame...
    if text_5.status == STARTED:
        # update params
        pass
    
    # *key_resp_5* updates
    waitOnFlip = False
    
    # if key_resp_5 is starting this frame...
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        # update status
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Example" ---
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Example_RetrievalA.xlsx', selection='0:4'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Example_Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Ex_Key.keys = []
    Ex_Key.rt = []
    _Ex_Key_allKeys = []
    # keep track of which components have finished
    Example_TrialComponents = [Example_Test, Ex_Key, text_6]
    for thisComponent in Example_TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Example_Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Example_Test* updates
        
        # if Example_Test is starting this frame...
        if Example_Test.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Example_Test.frameNStart = frameN  # exact frame index
            Example_Test.tStart = t  # local t and not account for scr refresh
            Example_Test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Test.started')
            # update status
            Example_Test.status = STARTED
            Example_Test.setAutoDraw(True)
        
        # if Example_Test is active this frame...
        if Example_Test.status == STARTED:
            # update params
            Example_Test.setImage(Stim2, log=False)
        
        # *Ex_Key* updates
        waitOnFlip = False
        
        # if Ex_Key is starting this frame...
        if Ex_Key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Ex_Key.frameNStart = frameN  # exact frame index
            Ex_Key.tStart = t  # local t and not account for scr refresh
            Ex_Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ex_Key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ex_Key.started')
            # update status
            Ex_Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Ex_Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Ex_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Ex_Key.status == STARTED and not waitOnFlip:
            theseKeys = Ex_Key.getKeys(keyList=['V','v','n','N'], waitRelease=False)
            _Ex_Key_allKeys.extend(theseKeys)
            if len(_Ex_Key_allKeys):
                Ex_Key.keys = _Ex_Key_allKeys[-1].name  # just the last key pressed
                Ex_Key.rt = _Ex_Key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Example_TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Example_Trial" ---
    for thisComponent in Example_TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Example_Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "StartScreen" ---
continueRoutine = True
# update component parameters for each repeat
start_key.keys = []
start_key.rt = []
_start_key_allKeys = []
# keep track of which components have finished
StartScreenComponents = [start_text, start_key]
for thisComponent in StartScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "StartScreen" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    
    # if start_text is starting this frame...
    if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_text.started')
        # update status
        start_text.status = STARTED
        start_text.setAutoDraw(True)
    
    # if start_text is active this frame...
    if start_text.status == STARTED:
        # update params
        pass
    
    # *start_key* updates
    waitOnFlip = False
    
    # if start_key is starting this frame...
    if start_key.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        start_key.frameNStart = frameN  # exact frame index
        start_key.tStart = t  # local t and not account for scr refresh
        start_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_key.started')
        # update status
        start_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_key.status == STARTED and not waitOnFlip:
        theseKeys = start_key.getKeys(keyList=['space'], waitRelease=False)
        _start_key_allKeys.extend(theseKeys)
        if len(_start_key_allKeys):
            start_key.keys = _start_key_allKeys[-1].name  # just the last key pressed
            start_key.rt = _start_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StartScreen" ---
for thisComponent in StartScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StartScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Retrieval_A.xlsx', selection='0:91'),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Test_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    respkey.keys = []
    respkey.rt = []
    _respkey_allKeys = []
    # keep track of which components have finished
    Test_1Components = [stimuli, respkey, text_2]
    for thisComponent in Test_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli* updates
        
        # if stimuli is starting this frame...
        if stimuli.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuli.started')
            # update status
            stimuli.status = STARTED
            stimuli.setAutoDraw(True)
        
        # if stimuli is active this frame...
        if stimuli.status == STARTED:
            # update params
            stimuli.setImage(Stim, log=False)
        
        # if stimuli is stopping this frame...
        if stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli.tStop = t  # not accounting for scr refresh
                stimuli.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli.stopped')
                # update status
                stimuli.status = FINISHED
                stimuli.setAutoDraw(False)
        
        # *respkey* updates
        waitOnFlip = False
        
        # if respkey is starting this frame...
        if respkey.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            respkey.frameNStart = frameN  # exact frame index
            respkey.tStart = t  # local t and not account for scr refresh
            respkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respkey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'respkey.started')
            # update status
            respkey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respkey.clock.reset)  # t=0 on next screen flip
        
        # if respkey is stopping this frame...
        if respkey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > respkey.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                respkey.tStop = t  # not accounting for scr refresh
                respkey.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respkey.stopped')
                # update status
                respkey.status = FINISHED
                respkey.status = FINISHED
        if respkey.status == STARTED and not waitOnFlip:
            theseKeys = respkey.getKeys(keyList=['V','v','N','n'], waitRelease=False)
            _respkey_allKeys.extend(theseKeys)
            if len(_respkey_allKeys):
                respkey.keys = _respkey_allKeys[0].name  # just the first key pressed
                respkey.rt = _respkey_allKeys[0].rt
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test_1" ---
    for thisComponent in Test_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respkey.keys in ['', [], None]:  # No response was made
        respkey.keys = None
    trials_1.addData('respkey.keys',respkey.keys)
    if respkey.keys != None:  # we had a response
        trials_1.addData('respkey.rt', respkey.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_1'


# --- Prepare to start Routine "Break" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
BreakComponents = [pause_instru, key_resp_4]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Break" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pause_instru* updates
    
    # if pause_instru is starting this frame...
    if pause_instru.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pause_instru.frameNStart = frameN  # exact frame index
        pause_instru.tStart = t  # local t and not account for scr refresh
        pause_instru.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pause_instru, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pause_instru.started')
        # update status
        pause_instru.status = STARTED
        pause_instru.setAutoDraw(True)
    
    # if pause_instru is active this frame...
    if pause_instru.status == STARTED:
        # update params
        pass
    
    # *key_resp_4* updates
    waitOnFlip = False
    
    # if key_resp_4 is starting this frame...
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        # update status
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Break" ---
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Retrieval_A.xlsx', selection='91:182'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Test_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    respkey2.keys = []
    respkey2.rt = []
    _respkey2_allKeys = []
    # keep track of which components have finished
    Test_2Components = [image_2, respkey2, text_3]
    for thisComponent in Test_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        
        # if image_2 is starting this frame...
        if image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            # update status
            image_2.status = STARTED
            image_2.setAutoDraw(True)
        
        # if image_2 is active this frame...
        if image_2.status == STARTED:
            # update params
            image_2.setImage(Stim, log=False)
        
        # if image_2 is stopping this frame...
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.stopped')
                # update status
                image_2.status = FINISHED
                image_2.setAutoDraw(False)
        
        # *respkey2* updates
        waitOnFlip = False
        
        # if respkey2 is starting this frame...
        if respkey2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            respkey2.frameNStart = frameN  # exact frame index
            respkey2.tStart = t  # local t and not account for scr refresh
            respkey2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respkey2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'respkey2.started')
            # update status
            respkey2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respkey2.clock.reset)  # t=0 on next screen flip
        
        # if respkey2 is stopping this frame...
        if respkey2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > respkey2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                respkey2.tStop = t  # not accounting for scr refresh
                respkey2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respkey2.stopped')
                # update status
                respkey2.status = FINISHED
                respkey2.status = FINISHED
        if respkey2.status == STARTED and not waitOnFlip:
            theseKeys = respkey2.getKeys(keyList=['V','v','N','n'], waitRelease=False)
            _respkey2_allKeys.extend(theseKeys)
            if len(_respkey2_allKeys):
                respkey2.keys = _respkey2_allKeys[0].name  # just the first key pressed
                respkey2.rt = _respkey2_allKeys[0].rt
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test_2" ---
    for thisComponent in Test_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respkey2.keys in ['', [], None]:  # No response was made
        respkey2.keys = None
    trials_2.addData('respkey2.keys',respkey2.keys)
    if respkey2.keys != None:  # we had a response
        trials_2.addData('respkey2.rt', respkey2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "End" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text_4]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
