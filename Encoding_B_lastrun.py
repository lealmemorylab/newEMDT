#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Fri Jan 17 15:22:10 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Encoding B'  # from the Builder filename that created this script
expInfo = {'Participant ID': '', 'Task': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Encoding B/%s_%s_%s' % (expInfo['Participant ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Fernanda/Library/CloudStorage/Box-Box/Leal Lab/Studies/In-Person Study Folders/125_ABBA NEW/Behavioral Task/A+B/Encoding_B_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2240, 1260], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='You will see a series of images on the screen and asked to rate each image as negative, neutral, or positive using the slider scale.\n\nThe image will be on screen for 3 seconds\n\nMake sure that you make your response while the image is still on the screen.\n\nPress the space bar for examples',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
instructionkey = keyboard.Keyboard()

# Initialize components for Routine "Examples"
ExamplesClock = core.Clock()
example_image = visual.ImageStim(
    win=win,
    name='example_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.05), size=[.6,.5],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
Valence_rating_slider = visual.Slider(win=win, name='Valence_rating_slider',
    startValue=None, size=(.8, 0.1), pos=(0, -0.3), units=None,
    labels=["Negative",None,None,None,"Neutral",None,None,None,"Positive"], ticks=(1,2,3,4,5,6,7,8,9), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Blue', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Start_Screen"
Start_ScreenClock = core.Clock()
start_screen = visual.TextStim(win=win, name='start_screen',
    text='The test will now start\n\nThis should take about 10 minutes. \n\nAny questions?\n\nPress the space bar to begin',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Study"
StudyClock = core.Clock()
Stimuli = visual.ImageStim(
    win=win,
    name='Stimuli', 
    image='sin', mask=None,
    ori=0.0, pos=(0, .05), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
emotional_valence_slider = visual.Slider(win=win, name='emotional_valence_slider',
    startValue=None, size=(.8, 0.1), pos=(0, -0.3), units=None,
    labels=["Negative",None,None,None,"Neutral",None,None,None,"Positive"], ticks=(1,2,3,4,5,6,7,8,9), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Blue', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "End"
EndClock = core.Clock()
endtext = visual.TextStim(win=win, name='endtext',
    text='END OF PART 1\n\nPlease ring the doorbell to let your experimenter know that you are finished.\n\nTHANK YOU',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructionkey.keys = []
instructionkey.rt = []
_instructionkey_allKeys = []
# keep track of which components have finished
instructionsComponents = [Instructions, instructionkey]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *instructionkey* updates
    if instructionkey.status == NOT_STARTED and t >= 3-frameTolerance:
        # keep track of start time/frame for later
        instructionkey.frameNStart = frameN  # exact frame index
        instructionkey.tStart = t  # local t and not account for scr refresh
        instructionkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionkey, 'tStartRefresh')  # time at next scr refresh
        instructionkey.status = STARTED
        # keyboard checking is just starting
        instructionkey.clock.reset()  # now t=0
    if instructionkey.status == STARTED:
        theseKeys = instructionkey.getKeys(keyList=['space'], waitRelease=False)
        _instructionkey_allKeys.extend(theseKeys)
        if len(_instructionkey_allKeys):
            instructionkey.keys = _instructionkey_allKeys[-1].name  # just the last key pressed
            instructionkey.rt = _instructionkey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Example_EncodingB.xlsx', selection='0:4'),
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
    
    # ------Prepare to start Routine "Examples"-------
    continueRoutine = True
    # update component parameters for each repeat
    Valence_rating_slider.reset()
    # keep track of which components have finished
    ExamplesComponents = [example_image, Valence_rating_slider]
    for thisComponent in ExamplesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExamplesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Examples"-------
    while continueRoutine:
        # get current time
        t = ExamplesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExamplesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *example_image* updates
        if example_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            example_image.frameNStart = frameN  # exact frame index
            example_image.tStart = t  # local t and not account for scr refresh
            example_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_image, 'tStartRefresh')  # time at next scr refresh
            example_image.setAutoDraw(True)
        if example_image.status == STARTED:  # only update if drawing
            example_image.setImage(Stim1, log=False)
        
        # *Valence_rating_slider* updates
        if Valence_rating_slider.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Valence_rating_slider.frameNStart = frameN  # exact frame index
            Valence_rating_slider.tStart = t  # local t and not account for scr refresh
            Valence_rating_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Valence_rating_slider, 'tStartRefresh')  # time at next scr refresh
            Valence_rating_slider.setAutoDraw(True)
        
        # Check Valence_rating_slider for response to end routine
        if Valence_rating_slider.getRating() is not None and Valence_rating_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExamplesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Examples"-------
    for thisComponent in ExamplesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Examples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "Start_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Start_ScreenComponents = [start_screen, key_resp]
for thisComponent in Start_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_Screen"-------
while continueRoutine:
    # get current time
    t = Start_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_screen* updates
    if start_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_screen.frameNStart = frameN  # exact frame index
        start_screen.tStart = t  # local t and not account for scr refresh
        start_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_screen, 'tStartRefresh')  # time at next scr refresh
        start_screen.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
    if key_resp.status == STARTED:
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
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_Screen"-------
for thisComponent in Start_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
task = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encoding_B.xlsx', selection='0:136'),
    seed=None, name='task')
thisExp.addLoop(task)  # add the loop to the experiment
thisTask = task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
if thisTask != None:
    for paramName in thisTask:
        exec('{} = thisTask[paramName]'.format(paramName))

for thisTask in task:
    currentLoop = task
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask:
            exec('{} = thisTask[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Study"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    emotional_valence_slider.reset()
    # keep track of which components have finished
    StudyComponents = [Stimuli, emotional_valence_slider]
    for thisComponent in StudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Study"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = StudyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StudyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli* updates
        if Stimuli.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Stimuli.frameNStart = frameN  # exact frame index
            Stimuli.tStart = t  # local t and not account for scr refresh
            Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli, 'tStartRefresh')  # time at next scr refresh
            Stimuli.setAutoDraw(True)
        if Stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli.tStop = t  # not accounting for scr refresh
                Stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli, 'tStopRefresh')  # time at next scr refresh
                Stimuli.setAutoDraw(False)
        if Stimuli.status == STARTED:  # only update if drawing
            Stimuli.setImage(Stim, log=False)
        
        # *emotional_valence_slider* updates
        if emotional_valence_slider.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            emotional_valence_slider.frameNStart = frameN  # exact frame index
            emotional_valence_slider.tStart = t  # local t and not account for scr refresh
            emotional_valence_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(emotional_valence_slider, 'tStartRefresh')  # time at next scr refresh
            emotional_valence_slider.setAutoDraw(True)
        if emotional_valence_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > emotional_valence_slider.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                emotional_valence_slider.tStop = t  # not accounting for scr refresh
                emotional_valence_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(emotional_valence_slider, 'tStopRefresh')  # time at next scr refresh
                emotional_valence_slider.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Study"-------
    for thisComponent in StudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task.addData('Stimuli.started', Stimuli.tStartRefresh)
    task.addData('Stimuli.stopped', Stimuli.tStopRefresh)
    task.addData('emotional_valence_slider.response', emotional_valence_slider.getRating())
    task.addData('emotional_valence_slider.rt', emotional_valence_slider.getRT())
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
EndComponents = [endtext, key_resp_2]
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
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endtext* updates
    if endtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endtext.frameNStart = frameN  # exact frame index
        endtext.tStart = t  # local t and not account for scr refresh
        endtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endtext, 'tStartRefresh')  # time at next scr refresh
        endtext.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
